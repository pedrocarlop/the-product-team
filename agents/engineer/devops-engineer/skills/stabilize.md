---
name: stabilize
description: Reduce operational risk during incidents or fragile changes by hardening failure modes, recovery paths, and support readiness.
activation_hints:
  - "Use when a system is unstable, noisy, or at risk of incident recurrence."
  - "Route here for remediation, hardening, runbooks, drift cleanup, and recovery readiness."
---

# Stabilize

## Purpose

Use this skill to make a fragile system safer to run by reducing blast radius, tightening recovery paths, and clearing the issues that keep operations shaky.

## When to Use

- During or after an incident when the system needs to be made safer
- When a deployment path, environment, or resource shows drift or repeated failure
- When a change needs additional guardrails before it can be considered stable

## When Not to Use

- When the core release plan has not been defined yet
- When the task is primarily observing healthy behavior
- When the work is only cosmetic cleanup with no operational impact

## Required Inputs

- The unstable service, environment, or failure mode
- The current symptoms, triggers, and known blast radius
- The rollback, disablement, or fallback options available
- Any runbooks, alerts, or ownership details that support recovery

## Workflow

1. Identify the most likely way the system will fail again.
2. Reduce risk first: add guardrails, tighten permissions, or narrow exposure.
3. Confirm the recovery path is documented, tested, and easy to execute.
4. Remove drift or conflicting state that could cause the next outage.
5. Update alerts, dashboards, and runbooks so operators can react faster.
6. Verify the system is stable enough for normal operation or release.

## Design Principles / Evaluation Criteria

- Contain failure before optimizing for elegance
- Recovery should be faster and more predictable than the incident
- Drift and ambiguity are operational liabilities
- Stability is proven by a reduced chance of recurrence

## Output Contract

- A stabilization summary with the changes made or recommended
- The failure mode that was reduced and how
- Any recovery, rollback, or disablement steps that now exist
- Remaining risks or follow-up work that still needs attention

## Examples

### Example 1

Input:
- Task: A deployment failed and the rollback path is unclear
- Concern: Operators need a safe way to restore service quickly

Expected output:
- Document and test the rollback path
- Add the missing alerts or runbook steps
- Tighten the deployment so the same failure is less likely again

## Guardrails

- Do not make changes that improve optics but not actual resilience
- Do not leave recovery steps undocumented or untested
- Do not widen production risk while trying to fix instability

## Optional Tools / Resources

- Incident notes and postmortems
- Runbooks and on-call procedures
- Deployment and infrastructure definitions
- Monitoring, alerting, and drift reports
