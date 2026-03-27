#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "references" / "role-catalog.md"
DISCIPLINE_ORDER = ("business", "design", "engineer")
DISCIPLINE_LABELS = {
    "business": "Business Roles",
    "design": "Design Roles",
    "engineer": "Engineering Roles",
}
EXCLUDED_ROLES = {"orchestrator", "reference"}


@dataclass(frozen=True)
class RoleEntry:
    discipline: str
    name: str
    display_name: str
    description: str
    owns: tuple[str, ...]
    role_kind: str


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def load_roles(root: Path = ROOT) -> list[RoleEntry]:
    roles: list[RoleEntry] = []

    for discipline in DISCIPLINE_ORDER:
        for path in sorted((root / "agents" / discipline).glob("*/*.toml")):
            data = load_toml(path)
            role_name = data["name"]
            if role_name in EXCLUDED_ROLES:
                continue

            roles.append(
                RoleEntry(
                    discipline=discipline,
                    name=role_name,
                    display_name=data["display_name"],
                    description=data["description"].strip().rstrip("."),
                    owns=tuple(data["role_boundary"]["owns"]),
                    role_kind=data["execution_policy"]["role_kind"],
                )
            )

    return roles


def list_phrase(items: tuple[str, ...], limit: int = 3) -> str:
    selected = [item.strip().rstrip(".") for item in items if item.strip()][:limit]
    if not selected:
        return "specialist work in this area"
    if len(selected) == 1:
        return selected[0]
    if len(selected) == 2:
        return f"{selected[0]} and {selected[1]}"
    return f"{selected[0]}, {selected[1]}, and {selected[2]}"


def useful_for(entry: RoleEntry) -> str:
    owned_scope = list_phrase(entry.owns, limit=3)
    if entry.role_kind == "reviewer":
        return f"review passes on {owned_scope}"
    return f"direct ownership of {owned_scope}"


def render_catalog(root: Path = ROOT) -> str:
    roles = load_roles(root)
    lines = [
        "# Role Catalog",
        "",
        "This is the canonical specialist-role catalog for orchestrator staffing decisions.",
        "",
        "- Read the full catalog before any best-team assessment or staffing decision.",
        "- Review every business, design, and engineering role before narrowing the team.",
        "- `orchestrator` and `reference` are intentionally excluded because they are workflow support roles, not staffed specialists.",
        f"- Generated from `agents/*/*/*.toml`. Refresh with `python3 {Path('scripts/render_role_catalog.py').as_posix()} --write`.",
        "",
    ]

    for discipline in DISCIPLINE_ORDER:
        lines.append(f"## {DISCIPLINE_LABELS[discipline]}")
        lines.append("")

        for entry in (role for role in roles if role.discipline == discipline):
            lines.append(
                f"- `{entry.name}` ({entry.display_name}) — "
                f"Why: {entry.description}. "
                f"Does: {list_phrase(entry.owns)}. "
                f"Useful for: {useful_for(entry)}."
            )

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the Product Team role catalog.")
    parser.add_argument("--write", action="store_true", help="Write the rendered catalog to references/role-catalog.md.")
    parser.add_argument("--check", action="store_true", help="Fail if references/role-catalog.md is missing or stale.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rendered = render_catalog(ROOT)

    if args.check:
        if not CATALOG_PATH.exists():
            print(f"FAIL: Missing role catalog: {CATALOG_PATH}", file=sys.stderr)
            return 1
        current = CATALOG_PATH.read_text(encoding="utf-8")
        if current != rendered:
            print(
                "FAIL: references/role-catalog.md is out of date. "
                "Run `python3 scripts/render_role_catalog.py --write`.",
                file=sys.stderr,
            )
            return 1
        print("Role catalog is current.")
        return 0

    if args.write:
        CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        CATALOG_PATH.write_text(rendered, encoding="utf-8")
        print(f"Wrote {CATALOG_PATH}")
        return 0

    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
