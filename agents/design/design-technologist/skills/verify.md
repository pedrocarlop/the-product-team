---
name: verify
description: Check that a design implementation matches the intended spec across layout, tokens, behavior, accessibility, and state coverage, then report the gaps that still need attention.
activation_hints:
  - "Use when an implementation needs final comparison against the design."
  - "Route here when you need to confirm fidelity, behavior, or state coverage."
  - "Do not use for proposing new design directions or rebuilding the surface."
---

# Verify

## Purpose

Use this skill to compare the built surface against the intended design and identify exactly where the implementation matches, drifts, or breaks under real conditions.

## When to Use

- When a screen, component, or interaction is ready for design QA
- When the team needs evidence that the implementation matches the spec
- When there is risk of token drift, spacing drift, state loss, or accessibility regressions

## When Not to Use

- When the implementation has not been built yet
- When the task is to reinterpret or improve the design itself
- When the primary need is a production prototype or implementation bridge

## Required Inputs

- The intended design source or spec
- The implemented surface or screenshot to compare
- The acceptance criteria, states, or interactions that matter most
- Any known constraints that might explain expected deviation
- Relevant tokens, component rules, or accessibility requirements

## Workflow

1. Compare the implementation against the source at the level of layout, spacing, tokens, content, and interaction.
2. Check the important states and edge cases, not just the happy path.
3. Distinguish acceptable implementation constraints from true fidelity gaps.
4. Capture evidence for each mismatch so the owning team can act quickly.
5. Prioritize findings by user impact and release risk.
6. Verify that any fix recommendation is traceable to the spec or design intent.

## Design Principles / Evaluation Criteria

- Fidelity should be measured against the intended design, not memory
- Significant state or behavior gaps matter more than tiny visual noise
- Evidence should be specific enough to reproduce the issue
- Accessibility and token discipline count as part of fidelity
- Verification should end with clear next steps, not vague approval

## Output Contract

- A verification report with matched areas and mismatches
- Prioritized findings with evidence and impact
- A short summary of release readiness or remaining risk
- Notes on any spec ambiguity that made verification uncertain

## Examples

### Example 1

Input:
- Spec: Payment form with validation, loading, and disabled states
- Implementation: Built screen from the design system

Expected output:
- Confirm the layout and tokens for the happy path
- Flag missing inline error states and disabled submit behavior
- Note the ambiguous spec around loading spinner placement

## Guardrails

- Do not confuse verification with redesign
- Do not ignore missing states just because the happy path looks correct
- Do not mark something approved when the evidence is incomplete

## Optional Tools / Resources

- Screenshots or screen recordings
- Design specs and acceptance criteria
- Accessibility checklists and token references
- Previous audit or hardening notes
