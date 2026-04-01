---
name: recover
description: Write error, empty, confirmation, and success messaging that helps users recover, proceed, or feel confident about what just happened.
---

# Recover

## Purpose

Use this skill to write state-based product messaging that reduces uncertainty, supports recovery, and helps users continue with confidence.

## When to Use

- When a feature needs error, empty, loading, success, or destructive-action copy
- When current messages describe the state but do not help the user move forward
- When state copy feels generic, alarmist, or inconsistent with the severity of the moment

## When Not to Use

- When the task is introducing a feature or teaching first-run behavior
- When the main issue is sentence-level clarity in ordinary interface copy
- When the product needs durable naming decisions or terminology governance

## Required Inputs

- The states that exist in the flow and what triggers each one
- What the user was trying to do before the state appeared
- Available recovery actions, fallback paths, or escalation options
- Severity, risk level, and whether the state is routine, blocking, or destructive
- Constraints such as localization, component limits, and legal wording

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: designer
project: <slug>
deliverable: designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. List the relevant states and define the user decision each state creates.
2. For each state, identify what happened, what the user needs to know, and what action is available next.
3. Write error and empty-state copy that matches the true cause and avoids unnecessary blame or alarm.
4. Write confirmation and success copy that is proportionate to the importance of the action.
5. Ensure every blocking or confusing state gives the user a clear path to proceed, retry, fix, or escalate.
6. Review the set together so tone and severity are calibrated consistently across the flow.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Clear explanation of what happened
- Accurate severity and calm tone
- Concrete next-step or recovery guidance
- Distinction between first-time empty, cleared empty, and error-caused empty states
- Proportionate success and confirmation messaging
- No false promises about system behavior or recovery certainty

## Output Contract

- A complete set of state-based strings for the relevant flow or surface
- Recovery paths or next-step guidance for failure and empty moments
- A brief note on any content rules for severity, reassurance, or escalation

## Examples

### Example 1

Input:
- State: User tries to delete a workspace
- Risk: High, destructive, irreversible for some content
- Available action: Confirm delete or cancel

Expected output:
- Confirmation title and body that clearly state the consequence
- Primary and secondary CTA labels
- Escalation note if recovery is not possible after confirmation

## Guardrails

- Do not write generic error copy when the system exposes a specific cause or action
- Do not invent recovery steps that engineering does not support
- Do not celebrate routine success states with distracting or cute language
- Do not use the same empty-state pattern for first-time, cleared, and failure conditions

## Optional Tools / Resources

- Product state diagrams or flow specs
- Error catalog, API notes, or support issue patterns
- Existing confirmation and empty-state patterns
- Localization and legal review guidance
