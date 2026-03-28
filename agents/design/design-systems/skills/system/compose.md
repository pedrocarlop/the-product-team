---
name: compose
description: Build components and patterns from approved tokens and primitives so the design system has clear anatomy, variants, and composition rules.
---

# Compose

## Purpose

Use this skill to assemble system components and patterns from approved tokens and primitives with clear structure and reuse boundaries.

## When to Use

- When a new component or pattern needs to be designed for the system
- When variants, states, or responsive behaviors need to be organized coherently
- When existing pieces need to be recomposed into a cleaner system asset
- When component composition rules need to be clarified for adopters

## When Not to Use

- When the main task is token naming or theme structure
- When the request is primarily about writing usage guidance or documentation
- When the work is about ownership, change control, or deprecation policy

## Required Inputs

- The component or pattern goal and the user problem it must solve
- Approved tokens and primitives available for reuse
- Required states, variants, and interaction behaviors
- Layout constraints, responsiveness needs, and accessibility requirements
- Any existing nearby components that should be reused or referenced

## Workflow

1. Confirm whether the request is for a component, variant, composite pattern, or extension of an existing asset.
2. Map the component anatomy and identify what is fixed, optional, or variant-driven.
3. Compose the asset from approved building blocks and named tokens only.
4. Define states, behavior, and composition rules so the asset can be used consistently.
5. Check for overlap with existing system assets and remove unnecessary duplication.
6. Verify that the component can be documented, implemented, and governed without ambiguity.

## Design Principles / Evaluation Criteria

- Composition should express intent, not just visual arrangement
- Reuse should come before novelty when the system already has a fit
- Variants should be bounded and understandable
- Anatomy should be explicit enough for design and code alignment
- The asset should strengthen the system vocabulary, not widen it casually

## Output Contract

- A component or pattern definition with anatomy, states, and variants
- Notes on token dependencies and composition rules
- Reuse or deprecation notes for related assets
- Any open implementation or accessibility questions that still need follow-up

## Examples

### Example 1

Input:
- A dashboard needs a card component that supports summary, action, and loading states
- The system already has typography, spacing, and surface tokens

Expected output:
- A composed card anatomy with header, body, and footer regions
- Defined variants for summary and action content
- State handling for loading and empty conditions
- Reuse notes for any existing primitives

## Guardrails

- Do not create one-off structure when an existing component already covers the need
- Do not hide missing behavior inside undocumented local exceptions
- Do not make variants so broad that they become separate components in disguise
- Do not compose against raw values when approved tokens exist
- Do not skip accessibility or interaction states because the component is mostly static

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for component composition context
- [Storybook Docs](https://storybook.js.org/docs)
- [W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/)
- [Material Design](https://m3.material.io/)
- [zeroheight](https://zeroheight.com/)
- [How to document components](https://storybook.js.org/docs/writing-docs)
