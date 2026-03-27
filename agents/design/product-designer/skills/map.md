---
name: map
description: Map each design decision to the source component, pattern, token, or exception it depends on so the handoff stays traceable.
activation_hints:
  - "Use when component choices need to be justified against the design system or source repository."
  - "Route here when the handoff needs a traceable mapping from UI requirements to existing assets."
  - "Do not use for flow design or problem framing."
---

# Map

## Purpose

Use this skill to document how each UI requirement resolves into an existing component, token, pattern, or justified exception.

## When to Use

- When engineering needs a clear source for each UI decision
- When component choices must be tied back to the design system or source repository
- When a fallback, wrapper, or custom pattern needs explicit justification

## When Not to Use

- When the work is still at the framing or flow level
- When no component decision has been made yet
- When the task is only about copy, content order, or narrative rationale

## Required Inputs

- The specified screens or states
- The available design-system components, tokens, and patterns
- Any source-system references or approved fallback rules
- Exceptions, wrappers, or custom behavior that need justification
- Accessibility or responsiveness constraints that affect the mapping

## Workflow

1. Identify each UI requirement that needs a source decision.
2. Match the requirement to the closest approved component, token, or pattern.
3. Document any deviations, wrappers, or custom behavior and why they are necessary.
4. Note what is reused, what is adapted, and what must be built or justified separately.
5. Verify the mapping is traceable and consistent across related screens or states.
6. Check that no critical decision is left as an unnamed custom solution.

## Design Principles / Evaluation Criteria

- Traceability over vague similarity
- Reuse before customization
- Justified exceptions rather than silent drift
- Consistency across related states and screens
- Enough detail for implementation to follow the decision safely

## Output Contract

- A component or token mapping for each major UI decision
- Source references for reused assets or patterns
- Explicit justification for wrappers, fallbacks, or custom work
- Notes on any accessibility or responsive implications

## Examples

### Example 1

Input:
- UI needs a multi-select tag picker with chips and keyboard support
- The system has a combobox but not an exact tag-picker pattern

Expected output:
- Map the field to the combobox base component
- Note the chip wrapper and why it is needed
- Document keyboard behavior and any gaps versus the base component

## Guardrails

- Do not claim reuse where the component does not actually fit
- Do not hide custom work inside a generic mapping entry
- Do not skip token or source references when they matter
- Do not let mapping become a substitute for design decisions

## Optional Tools / Resources

- Design-system inventory or component docs
- Figma context or source repository references
- Implementation constraints from engineering
- Accessibility and responsiveness notes
