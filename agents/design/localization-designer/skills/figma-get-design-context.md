---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve component specs, layout constraints, and token definitions to assess locale adaptation requirements before authoring localization design.
---

# Figma: Get Design Context

Use this skill to inspect the design system components for locale-sensitivity — fixed widths, hardcoded text containers, icon-text combinations, and layout patterns that will break under text expansion or RTL rendering.

## When to Use

- Before designing locale variants, to identify which components have hardcoded size constraints
- When assessing whether existing components support RTL layout natively or require wrapping
- When checking token values for any hardcoded LTR-biased spacing (e.g., asymmetric padding that assumes left-to-right reading)
- When determining which components need locale-specific variants versus those that adapt automatically

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL or the component library node. Inspect for:
- Fixed-width text containers that will clip on text-expansion locales (e.g., German, Finnish)
- Icon placement relative to text — does it flip for RTL?
- Text alignment tokens — are they direction-agnostic (`start`/`end`) or absolute (`left`/`right`)?
- Number formatting, date display, and currency placement components

## What to Extract

- Components with hardcoded dimensions that need locale variants
- Tokens that are LTR-specific and need RTL alternates
- Components that already support `dir="rtl"` via standard CSS logical properties
- Any component that embeds locale-specific strings (format, unit, label)

## Notes for Localization Designer

Document every identified constraint in `research-and-rationale.md` before proposing adaptations. Prefer CSS logical properties and direction-agnostic tokens over locale-specific overrides. Only propose custom locale variants when the component structurally cannot adapt.
