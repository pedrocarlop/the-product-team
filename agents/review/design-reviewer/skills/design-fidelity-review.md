---
name: design-fidelity-review
description: Compare the implemented surface against the design source of truth by building source and implementation models, then classifying meaningful drift by component, state, breakpoint, and layout behavior.
trigger: When a design or implemented surface needs fidelity review before sign-off, bug filing, or remediation planning.
comparison_framework: drift taxonomy across layout, spacing, typography, color, imagery, motion, component structure, interaction, and state coverage
primary_mcp: figma, chrome_devtools
fallback_tools:
  - reference/verify
  - open
required_inputs:
  - target surface or route
  - canonical design source of truth
  - breakpoints, states, or devices in scope
  - release context or acceptance threshold when known
recommended_passes:
  - source-of-truth alignment
  - layout and spacing
  - typography and visual styling
  - interaction and state coverage
  - responsive behavior and exception review
tool_stack:
  runtime:
    primary: [figma, chrome_devtools]
    secondary: [repository]
  artifacts:
    primary: [figma, reference/verify]
  fallback:
    primary: [open]
tool_routing:
  - if: design source and implementation are both accessible
    use: [figma, chrome_devtools]
  - if: implementation is not runnable but repo evidence or static implementation artifacts exist
    use: [figma, reference/verify]
  - if: only static exports, screenshots, or linked specs exist
    use: [open]
best_guess_output: A fidelity review with evidence-tagged drift findings, grouped patterns, and directional remediation guidance.
output_artifacts: logs/active/<project-slug>/reviews/design-reviewer.md
done_when: Meaningful design drift is identified with evidence, taxonomy, priority, and clear separation between implementation error and source ambiguity.
---

# Design Fidelity Review

## Purpose

Compare the implemented surface against the design source of truth and classify meaningful drift by component, state, and layout behavior.

This skill evaluates observable drift in hierarchy, structure, styling, behavior, and state coverage.

This skill does not treat every difference as a bug, assume the design source of truth is complete, or claim that implementation fixes have already been validated.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/design-reviewer-design-fidelity-review.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: design-fidelity-review`, include:
- `### Review framing`: Define the target surface, source-of-truth artifact, and what counts as meaningful drift for this review.
- `### Required inputs and assumptions`: State the target route or component, canonical design source, state and breakpoint scope, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: source design plus live implementation, source design plus repo or static implementation artifacts, screenshots or linked specs, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record browser, operating system, viewport, auth state, build or prototype version, and exact design references when known.
- `### Source-of-truth model`: Name the exact Figma frames, specs, annotations, tokens, or implementation references treated as canonical.
- `### Implementation model`: Capture the screens, breakpoints, components, states, and interaction behaviors actually inspected before evaluating drift.
- `### Surfaces compared`: State the exact screens, components, breakpoints, states, and source references included in the comparison.
- `### Comparison passes`: List the passes used such as source-of-truth alignment, layout and spacing, typography and visual styling, interaction and state coverage, and responsive behavior and exception review.
- `### Drift taxonomy`: Classify drift by layout, spacing, typography, color, motion, structure, interaction, state, or responsive behavior.
- `### Drift findings`: Record findings using the required finding schema below.
- `### Key mismatches`: Highlight the most important drift that changes hierarchy, affordance, comprehension, or implementation risk.
- `### Prioritized mismatches`: Include all critical and major drift as standalone findings, group minor issues into patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic drift patterns`: Group repeated drift across components, breakpoints, or states into broader implementation patterns.
- `### Coverage map`: State what was deeply compared, partially compared, and not compared.
- `### Severity and implementation risk`: Separate visible severity from implementation risk and explain whether the issue points to local drift or a broader implementation problem.
- `### Severity, confidence, and coverage confidence`: Separate visible impact severity from evidence confidence and state whether coverage came from live implementation comparison, repo or static artifact comparison, or screenshot-only inference.
- `### Directional remediation guidance`: Link remediation directions to findings without pretending every fix is fully specified.
- `### Exceptions and ambiguities`: Call out intentional differences, unclear specs, or cases where the design source of truth is incomplete.
- `### Limits and unknowns`: Explain what was not compared and where evidence was partial.

For each finding inside `### Drift findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Expected from source of truth:
- Likely cause:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity evidence path available: source design plus live implementation -> source design plus repo or static implementation artifacts -> screenshots or linked specs -> inference.
- Start with `figma, chrome_devtools` when the design source and live implementation are both accessible.
- Use `chrome_devtools` when layout behavior, computed styles, responsive breakpoints, state changes, or runtime interaction details matter.
- Use `figma` to inspect canonical frames, annotations, component variants, tokens, and intended states.
- Use `reference/verify` when code, review artifacts, or implementation notes are the best available proxy for a missing live runtime.
- Use `open` only when linked specs, screenshots, or static exports are the strongest evidence left.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both paths fail, produce the best-guess output described as: A fidelity review with evidence-tagged drift findings, grouped patterns, and directional remediation guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-source review.

## Workflow Notes

- Build a comparison model before listing bugs. Review the design source, the implementation, and the relevant states in parallel.
- Treat `required_inputs` as real prerequisites. If the canonical design source or state scope is missing, infer a provisional comparison frame, prefix each inferred item with `Assumed source:` or `Assumed state:`, and lower confidence for downstream findings that depend on it.
- Distinguish one-off deviations from systemic implementation drift.
- Capture missing states explicitly. Fidelity failures often come from unimplemented loading, error, hover, focus, or responsive states rather than static layout alone.
- Do not over-index on pixel trivia when the more important break is information hierarchy, affordance, or consistency.
- Separate spec ambiguity from implementation error so downstream teams know whether to fix code or clarify design.
- Run comparison passes in sequence so findings stay grounded: source alignment first, layout and spacing second, typography and styling third, then interactions, states, and responsive behavior.
- Distinguish clearly between observed drift, inferred cause, and recommendation direction.
- After all passes, merge duplicates and consolidate overlapping findings before prioritization.

