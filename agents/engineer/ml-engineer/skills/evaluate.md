---
name: evaluate
description: Design and interpret model, prompt, and retrieval evaluations so we know whether the system is actually good enough to ship.
activation_hints:
  - "Use after framing a problem and before shipping a model, prompt, or retrieval pipeline."
  - "Route here when comparing candidates, defining metrics, or validating a proposed solution."
  - "Do not use for serving or monitoring once the production path is already chosen."
---

# Evaluate

## Purpose

Use this skill to build a credible evaluation plan and turn measured results into a clear ship, iterate, or stop decision.

## When to Use

- When comparing candidate models, prompts, retrieval settings, or heuristics
- When you need to define test sets, slices, thresholds, or acceptance criteria
- When the team needs to understand failure modes, fairness gaps, or regression risk

## When Not to Use

- When the main task is deployment plumbing or runtime operations
- When the metric and evaluation set are already established and the work is only execution
- When you are already in live monitoring mode

## Required Inputs

- The framed problem and target decision
- Candidate approaches to compare
- Data splits, labels, or ground truth source
- The primary metric and any guardrail metrics
- Known slices, edge cases, or fairness dimensions
- Acceptance thresholds, latency budgets, and cost constraints

## Workflow

1. Choose an evaluation design that matches the problem type and risk level.
2. Separate training, validation, and test data before tuning anything.
3. Define the baseline and compare every candidate against it.
4. Measure the primary metric, guardrails, and slice performance on held-out data.
5. Inspect worst cases, calibration, and error patterns instead of relying on averages only.
6. Convert the results into a recommendation with clear tradeoffs and residual risk.

## Design Principles / Evaluation Criteria

- Held-out truth is required for ship decisions
- The metric must reflect the business goal, not just model convenience
- Baselines should be simple and defensible
- Slice-level regressions matter even when the aggregate improves
- Reproducibility matters as much as raw score

## Output Contract

- The evaluation plan or test design
- Metric results for the baseline and each candidate
- Slice analysis, calibration notes, and worst-case examples
- A recommendation with thresholds and tradeoffs called out explicitly
- Any follow-up experiments required before shipping

## Examples

### Example 1

Input:
- Candidate: new classifier for ticket routing
- Context: class imbalance and a high cost for false positives

Expected output:
- Evaluation plan: stratified split, F1, precision/recall, confusion matrix, and per-intent slice review
- Decision rule: ship only if precision exceeds the agreed threshold and no critical intent regresses

## Guardrails

- Do not tune on the test set
- Do not report only aggregate accuracy for an imbalanced problem
- Do not ignore slices because the overall average looks good
- Do not claim a model is ready if the worst cases are unacceptable

## Optional Tools / Resources

- MLflow or W&B experiment history
- Evaluation notebooks or scripts
- Notion model cards or review docs
- Labeled examples, adversarial cases, and slice definitions
