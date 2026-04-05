#!/usr/bin/env python3
import sys
import re
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime


def find_repo_root() -> Path:
    """Walk up the directory tree to find the git repository root."""
    path = Path(__file__).resolve()
    while path != path.parent:
        if (path / ".git").exists():
            return path
        path = path.parent
    raise RuntimeError("Could not find git repository root")


AUTO_IMPROVE_DIR = Path(__file__).resolve().parent
SCENARIOS_DIR = AUTO_IMPROVE_DIR / "scenarios"
REPO_ROOT = find_repo_root()
LOGS_DIR = REPO_ROOT / "logs/benchmarks"


def parse_artifact_name(instruction: str) -> str:
    """Extract the expected output filename from the Output Contract section."""
    match = re.search(r"Produce a `([^`]+)`", instruction)
    if match:
        return match.group(1)
    return "output.md"


def resolve_skill_path(role: str, skill: str, source: str) -> Path:
    """Resolve the skill file path based on role, skill name, and source directory."""
    if "/" in role:
        discipline, role_name = role.split("/", 1)
    else:
        discipline, role_name = role, role

    source_path = Path(source)
    if not source_path.is_absolute():
        source_path = REPO_ROOT / source_path

    skill_path = source_path / f"product-team-{discipline}/{role_name}/skills/{skill}.md"
    return skill_path


def invoke_runner(runner: str, context_path: Path, artifact_name: str, run_dir: Path) -> Path:
    """Invoke an agent runner (codex or claude) with the prepared context.

    Returns the path to the produced artifact.
    """
    context_content = context_path.read_text()
    artifact_path = run_dir / artifact_name

    prompt = (
        f"You are being evaluated on a benchmark task. Read the context below and produce "
        f"the requested artifact. Write ONLY the artifact content, nothing else.\n\n"
        f"{context_content}\n\n"
        f"Write the output to a file named: {artifact_name}"
    )

    if runner == "codex":
        cmd = [
            "codex", "--approval-mode", "full-auto",
            "--quiet",
            "-p", prompt,
        ]
    elif runner == "claude":
        cmd = [
            "claude", "--print",
            "-p", prompt,
        ]
    else:
        raise ValueError(f"Unknown runner: {runner}")

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=str(run_dir),
        )

        # If the runner produced the file directly, use it
        if artifact_path.exists():
            return artifact_path

        # Otherwise, save stdout as the artifact
        output = proc.stdout.strip()
        if output:
            artifact_path.write_text(output)
            return artifact_path

        # Check if stderr has useful info
        if proc.returncode != 0:
            error_log = run_dir / "runner-error.log"
            error_log.write_text(
                f"Runner '{runner}' exited with code {proc.returncode}\n"
                f"stderr: {proc.stderr}\n"
            )
            raise RuntimeError(
                f"Runner '{runner}' failed (exit {proc.returncode}): {proc.stderr[:500]}"
            )

        raise RuntimeError(f"Runner '{runner}' produced no output")

    except FileNotFoundError:
        raise RuntimeError(
            f"Runner '{runner}' not found. Make sure '{runner}' CLI is installed and on PATH."
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Runner '{runner}' timed out after 300 seconds")


def run_benchmark(scenario_name: str, role: str, skill: str,
                  runner: str = "dry-run", source: str = None):
    """Run a benchmark scenario against a skill.

    Args:
        scenario_name: Name of the scenario directory under scenarios/
        role: Agent role in "discipline/role-name" format
        skill: Skill filename (without .md extension)
        runner: Execution mode - "dry-run" (default), "codex", or "claude"
        source: Base directory for agent skills (default: agents/ in repo root)
    """
    if source is None:
        source = str(REPO_ROOT / "agents")

    scenario_path = SCENARIOS_DIR / scenario_name
    if not scenario_path.exists():
        return {"error": f"Scenario '{scenario_name}' not found at {scenario_path}"}

    instruction = (scenario_path / "instruction.md").read_text()
    artifact_name = parse_artifact_name(instruction)

    skill_path = resolve_skill_path(role, skill, source)
    if not skill_path.exists():
        return {"error": f"Skill '{skill}' not found at {skill_path}"}

    skill_content = skill_path.read_text()

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = LOGS_DIR / f"{scenario_name}_{run_id}"
    run_dir.mkdir(parents=True, exist_ok=True)

    context_path = run_dir / "context.md"
    context_path.write_text(
        f"### SKILL UNDER TEST: {skill}\n\n{skill_content}\n\n### TASK:\n{instruction}"
    )

    result = {
        "run_id": run_id,
        "run_dir": str(run_dir),
        "scenario": scenario_name,
        "role": role,
        "skill": skill,
        "artifact": artifact_name,
        "runner": runner,
    }

    if runner == "dry-run":
        print(f"Benchmark '{scenario_name}' prepared for {role}/{skill}.")
        print(f"Context saved to: {run_dir}/context.md")
        print(f"EXPECTATION: Produce '{artifact_name}' in {run_dir}")
    else:
        # Actually execute the skill via the chosen runner
        print(f"Executing benchmark '{scenario_name}' via {runner}...")
        try:
            artifact_path = invoke_runner(runner, context_path, artifact_name, run_dir)
            result["artifact_path"] = str(artifact_path)
            print(f"Artifact produced: {artifact_path}")
        except RuntimeError as e:
            result["error"] = str(e)
            print(f"ERROR: {e}", file=sys.stderr)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Run a benchmark scenario against an agent skill."
    )
    parser.add_argument("scenario_name", type=str, help="Name of the scenario to run")
    parser.add_argument("role", type=str, help="Agent role (e.g. design/ui-designer)")
    parser.add_argument("skill", type=str, help="Skill name (without .md)")
    parser.add_argument(
        "--runner",
        choices=["dry-run", "codex", "claude"],
        default="dry-run",
        help="Execution mode: dry-run (default), codex, or claude",
    )
    parser.add_argument(
        "--source",
        type=str,
        default=None,
        help="Base directory for agent skills (default: <repo>/agents/). "
             "Use '.codex/agents/' for installed repos.",
    )
    args = parser.parse_args()

    result = run_benchmark(
        args.scenario_name,
        args.role,
        args.skill,
        runner=args.runner,
        source=args.source,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
