---
name: wireframe-structure
description: Build low-to-mid fidelity structural wireframes that clarify hierarchy and task flow.
trigger: When teams need screen structure before visual polish.
primary_mcp: figma
fallback_tools: paper, reference/ground
best_guess_output: A wireframe set aligned to the approved flow.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: wireframe-structure"
done_when: Screen structure is clear enough for review or prototyping.
---

# Wireframe Structure

## Purpose

Build low-to-mid fidelity structural wireframes that clarify hierarchy and task flow.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: wireframe-structure`, include:
- `### Assignment type`: State whether the wireframes support `new design` or an extension of an existing pattern.
- `### Screen inventory`: List the screens or states covered by the wireframe set.
- `### Content hierarchy`: Explain how information and actions are prioritized on each screen.
- `### Navigation and task flow`: Describe how the user moves between screens and completes the task.
- `### Structural gaps`: Identify missing information, unresolved branches, or screens that still need definition.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/ground`.
- If both paths fail, produce the best-guess output described as: A wireframe set aligned to the approved flow.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep wireframes focused on hierarchy and task flow, not final visual styling.
- If the work is `new design`, leave space for divergent UI exploration downstream.
- Call out where the structural model depends on product decisions that are not final yet.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: wireframe-structure`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Screen structure is clear enough for review or prototyping.
