---
name: design-system-compliance-review
description: Audit alignment with the design system by modeling the system contract and tracing tokens, components, patterns, and exceptions across the reviewed surface.
trigger: When consistency or system conformance is in doubt before release, QA sign-off, or normalization work.
compliance_framework: token -> component -> pattern -> flow compliance review
primary_mcp: figma, repository
fallback_tools:
  - reference/reuse
  - chrome_devtools
required_inputs:
  - reviewed surface or flow
  - design system source of truth
  - allowed exceptions or platform constraints when known
  - implementation touchpoints in scope
recommended_passes:
  - token usage
  - component structure and variants
  - pattern and flow compliance
  - exception review
  - system gap versus adoption gap classification
tool_stack:
  runtime:
    primary: [figma, repository]
    secondary: [chrome_devtools]
  artifacts:
    primary: [figma, reference/reuse]
  fallback:
    primary: [chrome_devtools]
tool_routing:
  - if: system source and implementation touchpoints are accessible
    use: [figma, repository]
  - if: runtime inspection is needed to confirm token application or behavior
    use: [chrome_devtools]
  - if: system rules or reusable patterns must be recovered from prior work
    use: [reference/reuse]
best_guess_output: A design-system compliance review with evidence-tagged conformance issues, grouped variance patterns, and justified exceptions called out.
output_artifacts: knowledge/reviews/design-reviewer.md
done_when: Design-system conformance issues, justified exceptions, and system gaps are concrete, traceable, and actionable.
---

# Design System Compliance Review

## Purpose

Audit alignment with the design system by tracing tokens, components, patterns, and exceptions across the reviewed surface.

This skill evaluates whether the reviewed work is using the system as intended, diverging for a good reason, or exposing missing system coverage.

This skill does not assume every difference is a violation, treat the current implementation as canonical, or replace design-system governance decisions.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/design-reviewer-design-system-compliance-review.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: design-system-compliance-review`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Review framing`: Define the system source of truth, reviewed scope, and what counts as compliance versus justified divergence.
- `### Required inputs and assumptions`: State the reviewed surface, system source of truth, known exception rules, implementation touchpoints in scope, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: source design system plus implementation touchpoints, runtime confirmation, reusable implementation references, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record system version, library branch or package version, browser or platform context, auth state, and build or prototype version when known.
- `### System source of truth`: Name the exact tokens, component library, patterns, and reference materials treated as canonical.
- `### System contract model`: Name the tokens, component library, usage rules, or reference specs treated as canonical and summarize the expected contract at token, component, pattern, and flow level.
- `### Inventory checked`: List the screens, components, variants, states, and implementation touchpoints inspected before judging compliance.
- `### Surface inventory and adoption map`: List the screens, components, variants, states, and implementation touchpoints inspected before judging compliance.
- `### Compliance passes`: List the passes used such as token usage, component structure and variants, pattern and flow compliance, exception review, and system gap versus adoption gap classification.
- `### Token compliance findings`: Record token-level deviations such as color, spacing, typography, radius, or elevation mismatches.
- `### Component compliance findings`: Record component, variant, state, or pattern-level conformance issues.
- `### Compliance findings`: Record findings using the required finding schema below.
- `### Prioritized findings`: Include all critical and major conformance issues as standalone findings, group minor issues into patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic variance patterns`: Group repeated mismatches into broader system adoption problems.
- `### Exception register`: Separate justified exceptions from unjustified drift and note the rationale when known.
- `### Priority actions`: Highlight the normalization work that should happen first to reduce drift or maintenance overhead.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed.
- `### Severity, confidence, and coverage confidence`: Separate consistency impact severity from evidence confidence and state whether coverage came from direct system-plus-implementation comparison, runtime confirmation, reusable reference comparison, or inference.
- `### Directional normalization guidance`: Recommend what should be normalized first to reduce future drift or maintenance cost.
- `### Limits and unknowns`: Explain where the system itself is unclear, outdated, or incomplete.

For each finding inside `### Compliance findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Expected system rule:
- Compliance status:
- Likely cause:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity evidence path available: system source plus implementation touchpoints -> runtime confirmation -> reusable reference artifacts -> inference.
- Start with `figma, repository` when the design system source and implementation touchpoints are both accessible.
- Use `figma` to inspect tokens, component variants, usage guidance, and approved patterns.
- Use `repository` to inspect token application, component usage, local overrides, and adoption gaps in implementation.
- Use `chrome_devtools` when runtime confirmation is needed for computed styles, behavior, or state-specific rendering.
- Use `reference/reuse` when reusable implementation patterns or prior accepted exceptions are the strongest available evidence.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/reuse, chrome_devtools`.
- If both paths fail, produce the best-guess output described as: A design-system compliance review with evidence-tagged conformance issues, grouped variance patterns, and justified exceptions called out.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-source review.

## Workflow Notes

- Do not treat every difference as a violation. Some differences are intentional exceptions, platform constraints, or signs the system needs to evolve.
- Treat `required_inputs` as real prerequisites. If the system source or exception rules are missing, infer a provisional contract, prefix each inferred item with `Assumed rule:` or `Assumed exception:`, and lower confidence for findings that depend on it.
- Build the system contract model before analysis. Do not jump from visual difference to compliance judgment.
- Compare at multiple levels: token, component, pattern, and flow.
- Run compliance passes in sequence so findings stay grounded: token usage first, component structure second, pattern and flow compliance third, then exceptions and system-gap classification.
- Prioritize repeated drift over isolated local variation.
- Make it obvious whether the problem is system non-adoption, missing system coverage, or design-system ambiguity.
- Distinguish clearly between observed variance, inferred cause, compliance status, and recommendation direction.
- After all passes, merge duplicates and consolidate overlapping findings before prioritization.

