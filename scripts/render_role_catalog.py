#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import DISCIPLINE_LABELS, DISCIPLINE_ORDER, load_roles


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "references" / "role-catalog.md"


def repo_write_phrase(policy: str) -> str:
    if policy == "explicit_owner_only":
        return "only when explicitly assigned implementation ownership for a bounded repo scope"
    if policy == "direct_only":
        return "direct execution only"
    return "never in staffed workflows"


def render_catalog(root: Path = ROOT) -> str:
    roles = load_roles(root)
    lines = [
        "# Role Catalog",
        "",
        "This is the canonical staffed-role catalog for Product Team orchestration decisions.",
        "",
        "- Route by real job function, not by abstract discipline labels alone.",
        "- Staff the minimum viable role set and assign exact `skill_paths` instead of vague domain ownership.",
        "- `reference` remains a helper role for grounding, tracing, reuse, and verification; it is not a staffed specialist.",
        "- Every staffed role is skill-first and MCP-first: primary MCP -> alternative tool/MCP -> best guess inferred output.",
        "",
    ]

    for discipline in DISCIPLINE_ORDER:
        lines.append(f"## {DISCIPLINE_LABELS[discipline]}")
        lines.append("")
        for entry in (role for role in roles if role.discipline == discipline):
            role_tag = "reviewer" if entry.role_kind == "reviewer" else "executor"
            owns = ", ".join(entry.owns[:3])
            lines.append(
                f"- `{entry.name}` ({entry.display_name}, {role_tag}) — "
                f"Why: {entry.description}. Owns: {owns}. Repo writes: {repo_write_phrase(entry.repo_write_policy)}."
            )
        lines.append("")

    lines.extend(
        [
            "## Common Team Patterns",
            "",
            "- **Research-heavy discovery**: `ux-researcher` -> `product-designer` -> `product-lead`",
            "- **Greenfield visual concept**: `product-designer` -> `ui-designer` -> `frontend-engineer` -> `design-reviewer`",
            "- **Feature delivery**: `product-lead` -> `product-designer` or `ui-designer` -> `frontend-engineer` or `backend-engineer` -> `qa-reviewer`",
            "- **Design system work**: `design-systems-designer` -> `frontend-engineer` -> `design-reviewer`",
            "- **Platform change**: `platform-engineer` -> `qa-reviewer`",
            "- **Go-to-market launch**: `product-lead` + `go-to-market` + `analyst`",
            "",
            "## Sequencing Rules",
            "",
            "- Product framing before downstream execution when requirements are still ambiguous.",
            "- Research before product/UI design when the user problem is not yet well grounded.",
            "- Product/UI/content design before frontend implementation when user-facing behavior is still open.",
            "- Backend and platform work may run in parallel only with disjoint ownership and explicit contracts.",
            "- Design review and QA review happen after executor outputs exist; reviewers do not fix the work themselves.",
            "- Only one explicit repo implementation owner exists per stage by default.",
            "",
            "## Skill Routing",
            "",
            "- Roles are selected first by job function, then by exact `skill_paths`.",
            "- Do not assign a role without also assigning the core action it must execute.",
            "- Use `ui-designer` for Stitch-first concept work, `design-systems-designer` for token/library governance, `ux-researcher` for research operations and synthesis, and `qa-reviewer` for release readiness.",
            "",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the Product Team role catalog.")
    parser.add_argument("--write", action="store_true", help="Write the rendered catalog.")
    parser.add_argument("--check", action="store_true", help="Fail if the catalog is stale.")
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
