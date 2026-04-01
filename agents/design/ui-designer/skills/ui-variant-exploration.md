---
name: ui-variant-exploration
description: Generate and compare multiple visual variants against the same product goal.
trigger: When the team needs options before committing to a single UI direction.
primary_mcp: stitch
fallback_tools: paper, figma
best_guess_output: A variant comparison with recommendation and rationale.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: ui-variant-exploration"
done_when: The chosen direction clearly beats the alternatives on the intended goal.
---

# Ui Variant Exploration

## Purpose

Generate and compare multiple visual variants against the same product goal.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: ui-variant-exploration`, include:
- `### Variant comparison`: Provide a comparison table with at least `Variant`, `Reference mix`, `Core idea`, `Divergence axes`, `Strengths`, `Weaknesses`, `Risks`, `Best use case`, and `Why not chosen`.
- `### Winning direction`: Choose a single recommended direction and explain why it wins.
- `### Traits to carry forward`: List any qualities from losing variants that should survive into convergence.
- `### Similarity check`: Call out where variants drifted too close together or failed to diverge enough.

## Tool Path

- Start with `stitch`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, figma`.
- If both paths fail, produce the best-guess output described as: A variant comparison with recommendation and rationale.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- This skill is the comparison gate before convergence for `new design` work.
- Compare at least 3 variants and end with one recommendation, not a tie.
- Give each variant an explicit reference mix so the team can trace which borrowed principles produced the result.
- Use the `Similarity check` to prove the set explored real space rather than near-duplicates.
- If the variants are not meaningfully different, say so and broaden them before convergence.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: ui-variant-exploration`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The chosen direction clearly beats the alternatives on the intended goal.
