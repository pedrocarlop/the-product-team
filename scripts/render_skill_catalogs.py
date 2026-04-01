#!/usr/bin/env python3
"""Render skill catalogs for managed Product Team roles."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.+?)\s*$")


def parse_front_matter(markdown: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(markdown)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        field_match = FIELD_RE.match(line)
        if not field_match:
            continue
        value = field_match.group("value").strip()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        fields[field_match.group("key")] = value
    return fields


def render_catalog_for_toml(toml_path: Path) -> str:
    data = load_toml(toml_path)
    display_name = data["display_name"]
    role_name = data["name"]
    role_kind = data["execution_policy"]["role_kind"]
    skills_dir = toml_path.parent / "skills"
    first_line = "Read this file first on every request before meaningful work." if role_kind == "orchestrator" else "Read this file first when you are staffed for orchestrated work."

    lines = [
        f"# {display_name} Skill Catalog",
        "",
        first_line,
        "Use this catalog to choose or confirm the exact role-local workflow to run.",
        "Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`",
        "",
    ]

    if not skills_dir.is_dir():
        lines.append(f"`{role_name}` has no role-local `skills/` directory.")
        return "\n".join(lines).rstrip() + "\n"

    for skill_path in sorted(skills_dir.rglob("*.md"), key=lambda path: path.relative_to(skills_dir).as_posix()):
        fields = parse_front_matter(skill_path.read_text(encoding="utf-8"))
        relative = skill_path.relative_to(skills_dir).with_suffix("").as_posix()
        lines.append(f"## `{relative}`")
        lines.append("")
        lines.append(f"- Description: {fields.get('description', 'Missing description.')}")
        lines.append(f"- Trigger: {fields.get('trigger', 'Missing trigger.')}")
        lines.append(f"- Primary MCP/tool: {fields.get('primary_mcp', 'Missing primary_mcp.')}")
        lines.append(f"- Fallback: {fields.get('fallback_tools', 'Missing fallback_tools.')}")
        lines.append(f"- Best guess: {fields.get('best_guess_output', 'Missing best_guess_output.')}")
        lines.append(f"- Output: {fields.get('output_artifacts', 'Missing output_artifacts.')}")
        lines.append(f"- Done when: {fields.get('done_when', 'Missing done_when.')}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render per-role skill catalogs.")
    parser.add_argument("--write", action="store_true", help="Write catalogs in place.")
    parser.add_argument("--check", action="store_true", help="Fail if catalogs are stale.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    stale: list[str] = []
    updated = 0

    for toml_path in discover_toml_paths(ROOT):
        catalog_path = toml_path.parent / "skill-catalog.md"
        rendered = render_catalog_for_toml(toml_path)
        current = catalog_path.read_text(encoding="utf-8") if catalog_path.exists() else None

        if current == rendered:
            continue

        role_name = load_toml(toml_path)["name"]
        if args.check:
            stale.append(role_name)
            continue

        if args.write:
            catalog_path.write_text(rendered, encoding="utf-8")
            updated += 1
        else:
            print(f"--- {role_name} (would update)")
            print(rendered)

    if args.check:
        if stale:
            print(
                f"FAIL: {len(stale)} skill catalog(s) are missing or stale: {', '.join(stale)}. "
                "Run `python3 scripts/render_skill_catalogs.py --write`.",
                file=sys.stderr,
            )
            return 1
        print("Managed skill catalogs are current.")
        return 0

    if args.write:
        print(f"Updated {updated} of {len(discover_toml_paths(ROOT))} skill catalogs.")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
