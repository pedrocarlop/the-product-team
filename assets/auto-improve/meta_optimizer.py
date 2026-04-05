#!/usr/bin/env python3
import sys
import json
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
    if "engineering" in name:
        return "engineering"
    if "business" in name or "prd" in name:
        return "business"
    return "design"


def get_latest_run(scenario_name: str):
    runs = sorted(LOGS_DIR.glob(f"{scenario_name}_*"), reverse=True)
    return runs[0] if runs else None


def meta_optimize(scenario_name: str, role: str, skill: str):
    latest_run = get_latest_run(scenario_name)
    if not latest_run:
        return {"error": f"No baseline run found for scenario '{scenario_name}'"}

    # Find the output artifact (anything that isn't the context scaffold)
    artifacts = [f for f in latest_run.iterdir() if f.is_file() and f.name != "context.md"]
    if not artifacts:
        return {"error": f"No output artifact found in {latest_run}"}
    output_artifact = artifacts[0]

    scenario_type = infer_scenario_type(scenario_name)

    # Run the judge
    judge_cmd = [
        sys.executable, str(JUDGE_PATH),
        str(output_artifact),
        "--type", scenario_type,
    ]
    proc = subprocess.run(judge_cmd, capture_output=True, text=True)

    if proc.returncode != 0:
        return {"error": f"Judge failed: {proc.stderr.strip()}"}

    try:
        baseline_result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return {"error": f"Failed to parse judge output: {exc}\nRaw: {proc.stdout[:300]}"}

    baseline_score = baseline_result["score"]

    print(f"BASELINE SCORE: {baseline_score}")
    print(f"REASONS: {baseline_result['reasons']}")

    if baseline_score >= 1.0:
        print("Skill achieved a perfect score. No optimization needed.")
        return {"status": "complete", "score": baseline_score}

    # Parse "discipline/role-name" to build the correct skill path
    if "/" in role:
        discipline, role_name = role.split("/", 1)
    else:
        discipline, role_name = role, role

    skill_path = f".codex/agents/product-team-{discipline}/{role_name}/skills/{skill}.md"

    optimization_prompt = (
        f"OPTIMIZATION TARGET: {role}/{skill}\n"
        f"CURRENT SCORE: {baseline_score}/1.0\n"
        f"FAILURES:\n{json.dumps(baseline_result['reasons'], indent=2)}\n\n"
        f"TASK: Modify '{skill_path}' to specifically address these failures.\n"
        f"Ensure you follow the 'skill-authoring-guide.md' for formatting."
    )

    print("\n--- OPTIMIZATION PROMPT ---\n")
    print(optimization_prompt)
    print("\n--- END PROMPT ---\n")

    return {
        "status": "ready_for_iteration",
        "baseline_score": baseline_score,
        "failures": baseline_result["reasons"],
        "skill_path": skill_path,
    }


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: meta_optimizer.py <scenario_name> <role> <skill>")
        sys.exit(1)

    result = meta_optimize(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
