---
name: apply-patch
tool: apply_patch
description: Write the high-fidelity UI design package — visual surface specs, complete state coverage, and design-system-aligned component mappings.
---

# Apply Patch

Use this skill to write the four UI design artifacts at full design-system fidelity. The UI Designer's output is the visual specification that engineering implements directly — completeness and precision are non-negotiable.

## When to Use

- After completing all visual design decisions and state coverage for the feature
- When writing `ui-spec.md` with full component, token, and state specifications
- When revising artifacts in response to design-system review feedback
- When updating `component-mapping.md` after resolving component selection decisions

## How to Use

Invoke `apply_patch` targeting the correct output file path:

- **research-and-rationale.md**: Visual design rationale — system alignment decisions, token choices, state coverage strategy, and documented exceptions
- **task-flows.md**: Visual flow — how users move through screens, what they see at each step, and which visual state applies at each transition
- **ui-spec.md**: Full visual specification — for every screen and state: component name and variant, token values, content strings, responsive behavior, motion/transition specification
- **component-mapping.md**: Every `CMP-*` entry with component name, source system, variant props, and exception justification

## What to Produce

Every state must be specified:
- Default, hover, focus, active, disabled
- Loading, error, empty, success
- Responsive treatment at each defined breakpoint
- Motion specification for transitions where applicable

## Notes for UI Designer

A `ui-spec.md` with "error state TBD" is incomplete. A `component-mapping.md` with hardcoded hex colors instead of token names will fail design-system review. Write the spec as if engineering will implement it without asking any follow-up questions.
