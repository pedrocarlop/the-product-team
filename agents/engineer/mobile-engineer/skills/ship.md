---
name: ship
description: Validate, harden, and release a mobile feature safely with tests, rollout controls, store submission checks, and observability.
activation_hints:
  - "Use when a mobile feature is implemented and needs release readiness, QA, and operational safety."
  - "Route here for rollout planning, test coverage, monitoring, and cleanup before production."
  - "Do not use for early modeling, wireframing, or implementation mapping."
---

# Ship

## Purpose

Use this skill to turn an implemented mobile feature into a safe production release with verification, monitoring, and rollback readiness.

## When to Use

- When code is complete and the remaining work is validation or rollout
- When a feature flag, migration, submission, or deployment sequence needs coordination
- When test coverage, observability, or rollback planning must be tightened before release

## When Not to Use

- When the feature contract is still changing
- When the work is only about modeling, composing, or translating the design
- When rollout safety is not relevant because the feature is not ready to release

## Required Inputs

- The implemented UI, native, and data changes
- Test results, screenshots, or validation evidence
- Feature flag, build, submission, and migration constraints
- Observability and rollback requirements

## Workflow

1. Verify the implemented behavior against the intended model and mobile spec.
2. Confirm tests cover the happy path, key failure modes, and any auth or lifecycle boundaries.
3. Check that rollout dependencies such as flags, submissions, migrations, and app-store timing are safe.
4. Confirm logs, metrics, and alerts are in place for the new path.
5. Identify cleanup work such as dead code, stale flags, or temporary fallbacks.
6. State the release criteria and rollback trigger clearly.

## Design Principles / Evaluation Criteria

- A feature is not shipped until it is safe to operate
- Rollout safety should be explicit, not implied
- Monitoring should make the new path visible when it fails
- Cleanup should be planned as part of shipping, not deferred indefinitely

## Output Contract

- A release-readiness summary with known risks and mitigations
- Test and validation status for the feature
- Rollout, flag, submission, migration, and rollback notes
- Cleanup items that should happen before or after launch

## Guardrails

- Do not treat "works on my machine" as release readiness
- Do not ship without a rollback story for risky changes
- Do not leave temporary flags or workarounds untracked

## Optional Tools / Resources

- CI and test output
- Deployment and feature-flag plans
- Observability dashboards and logs
- Release notes or incident follow-up items
