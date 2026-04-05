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
output_artifacts: knowledge/product-lead.md
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

- Write or update `knowledge/product-lead.md`.
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
output_artifacts: knowledge/frontend-engineer.md
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

- Write or update `knowledge/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: {skill_name}`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The example is complete.
"""


def reviewer_skill_template(
    *,
    skill_name: str,
    description: str,
    primary_mcp: str,
    fallback_tools: str,
    output_artifact: str,
    purpose: str,
    required_sections: str,
) -> str:
    return f"""---
name: {skill_name}
description: {description}
trigger: When the example scenario applies.
primary_mcp: {primary_mcp}
fallback_tools: {fallback_tools}
best_guess_output: An example output.
output_artifacts: {output_artifact}
section_anchor: "## Skill: {skill_name}"
done_when: The example is complete.
---

# Example Reviewer Skill

## Purpose

{purpose}

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: {skill_name}`, include:
{required_sections}

## Tool Path

- Start with `{primary_mcp}`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `{fallback_tools}`.
- If both paths fail, produce the best-guess output described as: An example output.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Example notes.

## Output Contract

- Write or update `{output_artifact}`.
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


def run_reviewer_scenarios(root: Path, scenario_failures: list[str]) -> None:
    design_context = build_context(
        discipline="review",
        role_name="design-reviewer",
        mcp_servers=("figma", "chrome_devtools", "github", "notion"),
        web_tools=("search_query", "open"),
        skill_files=(),
    )

    design_valid_a = root / "usability-review.md"
    design_valid_b = root / "design-fidelity-review.md"
    design_valid_a.write_text(
        reviewer_skill_template(
            skill_name="usability-review",
            description="Example reviewer skill.",
            primary_mcp="chrome_devtools",
            fallback_tools="figma, open",
            output_artifact="knowledge/reviews/design-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Review framing`",
                    "- `### Required inputs and assumptions`",
                    "- `### Heuristic framework and evaluator passes`: Use Nielsen 10 usability heuristics.",
                    "- `### Input mode and evidence path`",
                    "- `### Tool selection rationale`",
                    "- `### Environment and reproducibility`",
                    "- `### UI model`",
                    "- `### Task walkthroughs`",
                    "- `### Heuristic findings`",
                    "- `#### Finding <id>`",
                    "- `- Observation:`",
                    "- `- Evidence:`",
                    "- `- Repro steps:`",
                    "- `- Violated heuristic:`",
                    "- `- Likely cause:`",
                    "- `- Severity:`",
                    "- `- Confidence:`",
                    "- `- Recommendation direction:`",
                    "- `### Prioritized findings`",
                    "- `### Systemic patterns`",
                    "- `### Coverage map`",
                    "- `### Severity, confidence, and coverage confidence`",
                    "- `### Directional recommendations`",
                    "- `### Limits and unknowns`",
                    "- Assumed task:",
                    "- merge duplicates and consolidate overlapping findings before prioritization",
                    "- Prefer the highest-fidelity path available",
                    "- Combine tools when useful rather than forcing a single path.",
                    "- Use `axe` as a supporting layer for accessibility violations, never as a substitute for full usability review.",
                ]
            ),
        ),
        encoding="utf-8",
    )
    design_valid_b.write_text(
        reviewer_skill_template(
            skill_name="design-fidelity-review",
            description="Example reviewer skill.",
            primary_mcp="figma, chrome_devtools",
            fallback_tools="open, search_query",
            output_artifact="knowledge/reviews/design-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Review framing`",
                    "- `### Source-of-truth model`",
                    "- `### Surfaces compared`",
                    "- `### Drift taxonomy`",
                    "- `### Key mismatches`",
                    "- `### Systemic drift patterns`",
                    "- `### Severity and implementation risk`",
                    "- `### Exceptions and ambiguities`",
                    "- `### Limits and unknowns`",
                ]
            ),
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=design_context.discipline,
            role_name=design_context.role_name,
            mcp_servers=design_context.mcp_servers,
            web_tools=design_context.web_tools,
            skill_files=(design_valid_a, design_valid_b),
        )
    )
    expect(not failures, f"Expected valid design reviewer skills to pass, got: {failures}", scenario_failures)

    design_missing_anchor = root / "design-reviewer-missing-anchor.md"
    design_missing_anchor.write_text(
        reviewer_skill_template(
            skill_name="usability-review",
            description="Example reviewer skill.",
            primary_mcp="chrome_devtools",
            fallback_tools="figma, open",
            output_artifact="knowledge/reviews/design-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Review framing`",
                    "- `### Required inputs and assumptions`",
                    "- `### Heuristic framework and evaluator passes`: Use Nielsen 10 usability heuristics.",
                    "- `### Input mode and evidence path`",
                    "- `### Tool selection rationale`",
                    "- `### Environment and reproducibility`",
                    "- `### UI model`",
                    "- `### Task walkthroughs`",
                    "- `### Heuristic findings`",
                    "- `#### Finding <id>`",
                    "- `- Observation:`",
                    "- `- Evidence:`",
                    "- `- Repro steps:`",
                    "- `- Violated heuristic:`",
                    "- `- Likely cause:`",
                    "- `- Severity:`",
                    "- `- Confidence:`",
                    "- `- Recommendation direction:`",
                    "- `### Prioritized findings`",
                    "- `### Systemic patterns`",
                    "- `### Coverage map`",
                    "- `### Severity, confidence, and coverage confidence`",
                    "- `### Directional recommendations`",
                    "- `### Limits and unknowns`",
                    "- Assumed task:",
                    "- merge duplicates and consolidate overlapping findings before prioritization",
                    "- Prefer the highest-fidelity path available",
                    "- Combine tools when useful rather than forcing a single path.",
                    "- Use `axe` as a supporting layer for accessibility violations, never as a substitute for full usability review.",
                ]
            ),
        ).replace(
            'section_anchor: "## Skill: usability-review"\n',
            "",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=design_context.discipline,
            role_name=design_context.role_name,
            mcp_servers=design_context.mcp_servers,
            web_tools=design_context.web_tools,
            skill_files=(design_missing_anchor,),
        )
    )
    expect(
        any("must declare section_anchor" in failure for failure in failures),
        f"Expected missing design reviewer section_anchor failure, got: {failures}",
        scenario_failures,
    )

    design_duplicate_a = root / "design-reviewer-duplicate-a.md"
    design_duplicate_b = root / "design-reviewer-duplicate-b.md"
    design_duplicate_a.write_text(design_valid_a.read_text(encoding="utf-8"), encoding="utf-8")
    design_duplicate_b.write_text(
        design_valid_b.read_text(encoding="utf-8").replace(
            'section_anchor: "## Skill: design-fidelity-review"',
            'section_anchor: "## Skill: usability-review"',
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=design_context.discipline,
            role_name=design_context.role_name,
            mcp_servers=design_context.mcp_servers,
            web_tools=design_context.web_tools,
            skill_files=(design_duplicate_a, design_duplicate_b),
        )
    )
    expect(
        any("duplicates section_anchor" in failure for failure in failures),
        f"Expected duplicate design reviewer section_anchor failure, got: {failures}",
        scenario_failures,
    )

    qa_context = build_context(
        discipline="review",
        role_name="qa-reviewer",
        mcp_servers=("chrome_devtools", "github", "notion"),
        web_tools=("search_query", "open"),
        skill_files=(),
    )

    qa_valid_a = root / "requirements-trace-review.md"
    qa_valid_b = root / "release-gate.md"
    qa_valid_a.write_text(
        reviewer_skill_template(
            skill_name="requirements-trace-review",
            description="Example reviewer skill.",
            primary_mcp="repository, logs",
            fallback_tools="open, search_query",
            output_artifact="knowledge/reviews/qa-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Review framing`",
                    "- `### Requirement matrix`",
                    "- `### Surface and flow mapping`",
                    "- `### Confirmed matches`",
                    "- `### Gaps and mismatches`",
                    "- `### Ambiguities and unverified assumptions`",
                    "- `### Priority risks`",
                    "- `### Limits and unknowns`",
                ]
            ),
        ),
        encoding="utf-8",
    )
    qa_valid_b.write_text(
        reviewer_skill_template(
            skill_name="release-gate",
            description="Example reviewer skill.",
            primary_mcp="repository, logs",
            fallback_tools="open, search_query",
            output_artifact="knowledge/reviews/qa-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Gate framing`",
                    "- `### Evidence reviewed`",
                    "- `### Ship recommendation`",
                    "- `### Blocking issues`",
                    "- `### Non-blocking risks`",
                    "- `### Evidence quality and confidence`",
                    "- `### Rollback and readiness posture`",
                    "- `### Required follow-up`",
                    "- `### Limits and unknowns`",
                ]
            ),
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=qa_context.discipline,
            role_name=qa_context.role_name,
            mcp_servers=qa_context.mcp_servers,
            web_tools=qa_context.web_tools,
            skill_files=(qa_valid_a, qa_valid_b),
        )
    )
    expect(not failures, f"Expected valid QA reviewer skills to pass, got: {failures}", scenario_failures)

    qa_missing_anchor = root / "qa-reviewer-missing-anchor.md"
    qa_missing_anchor.write_text(
        reviewer_skill_template(
            skill_name="requirements-trace-review",
            description="Example reviewer skill.",
            primary_mcp="repository, logs",
            fallback_tools="open, search_query",
            output_artifact="knowledge/reviews/qa-reviewer.md",
            purpose="Example purpose.",
            required_sections="\n".join(
                [
                    "- `### Review framing`",
                    "- `### Requirement matrix`",
                    "- `### Surface and flow mapping`",
                    "- `### Confirmed matches`",
                    "- `### Gaps and mismatches`",
                    "- `### Ambiguities and unverified assumptions`",
                    "- `### Priority risks`",
                    "- `### Limits and unknowns`",
                ]
            ),
        ).replace(
            'section_anchor: "## Skill: requirements-trace-review"\n',
            "",
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=qa_context.discipline,
            role_name=qa_context.role_name,
            mcp_servers=qa_context.mcp_servers,
            web_tools=qa_context.web_tools,
            skill_files=(qa_missing_anchor,),
        )
    )
    expect(
        any("must declare section_anchor" in failure for failure in failures),
        f"Expected missing QA reviewer section_anchor failure, got: {failures}",
        scenario_failures,
    )

    qa_duplicate_a = root / "qa-reviewer-duplicate-a.md"
    qa_duplicate_b = root / "qa-reviewer-duplicate-b.md"
    qa_duplicate_a.write_text(qa_valid_a.read_text(encoding="utf-8"), encoding="utf-8")
    qa_duplicate_b.write_text(
        qa_valid_b.read_text(encoding="utf-8").replace(
            'section_anchor: "## Skill: release-gate"',
            'section_anchor: "## Skill: requirements-trace-review"',
        ),
        encoding="utf-8",
    )
    failures = run_validation(
        build_context(
            discipline=qa_context.discipline,
            role_name=qa_context.role_name,
            mcp_servers=qa_context.mcp_servers,
            web_tools=qa_context.web_tools,
            skill_files=(qa_duplicate_a, qa_duplicate_b),
        )
    )
    expect(
        any("duplicates section_anchor" in failure for failure in failures),
        f"Expected duplicate QA reviewer section_anchor failure, got: {failures}",
        scenario_failures,
    )


def main() -> int:
    scenario_failures: list[str] = []

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        run_business_scenarios(root, scenario_failures)
        run_engineer_scenarios(root, scenario_failures)
        run_reviewer_scenarios(root, scenario_failures)

    if scenario_failures:
        for failure in scenario_failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Skill validation scenario checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
