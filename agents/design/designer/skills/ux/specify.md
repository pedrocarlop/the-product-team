---
name: specify
description: Write a complete UI specification for screens and states, including structure, behavior, responsiveness, content, and interaction details.
---

# Specify

## Purpose

Use this skill to turn a flow into a screen-by-screen specification that engineering and reviewers can implement and validate.

## When to Use

- When the task needs explicit screen behavior and state detail
- When responsive behavior, variants, and content need to be documented
- When handoff must be complete enough to reduce implementation ambiguity

## When Not to Use

- When the problem is still being framed
- When the request is only about the journey structure
- When the only need is component selection or mapping

## Required Inputs

- The approved flow and any unresolved assumptions
- The target screens, states, and interactions to specify
- Content requirements, validation rules, and accessibility constraints
- Responsive or platform-specific requirements
- Any approved component or design-system guidance

## Workflow

1. List every screen or state that the experience requires.
2. Specify what each screen contains, how it behaves, and what changes across states.
3. Document interactions, validations, feedback, and loading or error handling.
4. Define responsive behavior and any differences across breakpoints or platforms.
5. Check that copy, behavior, and visuals all align with the same product rules.
6. Verify there are no undefined transitions or "we'll figure it out later" gaps.

## Design Principles / Evaluation Criteria

- Every user-visible state should be explicit
- Behavior should be implementation-aware but not implementation-specific
- Content and interaction rules should agree
- Responsive behavior should be stated, not implied
- Ambiguity should be eliminated before handoff

## Output Contract

- A screen-by-screen UI specification
- State, variant, behavior, and responsiveness details
- Content and accessibility notes where relevant
- Open questions or exceptions that still need resolution

## Examples

### Example 1

Input:
- Screen: Payment method editor
- States: Default, validation error, loading, success

Expected output:
- Fields, labels, helper text, and primary action defined for each state
- Error handling described with exact trigger and user recovery
- Responsive rules stated for narrow and wide layouts

## Guardrails

- Do not leave critical behavior unspecified
- Do not describe one state as if it covered every state
- Do not over-index on visuals while ignoring interaction rules
- Do not specify behavior that conflicts with the approved flow

## Optional Tools / Resources

- Flow maps and research notes
- Design-system references and component constraints
- Accessibility requirements
- Existing page screenshots or mocks
