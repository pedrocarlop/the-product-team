---
name: bridge
description: Translate design intent into implementation-ready guidance by mapping Figma specs, design tokens, component anatomy, states, and interaction details to the code surface that should carry them.
---

# Bridge

## Purpose

Use this skill to create a precise translation layer between design artifacts and the engineering codebase so implementation preserves design intent with minimal back-and-forth.

## When to Use

- When a design needs component-by-component translation into implementation guidance
- When tokens, spacing, typography, motion, or state rules need to be mapped from Figma to code primitives
- When design and engineering agree on the goal but the exact technical shape needs a translation document
- When the design system has gaps that must be identified before engineering starts building

## When Not to Use

- When the task is to verify an already-implemented screen against the design (use audit instead)
- When the main need is a prototype or interactive proof of concept
- When the issue is broader product direction rather than design-to-code translation

## Required Inputs

- The design source: Figma file, spec document, or annotated screenshot
- The target stack: framework, component library, and styling approach in use
- The design system tokens, variables, and component inventory available in code
- Known edge cases, responsive breakpoints, and state variations in the design
- Any existing code components that should be reused rather than recreated

## Workflow

1. Read the design holistically and identify the component boundaries, layout structure, and interaction model.
2. Break the surface into translatable units: layout containers, reusable components, token-driven styles, state variants, and interaction behaviors.
3. Map each design element to the best available code primitive: existing component, design token, CSS variable, or utility class.
4. Identify gaps between the design and the current code inventory: missing components, tokens without code equivalents, states not yet implemented.
5. Write implementation notes that resolve ambiguity: what happens at breakpoints, how truncation works, which interactions have motion, what accessibility attributes are needed.
6. Verify the translation preserves design intent without inventing behavior that is not in the spec.

## Design Principles / Evaluation Criteria

- Preserve design intent before optimizing for engineering convenience
- Prefer reusing existing code primitives over creating one-off implementations
- Make every assumption explicit; implicit decisions cause implementation drift
- The bridge should be specific enough that an engineer can build without returning to the designer
- Respect both the design system's constraints and the codebase's real capabilities

## Output Contract

- A component and token mapping table for the surface
- Implementation notes for responsive behavior, state handling, and interaction details
- A gap list: missing components, tokens, or patterns that need to be created
- References to existing code components and patterns that should be reused
- Open questions that need designer or engineer resolution before implementation begins

## Examples

### Example 1

Input:
- Source: Settings panel design in Figma with toggles, helper text, section headers, and error states
- Target: React app with an existing design system and Tailwind tokens

Expected output:
- Map each settings row to the existing `SettingsRow` component
- Bind toggle to the `Switch` component using `--color-interactive` token
- Helper text uses `Text/body-sm` token; error state adds `--color-error` and swaps helper text content
- Gap: No inline validation pattern exists in the component library; needs a new `InlineValidation` primitive
- Responsive note: On mobile, section headers become sticky and settings rows stack vertically

## Guardrails

- Do not rewrite product requirements or user flows under the guise of implementation mapping
- Do not approve a technical approach that conflicts with the design system without explicitly flagging the deviation
- Do not bury unresolved gaps in prose; surface them as a structured list
- Do not assume the engineer has access to the Figma file; the bridge document should be self-contained

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for design-to-code grounding
- [Figma MCP Docs](https://developers.figma.com/docs/figma-mcp-server/)
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Storybook Docs](https://storybook.js.org/docs)
- [Motion](https://motion.dev/)
- [Material Design for Web](https://m3.material.io/develop/web)
