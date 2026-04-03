---
name: ui-variant-exploration
description: Build a comparison model, explore materially different UI directions, and recommend the strongest variant from evidence.
trigger: When the team needs options before committing to a single UI direction.
primary_mcp: paper
fallback_tools: figma
required_inputs:
  - product goal or decision to support
  - target surface, flow, or feature context
  - known constraints and must-keep elements
  - existing references or system baseline, if any
recommended_passes:
  - model the decision space
  - compare at least 3 materially different directions
  - check reference mix and divergence
  - score and recommend one winner
tool_stack:
  - paper for high-fidelity variant generation and production-ready options
  - figma for component-aware inspection and layout precision
  - chrome_devtools for live implementation sanity checks when needed
inspiration_tools:
  - stitch for browsing reference layouts and visual inspiration only — never for generating designs
best_guess_output: A variant comparison with recommendation and rationale.
output_artifacts:
  - logs/active/<project-slug>/runs/<run-id>/deliverables/ui-designer-ui-variant-exploration.md
  - logs/active/<project-slug>/runs/<run-id>/deliverables/assets/ (for visual artifacts)
done_when: The chosen direction clearly beats the alternatives on the intended goal.
tool_routing:
  - if: high-fidelity, production-shaped variants are needed
    use: [paper]
  - if: the variants need component, spacing, or state inspection
    use: [figma]
  - if: a live implementation must be used as context for comparison
    use: [chrome_devtools]
  - if: visual reference or inspiration layouts are needed for comparison context
    use: browse stitch screenshots only — do NOT generate designs with stitch
---

# Ui Variant Exploration

## Purpose

Generate and compare multiple visual variants against the same product goal.
This skill builds a decision model first, then explores a set of materially different directions, then recommends one winner.
It does not converge a single concept prematurely, and it does not replace production design or final polish.

## Required Inputs and Assumptions

- Required inputs: product goal, target surface or flow, constraints, and any must-keep elements.
- Assumptions: if the assignment omits a constraint, infer the most likely one and label it clearly in the output.
- Unknowns: if the system baseline, audience, or delivery context is unclear, note that the comparison is provisional.

## Input Mode and Evidence Path

Use the strongest available evidence path in this order:
1. Live interactive design canvas or editable prototype.
2. Structured design artifacts and shared references.
3. Static screenshots, exports, or notes.
4. Inference only when nothing else is available.

Label the resulting section as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Tool Selection Rationale

- Use `paper` (via `generate_variants` or `generate_screen_from_text`) for creating production-ready variants that can be directly refined into final screens.
- Browse `stitch` ONLY to screenshot and reference existing layouts for visual inspiration. NEVER generate screens, components, or HTML with stitch — it produces incomplete navigation and broken logic.
- Use `figma` when component structure, spacing, states, or token implications need sharper inspection.
- Use `chrome_devtools` only when a live implementation needs to be checked for context, not as a substitute for concept generation.
- Alternative tools worth borrowing patterns from in the wider ecosystem include Framer for fast motion-rich direction tests, Penpot for spec-minded component exploration, Storybook for state coverage, and Playwright or Percy for later visual regression checks.

## Environment and Reproducibility

- Record the project slug, task context, and any baseline system in play.
- Record canvas state, viewport or frame size if known, and whether the surface is greenfield or extending an existing pattern.
- Record whether references came from company inspiration sources, a shared design system, or the current product UI.
- If the environment changes during the comparison, note the change so the decision can be reproduced later.

## Model Building

Build a comparison model before evaluating visuals.

- Define the decision criteria.
- Define the divergence axes.
- Define the constraint set.
- Define the reference mix for each direction.
- Define what counts as a meaningful difference versus a cosmetic change.

No conclusion should be written before this model exists.

## Core Method

1. Confirm this is a comparison task and not a convergence or polish task.
2. List the goal, constraints, and non-negotiables.
3. Generate at least 3 materially different directions.
4. Give each direction an explicit reference mix so the borrowed principles are traceable.
5. Force divergence across at least 3 axes such as layout model, density, hierarchy model, visual language, typography strategy, color strategy, or interaction tone.
6. Compare the options against the same decision criteria.
7. Call out any near-duplicates and broaden the set if needed.
8. Choose one winner and name the traits to carry forward from the losing options.
9. Write the comparison so the team can make a decision without rereading the whole exploration.

## Structured Output Schema

Within `## Skill: ui-variant-exploration`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Variant comparison`: Provide a comparison table with at least `Variant`, `Reference mix`, `Core idea`, `Divergence axes`, `Strengths`, `Weaknesses`, `Risks`, `Best use case`, and `Why not chosen`.
- `### Winning direction`: Choose a single recommended direction and explain why it wins.
- `### Traits to carry forward`: List any qualities from losing variants that should survive into convergence.
- `### Similarity check`: Call out where variants drifted too close together or failed to diverge enough.

Use the table to separate observation from recommendation. Each row should read as a distinct option, not as a vague aesthetic mood.

## Prioritization Logic

- Prefer the variant that best satisfies the product goal, not the one that looks most polished in isolation.
- Give extra weight to clear differentiation, feasibility, and reuse potential.
- Treat constraint violations as vetoes, not minor weaknesses.
- If two variants are close, prefer the one that creates more decision clarity for the team.
- Never end in a tie if one direction clearly reduces risk or improves adoption.

## Coverage Map

State what was deeply explored, partially explored, and not explored.

- Deeply explored: the chosen divergence axes, reference mixes, and winner-vs-loser tradeoffs.
- Partially explored: adjacent interaction ideas, motion, or secondary states if they did not change the direction decision.
- Not explored: implementation details, final token values, and production polish unless they are decisive for the comparison.

## Limits and Unknowns

- Call out missing product context, unclear audience signals, or unresolved system constraints.
- State when the comparison is provisional because the only evidence was static or partial.
- Say explicitly when the set may need another pass before convergence.
- Do not pretend an option is proven if the evidence only supports a directionally better guess.

## Workflow Notes

- Compare at least 3 variants and end with one recommendation, not a tie.
- Give each variant an explicit reference mix so the team can trace which borrowed principles produced the result.
- Use the `Similarity check` to prove the set explored real space rather than near-duplicates.
- If the variants are not meaningfully different, say so and broaden them before convergence.
- Treat this as the comparison gate before `screen-production-design` for new design work.
- Borrow patterns from Framer, Penpot, Storybook, and Playwright/Percy when thinking about how a comparison should be structured, even though this skill still writes to the Product Team workflow.
- Use `stitch` for inspiration ideas and reference layouts ONLY.
- Do NOT use the HTML or code output from `stitch` as the foundation for production products; it is for visual reference and inspiration only.
- Use `paper` to create actual high-fidelity variants.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/ui-designer-ui-variant-exploration.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `logs/active/<project-slug>/runs/<run-id>/deliverables/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

## Required Deliverable Sections

Within `## Skill: ui-variant-exploration`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Variant comparison`: Provide a comparison table with at least `Variant`, `Reference mix`, `Core idea`, `Divergence axes`, `Strengths`, `Weaknesses`, `Risks`, `Best use case`, and `Why not chosen`.
- `### Winning direction`: Choose a single recommended direction and explain why it wins.
- `### Traits to carry forward`: List any qualities from losing variants that should survive into convergence.
- `### Similarity check`: Call out where variants drifted too close together or failed to diverge enough.

## Tool Path

- Start with `paper`.
- If you need visual reference or inspiration, browse stitch screenshots but do NOT generate designs with it.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `figma`.
- If both paths fail, produce the best-guess output described as: A variant comparison with recommendation and rationale.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
