---
name: ui-concept-direction
description: Compare and shape multiple visually distinct concept directions, grounded in reference systems and implementation constraints, so the team can choose a direction and seed the shared design spec.
trigger: When a new UI direction or concept needs exploration.
primary_mcp: stitch
fallback_tools: paper, search_query
best_guess_output: A concept direction with clear visual thesis and promising directions.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer-ui-concept-direction.md
done_when: A team can choose or refine one of 3 materially different directions, understand the recommended path, and see the shared design spec seeded.
required_inputs:
  - new-design confirmation or an explicit note that this is only an extension of an existing pattern
  - target surface, audience, and product goal
  - known constraints, platform context, and implementation foundation
  - up to 3 inspiration-only reference systems when available
recommended_passes:
  - new design check
  - reference selection
  - direction generation
  - divergence and comparison
  - project ds-spec seed
  - shadcn/ui suitability check
tool_stack:
  - runtime: stitch, v0
  - artifacts: figma, Framer, Penpot, reference-design-systems
  - fallback: paper, search_query
tool_routing:
  - if the work is already in a design canvas and needs concept iteration, use stitch first
  - if a quick prompt-to-UI draft would sharpen the direction, use v0
  - if motion or breakpoint behavior needs to be felt, use Framer preview
  - if open, collaborative boards or component libraries are the better fit, use Penpot
  - if only static references or notes exist, use paper and search_query
---

# Ui Concept Direction

## Purpose

Explore and establish the visual direction for a new surface before production detailing.

This is concept-first work, not final screen polish or component implementation.

## Required Inputs and Assumptions

- Required inputs:
  - target surface or product area
  - user and business goal
  - new-design confirmation, or confirmation that the work is only an extension of an existing pattern
  - implementation foundation, if one already exists
  - inspiration-only references, if the team has them
- If inputs are missing:
  - infer a provisional assumption
  - label it clearly as an assumption
  - keep confidence lower for anything that depends on it
- If the assignment is only an extension of an existing pattern:
  - record that explicitly
  - redirect toward the more concrete UI skill instead of inventing fake divergence

## Input Mode And Evidence Path

Use the strongest available evidence path in this order:

1. Live concepting or interactive design-canvas exploration.
2. Structured design artifacts and system references.
3. Static screenshots, notes, or copied references.
4. Inference from partial context.

This skill is evidence-guided, not opinion-led.
When the evidence path is weak, say so and keep the recommendation cautious.

## Tool Selection Rationale

- `stitch` is the primary path because it is best for quick concept boards, visual iteration, and comparing multiple directions in context.
- `v0` is the strongest alternate when a prompt-to-UI draft, screenshot-based translation, or code-shaped concept would clarify the direction. Its official docs support text prompting, screenshot/file uploads, design mode, and design-system-aware generation.
- `Framer` is useful when the concept needs interactive preview, component reuse, or breakpoint/motion rehearsal before the team commits. Its docs cover components, shared libraries, preview, and breakpoint-aware behavior.
- `Penpot` is useful when the team wants open, collaborative boards, reusable components and libraries, inspect mode, or lightweight prototyping with explicit design-system assets.
- `paper` and `search_query` are the fallback path when the canvas is unavailable or the work is mostly reference gathering.

## Environment And Reproducibility

- Record the target platform, device class, and product area.
- Record whether the surface is greenfield, a redesign, or an extension.
- Record the known implementation foundation, if any.
- Record which reference systems were used and whether they came from the local reference library or external inspiration.
- If the environment is incomplete, state the missing pieces instead of filling them in with certainty.

## Model Building

Before judging visual directions, build a concept model with these parts:

- user goal and emotional posture
- layout model
- hierarchy model
- density and spacing model
- typography strategy
- color and token posture
- interaction tone
- implementation constraints
- system follow-up needs

No conclusion should come before the model is explicit.

## Core Method Execution

1. Confirm whether this is truly `new design`.
2. Select up to 3 inspiration-only reference systems from `.codex/product-team/references/reference-design-systems/`.
3. Build three materially different directions, not cosmetic variants.
4. Compare the directions across at least 3 axes such as layout model, visual language, typography strategy, color strategy, hierarchy model, or framing metaphor.
5. Evaluate whether the blank-project case would benefit from a shadcn/ui foundation, but treat it as implementation support, not the concept itself.
6. Seed `project-ds-spec.md` with the shared principles, implementation foundation, and the parts that should survive convergence.
7. Choose one recommended direction and explain why it is the best next step.

## Structured Direction Records

Each direction must be written as a structured record, not free-form prose.

