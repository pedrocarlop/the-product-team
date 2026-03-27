---
name: bridge
description: Translate design intent into implementation-ready guidance by mapping specs, tokens, states, and interaction details to the code surface that should carry them.
---

# Bridge

## Purpose

Use this skill to turn design intent into a clear technical bridge between Figma, specs, and the codebase so implementation can proceed with fewer assumptions.

## When to Use

- When a design needs component-by-component translation into code
- When tokens, spacing, typography, or state rules need to be mapped to implementation details
- When design and engineering are aligned on the goal but not yet on the exact technical shape

## When Not to Use

- When the task is to check an implemented screen for correctness
- When the main need is a prototype or interactive proof of concept
- When the issue is broader product direction rather than implementation detail

## Required Inputs

- The design source, spec, or screenshot to translate
- The target stack, component library, or implementation surface
- The tokens, variables, or design system rules that must be preserved
- Known edge cases, states, or constraints that affect implementation
- Any existing code references that should be reused instead of recreated

## Workflow

1. Read the design in context and identify the implementation boundary.
2. Break the surface into reusable parts: layout, components, tokens, states, and interactions.
3. Map each part to the best code primitive available in the target system.
4. Call out any gaps between the design and the current codebase, including missing components or tokens.
5. Convert ambiguous areas into concrete implementation notes or questions.
6. Verify the bridge preserves intent without inventing behavior that is not in the design.

## Design Principles / Evaluation Criteria

- Preserve intent before optimizing for convenience
- Prefer reuse over one-off implementation
- Make assumptions explicit when they are unavoidable
- Keep the bridge specific enough that engineering can act without guesswork
- Respect the target system's real constraints, not just the ideal design

## Output Contract

- A component and token mapping for the surface
- Implementation notes for states, interactions, and constraints
- A short list of open questions or gaps that need resolution
- References to existing code or primitives that should be reused

## Examples

### Example 1

Input:
- Source design: Settings panel with toggles, helper text, and error states
- Target stack: React with an existing design system

Expected output:
- Map each row to a reusable settings-row component
- Bind toggles to existing switch tokens
- Specify helper text and error-state behavior for long localized strings
- Flag the missing inline validation pattern as a gap

## Guardrails

- Do not rewrite product requirements or user flows under the guise of implementation mapping
- Do not approve a technical approach that conflicts with the design system without calling it out
- Do not bury unresolved gaps in prose; make them visible

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for design-to-code grounding
- [Figma MCP Docs](https://developers.figma.com/docs/figma-mcp-server/)
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Storybook Docs](https://storybook.js.org/docs)
- [Motion](https://motion.dev/)
- [Material Design for Web](https://m3.material.io/develop/web)
