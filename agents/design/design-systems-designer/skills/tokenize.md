---
name: tokenize
description: Define, name, layer, and mode design tokens so the design system expresses values as a maintainable contract instead of scattered literals.
---

# Tokenize

## Purpose

Use this skill to turn raw design values into a structured token system that supports consistency, theming, and code alignment.

## When to Use

- When a feature exposes repeated hard-coded values that should become tokens
- When token names, scopes, or layers need to be clarified or reorganized
- When light/dark or brand modes need to be represented in a durable way
- When primitive values need to be normalized into semantic or component tokens

## When Not to Use

- When the main problem is how components are assembled rather than how values are named
- When the task is writing usage guidance or documentation for adopters
- When the issue is release policy, ownership, or approval rather than token structure

## Required Inputs

- The source values, screenshots, or files that expose the token need
- The current token taxonomy, if one exists
- Theme or mode requirements such as light, dark, brand, or density variants
- The code target or toolchain that will consume the tokens
- Any naming conventions, prohibitions, or compatibility constraints already in force

## Workflow

1. Inventory the values in play and separate repeated system candidates from one-off exceptions.
2. Decide whether each value belongs at the primitive, semantic, or component layer.
3. Name tokens so their role, scope, and intent are obvious without tribal knowledge.
4. Define mode behavior and inheritance so themes can remap semantics cleanly.
5. Check token coverage against component and pattern needs to avoid hidden literals.
6. Verify that the resulting structure can be transformed or exported to code without ambiguity.

## Design Principles / Evaluation Criteria

- Semantic tokens should carry meaning, not implementation detail
- Names should be predictable, scannable, and self-documenting
- Modes should remap intent, not fork the system
- Primitive values should be minimized in authored components
- Token layers should reduce drift, not multiply exceptions

## Output Contract

- A token inventory with proposed names, layers, and values
- A clear mapping from raw values to primitive, semantic, or component tokens
- Notes on modes, inheritance, and any migration impact
- Any unresolved naming or compatibility questions that need governance

## Examples

### Example 1

Input:
- A button feature uses `#2563EB`, `16px`, and `8px` directly in multiple files
- The system already has color, space, and radius token layers

Expected output:
- `color-action-primary`
- `space-component-inline`
- `radius-control-default`
- Rationale for each mapping and any migration notes for adopters

## Guardrails

- Do not create tokens for values that are unlikely to be reused
- Do not encode implementation details in semantic names
- Do not introduce duplicate tokens that represent the same intent
- Do not skip mode definitions when the surface must support multiple themes
- Do not leave authored components dependent on raw values

## Optional Tools / Resources

- Figma MCP for inspecting current usage and publishing token references
- Token management tooling such as Tokens Studio or Style Dictionary
- Existing design system glossary or naming conventions
- Code token consumers, snapshots, or exports for validation
