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

Use this skill to keep execution orderly, staged, and traceable once direct work is underway or an orchestrated plan has been approved.

## Rules

- Activate the right specialist at the right time
- Pass the minimum necessary inputs between roles
- Request reviews only when they are justified
- Update `status.md` as execution changes
- Route unresolved questions and decision changes into `/logs`
- Treat `00_routing.md` plus `01_intake.md` as the authoritative plan for direct work, and `03_unified-plan.md` as the authoritative plan for orchestrated work
- If a material change is needed in an orchestrated cycle, pause and reroute through a new full planning cycle instead of improvising repeated rework

## Output Contract

Maintain:

- `logs/active/<project-slug>/status.md`
- `logs/active/<project-slug>/deliverables/`
- `logs/active/<project-slug>/reviews/`
- `logs/active/<project-slug>/decisions/`
