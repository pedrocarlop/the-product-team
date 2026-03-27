---
name: respond
description: Define how the interface responds to user actions and system events with timely feedback, clear recovery paths, and behavior that feels immediate, understandable, and trustworthy.
---

# Respond

## Purpose

Use this skill to define how the UI responds when users act on it or when the system changes underneath them. The goal is to make each response feel clear, timely, and proportional so users always know whether their action worked, is still in progress, or needs recovery.

## When to Use

- When buttons, forms, menus, or content areas need feedback behavior after interaction
- When success, error, warning, or confirmation responses need to be specified
- When latency, optimistic updates, or background work affect what the user sees next

## When Not to Use

- When the main issue is visual polish rather than interaction feedback
- When the task is only to enumerate static states without describing what triggers them
- When the core problem is copy clarity, naming, or terminology drift instead of response behavior

## Required Inputs

- The triggering user action or system event
- The expected result, including success, failure, and timeout paths
- The latency or async behavior that affects how quickly feedback should appear
- Any motion, toast, inline message, or focus-management constraints
- Accessibility and recovery requirements for keyboard, screen reader, or error handling behavior

## Workflow

1. Start from the user action or system event, not from the visual treatment.
2. Describe the immediate feedback first, then the follow-up response, then the recovery path if something fails.
3. Decide whether the response should be inline, modal, ephemeral, or navigation-based.
4. Check whether the design system already provides the needed feedback pattern or interaction primitive.
5. Specify timing, ordering, and persistence so the response feels intentional rather than accidental.
6. Verify that the response does not hide progress, lose user input, or create uncertainty about what happened.

## Design Principles / Evaluation Criteria

- Feedback should arrive as quickly as the product can truthfully support
- Success should confirm the action without overcelebrating it
- Failure should explain what happened and how to recover
- Pending states should preserve user confidence and context
- Interruptions should not erase progress unless the product explicitly requires it
- Response behavior should be consistent across similar actions

## Output Contract

- A response specification for each trigger, including success, pending, failure, and recovery behavior
- Notes on feedback placement, timing, and duration
- Any focus, motion, or accessibility requirements needed for the response
- A short rationale for response choices that differ from the existing pattern library

## Examples

### Example 1

Input:
- Trigger: user saves billing details
- Constraint: request may take 2 to 4 seconds

Expected output:
- Response spec: show inline saving state immediately, disable duplicate submission, confirm success with a persistent inline message, and surface validation errors next to the field that failed

## Guardrails

- Do not create feedback that implies success before the product has actually succeeded
- Do not bury error recovery in a transient message that disappears too quickly
- Do not replace meaningful interaction response with decorative motion
- Do not design response behavior that depends on engineering guessing at timing

## Optional Tools / Resources

- Existing component and pattern library
- Prototype or screenshot evidence of the interaction in context
- Accessibility guidance for announcements, focus, and interruption handling
- Engineering notes on request timing, retries, and optimistic updates
