---
name: translate
description: Translate product specs, design intent, and implementation constraints into frontend code that matches the intended browser experience.
---

# Translate

## Purpose

Use this skill to turn product intent into frontend implementation that behaves correctly in the browser. It focuses on making sure the code reflects the actual UI, component structure, and interaction model rather than just the visual mock.

## When to Use

- When a design spec, Figma frame, or product brief needs to become a working UI
- When component structure, props, and layout need to be mapped from design intent
- When the task is implementing a browser surface while preserving accessibility and responsiveness

## When Not to Use

- When the main problem is missing states or state transitions
- When the code already exists and only needs resilience or safety improvements
- When the task is primarily about copy tone, wording, or interaction language

## Required Inputs

- The design spec, mock, screenshot, or product requirement being implemented
- The target component boundary or page surface
- Relevant design tokens, breakpoints, and platform constraints
- Known behavior for loading, empty, error, and success cases
- Any implementation notes that affect markup, data flow, or interactivity

## Workflow

1. Read the source material in context and identify the exact user-facing surface to build.
2. Break the spec into layout, content, interaction, and data requirements.
3. Map the design intent to existing components, tokens, and patterns before creating anything new.
4. Implement the browser UI with semantic structure, responsive layout, and accessible interaction.
5. Check the output against the source for visual and behavioral drift.
6. Verify that the result still fits the surrounding product architecture and can be maintained.

## Design Principles / Evaluation Criteria

- Preserve the intended user experience, not just the visual shape
- Prefer existing primitives and tokens over one-off implementation
- Keep markup semantic and interaction predictable
- Make responsive behavior explicit rather than inferred
- Align the implementation with how the product actually works

## Output Contract

- Working frontend code that matches the source intent
- Notes on any intentional deviations or unresolved spec gaps
- Any component or token dependencies needed to finish the implementation cleanly

## Examples

### Example 1

Input:
- Source: Figma frame for a settings drawer
- Goal: Implement the drawer in React

Expected output:
- Build the drawer structure with the correct spacing, actions, and responsive behavior
- Reuse existing tokens and controls where possible
- Call out any missing mobile or error-state details before guessing

## Guardrails

- Do not invent behavior that is not supported by the product
- Do not trade semantic structure for visual convenience
- Do not duplicate existing components without checking the library first
- Do not treat translation as complete until the browser output is verified

## Optional Tools / Resources

- MCP: GitHub MCP, Chrome DevTools MCP, Figma MCP, Notion MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [React Docs](https://react.dev/), [TypeScript Docs](https://www.typescriptlang.org/docs/), [Storybook Docs](https://storybook.js.org/docs), [web.dev](https://web.dev/)
- Figma spec, screenshots, and exports
- Existing component library and token documentation
- Browser devtools for visual verification
- Implementation notes from adjacent engineering work
