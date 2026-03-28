---
name: remediate
description: Turn security findings into targeted fixes, tests, and follow-up work without widening scope unnecessarily.
---

# Remediate

## Purpose

Use this skill to convert a security finding into a safe, minimal, and verifiable fix. Remediation should close the vulnerability, preserve product behavior, and make it hard for the same class of issue to return.

## When to Use

- When a security review has identified a real defect
- When a scanner, alert, or incident has produced a confirmed vulnerability
- When a mitigation needs implementation, not just documentation

## When Not to Use

- When the issue has not yet been validated
- When the task is to do the security review itself
- When the change would require a broader design decision that has not been agreed

## Required Inputs

- The confirmed finding or incident summary
- The affected files, config, or service boundaries
- The desired security outcome and any deadlines or severity targets
- The constraints on compatibility, rollout, or backwards behavior
- Any required test coverage or verification method

## Workflow

1. Restate the issue in operational terms so the fix targets the real failure mode.
2. Identify the smallest safe change that removes or contains the risk.
3. Patch the implementation or configuration with the least possible scope change.
4. Add or update tests that prove the weakness is closed.
5. Update related docs, alerts, or guardrails if they help prevent recurrence.
6. Check for adjacent regressions, especially in auth, validation, logging, and access control paths.
7. Record any residual risk or follow-up work that remains after the fix.

## Design Principles / Evaluation Criteria

- Minimal changes are safer than broad refactors during remediation
- Fixes should be testable and repeatable
- The root cause matters more than the visible symptom
- Remediation should not introduce a new security or availability risk

## Output Contract

- The concrete fix applied or proposed
- Tests, checks, or automation added with the fix
- Any follow-up work, rollout caveats, or residual risk
- A short note explaining why the chosen fix is sufficient

## Guardrails

- Do not widen scope unless it is required to close the issue safely
- Do not mark a finding fixed without proof in tests or verification
- Do not trade one security issue for another convenience regression
- Do not leave rollback or ownership unclear for a high-severity fix
