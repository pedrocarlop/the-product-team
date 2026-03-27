---
name: coordinate
description: Run the approved execution sequence, pass inputs between specialists, and keep status current.
activation_hints:
  - "Use after approval is explicit or when direct execution has been chosen."
  - "Use to sequence specialists, trigger reviews, and close the loop on deliverables."
  - "Do not let status or handoff context go stale during execution."
---

# Coordinate

## Purpose

Use this skill to keep execution orderly, staged, and traceable once work is approved.

## Rules

- Activate the right specialist at the right time
- Pass the minimum necessary inputs between roles
- Request reviews only when they are justified
- Update `status.md` as execution changes
- Route unresolved questions and decision changes into `/logs`

## Output Contract

Maintain:

- `logs/active/<project-slug>/status.md`
- `logs/active/<project-slug>/deliverables/`
- `logs/active/<project-slug>/reviews/`
- `logs/active/<project-slug>/decisions/`
