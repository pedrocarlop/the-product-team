---
name: spacing-and-layout-scale
description: Define the spacing, sizing, and layout scale that underpins UI consistency.
trigger: When system consistency depends on clearer spatial rules.
primary_mcp: figma
fallback_tools: paper, repository
best_guess_output: A spacing and layout scale with usage guidance.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md
section_anchor: "## Skill: spacing-and-layout-scale"
done_when: Designers can compose surfaces without inventing spacing ad hoc.
---

# Spacing And Layout Scale

## Purpose

Define the spacing, sizing, and layout scale that underpins UI consistency.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: spacing-and-layout-scale`, include:
- `### Scale definition`: Define the core spacing and sizing values and how they relate.
- `### Semantic usage`: Map raw values to semantic layout roles such as stack, inset, gap, or section spacing.
- `### Breakpoint adjustments`: Describe any breakpoint-specific spacing behavior.
- `### Exceptions`: Call out where the scale should intentionally bend or stop.
- `### Migration notes`: Explain how existing layouts should move onto the scale.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, repository`.
- If both paths fail, produce the best-guess output described as: A spacing and layout scale with usage guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prefer a scale that can survive real product layouts, not just tidy examples.
- Keep layout rules connected to the component system and breakpoints.
- Document where the scale is normative versus advisory.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Keep all work for this skill inside `## Skill: spacing-and-layout-scale`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Designers can compose surfaces without inventing spacing ad hoc.
