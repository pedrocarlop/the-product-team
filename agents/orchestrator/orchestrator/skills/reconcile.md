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

Use this skill to turn the available specialist input into one coherent, lossless execution path with explicit ownership, sequencing, and preserved quality detail.

## Review Checklist

- Same user goal across all plans
- No duplicate ownership
- No missing work
- Clear sequencing and dependencies
- Reasonable effort for the scope
- Review points and approval gate identified
- Every requested specialist plan's critical details are either carried into `03_unified-plan.md` or referenced as required direct reads
- Concrete behaviors, motion specs, thresholds, copy, test expectations, and edge-case handling are not replaced with generic summaries
- The orchestrator, not the specialists, defines the final process for this cycle
- Any material re-plan after approval requires a new full cycle instead of piecemeal edits

## Output Contract

Write `logs/active/<project-slug>/03_unified-plan.md` with:

- Request summary
- Selected roles
- Required direct reads per role
- Ownership by role
- Authoritative execution process for the cycle
- Work phases with phase-by-phase implementation detail
- Critical detail register preserving must-carry specifics from role plans
- Dependencies
- Deliverables
- Validation or acceptance checkpoints
- Review points
- Approval gate
- Execution sequence
