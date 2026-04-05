#!/usr/bin/env python3
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path


def find_repo_root() -> Path:
    """Walk up the directory tree to find the git repository root."""
    path = Path(__file__).resolve()
    while path != path.parent:
        if (path / ".git").exists():
            return path
        path = path.parent
    raise RuntimeError("Could not find git repository root")


AUTO_IMPROVE_DIR = Path(__file__).resolve().parent
JUDGE_PATH = AUTO_IMPROVE_DIR / "judge.py"
REPO_ROOT = find_repo_root()
LOGS_DIR = REPO_ROOT / "logs/benchmarks"


def infer_scenario_type(scenario_name: str) -> str:
    """Derive judge scenario type from the scenario directory name."""
    name = scenario_name.lower()
    if any(kw in name for kw in ["engineering", "backend", "api", "platform", "schema", "frontend"]):
        return "engineering"
    if any(kw in name for kw in ["business", "prd", "go-to-market", "launch", "qa", "release"]):
        return "business"
    return "design"


def get_latest_run(scenario_name: str):
    runs = sorted(LOGS_DIR.glob(f"{scenario_name}_*"), reverse=True)
    return runs[0] if runs else None


def run_judge(artifact_path: str, scenario_type: str) -> dict:
    """Run the judge script and return parsed results."""
    judge_cmd = [
        sys.executable, str(JUDGE_PATH),
        str(artifact_path),
        "--type", scenario_type,
    ]
    proc = subprocess.run(judge_cmd, capture_output=True, text=True)

    if proc.returncode != 0:
        raise RuntimeError(f"Judge failed: {proc.stderr.strip()}")

    # The judge may print extra info before the JSON; find the last JSON block
    stdout = proc.stdout.strip()
    # Find the last line that starts with '{'
    json_lines = []
    brace_depth = 0
    in_json = False
    for line in stdout.split("\n"):
        stripped = line.strip()
        if stripped.startswith("{"):
            in_json = True
            json_lines = []
            brace_depth = 0
        if in_json:
            json_lines.append(line)
            brace_depth += stripped.count("{") - stripped.count("}")
            if brace_depth <= 0:
                in_json = False

    if not json_lines:
        raise RuntimeError(f"No JSON found in judge output: {stdout[:300]}")

    return json.loads("\n".join(json_lines))


def apply_patch(skill_path: Path, patch_file: Path) -> bool:
    """Apply improved skill content from a patch file.

    The patch file should contain the complete new content for the skill file.
    Returns True if the file was modified.
    """
    if not patch_file.exists():
        raise FileNotFoundError(f"Patch file not found: {patch_file}")

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_path}")

    new_content = patch_file.read_text()
    old_content = skill_path.read_text()

    if new_content.strip() == old_content.strip():
        print("Patch content is identical to current skill. No changes applied.")
        return False

    # Back up the original
    backup_path = skill_path.with_suffix(".md.bak")
    shutil.copy2(skill_path, backup_path)
    print(f"Backup saved: {backup_path}")

    # Apply the patch
    skill_path.write_text(new_content)
    print(f"Patch applied to: {skill_path}")
    return True


def verify_improvement(scenario_name: str, skill_path: Path, baseline_score: float,
                       scenario_type: str) -> dict:
    """Re-run the judge after applying a patch. Revert if score did not improve."""
    latest_run = get_latest_run(scenario_name)
    if not latest_run:
        return {"error": "No run directory found for verification"}

    artifacts = [f for f in latest_run.iterdir()
                 if f.is_file() and f.name not in ("context.md", "runner-error.log")]
    if not artifacts:
        return {"error": "No artifact found for verification"}

    output_artifact = artifacts[0]

    try:
        new_result = run_judge(str(output_artifact), scenario_type)
    except RuntimeError as e:
        return {"error": f"Verification judge failed: {e}"}

    new_score = new_result.get("score", 0.0)
    improved = new_score > baseline_score

    print(f"VERIFICATION: baseline={baseline_score}, new={new_score}, improved={improved}")

    if not improved:
        # Revert
        backup_path = skill_path.with_suffix(".md.bak")
        if backup_path.exists():
            shutil.copy2(backup_path, skill_path)
            backup_path.unlink()
            print(f"Score did not improve. Reverted {skill_path} from backup.")
        else:
            print("WARNING: No backup file found to revert.", file=sys.stderr)

        return {
            "status": "reverted",
            "baseline_score": baseline_score,
            "new_score": new_score,
            "improved": False,
        }

    # Clean up backup on success
    backup_path = skill_path.with_suffix(".md.bak")
    if backup_path.exists():
        backup_path.unlink()

    return {
        "status": "improved",
        "baseline_score": baseline_score,
        "new_score": new_score,
        "improved": True,
    }


