---
name: recover
description: Restore database service after failures by diagnosing impact, choosing a safe recovery path, and validating the system is healthy again.
---

# Recover

## Purpose

Use this skill to bring the database back to a known-good state safely after a failure, incident, or bad deployment.

## When to Use

- When a migration failed and left the database partially changed
- When data must be restored, rolled back, or repaired
- When failover, replication, or backup validation is part of the task
- When the priority is service restoration rather than new feature work

## When Not to Use

- When the task is just to design the schema or index strategy
- When the system is healthy and the work is planned rather than reactive
- When the main concern is rollout sequencing for a future migration

## Required Inputs

- What failed and when it started
- The current blast radius and affected data or services
- Available backups, replicas, snapshots, or rollback points
- The recovery objective, including whether partial restoration is acceptable
- Any constraints on downtime, data loss, or manual intervention

## Workflow

1. Stabilize the situation and stop further damage if needed.
2. Determine the latest safe point to recover to.
3. Choose the least risky path among restore, rollback, failover, or repair.
4. Validate the recovered state before declaring success.
5. Confirm whether dependent systems need re-sync, replay, or cleanup.
6. Capture what happened so the same failure is easier to recover from next time.

## Design Principles / Evaluation Criteria

- Recovery should favor safety and verification over speed alone
- The chosen path should match the failure mode, not just the most familiar tool
- Recovery is incomplete until data integrity and service health are checked
- A good recovery plan reduces uncertainty for downstream consumers
- Post-incident learning is part of the work, not an optional extra

## Output Contract

- Recommended recovery path and sequence
- Immediate containment or stabilization actions
- Validation steps to confirm the system is healthy
- Follow-up items for documentation or prevention

## Examples

### Example 1

Input:
- A migration failed halfway through and the application cannot write safely

Expected output:
- A recovery plan that stops unsafe traffic, restores a consistent state, and verifies the database before reopening writes

## Guardrails

- Do not guess at recovery steps without checking the failure mode
- Do not declare success before validating consistency and access
- Do not trade away data integrity for a faster-looking fix

