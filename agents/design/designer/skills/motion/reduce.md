---
name: reduce
description: Design reduced-motion alternatives that preserve meaning while minimizing vestibular and attention load.
---

# Reduce

## Purpose

Use this skill to define how motion should behave when users prefer reduced motion or when animation would be disruptive, unnecessary, or risky.

## When to Use

- When a motion spec needs a reduced-motion counterpart
- When a surface contains large-area movement, zooming, parallax, or repeated animation
- When accessibility requirements call for simpler feedback instead of full motion

## When Not to Use

- When the task is about the main motion design itself
- When the surface needs detailed choreography rather than a fallback
- When the goal is to add motion rather than subtract it

## Required Inputs

- The original motion behavior
- The reason the motion exists
- The user context and accessibility concern
- The minimum communication that must remain after motion is reduced
- Any platform, browser, or product constraints on motion suppression

## Workflow

1. Identify the meaning the motion currently communicates.
2. Remove any movement that is not essential to that meaning.
3. Replace complex motion with instant state changes or minimal fades where needed.
4. Preserve timing only if it still improves comprehension.
5. Check for vestibular risk, repetition, and attention overload.
6. Specify what stays identical to the full-motion path, including state timing, focus behavior, and screen-reader-relevant changes.
7. Verify that the reduced version is still understandable on its own.

## Design Principles / Evaluation Criteria

- Preserve meaning, not ornament
- Prefer instant changes when motion adds no value
- Use minimal opacity changes when feedback still helps
- Avoid motion patterns that can trigger discomfort
- Make the reduced path deliberate, not an afterthought

## Output Contract

- A reduced-motion spec paired to the original motion, ideally as a side-by-side mapping
- Notes on which effects are removed, simplified, or replaced
- Notes on what remains identical, including focus, hierarchy, and state visibility
- Any accessibility rationale needed for engineering or QA

## Examples

### Example 1

Input:
- Original motion: Modal slides upward and scales in
- Context: Settings dialog

Expected output:
- Reduced motion: modal appears immediately with a brief opacity fade only.
- No scale or slide.
- Focus still moves into the dialog as expected.

## Guardrails

- Do not use reduced motion as a chance to redesign the interaction from scratch
- Do not preserve decorative effects that are not necessary
- Do not leave the reduced path undocumented
- Do not assume opacity fades are always sufficient if the meaning becomes unclear
- Do not describe reduced motion only as "less motion" without stating the exact fallback behavior

## Optional Tools / Resources

- Accessibility guidelines
- `prefers-reduced-motion` implementation notes
- Screen recordings of the full-motion experience
- QA checklists for motion accessibility