def meta_optimize(scenario_name: str, role: str, skill: str,
                  apply: bool = False, patch_file: str = None,
                  verify: bool = False) -> dict:
    """Run the meta-optimization loop.

    Without --apply: prints the optimization prompt (human-in-the-loop).
    With --apply --patch-file: applies the patch and optionally verifies improvement.
    """
    latest_run = get_latest_run(scenario_name)
    if not latest_run:
        return {"error": f"No baseline run found for scenario '{scenario_name}'"}

    # Find the output artifact (anything that isn't the context scaffold or error log)
    artifacts = [f for f in latest_run.iterdir()
                 if f.is_file() and f.name not in ("context.md", "runner-error.log")]
    if not artifacts:
        return {"error": f"No output artifact found in {latest_run}"}
    output_artifact = artifacts[0]

    scenario_type = infer_scenario_type(scenario_name)

    # Run the judge to get baseline score
    try:
        baseline_result = run_judge(str(output_artifact), scenario_type)
    except RuntimeError as e:
        return {"error": str(e)}

    baseline_score = baseline_result.get("score", 0.0)

    print(f"BASELINE SCORE: {baseline_score}")
    print(f"REASONS: {baseline_result.get('reasons', [])}")

    if baseline_score >= 1.0:
        print("Skill achieved a perfect score. No optimization needed.")
        return {"status": "complete", "score": baseline_score}

    # Parse "discipline/role-name" to build the correct skill path
    if "/" in role:
        discipline, role_name = role.split("/", 1)
    else:
        discipline, role_name = role, role

    skill_rel_path = f"agents/product-team-{discipline}/{role_name}/skills/{skill}.md"
    skill_abs_path = REPO_ROOT / skill_rel_path

    # --apply mode: apply a patch file to the skill
    if apply:
        if not patch_file:
            return {"error": "--apply requires --patch-file <path>"}

        try:
            changed = apply_patch(skill_abs_path, Path(patch_file))
        except (FileNotFoundError, IOError) as e:
            return {"error": str(e)}

        if not changed:
            return {
                "status": "no_change",
                "baseline_score": baseline_score,
                "skill_path": skill_rel_path,
            }

        result = {
            "status": "applied",
            "baseline_score": baseline_score,
            "skill_path": skill_rel_path,
        }

        # --verify: re-run judge and revert if no improvement
        if verify:
            verify_result = verify_improvement(
                scenario_name, skill_abs_path, baseline_score, scenario_type
            )
            result.update(verify_result)

        return result

    # Default: print optimization prompt for human-in-the-loop
    failures = [r for r in baseline_result.get("reasons", []) if r.startswith("FAIL")]

    optimization_prompt = (
        f"OPTIMIZATION TARGET: {role}/{skill}\n"
        f"CURRENT SCORE: {baseline_score}/1.0\n"
        f"FAILURES:\n{json.dumps(failures or baseline_result.get('reasons', []), indent=2)}\n\n"
        f"TASK: Modify '{skill_rel_path}' to specifically address these failures.\n"
        f"Ensure you follow the 'skill-authoring-guide.md' for formatting."
    )

    print("\n--- OPTIMIZATION PROMPT ---\n")
    print(optimization_prompt)
    print("\n--- END PROMPT ---\n")

    return {
        "status": "ready_for_iteration",
        "baseline_score": baseline_score,
        "failures": failures or baseline_result.get("reasons", []),
        "skill_path": skill_rel_path,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Meta-optimizer: score a skill and optionally apply improvements."
    )
    parser.add_argument("scenario_name", type=str, help="Name of the benchmark scenario")
    parser.add_argument("role", type=str, help="Agent role (e.g. design/ui-designer)")
    parser.add_argument("skill", type=str, help="Skill name (without .md)")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply a patch file to the skill (requires --patch-file)",
    )
    parser.add_argument(
        "--patch-file",
        type=str,
        default=None,
        help="Path to a file containing the improved skill content",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Re-run judge after applying; revert if score did not improve",
    )
    args = parser.parse_args()

    result = meta_optimize(
        args.scenario_name,
        args.role,
        args.skill,
        apply=args.apply,
        patch_file=args.patch_file,
        verify=args.verify,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
