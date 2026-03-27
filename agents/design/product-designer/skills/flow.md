---
name: flow
description: Design task flows that cover entry points, happy paths, alternates, errors, empty states, recovery, and completion for a product experience.
activation_hints:
  - "Use when you need to map the user's path through a feature before UI specification."
  - "Route here when edge cases, branching logic, or recovery steps need to be clarified."
  - "Do not use for copy-only edits or component-level documentation."
---

# Flow

## Purpose

Use this skill to define how users move through a product experience so the team can see every meaningful path, state, and handoff.

## When to Use

- When the user journey has branches, dependencies, or recovery steps
- When the team needs to understand the full path before designing screens
- When edge cases, errors, or empty states could change the user's next step

## When Not to Use

- When the problem is only a local screen hierarchy issue
- When the task is a single interaction or label rewrite
- When the journey is already settled and you only need UI details

## Required Inputs

- The framed problem and the user goal
- Entry points, exit points, and any known branching logic
- Validation, permission, loading, error, or empty-state conditions
- Recovery paths, fallback behavior, and success criteria
- Any platform or navigation constraints that affect the sequence

## Workflow

1. Start with entry points and the user's reason for arriving in the flow.
2. Map the happy path from first step to successful completion.
3. Add alternate paths, interruptions, and error recovery.
4. Include empty, loading, blocked, and success states where they change behavior.
5. Note any decision points where the user's next step depends on system state.
6. Verify the flow can be understood without reading the implementation details.

## Design Principles / Evaluation Criteria

- Complete coverage over optimistic coverage
- Recovery paths should be obvious and actionable
- Branching should reflect actual product behavior
- The flow should make dependencies and decision points visible
- Users should always know what happens next

## Output Contract

- A flow sequence or step list with all major branches
- Entry, success, alternate, error, empty, and recovery paths
- State transitions and any user decision points
- Open questions or assumptions that affect the final interaction model

## Examples

### Example 1

Input:
- Feature: Invite teammates to a workspace
- Concern: Some invites may be invalid or already in use

Expected output:
- Happy path: Enter email, send invite, confirm success
- Alternate path: Multiple invites entered at once
- Error path: Invalid email or duplicate member
- Recovery path: Correct entry and retry without losing valid invites

## Guardrails

- Do not model only the happy path
- Do not hide recovery logic inside a vague "error state"
- Do not collapse distinct states that change user behavior
- Do not create a flow that depends on behavior the product does not support

## Optional Tools / Resources

- Product requirements and acceptance criteria
- Screenshots or existing UI references
- Research notes or support cases
- Dependency or permission rules
