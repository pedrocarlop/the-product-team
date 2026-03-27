---
name: recover
description: Design fallback responses, error recovery, escalation behavior, and repeated-failure handling for conversation flows.
activation_hints:
  - "Use when the conversation must recover from misunderstanding, missing data, technical failure, or repeated user frustration."
  - "Route here for fallback copy, retry logic, escalation criteria, and dead-end prevention."
  - "Do not use for general script drafting unless recovery behavior is part of the flow."
---

# Recover

## Purpose

Use this skill to design how the assistant responds when the conversation goes off course, encounters failure, or needs to hand off to a different path.

## When to Use

- When the assistant may not understand the user's request
- When technical errors or unavailable data can interrupt the flow
- When repeated failure should trigger a human handoff or alternate route

## When Not to Use

- When the flow is already working and only wording needs tuning
- When the task is defining the assistant's overall scope
- When the conversation needs a normal happy-path script without failure handling

## Required Inputs

- The primary dialogue flow and the point where failures can occur
- Known error types, confidence thresholds, or unavailable states
- Escalation destinations and retry limits
- Any policy or product constraints on what recovery options are allowed
- Existing user-facing error patterns or support language

## Workflow

1. Identify the failure modes the conversation must survive.
2. Classify them by type: misunderstanding, missing information, technical failure, or repeated failure.
3. Define the assistant response for each failure mode, including what it should acknowledge and what it should ask next.
4. Add retry, clarification, or handoff behavior where needed.
5. Verify that every failure path still moves the user toward resolution.
6. Check that recovery language stays calm, honest, and aligned with the product's capabilities.

## Design Principles / Evaluation Criteria

- Recovery should preserve trust
- Fallbacks should explain the next step
- The assistant should not trap the user in loops
- Escalation should be available when the system cannot continue safely or usefully
- Error responses should be specific enough to be helpful

## Output Contract

- Fallback responses for each failure type
- Retry and clarification behavior
- Escalation triggers and handoff language
- Notes on failure modes that still need engineering support

## Examples

### Example 1

Input:
- Flow: appointment booking
- Failure: required slot remains empty after two attempts

Expected output:
- A clarification prompt after the first miss
- A handoff or alternate path after repeated failure

## Guardrails

- Do not use one generic fallback for every failure mode
- Do not blame the user for misunderstanding
- Do not promise a recovery action the product cannot perform
- Do not let recovery paths end without a next step

## Optional Tools / Resources

- `chrome-take-snapshot` to inspect existing error states
- `search-query` to compare fallback patterns in similar products
- `apply-patch` to write recovery copy into the design artifact

