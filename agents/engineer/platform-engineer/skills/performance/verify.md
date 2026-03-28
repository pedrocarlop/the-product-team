---
name: verify
description: Prove a performance change improved the target metric and did not regress other constraints.
---

# Verify

## Purpose

Use this skill to confirm that the change improved the target metric, held the budget, and did not create a new regression.

## When to Use

- After a performance fix has been applied
- When we need before/after numbers for a ticket, review, or release note
- When a CI or monitoring gate must be checked before merge or release

## When Not to Use

- When we are still deciding what the problem is
- When no baseline or threshold exists yet
- When the task is pure investigation without a proposed fix

## Required Inputs

- The original baseline and the post-change measurement
- The target budget or acceptance threshold
- The measurement method and environment for both runs
- Any related metrics that could regress as a side effect

## Workflow

1. Re-run the same measurement in conditions as close as possible to the baseline.
2. Compare the primary metric before and after.
3. Check the supporting metrics that could reveal a new regression.
4. Confirm that the budget, CI gate, or alert condition is satisfied.
5. Summarize the result in terms of user impact, not just a raw delta.

## Design Principles / Evaluation Criteria

- Verification must match the original measurement method
- Improvement is only real if the target budget is actually met
- Secondary regressions matter, even when the headline metric improves
- Field validation is stronger than lab validation when both are available

## Output Contract

- Before and after values for the primary metric
- Whether the budget passed
- Any secondary regressions or follow-up risks
- A short statement of user impact

## Guardrails

- Do not rely on a single lucky run
- Do not claim success without checking the agreed threshold
- Do not ignore regressions in nearby metrics or routes
