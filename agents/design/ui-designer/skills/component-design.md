---
name: component-design
description: Create or extend reusable UI components needed by the surface.
trigger: When the feature needs reusable UI patterns, not just one-off screens.
primary_mcp: figma
fallback_tools: paper, stitch
best_guess_output: A component proposal or production component design.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: component-design"
done_when: Component purpose, states, and intended reuse are explicit.
---

# Component Design

## Purpose

Create or extend reusable UI components needed by the surface.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: component-design`, include:
- `### Assignment type`: State whether the component supports `new design` exploration or extends an existing system.
- `### Component inventory`: List the components or subcomponents in scope and what each one is for.
- `### Variant and state table`: Define variants, states, triggers, and constraints in table form.
- `### Reuse rules`: State where the component should and should not be reused.
- `### Accessibility and layout notes`: Capture key layout, density, and accessibility requirements.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, stitch`.
- If both paths fail, produce the best-guess output described as: A component proposal or production component design.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Design for reuse, not for one screen only.
- Avoid proliferating variants when layout rules or tokens would solve the problem more cleanly.
- Tie component decisions back to the broader system and intended adoption.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: component-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Component purpose, states, and intended reuse are explicit.
