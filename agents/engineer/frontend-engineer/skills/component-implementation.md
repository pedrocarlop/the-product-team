---
name: component-implementation
description: Build or extend reusable frontend components that align with the design system.
trigger: When implementation needs a reusable component, not just a one-off screen.
primary_mcp: repository, figma
fallback_tools: reference/reuse, chrome_devtools
best_guess_output: A reusable component implementation with intended states and props.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: component-implementation"
done_when: The component is reusable and aligned to system expectations.
---

# Component Implementation

## Purpose

Build or extend reusable frontend components that align with the design system.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: component-implementation`, include:
- `### Component purpose`: Describe what the component should solve and where it should be reused.
- `### System foundation alignment`: State whether the component builds on an existing foundation or first bootstraps one from `project-ds-spec.md`.
- `### API or props`: Define the public API, props, slots, or configuration surface.
- `### Variants and states`: List the supported variants, interactive states, and edge conditions.
- `### Composition and reuse constraints`: Explain composition boundaries, dependencies, and what should stay outside the component.
- `### Code touchpoints`: Identify the files, modules, or component families involved.
- `### Adoption notes`: Capture migration or usage guidance for downstream implementers.

## Tool Path

- Start with `repository, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/reuse, chrome_devtools`.
- If both paths fail, produce the best-guess output described as: A reusable component implementation with intended states and props.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for reusability boundaries, not just visual parity for one screen.
- Keep the API explicit enough that later consumers do not infer unsupported patterns.
- Preserve exact design-system or existing-component references when reuse is the right path.
- Read `logs/active/<project-slug>/deliverables/project-ds-spec.md` first when it exists.
- If the component work is landing in a blank or near-empty frontend and `project-ds-spec.md` recommends shadcn/ui, initialize the latest official shadcn/ui foundation first through the approved repo-write assignment, then build the component on top of that aligned baseline instead of improvising local primitives.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: component-implementation`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The component is reusable and aligned to system expectations.
