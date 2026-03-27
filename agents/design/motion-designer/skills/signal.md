---
name: signal
description: Design motion that signals status, urgency, attention, and meaning without overwhelming the interface.
activation_hints:
  - "Use when motion needs to communicate status, priority, or attention shift."
  - "Route here for error states, success states, progress cues, live updates, and notification motion."
  - "Do not use for full state transitions, sequencing multiple elements, or reduced-motion fallback design."
---

# Signal

## Purpose

Use this skill to design motion as a signal: to tell users that something needs attention, something succeeded, something is in progress, or something changed.

## When to Use

- When a badge, alert, toast, or status indicator needs motion to carry meaning
- When the interface needs a gentle attention cue without stealing focus
- When a system event should feel visible but not noisy

## When Not to Use

- When the task is about navigation between states or screens
- When the motion is only decorative and does not change understanding
- When the signal would compete with the primary task or create anxiety

## Required Inputs

- The message the motion must communicate
- The urgency and severity of the signal
- The target audience's attention state and current task
- The surface where the signal appears and how long it should persist
- Accessibility constraints and reduced-motion requirements

## Workflow

1. Define the message in one sentence: what should the user understand?
2. Classify the signal by urgency, frequency, and importance.
3. Choose the smallest motion that makes the meaning legible.
4. Set the duration, repeat behavior, and stopping condition.
5. Make sure the signal supports the content instead of overpowering it.
6. Specify reduced-motion behavior and verify the meaning survives without movement.

## Design Principles / Evaluation Criteria

- Meaning first, motion second
- Minimal motion for high-frequency surfaces
- Distinct enough to be noticed, subtle enough to be ignored when not needed
- Consistent signal language across the product
- No motion that increases stress unnecessarily

## Output Contract

- A motion signal spec with trigger, intent, duration, and repeat behavior
- Guidance for prominence, color, and accompanying copy if needed
- Reduced-motion fallback that preserves the message

## Examples

### Example 1

Input:
- Signal: New message received
- Context: Messaging inbox header

Expected output:
- The unread badge pulses once at low amplitude over 180ms.
- The motion should not loop.
- Reduced motion: badge appears statically with no pulse.

## Guardrails

- Do not use attention-grabbing motion for low-priority events
- Do not create looping motion unless it is necessary and bounded
- Do not use the same signal treatment for success, warning, and error
- Do not make users chase status with distracting movement

## Optional Tools / Resources

- Product status taxonomy
- Alert and notification guidelines
- Figma mocks or screen recordings
- Accessibility guidance for motion and attention
