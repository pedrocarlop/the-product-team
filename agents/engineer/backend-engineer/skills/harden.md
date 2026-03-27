---
name: harden
description: Strengthen backend work for security, reliability, rollout safety, and incident readiness before it reaches users.
---

# Harden

## Purpose

Use this skill to make backend code safer to ship and safer to run. It focuses on security, reliability, performance guardrails, and operational readiness.

## When to Use

- Before releasing a backend change that affects auth, data access, or external calls
- When a feature needs rate limits, retries, timeouts, or rollback planning
- When the code path could fail loudly or create an incident if left unguarded

## When Not to Use

- When the core model is still unsettled
- When the only remaining work is basic implementation
- When the task is purely about observing or measuring already-shipped behavior

## Required Inputs

- The implementation or code path to harden
- The risk area: security, reliability, performance, deployment, or incident response
- Any known constraints around rollout, fallback, or rollback
- The team standards for secrets, logging, and public exposure

## Workflow

1. Review the code path for the highest-risk failure modes first.
2. Check auth, validation, secrets handling, error messages, and public data exposure.
3. Add resilience controls where needed: retries, timeouts, idempotency, backoff, or circuit breakers.
4. Confirm deployment safety with feature flags, migrations, or rollback steps when relevant.
5. Make sure the system can be operated: alerts, dashboards, runbooks, and incident notes.
6. Re-check that the hardening did not change user-visible behavior unintentionally.

## Design Principles / Evaluation Criteria

- Safer defaults beat clever fixes
- Public surfaces should be least-privilege and least-knowledge
- Production failures should be contained, not amplified
- Rollback should be possible without guesswork

## Output Contract

- A concise risk review with the fixes applied or recommended
- Any security, reliability, or rollout changes that must accompany the code
- Residual risks that still need attention
- A clear statement of what is now safe enough to ship

## Examples

### Example 1

Input:
- Task: Prepare a job worker for production
- Risk: retries could double-process side effects

Expected output:
- Add idempotency protection and explicit retry behavior
- Confirm logs and alerts exist for failures
- Document the rollback or disablement path

## Guardrails

- Do not treat hardening as a substitute for missing core functionality
- Do not add security controls that break the contract without documenting the tradeoff
- Do not ship public endpoints without checking for secrets, PII, and authorization gaps

## Optional Tools / Resources

- Security review notes and threat models
- Deployment tooling and feature flags
- Observability dashboards and alert configuration
- Incident runbooks and rollback procedures
