---
name: prototype-and-usability-validation
description: Build and validate a prototype to test whether the proposed interaction actually works.
trigger: When a flow or concept should be tested before full build.
primary_mcp: paper
fallback_tools: figma, chrome_devtools
best_guess_output: A prototype summary with validation findings.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: prototype-and-usability-validation"
done_when: The prototype answers a real decision and any unresolved risk is explicit.
---

# Prototype And Usability Validation

## Purpose

Build and validate a prototype to test whether the proposed interaction actually works.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: prototype-and-usability-validation`, include:
- `### Prototype scope`: Define what was prototyped and what was intentionally left out.
- `### Test plan`: State the task, scenario, or question the prototype is meant to answer.
- `### Participant or walkthrough setup`: Describe who interacted with it or how the scenario was exercised.
- `### Findings`: Summarize what worked, what failed, and where users hesitated.
- `### Decision and outstanding risk`: State what the team can now decide and what still remains unresolved.

## Tool Path

- Start with `paper`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, chrome_devtools`.
- If both paths fail, produce the best-guess output described as: A prototype summary with validation findings.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use `paper` first when available; if not, fall back to `figma, chrome_devtools` instead of abstract browser wording.
- Tie findings back to a concrete product decision instead of a vague sense of confidence.
- Keep unresolved risk explicit so the prototype is not mistaken for proof of completeness.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: prototype-and-usability-validation`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The prototype answers a real decision and any unresolved risk is explicit.
