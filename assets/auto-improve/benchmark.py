#!/usr/bin/env python3
import sys
import re
import json
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


def run_benchmark(scenario_name: str, role: str, skill: str):
    scenario_path = SCENARIOS_DIR / scenario_name
    if not scenario_path.exists():
        return {"error": f"Scenario '{scenario_name}' not found at {scenario_path}"}

    instruction = (scenario_path / "instruction.md").read_text()
    artifact_name = parse_artifact_name(instruction)

    # Parse "discipline/role-name" (e.g. "design/ui-designer" → discipline=design, role_name=ui-designer)
    if "/" in role:
        discipline, role_name = role.split("/", 1)
    else:
        discipline, role_name = role, role

    skill_path = REPO_ROOT / f".codex/agents/product-team-{discipline}/{role_name}/skills/{skill}.md"
    if not skill_path.exists():
        return {"error": f"Skill '{skill}' not found at {skill_path}"}

    skill_content = skill_path.read_text()

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = LOGS_DIR / f"{scenario_name}_{run_id}"
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "context.md").write_text(
        f"### SKILL UNDER TEST: {skill}\n\n{skill_content}\n\n### TASK:\n{instruction}"
    )

    print(f"Benchmark '{scenario_name}' prepared for {role}/{skill}.")
    print(f"Context saved to: {run_dir}/context.md")
    print(f"EXPECTATION: Produce '{artifact_name}' in {run_dir}")

    return {
        "run_id": run_id,
        "run_dir": str(run_dir),
        "scenario": scenario_name,
        "role": role,
        "skill": skill,
        "artifact": artifact_name,
    }


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: benchmark.py <scenario_name> <role> <skill>")
        sys.exit(1)

    result = run_benchmark(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
