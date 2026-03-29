---
name: reconcile
description: Merge specialist input into one coherent execution plan.
activation_hints:
  - "Use when specialist notes need to be merged into one execution path."
  - "Use when ownership, sequencing, or tradeoffs are unclear after staffing."
---

# Reconcile

## Purpose

Turn specialist input into one coherent execution plan with clear ownership and sequencing.

## Review Checklist

- Same user goal across all inputs
- No duplicate ownership
- No missing work
- Clear sequencing and dependencies
- Conflicts explicitly resolved, not silently dropped
- Concrete details preserved, not replaced with generic summaries

## Output

Present the reconciled plan in the conversation. Update `logs/active/<project-slug>/context.md` with the approved direction. Execution plans live in the context window, not as separate log files.
