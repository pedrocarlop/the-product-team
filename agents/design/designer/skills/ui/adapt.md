---
name: adapt
description: Adapt an approved UI surface across breakpoints, devices, and contexts without losing hierarchy, usability, or design-system fidelity.
---

# Adapt

Use this skill to translate a UI surface from one context into a complete cross-context specification.

## When to Use

- When a screen or component needs mobile, tablet, desktop, or platform-specific treatment
- When the current design only works at one viewport or interaction mode
- When content, navigation, or controls need to change shape across contexts

## How to Use

List the required contexts first: viewport ranges, device classes, pointer modes, platform conventions, and any special outputs such as print or email if they are explicitly in scope. For each context, decide what stays constant, what reflows, what collapses, and what must be reprioritized.

Adapt the layout structurally rather than simply shrinking it. Rework navigation patterns, touch target sizes, spacing density, reading order, and content priority for each context. Account for text expansion, localization, and error or empty states at smaller sizes.

## What to Produce

- Breakpoint-specific layout and component behavior
- Navigation and information-priority changes by context
- Touch, spacing, and text-length rules needed for each viewport
- Any platform-specific exceptions that must be called out in the UI spec

## Notes for UI Designer

Do not hide critical functionality just to make a layout fit. If the surface needs materially different behavior by platform or locale, flag that explicitly instead of leaving engineering to infer it.
