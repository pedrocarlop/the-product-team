---
name: orchestrate
description: Design and operate data workflow coordination, dependency management, retries, backfills, and alerting for reliable pipeline execution.
activation_hints:
  - "Use when a task involves Airflow, Prefect, DAG structure, scheduling, retries, sensors, or backfill behavior."
  - "Route here for task dependencies, failure recovery, SLAs, or pipeline operational design."
  - "Do not use for source loading or transformation logic unless orchestration choices are the main issue."
---

# Orchestrate

## Purpose

Use this skill to coordinate how data work runs over time so that tasks execute in the right order, recover cleanly after failures, and remain safe to rerun.

## When to Use

- When building or changing DAGs, flows, schedules, or task graphs
- When defining retries, timeouts, sensors, or alerting behavior
- When planning backfills, reprocessing, or manual recovery steps
- When a pipeline needs idempotency or stronger operational boundaries

## When Not to Use

- When the primary issue is a broken extractor or source schema change
- When the work is mainly warehouse modeling or dbt transformation logic
- When you are setting privacy, retention, or access controls

## Required Inputs

- Task list and dependency graph
- Freshness or latency target
- Failure scenarios and retry expectations
- Backfill range and replay rules
- Runtime and resource constraints
- Operational alerting and escalation path

## Workflow

1. Map the smallest set of tasks that can fail and recover independently.
2. Keep orchestration logic separate from transformation logic.
3. Make every task idempotent so reruns do not create duplicate side effects.
4. Choose schedules, sensors, and retries that match source availability and downstream SLAs.
5. Define backfill and recovery steps before launch, not after the first incident.
6. Attach meaningful alerts to the failure modes that actually matter.
7. Write the runbook so an on-call engineer can restore the pipeline without tribal knowledge.

## Design Principles / Evaluation Criteria

- Orchestration is plumbing, not business logic
- Reruns should be safe by design
- Dependencies should be explicit, not implied
- Recovery paths must be documented and tested
- Alerting should point to action, not just awareness

## Output Contract

- DAG or flow structure
- Retry, timeout, sensor, and alerting plan
- Backfill and recovery procedure
- Runbook or operational notes
- Idempotency assumptions and constraints

## Examples

### Example 1

Input:
- Problem: Nightly pipeline fails when upstream data arrives late
- Need: Avoid brittle timing and preserve freshness

Expected output:
- Recommendation: Replace fixed timing assumptions with an upstream sensor, keep tasks idempotent, and document a replay path for the missed interval
- Rationale: Reduces false failures and makes recovery predictable

## Guardrails

- Do not use `datetime.now()` to drive pipeline state
- Do not put business logic into branching or scheduling code
- Do not rely on manual intervention as the normal execution path
- Do not ship orchestration without documented rerun behavior

## Optional Tools / Resources

- DAG or flow definitions
- Pipeline logs and historical runtimes
- SLA definitions and incident history
- Backfill test results

