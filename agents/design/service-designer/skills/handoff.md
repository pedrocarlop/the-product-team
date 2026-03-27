---
name: handoff
description: Design, clarify, and document transitions between channels, teams, systems, and ownership boundaries so context moves cleanly through the service.
---

# Handoff

## Purpose

Use this skill to make transition points explicit so the next person, team, or system receives the context it needs without forcing the user to repeat themselves.

## When to Use

- When a user moves from self-service to assisted service
- When work changes ownership between teams or systems
- When escalation, approval, or callback behavior must be specified
- When a service failure is caused by missing context at the boundary

## When Not to Use

- When the experience has no meaningful ownership change
- When the task is only to document a single touchpoint
- When the problem is purely visual or copy-level and does not involve transition logic

## Required Inputs

- The source and destination of each handoff
- What context, data, or state must be transferred
- Who owns the step before and after the handoff
- What happens if the handoff fails or stalls
- Any service-level timing, SLA, or escalation expectations

## Workflow

1. Identify every point where ownership, channel, or system changes.
2. Specify what the receiving side must know to continue the experience.
3. Document what the user sees during the transition and how they know progress is happening.
4. Define fallback behavior if the next step does not complete on time.
5. Call out manual interventions and exceptional paths separately from the default path.
6. Check that no handoff requires the user to reconstruct information the service already has.

## Design Principles / Evaluation Criteria

- Context transfer over re-entry
- Ownership clarity over shared ambiguity
- Predictable recovery over silent failure
- User confidence during waiting states
- Escalation that is explicit and timed

## Output Contract

- A handoff specification listing source, destination, transferred context, ownership, and fallback behavior
- Notes on latency, escalation, and communication during the transition
- Any unresolved dependencies that need operational confirmation

## Guardrails

- Do not assume a handoff works just because the UI displays a confirmation
- Do not hide manual work behind vague automation language
- Do not leave the receiving owner undefined
