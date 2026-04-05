#!/usr/bin/env python3
"""Render the agent roster section of AGENTS.md from TOML role definitions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import DISCIPLINE_LABELS, DISCIPLINE_ORDER, discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]
AGENTS_MD_PATH = ROOT / "AGENTS.md"

START_MARKER = "<!-- AGENT_ROSTER:START -->"
END_MARKER = "<!-- AGENT_ROSTER:END -->"

# Extend discipline labels to include orchestrator and reference roles.
ALL_DISCIPLINE_ORDER = ("orchestrator",) + DISCIPLINE_ORDER
ALL_DISCIPLINE_LABELS = {
    **DISCIPLINE_LABELS,
    "orchestrator": "Orchestrator",
}


def repo_write_phrase(policy: str) -> str:
    if policy == "explicit_owner_only":
        return "scoped"
    if policy == "direct_only":
        return "direct"
    return "never"


def count_skills(toml_path: Path) -> int:
    skills_dir = toml_path.parent / "skills"
    if not skills_dir.is_dir():
        return 0
    return len(list(skills_dir.glob("*.md")))


def render_roster(root: Path = ROOT) -> str:
    toml_paths = discover_toml_paths(root)

    # Group roles by discipline.
    by_discipline: dict[str, list[dict]] = {d: [] for d in ALL_DISCIPLINE_ORDER}

    for path in toml_paths:
        data = load_toml(path)
        discipline = path.parent.parent.name
        if discipline not in by_discipline:
            continue
        by_discipline[discipline].append(
            {
                "name": data["name"],
                "display_name": data["display_name"],
                "description": data["description"].strip().rstrip("."),
                "discipline": discipline,
                "role_kind": data["execution_policy"]["role_kind"],
                "repo_write_policy": data["execution_policy"].get("repo_write_policy", "never"),
                "skills": count_skills(path),
            }
        )

    lines = [
        START_MARKER,
        "",
        "| Role | Display Name | Discipline | Kind | Skills | Repo Writes | Description |",
        "| ---- | ------------ | ---------- | ---- | -----: | ----------- | ----------- |",
    ]

    for discipline in ALL_DISCIPLINE_ORDER:
        for entry in by_discipline[discipline]:
            lines.append(
                f"| `{entry['name']}` "
                f"| {entry['display_name']} "
                f"| {ALL_DISCIPLINE_LABELS[discipline]} "
                f"| {entry['role_kind']} "
                f"| {entry['skills']} "
                f"| {repo_write_phrase(entry['repo_write_policy'])} "
                f"| {entry['description']} |"
            )

    lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)


def inject_roster(full_text: str, roster: str) -> str:
    start_idx = full_text.find(START_MARKER)
    end_idx = full_text.find(END_MARKER)

    if start_idx == -1 or end_idx == -1:
        raise ValueError(
            f"AGENTS.md is missing roster markers ({START_MARKER} / {END_MARKER}). "
            "Add them manually before running this script."
        )

    return full_text[:start_idx] + roster + full_text[end_idx + len(END_MARKER):]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the AGENTS.md agent roster.")
    parser.add_argument("--write", action="store_true", help="Update AGENTS.md in place.")
    parser.add_argument("--check", action="store_true", help="Fail if AGENTS.md roster is stale.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roster = render_roster(ROOT)

    if not AGENTS_MD_PATH.exists():
        print(f"FAIL: Missing AGENTS.md: {AGENTS_MD_PATH}", file=sys.stderr)
        return 1

    current_text = AGENTS_MD_PATH.read_text(encoding="utf-8")
    updated_text = inject_roster(current_text, roster)

    if args.check:
        if current_text != updated_text:
            print(
                "FAIL: AGENTS.md agent roster is out of date. "
                "Run `python3 scripts/render_agents_md.py --write`.",
                file=sys.stderr,
            )
            return 1
        print("AGENTS.md agent roster is current.")
        return 0

    if args.write:
        AGENTS_MD_PATH.write_text(updated_text, encoding="utf-8")
        print(f"Wrote {AGENTS_MD_PATH}")
        return 0

    sys.stdout.write(roster + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
