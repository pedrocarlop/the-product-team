---
name: screen-production-design
description: Produce or refine the definitive screen design for implementation.
trigger: When a concept must become a production-ready design.
primary_mcp: figma
fallback_tools: paper, stitch
best_guess_output: A production-ready screen spec or screen set.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: screen-production-design"
done_when: Layout, hierarchy, tokens, and core states are specified clearly.
---

# Screen Production Design

## Purpose

Produce or refine the definitive screen design for implementation.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: screen-production-design`, include:
- `### Assignment type`: State whether this is `new design` convergence or an extension of an existing pattern.
- `### Chosen direction`: For `new design`, name the exact upstream concept or variant section being converged.
- `### Inherited principles`: List the traits from the winning direction that must remain visible in the production design.
- `### Non-goals`: State what this production pass is not trying to solve or reinvent.
- `### Screen inventory`: List the screens or states covered in the production design set.
- `### Layout and tokens`: Define the layout model, hierarchy, and token usage concretely.
- `### State coverage`: Specify all core states required for implementation.
- `### Implementation notes`: Call out constraints and details engineering must preserve.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, stitch`.
- If both paths fail, produce the best-guess output described as: A production-ready screen spec or screen set.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- This is convergence-only work for `new design`; do not use it as a substitute for concept exploration.
- Preserve the winning direction's distinguishing traits instead of collapsing back to safe defaults.
- If no upstream direction exists for a `new design` assignment, stop and note the mismatch instead of inventing one.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: screen-production-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Layout, hierarchy, tokens, and core states are specified clearly.
