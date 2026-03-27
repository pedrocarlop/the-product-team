---
name: monitor
description: Keep a production model or LLM workflow healthy by watching drift, performance, and business impact after launch.
activation_hints:
  - "Use after a model or inference workflow is in production."
  - "Route here when defining alerts, drift checks, review cadence, or incident response."
  - "Do not use before the system has shipped or before serving has been defined."
---

# Monitor

## Purpose

Use this skill to detect when a deployed ML system is drifting, degrading, or causing business harm so the team can respond before users feel the impact.

## When to Use

- When setting up post-launch alerts and dashboards
- When defining performance review cadence for a model in production
- When investigating drift, degraded metrics, or suspicious inference behavior

## When Not to Use

- When the model has not yet been deployed
- When the issue is primarily offline evaluation or service design
- When the task is a one-time analysis rather than ongoing oversight

## Required Inputs

- The production model or workflow identifier
- The baseline distribution or training reference
- The business metrics that matter post-launch
- Alert thresholds and the routing path for incidents
- The label lag or review cadence for ground truth
- Any known slices, cohorts, or failure patterns to watch

## Workflow

1. Decide which signals prove the system is healthy and which signals prove it is failing.
2. Compare live distributions against the training or launch baseline.
3. Track business metrics, not only infrastructure metrics.
4. Set alert thresholds and escalation paths for drift, latency, errors, or metric regressions.
5. Schedule periodic reviews with fresh labels or manual audits to catch silent degradation.
6. Use incidents and review findings to decide whether to tune, retrain, roll back, or pause the system.

## Design Principles / Evaluation Criteria

- Monitoring should cover model behavior, not just service uptime
- Drift is a trigger for investigation, not a conclusion by itself
- Business impact matters more than isolated technical signals
- Alerts should be actionable and routed to the right owner
- Review cadence must match label freshness and user risk

## Output Contract

- The monitoring plan and signal list
- Alert thresholds, owners, and escalation path
- The review cadence for fresh labels or audits
- The rollback or retraining trigger conditions
- Any known blind spots or monitoring gaps

## Examples

### Example 1

Input:
- A recommendation model is live and engagement is slipping

Expected output:
- Monitoring plan: track prediction distribution drift, input drift, CTR correlation, and a monthly review with fresh labels
- Escalation: alert when drift exceeds the agreed threshold and route to the on-call owner

## Guardrails

- Do not monitor only CPU, memory, and request rate
- Do not wait for a severe incident before defining alert thresholds
- Do not rely only on distribution metrics when business outcomes are available
- Do not let a model stay live without a review cadence

## Optional Tools / Resources

- Datadog or equivalent observability platform
- Ground-truth label pipelines and review queues
- Model registry and rollback docs
- Incident postmortems and dashboard history
