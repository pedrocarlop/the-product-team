---
name: reconcile
description: Turn specialist advice or sequencing constraints into one authoritative staged execution path and record it in `03_unified-plan.md`.
activation_hints:
  - "Use when specialist notes or plans need to be merged into one execution path."
  - "Use when ownership, sequencing, or tradeoffs are still unclear after staffing."
  - "Do not move to approval without a reconciled plan when orchestration needs one."
---

# Reconcile

## Purpose

Use this skill to turn the available specialist input into one coherent execution path with explicit ownership and sequencing.

## Review Checklist

- Same user goal across all plans
- No duplicate ownership
- No missing work
- Clear sequencing and dependencies
- Reasonable effort for the scope
- Review points and approval gate identified
- The orchestrator, not the specialists, defines the final process for this cycle
- Any material re-plan after approval requires a new full cycle instead of piecemeal edits

## Output Contract

Write `logs/active/<project-slug>/03_unified-plan.md` with:

- Request summary
- Selected roles
- Ownership by role
- Authoritative execution process for the cycle
- Work phases
- Dependencies
- Deliverables
- Review points
- Approval gate
- Execution sequence
