---
name: stateful
description: Specify the complete visual state model for a UI surface so every control, container, and feedback area has defined appearance, content, and transition behavior across all interactive and data-driven states.
---

# Stateful

## Purpose

Use this skill to define the full visual state model of a UI surface so every element has a designed appearance for every moment the user might encounter. A good interface is not one screen at its best; it is every visual state that can appear when the product is used, interrupted, delayed, or partially complete.

## When to Use

- When a screen, component, or flow needs explicit visual coverage for idle, hover, focus, active, pressed, loading, empty, success, error, disabled, and partial states
- When a design is structurally complete but state appearance, content, and affordance are still ambiguous
- When the design system lacks state variants for a surface and new visual definitions are needed

## When Not to Use

- When the main issue is component logic, data flow, or state management architecture rather than visual state definition
- When the task is only to refine copy, naming, or label wording within an already-specified state
- When interaction behavior is already fully specified and the remaining work is implementation

## Required Inputs

- The exact surface or component boundary that needs state coverage
- User goals and the emotional context of each state (confidence during loading, reassurance during error)
- Any screenshots, flows, or specs that show the current visual treatment
- Existing design system state variants, tokens, and visual conventions
- Constraints: async latency expectations, data absence likelihood, permission gating, form validation rules

## Workflow

1. Inventory every visual entity that can change state: page sections, components, fields, action buttons, and feedback areas.
2. Enumerate the full visual lifecycle for each entity: default appearance, interaction states (hover, focus, active, pressed), data states (loading, empty, populated, partial), and outcome states (success, error, disabled).
3. Check the design system for existing state variants and tokens before creating new visual treatments.
4. Specify each state with its visual treatment: colors, opacity, iconography, content swap, placeholder style, and affordance changes.
5. Define visual transition rules: what changes instantly, what fades, what animates, and what uses skeleton or shimmer patterns.
6. Verify that edge states preserve visual hierarchy, layout stability, and accessibility (contrast ratios, focus indicators, screen reader announcements).

## Design Principles / Evaluation Criteria

- No visible state should be left to engineering interpretation
- State transitions should communicate change clearly without being distracting
- Loading and empty states should feel designed, not placeholder-like
- Error states should use visual emphasis proportional to severity and include recovery guidance
- Disabled states must be visually distinguishable and semantically correct for assistive technology
- Partial and recovery states should visually preserve progress and reduce user anxiety

## Output Contract

- A state inventory matrix for every interactive or data-driven element in scope
- Visual specs for each state: color, opacity, iconography, content, and affordance treatment
- Transition and animation notes for state changes
- Any state gaps in the design system that need new token or variant definitions
- A rationale for any visual state that deviates from existing system conventions

## Examples

### Example 1

Input:
- Surface: File upload panel with multi-file support
- Context: Users can add multiple files; some may fail validation

Expected output:
- State inventory: idle (drop zone visible), drag-over (highlighted border), uploading (progress indicator per file), upload-success (checkmark, file preview), upload-failed (error icon, inline retry affordance), disabled (muted, no drop zone)
- Visual notes: Failed files show red accent with retry button; successful uploads remain visible; primary action disabled during active uploads
- Transition: Upload progress uses determinate bar; success state fades in checkmark over 200ms

## Guardrails

- Do not define visual states that imply system behavior the product does not support
- Do not collapse distinct visual states into one generic fallback appearance
- Do not leave asynchronous moments without a designed loading or transition treatment
- Do not use state visual language inconsistently across related surfaces
- Do not skip accessibility review for contrast, focus visibility, and screen reader state announcements

## Optional Tools / Resources

- Design system component library, variant documentation, and token definitions
- Figma MCP for inspecting existing state treatments
- Screenshots or prototype flows showing current interaction moments
- Accessibility guidance for focus indicators, disabled patterns, and error announcement behavior
