---
name: observe
description: Verify runtime behavior using logs, metrics, traces, alerts, and production-like checks after a change ships.
activation_hints:
  - "Use when a change needs proof in the real execution path."
  - "Route here for dashboards, alerts, logging, tracing, and operational validation."
---

# Observe

## Purpose

Use this skill to confirm a deployed change is visible, measurable, and behaving as intended in the environments that matter.

## When to Use

- After a deployment or infrastructure change needs validation
- When adding dashboards, alerts, logs, or traces
- When diagnosing latency, failure, saturation, or query issues

## When Not to Use

- When no change has been deployed yet and the next step is planning
- When the main problem is rollout safety rather than runtime behavior
- When the task is primarily incident containment or stabilization

## Required Inputs

- The service, environment, or workflow to inspect
- The expected healthy and unhealthy signals
- The available observability tools and data sources
- Any thresholds or SLOs that define success

## Workflow

1. Define what evidence would prove the system is healthy enough to trust.
2. Inspect logs, metrics, traces, alerts, or query behavior for the changed path.
3. Confirm the signals are structured, actionable, and free of sensitive data.
4. Compare actual measurements to the expected baseline or target.
5. Check whether alerts and dashboards expose the failure mode quickly enough.
6. Record the result and any gaps that need follow-up.

## Design Principles / Evaluation Criteria

- Production visibility is part of the change, not an afterthought
- Signals should be easy to interpret during an incident
- Missing telemetry is a delivery risk
- Measurement should beat guesswork

## Output Contract

- A short verification summary with the evidence gathered
- Any logs, metrics, traces, or query findings that matter
- Gaps in visibility or correctness that still need follow-up
- A clear pass/fail statement for the observed behavior

## Examples

### Example 1

Input:
- Task: Validate a newly deployed service
- Concern: It may have hidden errors and no request tracing

Expected output:
- Check logs and traces for representative requests
- Confirm dashboards or alerts reflect the healthy path
- Report any blind spots that still prevent confident operation

## Guardrails

- Do not treat tests alone as enough when the runtime path changed
- Do not claim the system is observable if the critical path has no useful signal
- Do not expose secrets or PII while collecting evidence

## Optional Tools / Resources

- Log, metric, and trace dashboards
- Test data or production-like fixtures
- Query inspection tools
- Incident history or prior debugging notes
