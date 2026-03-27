---
name: image-query
tool: image_query
description: Search for visual design references and UI pattern examples to inform high-fidelity visual decisions and validate design choices.
---

# Image Query

Use this skill to research visual precedents, UI pattern references, and competitive examples that inform high-fidelity design decisions — particularly for visual treatments not yet established in the design system.

## When to Use

- When designing a visual surface for a pattern that is not yet in the design system and you need to establish a fallback baseline
- When researching how high-fidelity visual treatments are applied across similar products (motion, elevation, surface color, state transitions)
- When looking for examples of a specific visual state (skeleton loading, progressive disclosure, inline editing) to understand the expected visual language
- When validating a proposed visual treatment against established design conventions

## How to Use

Call `image_query` with precise queries describing the visual pattern needed:
- `"skeleton loading state cards ecommerce product list"` — not `"loading design"`
- `"inline form validation error state design system"` — not `"form error"`
- `"data visualization empty state illustration product analytics"` — not `"empty state"`

Review returned images for:
- Visual hierarchy — how the layout guides attention
- State completeness — are all states shown?
- Design system signals — token-based spacing and color, not arbitrary values

## What to Extract

- Visual treatment patterns to document in `research-and-rationale.md` as evidence for design decisions
- Reference examples for states that the design system does not yet cover
- Anti-patterns — visual treatments that obscure information, reduce affordance, or violate conventions

## Notes for UI Designer

Use image references to establish visual precedent, not to copy solutions. Every visual decision that deviates from the design system must be justified in `research-and-rationale.md` with evidence that the deviation serves a documented user or design need.
