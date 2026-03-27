---
name: unblock
description: Remove delivery blockers by clarifying ownership, negotiating tradeoffs, and escalating only when the team cannot solve the issue locally.
activation_hints:
  - "Use when work is stuck because of dependencies, ambiguity, or conflicting priorities."
  - "Route here for blocker triage, dependency negotiation, and escalation decisions."
  - "Do not use for long-range planning, staffing, or performance calibration."
---

# Unblock

## Purpose

Use this skill to get engineering work moving again when progress is stalled by missing information, blocked dependencies, or unresolved tradeoffs.

## When to Use

- When a team cannot make progress without another person or function
- When ownership, priority, or approval is unclear
- When a decision is stuck between engineering and another stakeholder
- When a blocker needs a clear next action, owner, and deadline

## When Not to Use

- When the issue is just ordinary sequencing in a healthy plan
- When the team needs to rework staffing or ownership more broadly
- When the work is finished and only needs review
- When the main issue is individual performance rather than a workflow block

## Required Inputs

- What is blocked and what is still moving
- Who owns the next decision or dependency
- The business impact of waiting
- Any options already tried
- What escalation paths are available if local resolution fails

## Workflow

1. Name the specific block in one sentence.
2. Separate facts, assumptions, and opinions about why the work is stuck.
3. Identify the decision, dependency, or approval that would clear the block.
4. Assign an owner and deadline for the next action.
5. Negotiate the smallest acceptable tradeoff if the ideal path is not available.
6. Escalate with context, alternatives, and a recommended path if the blocker cannot be solved locally.
7. Confirm that the block is actually removed and not just renamed.

## Design Principles / Evaluation Criteria

- A blocker should be specific enough to action
- The fastest safe unblock is usually better than a perfect but delayed one
- Escalation should come with a recommendation, not just a complaint
- Ownership and deadlines reduce repeat blocking
- The team should leave with a next step, not just sympathy

## Output Contract

- Clear statement of the blocker and the path to resolution
- Named owner, deadline, and escalation point if needed
- Tradeoff summary when the ideal path is unavailable
- Follow-up check to verify the work is moving again

## Examples

### Example 1

Input:
- Situation: a feature is waiting on a product decision for two days
- Constraint: launch date is fixed

Expected output:
- Next step: request a decision by a specific time with the two viable options
- Tradeoff: explain the impact of each option on launch scope or quality
- Escalation: if there is no response, route to the agreed decision maker

## Guardrails

- Do not let blockers sit without an owner
- Do not escalate before clarifying the actual decision needed
- Do not accept vague promises in place of a deadline
- Do not confuse local frustration with a true organizational blocker

## Optional Tools / Resources

- Project trackers and dependency lists
- Decision logs and meeting notes
- Cross-functional chat or status updates
- Escalation paths and approval chains