### Direction record schema

- Direction name:
- Visual thesis:
- Style pillars:
- Layout model:
- Token direction:
- Reference cues:
- Divergence axes:
- Why this is materially different:
- Risks:
- Confidence:
- Evidence path:

### Comparison requirements

- Each direction must differ on at least 3 axes.
- The directions must be meaningfully different, not spaced-out versions of the same idea.
- The comparison must name the winner and state why the others lost.
- If the set is too similar, say so and broaden the exploration before converging.

## Prioritization Logic

Rank the directions using this order:

1. Product fit and user goal clarity.
2. Distinctness from the other directions.
3. Implementation plausibility.
4. Strength of the system seed it creates.
5. Accessibility and responsiveness fit.
6. Confidence in the evidence path.

Do not end in a tie.

## Coverage Map

- Deeply covered:
  - primary surface
  - main user goal
  - the three candidate directions
  - shared design-system seed
- Partially covered:
  - edge-case states
  - breakpoint nuance
  - motion and interaction detail
- Not covered:
  - final production polish
  - implementation-level component specs
  - exhaustive state matrices

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/ui-designer-ui-concept-direction.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: ui-concept-direction`, include:
- `### New design check`: Confirm whether the assignment is truly `new design` or only an extension of an existing pattern.
- `### Reference selection`: List up to 3 inspiration-only company references from `.codex/product-team/references/reference-design-systems/` and why each one is relevant.
- `### Direction 1`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Direction 2`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Direction 3`: Include `Visual thesis`, `Style pillars`, `Token direction`, `Reference cues`, `Divergence axes`, and `Why this is materially different`.
- `### Project ds-spec seed`: Include `Design principles and brand posture`, `Reference inspirations`, `Typography direction`, `Color and token direction`, `Implementation foundation`, `Spacing and layout rules`, and `State, motion, and accessibility rules`.
- `### Recommended direction`: Name the most promising direction and why it is the best next step.
- `### Anti-patterns to avoid`: List the generic or over-polished traps the team should avoid during convergence.

## Project Ds-Spec Seed

Use the concept pass to seed `logs/active/<project-slug>/deliverables/project-ds-spec.md` when the work is greenfield.

- `Design principles and brand posture`: describe the posture the product should sustain as it converges.
- `Reference inspirations`: call out the inspiration-only cues that should survive, not copied branding.
- `Typography direction`: define the typography family, hierarchy logic, and tone.
- `Color and token direction`: define the palette posture and semantic-token direction.
- `Implementation foundation`: state whether shadcn/ui is recommended, and if so, why it fits the stack and product.
- `Spacing and layout rules`: capture the base grid, rhythm, density, and page structure.
- `State, motion, and accessibility rules`: capture the motion posture, state expectations, and accessibility guardrails.

If shadcn/ui is recommended, write that decision into `project-ds-spec.md` with the rationale, the blank-project check, and the intended setup path.
If the product already has a meaningful foundation, say not to initialize shadcn/ui and explain why reuse or incremental adoption is the better call.

## Tool Path

- Start with `stitch`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, search_query`.
- If both paths fail, produce the best-guess output described as: A concept direction with clear visual thesis and promising directions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single tool.

## Workflow Notes

- This skill is the first-stage requirement for `new design` work.
- Read up to 3 reference systems from `.codex/product-team/references/reference-design-systems/` before generating directions.
- Produce 3 meaningfully different high-level directions, not cosmetic variations of one idea.
- Each direction must differ on at least 3 axes chosen from layout model, density, interaction tone, visual language, typography strategy, color strategy, hierarchy model, or framing metaphor.
- Treat company references as inspiration-only cues. Borrow principles, not brand identity, named tokens, or exact visual replicas.
- For blank or near-empty frontend projects, evaluate whether the latest official shadcn/ui foundation would materially improve quality, accessibility, and delivery speed for this product.
- Recommend shadcn/ui only when the stack is compatible and the product benefits from composable primitives. Do not treat shadcn defaults as the product's design direction.
- If shadcn/ui is recommended, write the decision into `project-ds-spec.md` under `## Implementation Foundation` with the rationale, the blank-project check, and the intended setup path.
- If the work is only an extension of an existing pattern, record that and redirect to the more concrete UI skill instead of forcing fake divergence.

## Limits And Unknowns

- This skill does not produce final production comps.
- It does not replace implementation validation.
- It cannot prove the chosen direction is correct without product and engineering follow-through.
- Confidence should drop when the evidence path is only static or inferred.
- If a reference system or implementation foundation is missing, say so explicitly.

