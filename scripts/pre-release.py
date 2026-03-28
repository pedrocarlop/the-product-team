#!/usr/bin/env python3
"""Pre-release validation for the Product Team package.

Checks that all generated artifacts are current, all referenced skills exist,
MCP assignments use known servers, and no orphaned files remain.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import EXCLUDED_ROLES, discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]

KNOWN_MCP_SERVERS = {
    "figma",
    "chrome_devtools",
    "notion",
    "linear",
    "slack",
    "github",
    "paper",
}

REQUIRED_TOML_FIELDS = {
    "name",
    "display_name",
    "description",
    "system_prompt",
}


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def check_generated_artifacts(failures: list[str]) -> None:
    """Verify role catalog and managed archetype prompts are current."""
    for script, label in [
        ("scripts/render_role_catalog.py", "Role catalog"),
        ("scripts/render_role_prompts.py", "Archetype prompts"),
    ]:
        result = subprocess.run(
            [sys.executable, str(ROOT / script), "--check"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            failures.append(f"{label}: {result.stderr.strip()}")
        else:
            print(f"  OK: {label} are current.")


def check_orchestrator_contract(failures: list[str]) -> None:
    """Verify orchestrator contract checks pass."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check-orchestrator-scenarios.py")],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"Orchestrator contract: {result.stderr.strip()}")
    else:
        print("  OK: Orchestrator contract checks passed.")


def check_skills_integrity(failures: list[str]) -> None:
    """Verify all local_skills have matching .md files and no orphans exist."""
    toml_paths = discover_toml_paths(ROOT)

    for toml_path in toml_paths:
        data = load_toml(toml_path)
        role_name = data["name"]
        if role_name in EXCLUDED_ROLES:
            continue

        skills_dir = toml_path.parent / "skills"
        local_skills = data.get("capabilities", {}).get("local_skills", [])

        if not skills_dir.is_dir():
            if local_skills:
                failures.append(
                    f"{role_name}: declares local_skills {local_skills} "
                    f"but has no skills/ directory."
                )
            continue

        existing_skill_files = {p.stem for p in skills_dir.rglob("*.md")}

        for skill in local_skills:
            if skill == "reference" or skill.startswith("product-team-"):
                continue
            skill_stem = skill.removesuffix(".md")
            if skill_stem not in existing_skill_files:
                failures.append(
                    f"{role_name}: local_skills references '{skill}' "
                    f"but no skills/{skill_stem}.md found."
                )

    print("  OK: Skills integrity checked.")


def check_mcp_servers(failures: list[str]) -> None:
    """Verify all mcp_servers entries use known server names."""
    toml_paths = discover_toml_paths(ROOT)

    for toml_path in toml_paths:
        data = load_toml(toml_path)
        role_name = data["name"]
        mcp_servers = data.get("capabilities", {}).get("mcp_servers", [])

        for server in mcp_servers:
            if server not in KNOWN_MCP_SERVERS:
                failures.append(
                    f"{role_name}: unknown mcp_server '{server}'. "
                    f"Known: {', '.join(sorted(KNOWN_MCP_SERVERS))}."
                )

    print("  OK: MCP server assignments are valid.")


def check_required_fields(failures: list[str]) -> None:
    """Verify all specialist TOMLs have required fields."""
    toml_paths = discover_toml_paths(ROOT)

    for toml_path in toml_paths:
        data = load_toml(toml_path)
        role_name = data.get("name", toml_path.stem)

        for field in REQUIRED_TOML_FIELDS:
            expect(
                field in data and data[field],
                f"{role_name}: missing required field '{field}'.",
                failures,
            )

        expect(
            "execution_policy" in data and "role_kind" in data.get("execution_policy", {}),
            f"{role_name}: missing execution_policy.role_kind.",
            failures,
        )

        expect(
            "role_boundary" in data and "owns" in data.get("role_boundary", {}),
            f"{role_name}: missing role_boundary.owns.",
            failures,
        )

        if role_name not in EXCLUDED_ROLES and role_name != "orchestrator":
            expect(
                "role_boundary" in data and "handoff_to" in data.get("role_boundary", {}),
                f"{role_name}: missing role_boundary.handoff_to.",
                failures,
            )

    print("  OK: Required fields present in all TOMLs.")


def main() -> int:
    print("Running pre-release checks...\n")
    failures: list[str] = []

    check_generated_artifacts(failures)
    check_orchestrator_contract(failures)
    check_skills_integrity(failures)
    check_mcp_servers(failures)
    check_required_fields(failures)

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
