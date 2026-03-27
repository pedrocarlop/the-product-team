---
name: migrate
description: Plan and author database migrations so schema changes deploy safely, backfill cleanly, and remain reversible where possible.
activation_hints:
  - "Use when a task involves adding, changing, or removing schema in a live system."
  - "Route here for rollout order, backfills, compatibility windows, or zero-downtime migration planning."
  - "Do not use for pure schema design, index tuning, or incident remediation."
---

# Migrate

## Purpose

Use this skill to change database structure safely across environments and deployments without breaking existing application behavior.

## When to Use

- When adding or changing tables, columns, constraints, or indexes in production
- When planning dual-write, backfill, or cutover steps
- When a change needs to stay compatible across multiple releases
- When a migration might lock tables or affect high-volume workloads

## When Not to Use

- When the task is only to design the target schema
- When the task is only to improve a query plan with indexing
- When the database is already broken and recovery is the primary goal

## Required Inputs

- The source schema and desired end state
- Expected table size and traffic level
- Reversibility requirements and acceptable downtime
- Rollout constraints across services, jobs, and consumers
- Any data backfill or validation that must occur before cutover

## Workflow

1. Define the target state and the minimum safe path from the current state.
2. Break risky changes into additive, backfill, validation, and cleanup phases.
3. Preserve compatibility with older application versions during the transition.
4. Identify steps that might lock data or rewrite large portions of a table.
5. Plan verification for both the schema change and the live data movement.
6. Document rollback or recovery options before the first deployment step.

## Design Principles / Evaluation Criteria

- Additive changes are safer than destructive ones
- Compatibility windows reduce deployment risk
- Backfills should be observable, throttled, and resumable
- Reversible migrations are preferred, but irreversible changes must be explicitly called out
- A migration is not complete until the rollout path is clear

## Output Contract

- Ordered migration steps
- Compatibility and rollback notes
- Backfill or validation plan if data movement is involved
- Risks, lock concerns, and operational dependencies

## Examples

### Example 1

Input:
- Add `status` to a large orders table and populate existing rows

Expected output:
- An additive migration plan with backfill and validation steps
- A note to avoid a single-step destructive change

## Guardrails

- Do not assume a one-step migration is safe on production-scale data
- Do not drop or rename structures before consumers have switched
- Do not ignore lock duration, retry behavior, or rollback paths

