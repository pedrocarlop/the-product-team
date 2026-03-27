---
name: stateful
description: Define the full set of frontend states so every surface has clear idle, loading, empty, success, error, disabled, and transition behavior.
activation_hints:
  - "Use when a frontend surface needs explicit state coverage beyond its default visual appearance."
  - "Route here when forms, controls, data regions, or feedback surfaces need complete state definition."
  - "Do not use for copy cleanup, layout-only work, or safety hardening without state implications."
---

# Stateful

## Purpose

Use this skill to define the full state model of a frontend surface so engineering does not have to guess what happens when things change. A good UI is not only the happy path; it is every state that can happen when data is missing, delayed, interrupted, or partially complete.

## When to Use

- When a screen, component, or flow needs coverage for idle, hover, focus, active, loading, empty, success, error, disabled, and partial states
- When a design is visually complete but state behavior is still ambiguous
- When multiple UI regions need to stay consistent across shared states or recovery moments

## When Not to Use

- When the main issue is typography, spacing, or layout rhythm rather than state coverage
- When the task is only to refine copy or tone
- When the interaction behavior is already fully specified and only small polish remains

## Required Inputs

- The surface or component boundary that needs state coverage
- User goals, system outcomes, and known failure modes
- Any screenshots, flows, or implementation notes showing current behavior
- Existing design system states, variants, and token conventions
- Constraints such as async latency, permission gating, form validation, or data absence

## Workflow

1. Identify every element that can change state: page sections, components, fields, actions, and feedback areas.
2. Enumerate the full lifecycle for each element, including start, interaction, pending, completion, and failure moments.
3. Check the design system for existing state variants before inventing new ones.
4. Specify each state with its visual treatment, content, affordance, and any disabled or fallback behavior.
5. Define transition rules between states so engineering knows what changes instantly and what animates.
6. Verify that edge states do not break the hierarchy, layout, or accessibility of the surface.

## Design Principles / Evaluation Criteria

- No visible state should be left to guesswork
- State changes should be obvious without being noisy
- Loading and empty states should feel intentional, not placeholder-like
- Error states should tell users what happened and what they can do next
- Disabled states should be distinguishable and semantically correct
- Partial and recovery states should preserve progress whenever possible

## Output Contract

- A state inventory for every interactive or data-driven element in scope
- Visual and behavioral notes for each state, including transitions and fallback handling
- Any state gaps in the design system that need follow-up
- A concise rationale for any state that deviates from the existing system

## Examples

### Example 1

Input:
- Surface: file upload panel
- Context: users can add multiple files, some may fail validation

Expected output:
- State inventory: idle, drag-over, uploading, upload-success, upload-failed, disabled
- Notes: show inline retry for failed files, preserve successful uploads, disable the primary action during upload

## Guardrails

- Do not invent product behavior that the system does not support
- Do not collapse distinct states into one generic fallback
- Do not leave asynchronous moments unspecified
- Do not use state language to cover problems that are really layout or copy issues

## Optional Tools / Resources

- Design system component library and variant docs
- Screenshots or prototype flows showing interaction moments
- Implementation notes about async timing or validation
- Accessibility guidance for focus, disabled, and error behavior
