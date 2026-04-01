---
name: implement-from-design
description: Implement a design faithfully in production code with the required states and interactions.
trigger: When approved design work is ready for implementation.
primary_mcp: repository, figma
fallback_tools: chrome_devtools, reference/trace
best_guess_output: Working UI implementation aligned to the design spec.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: implement-from-design"
done_when: The implemented surface matches the intended structure and behavior.
---

# Implement From Design

## Purpose

Implement a design faithfully in production code with the required states and interactions.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: implement-from-design`, include:
- `### Design target`: Identify the design source, surface, or approved direction being implemented.
- `### Implementation scope`: Define what parts of the design are in scope for this pass.
- `### State coverage`: List required states, flows, and conditional behavior that must be represented in code.
- `### Interaction notes`: Capture important interactions, transitions, or behavioral nuances.
- `### Code touchpoints`: Identify the files, components, or routes involved.
- `### Open implementation risks`: Call out remaining uncertainty, gaps, or blockers.

## Tool Path

- Start with `repository, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `chrome_devtools, reference/trace`.
- If both paths fail, produce the best-guess output described as: Working UI implementation aligned to the design spec.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Preserve fidelity-critical design details without turning the artifact into line-by-line implementation prose.
- Call out where design intent is clear versus where engineering judgment had to fill gaps.
- Keep code touchpoints exact so downstream review can verify the right surface.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: implement-from-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The implemented surface matches the intended structure and behavior.
