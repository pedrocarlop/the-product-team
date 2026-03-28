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

Use this skill to turn the available specialist input and the relevant staffed-role skills into one coherent, lossless implementation blueprint with explicit ownership, sequencing, and preserved quality detail.

## Review Checklist

- Same user goal across all plans
- No duplicate ownership
- No missing work
- Clear sequencing and dependencies
- Reasonable effort for the scope
- Relevant staffed-role `skill-catalog.md` files and matching role-local skills were read before the merge
- The merged plan reflects best practices pulled from those skills, not just what happened to appear in the role plans
- Review points and approval gate identified
- Every requested specialist plan's critical details are either carried into `03_unified-plan.md` or referenced as required direct reads
- All non-conflicting detail from specialist plans is preserved
- Overlapping details are merged once at the strongest level of specificity instead of being repeated or deleted
- Conflicts and ownership collisions are explicitly resolved rather than silently smoothed over
- Concrete behaviors, motion specs, thresholds, copy, test expectations, and edge-case handling are not replaced with generic summaries
- The orchestrator, not the specialists, defines the final process for this cycle
- Any material re-plan after approval requires a new full cycle instead of piecemeal edits

## Output Contract

Write `logs/active/<project-slug>/03_unified-plan.md` with:

- Request summary
- Selected roles
- Skill sources read and the best-practice implications they contributed
- Required direct reads per role
- Ownership by role
- Authoritative execution process for the cycle
- Work phases with phase-by-phase implementation detail
- Detailed merged implementation sections by role
- Critical detail register preserving must-carry specifics from role plans
- Overlap resolutions and conflict decisions
- Dependencies
- Deliverables
- Validation or acceptance checkpoints
- Review points
- Approval gate
- Execution sequence
