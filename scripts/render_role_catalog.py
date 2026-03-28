#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import DISCIPLINE_LABELS, DISCIPLINE_ORDER, load_roles


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "references" / "role-catalog.md"


def list_phrase(items: tuple[str, ...], limit: int = 3) -> str:
    selected = [item.strip().rstrip(".") for item in items if item.strip()][:limit]
    if not selected:
        return "specialist work in this area"
    if len(selected) == 1:
        return selected[0]
    if len(selected) == 2:
        return f"{selected[0]} and {selected[1]}"
    return f"{selected[0]}, {selected[1]}, and {selected[2]}"


def render_catalog(root: Path = ROOT) -> str:
    roles = load_roles(root)
    lines = [
        "# Role Catalog",
        "",
        "This is the canonical archetype catalog for orchestrator staffing decisions when orchestration is actually warranted.",
        "",
        "- Route by domain first.",
        "- If the task is clearly single-domain, consult only the relevant discipline slice before staffing.",
        "- Read the full catalog only when the work is ambiguous, cross-functional, or the right team is genuinely unclear.",
        "- `orchestrator` and `reference` are intentionally excluded because they are workflow support roles, not staffed archetypes.",
        "- Each archetype organizes skills into discipline groups and routes internally, so one staffed role can cover multiple specialties without handoff.",
        f"- Generated from the managed archetype TOMLs under `agents/`. Refresh with `python3 {Path('scripts/render_role_catalog.py').as_posix()} --write`.",
        "",
    ]

    for discipline in DISCIPLINE_ORDER:
        lines.append(f"## {DISCIPLINE_LABELS[discipline]}")
        lines.append("")

        for entry in (role for role in roles if role.discipline == discipline):
            role_tag = "reviewer" if entry.role_kind == "reviewer" else "executor"
            lines.append(
                f"- `{entry.name}` ({entry.display_name}, {role_tag}) — "
                f"Why: {entry.description}. "
                f"Owns: {list_phrase(entry.owns)}."
            )

        lines.append("")

    # -- Common Team Patterns --
    lines.append("## Common Team Patterns")
    lines.append("")
    lines.append(
        "These patterns help the orchestrator staff teams for frequent task types. "
        "They are starting points, not rigid requirements — always assess actual role needs. "
        "Each archetype routes internally to the right discipline group, so a single `designer` "
        "handles research → UX → UI → content without separate handoffs."
    )
    lines.append("")
    lines.append("- **UI Feature**: `designer` → `engineer` (+ `reviewer` for complex flows)")
    lines.append("- **API Feature**: `engineer` + `platform-engineer` (+ `reviewer`)")
    lines.append("- **Full Feature**: `product-lead` → `designer` → `engineer` (+ `reviewer`)")
    lines.append("- **Design System Update**: `design-systems` (+ `reviewer`)")
    lines.append("- **Data Pipeline**: `platform-engineer` (+ `reviewer`)")
    lines.append("- **Growth Initiative**: `go-to-market` + `analyst` + `product-lead`")
    lines.append("- **Infrastructure Change**: `platform-engineer` (+ `reviewer`)")
    lines.append("- **Mobile Feature**: `designer` → `engineer` (+ `reviewer`)")
    lines.append("- **Content Update**: `designer` (content/ + localization/ discipline groups)")
    lines.append("- **Strategy**: `product-lead` + `analyst`")
    lines.append("")

    # -- Sequencing Rules --
    lines.append("## Sequencing Rules")
    lines.append("")
    lines.append("- Product-lead before design: designers need approved requirements as input.")
    lines.append("- Design before engineering: engineers implement from approved design, not the reverse.")
    lines.append("- Engineering before review: the reviewer is staffed after executors produce artifacts.")
    lines.append("- Reviewers do not execute: the reviewer validates and recommends, it does not fix or reauthor.")
    lines.append("- Each archetype chains discipline groups internally — no handoff needed within a single role.")
    lines.append("")

    # -- Skill Routing --
    lines.append("## Skill Routing")
    lines.append("")
    lines.append("Each archetype organizes skills into discipline groups. The archetype routes internally to the right group:")
    lines.append("")
    lines.append("- `designer`: research/ → ux/ → ui/ → content/ → motion/ → accessibility/ → architecture/ → localization/ → service/")
    lines.append("- `design-systems`: system/ → technology/ → direction/ → operations/")
    lines.append("- `product-lead`: strategy/ → product/ → portfolio/ → requirements/")
    lines.append("- `analyst`: data/ → financial/ → revenue/")
    lines.append("- `go-to-market`: growth/ → marketing/ → product-marketing/ → partnerships/ → customer-success/ → sales/")
    lines.append("- `business-ops`: analysis/ → operations/")
    lines.append("- `engineer`: frontend/ → backend/ → fullstack/ → mobile/ → ml/ → implementation/")
    lines.append("- `platform-engineer`: api/ → database/ → data/ → devops/ → performance/ → security/ → architecture/ → leadership/")
    lines.append("- `reviewer`: requirements/ → ux-flow/ → usability/ → copy/ → design-system/ → engineering/ → qa/")
    lines.append("")

    # -- Conflict Resolution --
    lines.append("## Conflict Resolution")
    lines.append("")
    lines.append("When archetypes produce conflicting advice or deliverables:")
    lines.append("")
    lines.append("1. Both positions are documented in `decisions/<topic>.md` with rationale.")
    lines.append("2. The orchestrator consults the archetype whose ownership area covers the disputed scope.")
    lines.append("3. The orchestrator makes a binding decision, updates `03_unified-plan.md`, and records the resolution in `decisions/`.")
    lines.append("4. Overruled archetypes acknowledge the decision and align their work accordingly.")
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
