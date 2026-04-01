---
name: journey-and-flow-design
description: Map the end-to-end journey, decisions, states, and edge cases for the experience.
trigger: When a feature or service flow needs clear behavioral structure.
primary_mcp: figma
fallback_tools: paper, notion
best_guess_output: A journey or flow artifact with key paths and branches.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: journey-and-flow-design"
done_when: The main path and critical alternatives are unambiguous.
---

# Journey And Flow Design

## Purpose

Map the end-to-end journey, decisions, states, and edge cases for the experience.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: journey-and-flow-design`, include:
- `### Entry points`: Describe where the user enters the journey and what context they bring.
- `### Main path`: Document the happy path in sequential order.
- `### Alternate paths`: Capture meaningful branches, detours, or fallback routes.
- `### Edge cases`: List the conditions that break or complicate the nominal path.
- `### Decision points`: Call out moments where user choice or system policy changes the route.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, notion`.
- If both paths fail, produce the best-guess output described as: A journey or flow artifact with key paths and branches.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Focus on the behavioral structure of the experience, not polished screen design.
- Make branches and state changes easy for downstream roles to follow.
- Record assumptions where the upstream product decision is still soft.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: journey-and-flow-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The main path and critical alternatives are unambiguous.
