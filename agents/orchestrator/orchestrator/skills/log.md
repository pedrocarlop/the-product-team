---
name: log
description: Maintain the compressed project memory in `/logs`, especially `context.md` and decision history.
activation_hints:
  - "Use throughout the lifecycle of a project."
  - "Use whenever status, scope, approvals, or deliverables change."
  - "Do not leave future roles without a usable handoff."
---

# Log

## Purpose

Use this skill to keep project memory concise, current, and sufficient for future continuation without the full conversation.

## Required Files

- `logs/active/<project-slug>/context.md`
- `logs/active/<project-slug>/status.md`
- `logs/active/<project-slug>/decisions/`

## Context Contract

`context.md` should summarize:

- Project goal
- Current state
- Approved direction
- Active roles
- Latest deliverables
- Open questions
- Next step
