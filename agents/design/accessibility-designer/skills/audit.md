---
name: audit
description: Audit designs, flows, and implementations for accessibility barriers, WCAG gaps, and assistive-technology regressions before they ship.
activation_hints:
  - "Use when you need to evaluate a screen, flow, component, or implementation for accessibility risks."
  - "Route here for keyboard access, screen reader support, contrast, focus order, form semantics, motion, and color-only state problems."
  - "Do not use for simply rewriting content or making generic visual polish changes."
---

# Audit

## Purpose

Use this skill to find accessibility barriers, classify their severity, and turn vague concerns into specific, testable findings.

## When to Use

- When a design, prototype, or implementation needs an accessibility review
- When you need to identify WCAG issues before handoff or release
- When you need to compare the intended interaction against the actual keyboard or screen reader experience
- When you need a prioritized list of barriers and their likely impact

## When Not to Use

- When the task is only to annotate a spec after the accessibility decisions are already made
- When the task is to rewrite the UI so it better fits accessibility constraints
- When the task is to verify a known fix after implementation

## Required Inputs

- The screen, flow, component, or code path to review
- The interaction model and user task for the moment being audited
- Relevant screenshots, prototypes, code, or DOM markup
- Any known accessibility requirements, standards, or product policies
- The assistive technologies or devices that matter for this review

## Workflow

1. Define the user task and the accessibility-critical moments in the flow.
2. Check structural accessibility first: semantics, labels, headings, landmarks, and reading order.
3. Test interaction accessibility next: keyboard reachability, focus order, focus visibility, and traps.
4. Evaluate perceptual accessibility: contrast, text legibility, motion, state communication, and reliance on color alone.
5. Test assistive-technology behavior where possible, including screen readers and browser accessibility trees.
6. Record each issue with the affected element, the user impact, and the specific criterion or rule it violates.
7. Sort findings by severity and by the likelihood that they block task completion.

## Design Principles / Evaluation Criteria

- Accessibility failures are user-blocking product defects, not cosmetic issues
- A good audit distinguishes between design gaps and implementation bugs
- Findings should be reproducible and tied to concrete evidence
- Severity should reflect actual user harm, not just checklist presence
- The audit should surface systemic patterns, not only isolated defects

## Output Contract

- A prioritized list of accessibility findings
- For each finding: what breaks, who it affects, how to reproduce it, and the likely fix direction
- WCAG references or other applicable standards when relevant
- A short summary of overall risk, including any areas not fully tested

## Examples

### Example 1

Input:
- Screen: Checkout payment step
- Context: New payment method form
- Concern: Users cannot tab to the submit button in a predictable order

Expected output:
- Finding: Focus order skips the card expiry field and lands on the submit button early
- Impact: Keyboard users may submit incomplete data or become disoriented
- Likely fix: Reorder the DOM or focus sequence so fields follow the visual order

## Guardrails

- Do not label everything as a blocker unless it actually prevents completion
- Do not guess at screen reader behavior if the control was not tested
- Do not stop at automated scan output if manual checks are still needed
- Do not bury the real user impact under generic compliance language

## Optional Tools / Resources

- Axe or other automated accessibility scanners
- Browser accessibility tree inspection tools
- Keyboard-only navigation testing
- Screen reader testing with NVDA, VoiceOver, or similar tools
- Figma or prototype inspection for contrast and layout risks
