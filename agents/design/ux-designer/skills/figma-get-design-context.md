---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve existing UX patterns, component library definitions, and interaction scaffolding from Figma before authoring new flows and wireframes.
---

# Figma: Get Design Context

Use this skill to inspect the existing UX components, interaction patterns, and design-system scaffolding before proposing new flows or wireframes. The target repository's existing UX patterns are the first source of truth — reuse before inventing.

## When to Use

- Before designing a new flow — check what interaction patterns and navigation components already exist
- When selecting wireframe-level components (modals, drawers, steppers, accordions) — verify available variants
- When grounding the IA of the feature in the existing product's structural conventions
- When mapping components to `CMP-*` entries in `component-mapping.md`

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL or the specific component set node. Inspect for:
- Navigation and layout scaffolding components (page shell, sidebars, content areas)
- Interactive pattern components (steppers, tabs, accordions, modals, drawers)
- State components for loading, error, and empty conditions
- Interaction triggers and their documented behavior (what opens a modal, what triggers a drawer)

## What to Extract

- Component names for all structural and interactive elements used in the flows
- Variant options that cover different UX states without requiring custom components
- Documented constraints on component usage (e.g., modal depth limit, drawer z-index stacking)
- Any interaction patterns already established for similar flows in the product

## Notes for UX Designer

Map every wireframe element to an existing component before proposing custom patterns. A wireframe that shows "custom multi-select picker" when the design system has an approved multi-select component is an avoidable blocker. Check the system first.
