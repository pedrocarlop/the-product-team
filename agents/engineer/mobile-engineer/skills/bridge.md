---
name: bridge
description: Translate mobile design intent into implementation-ready guidance by mapping specs, tokens, states, and bridge boundaries to the code surface that should carry them.
activation_hints:
  - "Use when a mobile design needs to be handed off to engineering with fewer ambiguities."
  - "Route here when platform choices, native boundaries, or token usage need explicit mapping."
  - "Do not use for visual QA or post-implementation verification."
---

# Bridge

## Purpose

Use this skill to turn mobile design intent into a clear technical bridge between Figma, specs, and the codebase so implementation can proceed with fewer assumptions.

## When to Use

- When a mobile design needs component-by-component translation into code
- When tokens, spacing, typography, or state rules need to be mapped to implementation details
- When JS-to-native boundaries, platform-specific modules, or bridge behavior need explicit mapping
- When design and engineering agree on the goal but not yet the exact technical shape

## When Not to Use

- When the task is to check an implemented screen for correctness
- When the main need is a prototype or interactive proof of concept
- When the issue is broader product direction rather than implementation detail

## Required Inputs

- The design source, spec, screenshot, or Figma node to translate
- The target stack, component library, and mobile implementation surface
- The tokens, variables, or system rules that must be preserved
- Known edge cases, states, or constraints that affect implementation
- Any existing code references or native capabilities that should be reused

## Workflow

1. Read the design in context and identify the implementation boundary.
2. Break the surface into reusable parts: layout, components, tokens, states, interactions, and native dependencies.
3. Map each part to the best code primitive available in the target system.
4. Call out gaps between the design and the current codebase, including missing components, tokens, or native APIs.
5. Convert ambiguous areas into concrete implementation notes or questions.
6. Verify the bridge preserves intent without inventing behavior that is not in the design.

## Design Principles / Evaluation Criteria

- Preserve intent before optimizing for convenience
- Prefer reuse over one-off implementation
- Make assumptions explicit when they are unavoidable
- Keep the bridge specific enough that engineering can act without guesswork
- Respect the target system's real constraints, not just the ideal design

## Output Contract

- A component, token, and native-boundary mapping for the surface
- Implementation notes for states, interactions, and constraints
- A short list of open questions or gaps that need resolution
- References to existing code, primitives, or platform APIs that should be reused

## Guardrails

- Do not rewrite product requirements or user flows under the guise of implementation mapping
- Do not approve a technical approach that conflicts with the mobile design system without calling it out
- Do not bury unresolved gaps in prose; make them visible

## Optional Tools / Resources

- Figma MCP for exact values, screenshots, and assets
- Component inventory or mobile design system docs
- Existing implementation patterns in the codebase
- State matrices, content rules, and accessibility guidance
