---
name: annotate
description: Add accessibility notes, constraints, and implementation guidance to designs, specs, and handoffs so teams can build them correctly.
activation_hints:
  - "Use when a design or spec needs explicit accessibility annotations for handoff."
  - "Route here for notes about labels, focus order, states, keyboard behavior, ARIA, contrast, and motion requirements."
  - "Do not use for finding issues in a review or for rewriting the UI itself."
---

# Annotate

## Purpose

Use this skill to write accessibility annotations that make the intended behavior explicit for design, product, and engineering teams.

## When to Use

- When a design needs notes about keyboard, screen reader, or focus behavior
- When a prototype or spec needs accessibility constraints added to it
- When state changes, errors, or announcements need to be documented for implementation
- When the team needs a handoff artifact that removes ambiguity about accessibility expectations

## When Not to Use

- When the main job is to discover defects in an existing design or implementation
- When you need to rework the interface to make it more accessible
- When you are verifying that an implementation matches a known accessibility requirement

## Required Inputs

- The design, screen, flow, or component being annotated
- The user interactions that matter for accessibility
- Any findings from an audit that need to be translated into notes
- Existing design system conventions or component rules
- The target platform, framework, or handoff format

## Workflow

1. Identify the part of the interface where ambiguity would create accessibility risk.
2. Add notes for semantics, labels, names, states, and relationships that must exist in implementation.
3. Specify keyboard behavior and focus movement where users interact with dynamic UI.
4. Call out contrast, motion, and color-only dependencies where the design needs constraints.
5. Mark any requirement that must be preserved across responsive states, localization, or theming.
6. Keep notes concise enough for handoff, but precise enough to be implemented without guesswork.

## Design Principles / Evaluation Criteria

- Notes should describe user-facing behavior, not just technical jargon
- Annotations should reduce ambiguity, not create a second spec layer that conflicts with the first
- Critical accessibility decisions should be visible where the design is reviewed
- Accessibility annotations should stay aligned with component and system standards

## Output Contract

- Clear accessibility notes attached to the relevant design or spec
- Implementation guidance for labels, focus, state changes, and announcements
- Any open questions or unresolved decisions that still need product input
- Short rationale when a note changes the intended interaction or structure

## Examples

### Example 1

Input:
- Component: Dialog
- Context: Confirmation before deleting a project

Expected output:
- Annotation: "Move focus to the dialog heading on open; return focus to the triggering button on close."
- Annotation: "Disable background interaction while the dialog is open."
- Annotation: "Provide a descriptive accessible name that includes the project name."

## Guardrails

- Do not annotate unsupported behavior as if it already exists
- Do not rely on placeholder text to convey required input labels
- Do not add notes that conflict with the product or design system language
- Do not turn annotations into implementation code unless the handoff format requires it

## Optional Tools / Resources

- Figma MCP and Chrome DevTools MCP for grounded screenshots, snapshots, and interaction checks
- Notion MCP for audit notes and handoff context
- [WCAG Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [Material Design Accessibility](https://m3.material.io/components)
- [Carbon Accessibility Guidelines](https://carbondesignsystem.com/guidelines/accessibility/overview/)
