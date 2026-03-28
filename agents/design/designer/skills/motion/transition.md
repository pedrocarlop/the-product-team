---
name: transition
description: Design state-to-state motion that preserves continuity, clarifies cause and effect, and helps users understand what changed.
---

# Transition

## Purpose

Use this skill to design motion between states so users can track what changed, where it came from, and what is now available.

## When to Use

- When screens, panels, or components enter or leave the viewport
- When one UI state replaces another and continuity matters
- When the path between before and after needs explicit timing, easing, or sequencing

## When Not to Use

- When the task is only about a small feedback motion, like a button press or toggle snap
- When the main problem is attention hierarchy rather than state continuity
- When the surface should not animate at all in reduced-motion mode and only needs a static alternative

## Required Inputs

- The before state and after state for the interaction
- The spatial relationship between the old and new surfaces
- The user action or system event that triggers the change
- Timing constraints, interruption rules, and any shared elements
- Accessibility constraints, including reduced-motion behavior

## Workflow

1. Identify the exact state pair being designed.
2. Decide whether the motion should preserve spatial continuity, confirm causality, or simply minimize abruptness.
3. Define the entry, exit, overlap, and unchanged behavior for every moving piece.
4. Set duration, easing, delay, interruption, and reverse rules for each state change.
5. Check that the motion direction matches the interface model and does not create false affordances.
6. Specify implementation constraints such as allowed properties, performance limits, and focus behavior if relevant.
7. Specify the reduced-motion version and confirm it still communicates the change clearly.

## Design Principles / Evaluation Criteria

- Continuity over teleportation
- Cause and effect over decorative movement
- Directionality that matches the interface structure
- Fast enough that the user keeps task momentum
- Explicit reverse behavior, not just the happy path

## Output Contract

- A state-transition spec covering trigger, affected elements, entry, exit, overlap, unchanged elements, timing, easing, delay, interruption, and reverse behavior
- Any shared-element or morphing guidance needed for engineering or prototyping
- Reduced-motion fallback behavior for the same transition
- Implementation notes for performance, focus, and interaction safety

## Examples

### Example 1

Input:
- Before state: Filter panel collapsed
- After state: Filter panel expanded
- Context: Sidebar on desktop

Expected output:
- The panel expands from the sidebar edge over 220ms using ease-out.
- The trigger icon rotates 180 degrees over the first 120ms.
- Content inside the panel staggers in after the container begins moving.
- Reduced motion: instant state change with a brief opacity reveal for content.

## Guardrails

- Do not invent a motion path that contradicts the product layout
- Do not design only the forward transition and ignore the reverse
- Do not rely on long durations to disguise unclear state logic
- Do not skip reduced-motion behavior
- Do not summarize the transition as "slides in" without specifying from where, how fast, and what happens to the rest of the UI

## Optional Tools / Resources

- Figma prototypes
- Motion system tokens
- Screen recordings of the current interaction
- Accessibility guidance for reduced motion
