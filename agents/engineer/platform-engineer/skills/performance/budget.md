---
name: budget
description: Define and encode performance budgets that prevent regressions from shipping.
---

# Budget

## Purpose

Use this skill to turn performance goals into explicit thresholds that engineering can test, enforce, and monitor.

## When to Use

- When a product area needs an agreed performance target
- When a team wants to prevent regressions with CI or monitoring
- When we need to translate user impact into measurable thresholds

## When Not to Use

- When the metric has not yet been measured well enough to set a target
- When the issue is already isolated and the task is implementation
- When the change is about diagnosis rather than policy

## Required Inputs

- The metric to budget, such as LCP, INP, CLS, TTFB, bundle size, or p99 latency
- The surface or endpoint the budget applies to
- The device, network, or traffic assumptions behind the target
- The enforcement mechanism available, such as Lighthouse CI, Datadog, or test gates

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Choose a budget that reflects the user experience under realistic conditions.
2. Tie the budget to a concrete metric with a clear threshold.
3. Document the measurement environment so the target is not ambiguous.
4. Decide where the budget is enforced: CI, alerting, release review, or all three.
5. Record how exceptions or tradeoffs should be handled.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Budgets should be strict enough to matter and realistic enough to enforce
- A budget without a gate is a suggestion
- Tie thresholds to user-facing impact, not internal convenience
- Keep the policy simple enough to explain in one sentence

## Output Contract

- The metric and threshold
- The conditions under which it applies
- The enforcement point
- Any exceptions or tradeoffs that require review

## Guardrails

- Do not set budgets from localhost-only runs
- Do not invent a target without a representative baseline
- Do not hide tradeoffs behind vague wording
