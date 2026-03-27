---
name: approve
description: Present the unified plan to the user, capture feedback, and enforce the approval gate in `04_approval.md`.
activation_hints:
  - "Use after `03_unified-plan.md` is ready."
  - "Use whenever scope, sequencing, or staffing changes materially."
  - "Do not start substantial orchestrated execution until approval is explicit."
---

# Approve

## Purpose

Use this skill to make approval visible, editable, and durable so execution starts from an agreed plan.

## Required Behavior

- Present the unified plan clearly
- Capture edits, scope reductions, added constraints, or specialist changes
- Record the approval state explicitly
- Stop substantial orchestrated execution when approval is missing
- If approval feedback materially changes staffing, scope, or sequence, rerun the full planning cycle before execution starts

## Output Contract

Write `logs/active/<project-slug>/04_approval.md` with:

- Presented plan version
- User feedback
- Approval state
- Requested edits
- Approved scope
