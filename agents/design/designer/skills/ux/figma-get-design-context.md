---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve component specs, tokens, and design system patterns from Figma before authoring the UX/UI design package.
---

# Figma: Get Design Context

Use this skill to pull the full design system context — existing components, tokens, variants, and patterns — before making any component or visual design decisions. The target repository's design system is the first source of truth.

## When to Use

- Before selecting any component for the design package — verify it exists in the system first
- When you need exact token names for spacing, color, or typography to use in `ui-spec.md`
- When checking what states a component already supports versus which need design decisions
- When mapping the design to `CMP-*` entries in `component-mapping.md`

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL or the specific component or frame node ID. The response includes:
- Component hierarchy — how components are composed
- Property names and valid values (use these verbatim in `component-mapping.md`)
- Token names for design system values
- Variant conditions that define which props trigger which visual state

## What to Extract

- Component names (exactly as defined — not guessed from the visual)
- All available variants and the props that trigger them
- Token names for every design attribute (use the token name, never the raw value)
- Annotation content that clarifies designer intent for edge cases

## Notes for Product Designer

Never guess at a component name or variant from memory. Pull the exact definition from Figma. If the design system does not have a component that covers the use case, document the gap in `research-and-rationale.md` and justify the fallback choice — do not silently invent a custom pattern.
