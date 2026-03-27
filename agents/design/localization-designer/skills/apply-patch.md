---
name: apply-patch
tool: apply_patch
description: Write the localization design package — locale adaptation specs, RTL layout guidelines, and component mapping for multi-locale support.
---

# Apply Patch

Use this skill to write the localization design package — documenting every locale-specific adaptation, layout change, and component decision needed to support the target locales.

## When to Use

- After completing locale research and component analysis
- When writing locale-specific layout requirements in `ui-spec.md`
- When documenting text expansion tolerances and RTL layout rules in `research-and-rationale.md`
- When mapping locale-specific component variants to `CMP-*` entries in `component-mapping.md`

## How to Use

Invoke `apply_patch` targeting the correct output file path. Structure each artifact for clarity across multiple locales:

- **research-and-rationale.md**: Document the target locales, their specific requirements, expansion ratios, and cultural adaptation rationale
- **task-flows.md**: Map how flows change across locales — different entry points, locale-specific paths, or conditional states
- **ui-spec.md**: Per-locale layout specifications — breakpoints adjusted for text density, RTL mirroring rules, locale-specific component states
- **component-mapping.md**: Each `CMP-*` entry must specify whether the component is locale-agnostic or requires a locale-specific variant

## What to Produce

For every adapted component:
- Whether adaptation is CSS-level (logical properties, `dir` attribute) or requires a design variant
- Text expansion tolerance specified as a percentage (e.g., "must support 40% text expansion")
- RTL mirroring specification — which elements flip, which do not

## Notes for Localization Designer

Specify adaptations at the component level, not just the page level. An IA spec that says "supports RTL" without per-component rules is not implementable. Every locale-specific behavior must have an explicit rule.
