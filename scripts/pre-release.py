#!/usr/bin/env python3
"""Pre-release validation for the Product Team package."""

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
    "stitch",
    "refero",
    "google_forms",
}
BANNED_SKILL_NAMES = {
    "apply-patch",
    "search-query",
    "chrome-click",
    "chrome-lighthouse-audit",
    "chrome-list-console-messages",
    "chrome-list-network-requests",
    "chrome-navigate-page",
    "chrome-take-snapshot",
    "figma-get-design-context",
    "figma-get-screenshot",
    "image-query",
}
REQUIRED_SKILL_FIELDS = {
    "name",
    "description",
    "trigger",
    "primary_mcp",
    "fallback_tools",
    "best_guess_output",
    "output_artifacts",
    "done_when",
}


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run_check(script: str, label: str, failures: list[str]) -> None:
    result = subprocess.run([sys.executable, str(ROOT / script), "--check"], capture_output=True, text=True)
    if result.returncode != 0:
        failures.append(f"{label}: {result.stderr.strip()}")
    else:
        print(f"  OK: {label} are current.")


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    body = text.split("---\n", 2)[1]
    fields: dict[str, str] = {}
    for line in body.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_role_and_skill_contracts(failures: list[str]) -> None:
    for toml_path in discover_toml_paths(ROOT):
        data = load_toml(toml_path)
        role = data["name"]
        mcp_servers = set(data.get("capabilities", {}).get("mcp_servers", []))
        for server in mcp_servers:
            expect(server in KNOWN_MCP_SERVERS, f"{role}: unknown mcp_server '{server}'.", failures)

        if role in EXCLUDED_ROLES:
            continue

        skills_dir = toml_path.parent / "skills"
        skill_files = sorted(skills_dir.rglob("*.md"))
        expect(4 <= len(skill_files) <= 8, f"{role}: must have 4-8 core skills; found {len(skill_files)}.", failures)

        for skill_path in skill_files:
            fields = parse_front_matter(skill_path)
            missing = REQUIRED_SKILL_FIELDS - set(fields)
            expect(not missing, f"{role}: {skill_path.name} missing fields: {', '.join(sorted(missing))}.", failures)
            expect(skill_path.stem not in BANNED_SKILL_NAMES, f"{role}: banned thin-wrapper skill remains: {skill_path.name}.", failures)

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
