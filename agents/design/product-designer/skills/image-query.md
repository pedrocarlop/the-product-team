---
name: image-query
tool: image_query
description: Search for and analyze visual design references, competitor UI patterns, and design system examples to inform and validate design decisions.
---

# Image Query

Use this skill to research visual design patterns, competitive UX references, and design precedents before committing to a visual or structural design direction. Design decisions grounded in observed patterns are stronger than decisions made from first principles alone.

## When to Use

- When researching how comparable products solve the same design problem visually
- When looking for visual references to justify a component or layout choice
- When validating that a proposed visual pattern is consistent with established UI conventions
- When the design system does not cover a needed pattern and you are establishing a fallback with evidence

## How to Use

Call `image_query` with a targeted search query describing the visual pattern you need. Be specific:
- `"data table with inline editing and row actions"` — not `"table design"`
- `"empty state illustration with primary action button"` — not `"empty state"`
- `"multi-step form with step indicator progress bar"` — not `"form design"`

Review the returned images for:
- Structural patterns (layout, hierarchy, component placement)
- State coverage (does the reference show error, loading, and empty states?)
- Accessibility signals (keyboard navigation, focus indicators visible?)

## What to Extract

- Pattern approaches to document in `research-and-rationale.md` as design precedents
- Evidence that the chosen approach is an established convention rather than a novel invention
- Anti-patterns visible in references that the design should explicitly avoid

## Notes for Product Designer

Cite the visual references used in `research-and-rationale.md`. A design decision with a cited precedent is defensible; one based solely on aesthetic preference is not. Image references support rationale — they do not replace it.
