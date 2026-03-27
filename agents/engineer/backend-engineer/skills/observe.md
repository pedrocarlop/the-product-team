---
name: observe
description: Verify backend behavior in practice using tests, logs, metrics, traces, and query inspection.
activation_hints:
  - "Use when the code exists and you need to prove it works in real conditions."
  - "Route here for instrumentation, debugging, test verification, and performance checks."
---

# Observe

## Purpose

Use this skill to confirm that backend changes behave correctly in production-like conditions and are visible enough to operate safely.

## When to Use

- After implementing a backend change that needs validation
- When adding logging, metrics, traces, dashboards, or alerts
- When diagnosing an unexpected bug, latency spike, or failure path

## When Not to Use

- When no code exists yet and the right next step is modeling
- When the task is primarily security hardening or rollout preparation
- When the problem is already solved and only documentation needs updating

## Required Inputs

- The code path, endpoint, worker, or query to verify
- The expected success and failure signals
- The observability tools available in the repo or environment
- Any performance or correctness thresholds that matter

## Workflow

1. Identify what proof would make the change trustworthy: tests, logs, metrics, traces, or query plans.
2. Exercise the code path with representative input and capture the observable signals.
3. Check that logs are structured, errors are actionable, and sensitive data is absent.
4. Validate performance-sensitive paths with realistic data volume or query inspection.
5. Compare actual behavior to expected behavior and note any gaps.
6. Turn the findings into follow-up fixes if the evidence does not match the model.

## Design Principles / Evaluation Criteria

- Production visibility is part of the feature
- Proof should come from the real execution path, not just static reasoning
- Missing telemetry is a delivery risk, not a nice-to-have
- Performance claims should be backed by measurement

## Output Contract

- A short verification summary with the evidence gathered
- Any logs, metrics, traces, or query findings that matter
- Gaps in observability or correctness that still need follow-up
- A clear pass/fail statement for the behavior under review

## Examples

### Example 1

Input:
- Task: Verify a new list endpoint
- Concern: It may hide an N+1 query and lacks request tracing

Expected output:
- Confirm the endpoint with representative data and inspect query behavior
- Check that trace IDs and structured logs appear in the request path
- Report any missing metrics or expensive query patterns

## Guardrails

- Do not treat passing unit tests as enough for production confidence when queries or integrations changed
- Do not claim observability is complete if the critical path has no trace or metric
- Do not expose secrets or PII while collecting evidence

## Optional Tools / Resources

- Test runner and fixture data
- Logging, metrics, and tracing dashboards
- Database query explain tools
- Incident notes or prior debugging history

