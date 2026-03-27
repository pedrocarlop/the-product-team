---
name: reconcile
description: Merge specialist plans into one staged execution path and record it in `03_unified-plan.md`.
activation_hints:
  - "Use after accepted specialists have written their individual plans."
  - "Use when plans conflict, duplicate work, or leave gaps."
  - "Do not move to approval without a reconciled plan."
---

# Reconcile

## Purpose

Use this skill to turn separate specialist plans into one coherent execution path with explicit ownership and sequencing.

## Review Checklist

- Same user goal across all plans
- No duplicate ownership
- No missing work
- Clear sequencing and dependencies
- Reasonable effort for the scope
- Review points and approval gate identified

## Output Contract

Write `logs/active/<project-slug>/03_unified-plan.md` with:

- Request summary
- Selected roles
- Ownership by role
- Work phases
- Dependencies
- Deliverables
- Review points
- Approval gate
- Execution sequence
