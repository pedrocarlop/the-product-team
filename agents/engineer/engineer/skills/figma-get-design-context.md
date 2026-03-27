---
name: figma-get-design-context
tool: mcp__figma__get_design_context
description: Retrieve full design specs — component structure, properties, tokens, and annotations — from the Figma file before implementing.
---

# Figma: Get Design Context

Use this skill to pull complete, structured design context from the approved Figma file. This gives you component hierarchy, property definitions, token names, variant conditions, and designer annotations needed to implement accurately without guessing.

## When to Use

- Before implementing any UI component to get exact specs rather than interpreting screenshots
- When resolving ambiguity between `ui-spec.md` and the visual design — the Figma context is the authoritative source
- When you need exact token names (spacing, color, typography) to use in implementation
- When checking variant conditions — what props trigger which visual states

## How to Use

Call `mcp__figma__get_design_context` with the Figma file URL and optionally the node ID for the specific frame or component. The response includes:
- Component hierarchy (which components compose the layout)
- Property names and values (exact prop names as defined in the design system)
- Token references (use these verbatim in CSS custom properties or component props)
- Annotation layers (read these — they contain design decisions not visible in the comp)

## What to Extract

- `CMP-*` component names to match against `component-mapping.md`
- Token names to use in implementation (do not hardcode values)
- All specified states — map each to an implementation condition
- Any annotation that says "implemented as X" or "edge case: do Y"

## Notes for Engineer

Prefer this tool over screenshots. The design context gives structured data; screenshots require interpretation. If the Figma context contradicts the written spec in `ui-spec.md`, surface the conflict in `implementation-notes.md` before proceeding.
