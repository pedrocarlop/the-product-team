---
name: coordinate
description: Run the execution sequence, pass inputs between specialists, and keep context current.
activation_hints:
  - "Use after approval or when direct execution has been chosen."
  - "Use to sequence specialists, trigger reviews, and close the loop on deliverables."
---

# Coordinate

## Purpose

Keep execution orderly and staged once work is underway.

## Rules

- Activate the right specialist at the right time.
- Pass the minimum necessary inputs between roles, but not less than needed for quality.
- Request reviews only when justified.
- Route unresolved questions through the orchestrator.
- If a material change is needed mid-cycle, pause and replan rather than improvising.

## Output

Update `logs/active/<project-slug>/context.md` as state changes. Store deliverables in `deliverables/` and decisions in `decisions/` when they need to persist beyond the conversation.
