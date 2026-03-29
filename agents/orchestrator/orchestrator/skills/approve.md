---
name: approve
description: Present the plan to the user and capture approval before substantial execution.
activation_hints:
  - "Use after the plan is ready for orchestrated work."
  - "Use whenever scope or staffing changes materially."
---

# Approve

## Purpose

Get explicit user approval before substantial multi-role execution starts.

## Required Behavior

- Present the plan clearly in the conversation.
- End with "Do you want to proceed?"
- Capture edits, scope reductions, or added constraints.
- Do not start substantial multi-role execution without approval.
- If feedback materially changes scope, replan before executing.

## Output

Update `logs/active/<project-slug>/context.md` with approved direction and any scope clarifications.
