---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve existing navigation components, taxonomy structures, and IA patterns from the Figma design system before authoring new IA decisions.
---

# Figma: Get Design Context

Use this skill to inspect the existing navigation and structural patterns in the design system before proposing new IA decisions. Reuse approved navigation components and structural templates before introducing new patterns.

## When to Use

- Before designing a new navigation structure to check what components and patterns already exist in the system
- When selecting which components to use for menus, breadcrumbs, sidebars, filters, or search surfaces
- When verifying that the proposed IA aligns with the visual language of the existing product structure
- When mapping content groupings to the available component options

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL or the node ID for the navigation or layout library. Inspect:
- Navigation component names and their variant conditions
- Available layout templates for multi-level navigation
- Existing filter, search, and taxonomy display components
- Spacing tokens and column systems used in structural layouts

## What to Extract

- Component names for use in `component-mapping.md`
- Variant options that support different IA hierarchy depths
- Structural patterns that the IA must stay consistent with (e.g., sidebar width constraints, breadcrumb depth)

## Notes for Information Architect

The IA must be buildable with available components. Proposing a navigation structure that requires entirely new components is an avoidable blocker. Ground structural decisions in what the design system already supports, and justify any gap explicitly in `research-and-rationale.md`.
