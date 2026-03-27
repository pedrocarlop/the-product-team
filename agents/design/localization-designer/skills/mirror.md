---
name: mirror
description: Adapt layouts, navigation, and directional UI so RTL locales read and operate naturally instead of appearing flipped as an afterthought.
activation_hints:
  - "Use when designing for Arabic, Hebrew, Persian, Urdu, or other RTL locales."
  - "Route here for mirrored layout order, directional icons, alignment, and reading order decisions."
  - "Do not use for text expansion alone or for general localization copy work."
---

# Mirror

## Purpose

Use this skill to make RTL interfaces feel native by mirroring structure, direction, and interaction cues where appropriate.

## When to Use

- When a screen will be shipped in an RTL locale
- When navigation, breadcrumbs, steppers, or directional icons must be reversed
- When alignment, padding, or reading order needs locale-specific adjustment

## When Not to Use

- When the work is purely about longer translated copy in an LTR layout
- When the issue is cultural adaptation rather than directionality
- When the component already has a tested RTL implementation and only copy is changing

## Required Inputs

- The screen or component to review
- Target locales and whether each one is RTL
- Screenshots or Figma context showing current LTR behavior
- Any design system or component RTL support notes

## Workflow

1. Identify every directional element on the surface: layout, text alignment, icons, progress, and navigation order.
2. Mirror the reading order and spatial hierarchy where the locale expects it.
3. Flip directional icons and motion cues only when they communicate movement or progression.
4. Recheck components with mixed-content rows such as numbers, icons, and labels.
5. Confirm that focus order, affordances, and visual scanning still match user expectations.
6. Validate the mirrored state alongside the default layout so both remain coherent.

## Design Principles / Evaluation Criteria

- Directional meaning must match the locale
- Mirroring should feel intentional, not mechanically flipped
- Text alignment and spacing should support natural reading flow
- Icons should preserve semantic meaning after adaptation
- Mixed-direction content should remain legible and stable

## Output Contract

- List of mirrored elements and the rationale for each
- Any directional icons or motion cues that need locale-specific handling
- Notes on components that require explicit RTL support from engineering
- Remaining gaps that need locale QA

## Examples

### Example 1

Input:
- Surface: Stepper with three stages
- Locale: Arabic

Expected output:
- Recommendation: Mirror the stage order, move the active step indicator to the RTL reading side, and review arrow icons for directionality.

## Guardrails

- Do not treat RTL as a CSS-only flip
- Do not reverse meaning-bearing icons blindly
- Do not forget mixed LTR content such as product names, numbers, or codes
- Do not assume the default layout works once the text direction changes

## Optional Tools / Resources

- Figma MCP for mirrored layout review
- Design system RTL documentation
- Locale-specific QA screenshots
- Component implementation notes for direction-aware behavior
