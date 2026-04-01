#!/usr/bin/env python3
"""Pre-release validation for the Product Team package."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import EXCLUDED_ROLES, discover_toml_paths, load_toml
from lib.skill_validation import KNOWN_MCP_SERVERS, SkillValidationContext, validate_skill_contexts


ROOT = Path(__file__).resolve().parents[1]


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run_check(script: str, label: str, failures: list[str]) -> None:
    result = subprocess.run([sys.executable, str(ROOT / script), "--check"], capture_output=True, text=True)
    if result.returncode != 0:
        failures.append(f"{label}: {result.stderr.strip()}")
    else:
        print(f"  OK: {label} are current.")


def check_role_and_skill_contracts(failures: list[str]) -> None:
    skill_contexts: list[SkillValidationContext] = []

    for toml_path in discover_toml_paths(ROOT):
        data = load_toml(toml_path)
        role = data["name"]
        mcp_servers = set(data.get("capabilities", {}).get("mcp_servers", []))
        for server in mcp_servers:
            expect(server in KNOWN_MCP_SERVERS, f"{role}: unknown mcp_server '{server}'.", failures)

        skills_dir = toml_path.parent / "skills"
        skill_files = sorted(skills_dir.rglob("*.md"))
        skill_contexts.append(
            SkillValidationContext(
                discipline=toml_path.parent.parent.name,
                role_name=role,
                mcp_servers=tuple(sorted(mcp_servers)),
                web_tools=tuple(sorted(data.get("capabilities", {}).get("web_tools", []))),
                skill_files=tuple(skill_files),
            )
        )

        if role in EXCLUDED_ROLES:
            continue

        expect(4 <= len(skill_files) <= 8, f"{role}: must have 4-8 core skills; found {len(skill_files)}.", failures)

    validate_skill_contexts(skill_contexts, failures, enforce_banned_names=True)

    print("  OK: Role and skill contracts checked.")


def main() -> int:
    print("Running pre-release checks...\n")
    failures: list[str] = []

    run_check("scripts/render_role_catalog.py", "Role catalog", failures)
    run_check("scripts/render_skill_catalogs.py", "Skill catalogs", failures)
    run_check("scripts/render_role_prompts.py", "Archetype prompts", failures)

    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "check-orchestrator-scenarios.py")], capture_output=True, text=True)
    if result.returncode != 0:
        failures.append(f"Orchestrator contract: {result.stderr.strip()}")
    else:
        print("  OK: Orchestrator contract checks passed.")

    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_skill_validation_scenarios.py")], capture_output=True, text=True)
    if result.returncode != 0:
        failures.append(f"Skill validation scenarios: {result.stderr.strip()}")
    else:
        print("  OK: Skill validation scenario checks passed.")

    check_role_and_skill_contracts(failures)

    print()
    if failures:
        print(f"FAILED: {len(failures)} issue(s) found:\n", file=sys.stderr)
        for failure in failures:
            print(f"  FAIL: {failure}", file=sys.stderr)
        return 1

    print("All pre-release checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
