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
- Current cycle and authoritative plan version
- Current state
- Approved direction
- Active roles
- Latest deliverables
- Open questions
- Next step

## Timeline Maintenance

`logs/TIMELINE.md` is the chronological project index. The orchestrator is the sole writer.

### When to write

- **New project**: Append a row immediately after creating `00_routing.md`. Set Status to `planning`. Set Outcome to `—`.
- **Status change**: Update the Status column when `status.md` transitions.
- **Completion or archival**: Fill in the Outcome column with a one-sentence summary of what was delivered, any notable scope changes, or why the project was abandoned.
- **Archival move**: Update the Slug link from `active/<slug>/` to `archive/<slug>/`.

### Row format

```
| YYYY-MM-DD | [slug](active/slug/ or archive/slug/) | objective | direct or orchestrated | role1, role2 | status | outcome |
```
