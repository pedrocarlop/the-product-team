---
name: responsive-refinement
description: Adapt or improve the surface so it works cleanly across breakpoints and devices.
trigger: When responsive behavior is missing or under-specified.
primary_mcp: repository, chrome_devtools
fallback_tools: figma, reference/verify
best_guess_output: A responsive implementation or refinement pass.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: responsive-refinement"
done_when: Desktop and mobile behavior are both acceptable and intentional.
---

# Responsive Refinement

## Purpose

Adapt or improve the surface so it works cleanly across breakpoints and devices.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: responsive-refinement`, include:
- `### Target breakpoints`: Define the breakpoint set or device range this refinement covers.
- `### Current issues`: Summarize the responsive problems or gaps found.
- `### Responsive adjustments`: Describe the intended layout, spacing, or component changes.
- `### State-specific behavior`: Note state handling that changes across breakpoints.
- `### Risks and regressions`: Capture likely regressions, fragile areas, or remaining gaps.
- `### Verification plan`: Explain how the responsive behavior should be checked.

## Tool Path

- Start with `repository, chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma, reference/verify`.
- If both paths fail, produce the best-guess output described as: A responsive implementation or refinement pass.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep breakpoint behavior intentional rather than describing a single flexible layout vaguely.
- Note where the responsive design is constrained by existing component architecture.
- Preserve concrete viewport or device observations that matter to regression checking.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: responsive-refinement`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Desktop and mobile behavior are both acceptable and intentional.
