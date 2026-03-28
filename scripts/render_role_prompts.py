#!/usr/bin/env python3
"""Render managed archetype system_prompt fields from TOML metadata and the shared baseline template."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import EXCLUDED_ROLES, discover_toml_paths, load_toml


ROOT = Path(__file__).resolve().parents[1]

UNIVERSAL_GUARDRAILS = {
    "Skip the mandatory fit-check protocol",
    "Silently accept a mismatched assignment or missing dependency",
    "Bypass the orchestrator for staffing, sequencing, or approval decisions",
    "Start substantial execution before the orchestrator approval gate when one is required",
    "Start substantial execution before the orchestrator signals execution when an approval gate is in place",
}

NEVER_LINE = (
    "Never: silently accept a mismatched assignment, bypass the orchestrator for "
    "staffing/sequencing/approval, rework another role's approved artifacts without "
    "orchestrator direction, or add planning ceremony the task does not need."
)

SYSTEM_PROMPT_RE = re.compile(
    r'(system_prompt\s*=\s*""")\n.*?(""")',
    re.DOTALL,
)


def render_skill_routing(skill_groups: dict[str, list[str]]) -> str:
    """Render skill routing section from skill_groups config."""
    if not skill_groups:
        return ""
    lines = [
        "",
        "Skill routing — select the right discipline group for each part of the task:",
    ]
    for group_name, skills in skill_groups.items():
        skills_str = ", ".join(skills)
        lines.append(f"- {group_name}/ → {skills_str}.")
    lines.append("")
    lines.append("You may chain multiple discipline groups in a single execution without handoff.")
    return "\n".join(lines)


def render_prompt(data: dict) -> str:
    display_name = data["display_name"]
    description = data["description"].strip().rstrip(".")
    role_name = data["name"]
    owns = data["role_boundary"]["owns"]
    role_kind = data["execution_policy"]["role_kind"]
    must_not_do = data["role_boundary"].get("must_not_do", [])

    owns_str = ", ".join(owns)

    role_guardrails = [g for g in must_not_do if g not in UNIVERSAL_GUARDRAILS]
    guardrail_bullets = "\n".join(f"- {g}" for g in role_guardrails)

    if role_kind == "reviewer":
        output_type = "reviews"
        reviewer_extra = " Write review output only when the orchestrator requests a review pass."
    else:
        output_type = "deliverables"
        reviewer_extra = ""

    # Build skill routing section if skill_groups exist
    skill_groups = data.get("capabilities", {}).get("skill_groups", {})
    skill_routing = render_skill_routing(skill_groups)

    prompt = f"""
You are the {display_name} in the direct-first orchestrator workflow.

Role charter:
- {description}.
- Primary ownership: {owns_str}.
- Work only from orchestrator-issued assignments for the active project at `logs/active/<project-slug>/`.
- Before meaningful work, quickly read the `skill-catalog.md` file in your own role folder. This is mandatory and is the fast scan for this role's local skills only.
{skill_routing}
Default behavior:
- Start from the orchestrator-issued assignment and execute within your owned scope.
- Use `skill-catalog.md` to identify matching role-local skills, then open only the matching `skills/*.md` files instead of reading the whole skill tree.
- If the assignment is clearly mismatched, blocked by missing inputs, or overlaps another role, stop and return a brief mismatch note for `02_staffing.md` with the reason and recommended adjustment.
- Only write `logs/active/<project-slug>/plans/{role_name}.md` when the orchestrator explicitly asks for advisory planning or sequencing input.
- If an approval gate is in place, wait for the orchestrator to signal execution before substantial work begins.

When advisory planning is requested: write `logs/active/<project-slug>/plans/{role_name}.md` covering objective, assumptions, scope, steps, deliverables, dependencies, risks, and status. Plans are optional specialist input — the orchestrator decides whether to merge them into `03_unified-plan.md`.

During execution: follow the current orchestrator direction, keep `logs/active/<project-slug>/{output_type}/{role_name}.md` current.{reviewer_extra} Escalate blockers, conflicts, ambiguous ownership, and material scope changes to the orchestrator. In your closing handoff, append `Read <skill-paths> skills for this task.` with the role-local skills you opened from `skills/`; if none matched, append `Read no additional role-local skills for this task.`

Guardrails:
{guardrail_bullets}
- {NEVER_LINE}
"""
    return prompt


def update_toml_text(original: str, new_prompt: str) -> str:
    def replacer(match: re.Match[str]) -> str:
        return f'{match.group(1)}\n{new_prompt.rstrip()}\n{match.group(2)}'

    result, count = SYSTEM_PROMPT_RE.subn(replacer, original, count=1)
    if count == 0:
        raise ValueError("Could not find system_prompt = \"\"\"...\"\"\" block in TOML")
    return result


def discover_specialist_tomls(root: Path = ROOT) -> list[Path]:
    paths: list[Path] = []
    for toml_path in discover_toml_paths(root):
        data = load_toml(toml_path)
        if data["name"] not in EXCLUDED_ROLES:
            paths.append(toml_path)
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render managed archetype system_prompt fields from TOML metadata."
    )
    parser.add_argument(
        "--write", action="store_true",
        help="Update each TOML's system_prompt in place.",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Fail if any TOML's system_prompt does not match the rendered version.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    toml_paths = discover_specialist_tomls(ROOT)
    stale: list[str] = []
    updated = 0

    for path in toml_paths:
        original_text = path.read_text(encoding="utf-8")
        data = load_toml(path)
        rendered = render_prompt(data)
        new_text = update_toml_text(original_text, rendered)

        if original_text == new_text:
            continue

        if args.check:
            stale.append(data["name"])
            continue

        if args.write:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
        else:
            print(f"--- {data['name']} (would update)")
            print(rendered)

    if args.check:
        if stale:
            print(
                f"FAIL: {len(stale)} managed archetype role(s) have stale system_prompt: {', '.join(stale)}. "
                "Run `python3 scripts/render_role_prompts.py --write`.",
                file=sys.stderr,
            )
            return 1
        print(f"All {len(toml_paths)} managed archetype prompts are current.")
        return 0

    if args.write:
        print(f"Updated {updated} of {len(toml_paths)} managed archetype prompts.")
        return 0

    if not stale and updated == 0:
        print(f"All {len(toml_paths)} specialist prompts already match the template.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
