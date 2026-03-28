---
name: approve
description: Present the orchestrated plan to the user, capture feedback, and enforce the approval gate in `04_approval.md`.
activation_hints:
  - "Use after `03_unified-plan.md` is ready."
  - "Use whenever scope, sequencing, or staffing changes materially."
  - "Do not start substantial multi-role execution until approval is explicit."
---

# Approve

## Purpose

Use this skill to make approval visible, editable, and durable so substantial orchestrated execution starts from an agreed plan.

## Required Behavior

- Present the unified plan clearly
- When approval is still pending, end the user-facing handoff with: "This is the plan", references to `03_unified-plan.md`, `04_approval.md`, `status.md`, and `context.md`, and the exact closing question "Do you want to proceed?"
- Capture edits, scope reductions, added constraints, or specialist changes
- Record the approval state explicitly
- Stop substantial multi-role execution when approval is missing
- If approval feedback materially changes staffing, scope, or sequence, rerun the full planning cycle before execution starts

## Output Contract

Write `logs/active/<project-slug>/04_approval.md` with:

- Presented plan version
- User feedback
- Approval state
- Referenced log files for the pending handoff
- Pending approval question when approval is not yet explicit
- Requested edits
- Approved scope
