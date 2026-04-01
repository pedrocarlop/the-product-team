#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.skill_validation import SkillValidationContext, validate_skill_contexts


def build_context(
    *,
    discipline: str,
    role_name: str,
    mcp_servers: tuple[str, ...],
    web_tools: tuple[str, ...],
    skill_files: tuple[Path, ...],
) -> SkillValidationContext:
    return SkillValidationContext(
        discipline=discipline,
        role_name=role_name,
        mcp_servers=mcp_servers,
        web_tools=web_tools,
        skill_files=skill_files,
    )


def run_validation(context: SkillValidationContext) -> list[str]:
    failures: list[str] = []
    validate_skill_contexts([context], failures, enforce_banned_names=False)
    return failures


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


BUSINESS_VALID_SKILL_TEMPLATE = """---
name: {skill_name}
description: Example business skill.
trigger: When the example scenario applies.
primary_mcp: notion
fallback_tools: search_query
best_guess_output: An example output.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: {skill_name}"
done_when: The example is complete.
---

# Example Skill

## Purpose

Example purpose.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: {skill_name}`, include:
- `### Problem statement`
- `### Objective and success criteria`
- `### Constraints and non-goals`
- `### Decision frame`
- `### Open questions`

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query`.
- If both paths fail, produce the best-guess output described as: An example output.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Example notes.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: {skill_name}`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The example is complete.
"""


ENGINEER_VALID_SKILL_TEMPLATE = """---
name: {skill_name}
description: Example engineer skill.
trigger: When the example scenario applies.
primary_mcp: repository
fallback_tools: search_query
best_guess_output: An example output.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: {skill_name}"
done_when: The example is complete.
---

# Example Skill

## Purpose

Example purpose.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: {skill_name}`, include:
- `### Design target`
- `### Implementation scope`
- `### State coverage`
- `### Interaction notes`
- `### Code touchpoints`
- `### Open implementation risks`

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query`.
- If both paths fail, produce the best-guess output described as: An example output.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Example notes.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: {skill_name}`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The example is complete.
"""


def run_business_scenarios(root: Path, scenario_failures: list[str]) -> None:
    context = build_context(
        discipline="business",
        role_name="product-lead",
        mcp_servers=("notion", "linear"),
        web_tools=("search_query",),
        skill_files=(),
    )

    valid_a = root / "frame-problem.md"
    valid_b = root / "write-prd.md"
    valid_a.write_text(BUSINESS_VALID_SKILL_TEMPLATE.format(skill_name="frame-problem"), encoding="utf-8")
    valid_b.write_text(
        BUSINESS_VALID_SKILL_TEMPLATE.format(skill_name="write-prd").replace(
            "- `### Problem statement`\n"
            "- `### Objective and success criteria`\n"
            "- `### Constraints and non-goals`\n"
            "- `### Decision frame`\n"
            "- `### Open questions`",
            "- `### Objective`\n"
            "- `### Scope`\n"
            "- `### Non-goals`\n"
            "- `### Key scenarios`\n"
            "- `### Requirements and decisions`\n"
            "- `### Acceptance criteria`\n"
            "- `### Dependencies and risks`\n"
            "- `### Open questions`",
        ),
        encoding="utf-8",
    )

    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(valid_a, valid_b),
        )
    )
    expect(not failures, f"Expected valid business skills to pass, got: {failures}", scenario_failures)

    missing_anchor = root / "missing-anchor.md"
    missing_anchor.write_text(
        BUSINESS_VALID_SKILL_TEMPLATE.format(skill_name="frame-problem").replace(
            'section_anchor: "## Skill: frame-problem"\n',
            "",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(missing_anchor,),
        )
    )
    expect(
        any("must declare section_anchor" in failure for failure in failures),
        f"Expected missing business section_anchor failure, got: {failures}",
        scenario_failures,
    )

    duplicate_a = root / "duplicate-a.md"
    duplicate_b = root / "duplicate-b.md"
    duplicate_a.write_text(BUSINESS_VALID_SKILL_TEMPLATE.format(skill_name="frame-problem"), encoding="utf-8")
    duplicate_b.write_text(
        BUSINESS_VALID_SKILL_TEMPLATE.format(skill_name="write-prd").replace(
            'section_anchor: "## Skill: write-prd"',
            'section_anchor: "## Skill: frame-problem"',
        ).replace(
            "- `### Problem statement`\n"
            "- `### Objective and success criteria`\n"
            "- `### Constraints and non-goals`\n"
            "- `### Decision frame`\n"
            "- `### Open questions`",
            "- `### Objective`\n"
            "- `### Scope`\n"
            "- `### Non-goals`\n"
            "- `### Key scenarios`\n"
            "- `### Requirements and decisions`\n"
            "- `### Acceptance criteria`\n"
            "- `### Dependencies and risks`\n"
            "- `### Open questions`",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(duplicate_a, duplicate_b),
        )
    )
    expect(
        any("duplicates section_anchor" in failure for failure in failures),
        f"Expected duplicate business section_anchor failure, got: {failures}",
        scenario_failures,
    )


