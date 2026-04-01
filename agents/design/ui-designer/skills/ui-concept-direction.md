---
name: ui-concept-direction
description: Explore and establish the visual direction for a new surface before production detailing.
trigger: When a new UI direction or concept needs exploration.
primary_mcp: stitch
fallback_tools: paper, search_query
best_guess_output: A concept direction with clear visual thesis and promising directions.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: ui-concept-direction"
done_when: A team can choose or refine a direction instead of staring at a blank page.
---

# Ui Concept Direction

## Purpose

Explore and establish the visual direction for a new surface before production detailing.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: ui-concept-direction`, include:
- `### New design check`: Confirm whether the assignment is truly `new design` or only an extension of an existing pattern.
- `### Direction 1`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Direction 2`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Direction 3`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Recommended direction`: Name the most promising direction and why it is the best next step.
- `### Anti-patterns to avoid`: List the generic or over-polished traps the team should avoid during convergence.

## Tool Path

- Start with `stitch`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, search_query`.
- If both paths fail, produce the best-guess output described as: A concept direction with clear visual thesis and promising directions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- This skill is the first-stage requirement for `new design` work.
- Produce 3 meaningfully different high-level directions, not cosmetic variations of one idea.
- Each direction must differ on at least 3 axes chosen from layout model, density, interaction tone, visual language, typography strategy, color strategy, hierarchy model, or framing metaphor.
- Keep the output high-level and exploratory; do not polish into final implementation-ready comps here.
- If the work is only an extension of an existing pattern, record that and redirect to the more concrete UI skill instead of forcing fake divergence.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: ui-concept-direction`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A team can choose or refine a direction instead of staring at a blank page.
