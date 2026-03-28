#!/usr/bin/env python3
"""Render lightweight role-local skill catalogs for fast skill scanning."""

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


def catalog_path_for(toml_path: Path) -> Path:
    return toml_path.parent / "skill-catalog.md"


def parse_front_matter(markdown: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(markdown)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("-"):
            continue
        field_match = FIELD_RE.match(line)
        if not field_match:
            continue
        value = field_match.group("value").strip()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        fields[field_match.group("key")] = value
    return fields


def skill_summary(skill_path: Path) -> tuple[str, str]:
    markdown = skill_path.read_text(encoding="utf-8")
    fields = parse_front_matter(markdown)
    name = fields.get("name", skill_path.stem).strip()
    description = fields.get("description", "").strip()
    if not description:
        raise ValueError(f"Missing description in {skill_path}")
    return name, description.rstrip(".") + "."


def grouped_skill_paths(skills_dir: Path, data: dict) -> list[tuple[str | None, list[Path]]]:
    configured_groups = data.get("capabilities", {}).get("skill_groups", {})
    groups: list[tuple[str | None, list[Path]]] = []
    seen: set[Path] = set()

    for group_name, skill_names in configured_groups.items():
        group_dir = skills_dir / group_name
        paths: list[Path] = []
        for skill_name in skill_names:
            skill_path = group_dir / f"{skill_name}.md"
            if skill_path.exists():
                paths.append(skill_path)
                seen.add(skill_path)
        if paths:
            groups.append((group_name, paths))

    ungrouped = sorted(
        (
            path
            for path in skills_dir.rglob("*.md")
            if path.name != ".DS_Store" and path not in seen
        ),
        key=lambda path: path.relative_to(skills_dir).as_posix(),
    )
    if ungrouped:
        groups.append((None, ungrouped))

    return groups


def render_catalog_for_toml(toml_path: Path) -> str:
    data = load_toml(toml_path)
    display_name = data["display_name"]
    role_name = data["name"]
    skills_dir = toml_path.parent / "skills"
    role_kind = data.get("execution_policy", {}).get("role_kind")
    first_read_line = "Read this file first when you are staffed for orchestrated work."
    if role_kind == "orchestrator":
        first_read_line = "Read this file first on every request before meaningful work."

    lines = [
        f"# {display_name} Skill Catalog",
        "",
        first_read_line,
        "It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.",
        "Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`",
        "",
    ]

    if not skills_dir.is_dir():
        lines.append(f"`{role_name}` has no role-local `skills/` directory.")
        return "\n".join(lines).rstrip() + "\n"

    groups = grouped_skill_paths(skills_dir, data)
    if not groups:
        lines.append(f"`{role_name}` has no role-local markdown skills yet.")
        return "\n".join(lines).rstrip() + "\n"

    for group_name, skill_paths in groups:
        if group_name is None:
            lines.append("## Additional Skills")
        else:
            lines.append(f"## {group_name}/")
        lines.append("")
        for skill_path in skill_paths:
            _, description = skill_summary(skill_path)
            relative = skill_path.relative_to(skills_dir).with_suffix("").as_posix()
            lines.append(f"- `{relative}` — {description}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render per-role skill catalogs.")
    parser.add_argument("--write", action="store_true", help="Write catalogs in place.")
    parser.add_argument("--check", action="store_true", help="Fail if catalogs are missing or stale.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    toml_paths = discover_toml_paths(ROOT)
    stale: list[str] = []
    updated = 0

    for toml_path in toml_paths:
        rendered = render_catalog_for_toml(toml_path)
        catalog_path = catalog_path_for(toml_path)
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
        print(f"All {len(toml_paths)} skill catalogs are current.")
        return 0

    if args.write:
        print(f"Updated {updated} of {len(toml_paths)} skill catalogs.")
        return 0

    print(f"All {len(toml_paths)} skill catalogs already match the renderer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