def run_engineer_scenarios(root: Path, scenario_failures: list[str]) -> None:
    context = build_context(
        discipline="engineer",
        role_name="frontend-engineer",
        mcp_servers=("figma", "chrome_devtools", "github", "linear"),
        web_tools=("search_query",),
        skill_files=(),
    )

    valid_a = root / "implement-from-design.md"
    valid_b = root / "frontend-verify.md"
    valid_a.write_text(ENGINEER_VALID_SKILL_TEMPLATE.format(skill_name="implement-from-design"), encoding="utf-8")
    valid_b.write_text(
        ENGINEER_VALID_SKILL_TEMPLATE.format(skill_name="frontend-verify").replace(
            "- `### Design target`\n"
            "- `### Implementation scope`\n"
            "- `### State coverage`\n"
            "- `### Interaction notes`\n"
            "- `### Code touchpoints`\n"
            "- `### Open implementation risks`",
            "- `### Verification scope`\n"
            "- `### Behavior checks`\n"
            "- `### Layout and responsive checks`\n"
            "- `### Accessibility or quality checks`\n"
            "- `### Findings`\n"
            "- `### Residual risk`",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(valid_a, valid_b),
        )
    )
    expect(not failures, f"Expected valid engineer skills to pass, got: {failures}", scenario_failures)

    missing_anchor = root / "engineer-missing-anchor.md"
    missing_anchor.write_text(
        ENGINEER_VALID_SKILL_TEMPLATE.format(skill_name="implement-from-design").replace(
            'section_anchor: "## Skill: implement-from-design"\n',
            "",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(missing_anchor,),
        )
    )
    expect(
        any("must declare section_anchor" in failure for failure in failures),
        f"Expected missing engineer section_anchor failure, got: {failures}",
        scenario_failures,
    )

    duplicate_a = root / "engineer-duplicate-a.md"
    duplicate_b = root / "engineer-duplicate-b.md"
    duplicate_a.write_text(ENGINEER_VALID_SKILL_TEMPLATE.format(skill_name="implement-from-design"), encoding="utf-8")
    duplicate_b.write_text(
        ENGINEER_VALID_SKILL_TEMPLATE.format(skill_name="frontend-verify").replace(
            'section_anchor: "## Skill: frontend-verify"',
            'section_anchor: "## Skill: implement-from-design"',
        ).replace(
            "- `### Design target`\n"
            "- `### Implementation scope`\n"
            "- `### State coverage`\n"
            "- `### Interaction notes`\n"
            "- `### Code touchpoints`\n"
            "- `### Open implementation risks`",
            "- `### Verification scope`\n"
            "- `### Behavior checks`\n"
            "- `### Layout and responsive checks`\n"
            "- `### Accessibility or quality checks`\n"
            "- `### Findings`\n"
            "- `### Residual risk`",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=context.discipline,
            role_name=context.role_name,
            mcp_servers=context.mcp_servers,
            web_tools=context.web_tools,
            skill_files=(duplicate_a, duplicate_b),
        )
    )
    expect(
        any("duplicates section_anchor" in failure for failure in failures),
        f"Expected duplicate engineer section_anchor failure, got: {failures}",
        scenario_failures,
    )


def main() -> int:
    scenario_failures: list[str] = []

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        run_business_scenarios(root, scenario_failures)
        run_engineer_scenarios(root, scenario_failures)

    if scenario_failures:
        for failure in scenario_failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Skill validation scenario checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
