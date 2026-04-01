---
name: problem-framing
description: Translate product goals and user context into a design-ready framing.
trigger: When design work needs a crisp problem statement and design lens.
primary_mcp: notion, repository
fallback_tools: reference/ground, search_query
best_guess_output: A design framing artifact with users, task, constraints, and success criteria.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: problem-framing"
done_when: Downstream design work has a stable framing.
---

# Problem Framing

## Purpose

Translate product goals and user context into a design-ready framing.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: problem-framing`, include:
- `### Problem statement`: State the design problem in one crisp, bounded statement.
- `### Users and context`: Describe who the user is, what context they are in, and what job they are trying to do.
- `### Constraints and risks`: List the non-negotiables, unknowns, and delivery risks.
- `### Success criteria`: Define how the team will know the design solved the right problem.
- `### Open questions`: Call out unresolved product questions that still affect the framing.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A design framing artifact with users, task, constraints, and success criteria.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Anchor the framing in evidence and delivery constraints, not only aspiration.
- Preserve exact goals, metrics, or product language that downstream roles must not lose.
- State whether the eventual UI work should be treated as `new design` or an extension.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: problem-framing`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Downstream design work has a stable framing.
