---
name: adapt
description: Adapt mobile screens, patterns, and interactions so they work across iOS, Android, assistive technologies, and device constraints without losing product intent.
---

# Adapt

## Purpose

Use this skill to change a mobile design or interaction model so accessibility and platform constraints are built into the experience instead of layered on afterward.

## When to Use

- When the current layout or interaction pattern excludes some users
- When a component needs a more accessible or device-appropriate pattern than the one originally chosen
- When contrast, focus visibility, text size, motion, or structure needs to be redesigned
- When the interface needs to better support assistive technologies or platform conventions without losing product intent

## When Not to Use

- When the issue is only to document an existing decision
- When the task is to inspect for defects without changing the design
- When the implementation already exists and only verification is needed

## Required Inputs

- The original mobile design, flow, or component
- The barrier or platform mismatch that must be addressed
- The user task and the context in which the barrier appears
- Any product or design constraints that must be preserved
- Relevant mobile patterns or platform primitives available for reuse

## Workflow

1. Identify the minimum change needed to remove the barrier without breaking the product goal.
2. Prefer established accessible and platform-native patterns over custom interaction design.
3. Adjust structure, spacing, hierarchy, or affordance so the interaction is perceivable and operable.
4. Ensure states such as hover, focus, disabled, error, and loading remain accessible where relevant.
5. Recheck the design across responsive states, localization, motion preferences, and both major platforms.
6. Capture the updated accessibility requirements so the fix can be implemented consistently.

## Design Principles / Evaluation Criteria

- Accessibility improvements should preserve task clarity and product intent
- Changes should reduce reliance on memory, precision, or hidden affordances
- The adapted design should be robust across input modes and assistive technologies
- A good adaptation avoids introducing new barriers while fixing the old one

## Output Contract

- Revised mobile design direction or interaction model
- Explanation of the barrier being removed
- Any tradeoffs introduced by the adaptation
- Notes needed for implementation or follow-up verification

## Guardrails

- Do not preserve inaccessible patterns just because they look familiar
- Do not fix one barrier in a way that creates another, such as a focus trap or poor contrast
- Do not assume a visual change is enough if keyboard or screen reader behavior is still unclear
- Do not introduce motion or complexity when a simpler pattern works better

## Optional Tools / Resources

- Figma MCP for screenshots, specs, and platform variants
- Design system components and tokens
- Contrast and typography checks
- Keyboard, VoiceOver, and TalkBack notes from audits
