---
name: harden
description: Strengthen frontend work for resilience, accessibility, performance, and release safety before it reaches users.
activation_hints:
  - "Use when a frontend change needs reliability work, security review, performance guardrails, or release safety."
  - "Route here before release if the code path touches auth, secrets, public data, or browser performance risk."
---

# Harden

## Purpose

Use this skill to make frontend code safer to ship and safer to run in the browser. It focuses on resilience, security, accessibility, performance, and operational readiness.

## When to Use

- Before releasing frontend work that affects auth, sensitive data, or external calls
- When a feature needs retries, timeouts, fallbacks, or rollback planning
- When the code path could fail loudly, leak data, or cause a production regression

## When Not to Use

- When the implementation is still unsettled
- When the only remaining work is basic feature completion
- When the task is purely about measuring behavior that is already shipped

## Required Inputs

- The implementation or code path to harden
- The risk area: security, resilience, accessibility, performance, deployment, or incident response
- Any constraints around rollout, fallback, or rollback
- Team standards for logging, secrets, and public exposure

## Workflow

1. Review the code path for the highest-risk failure modes first.
2. Check auth handling, validation, secrets handling, error messages, and public data exposure.
3. Add resilience controls where needed: retries, timeouts, fallbacks, guards, or circuit breakers.
4. Confirm deployment safety with flags, migrations, or rollback steps when relevant.
5. Make sure the system can be operated: alerts, dashboards, runbooks, and incident notes.
6. Re-check that the hardening did not change user-visible behavior unintentionally.

## Design Principles / Evaluation Criteria

- Safer defaults beat clever fixes
- Public surfaces should be least-privilege and least-knowledge
- Production failures should be contained, not amplified
- Rollback should be possible without guesswork
- Browser performance and accessibility are part of shipping safely

## Output Contract

- A concise risk review with the fixes applied or recommended
- Any security, resilience, performance, or rollout changes that must accompany the code
- Residual risks that still need attention
- A clear statement of what is now safe enough to ship

## Examples

### Example 1

Input:
- Task: Prepare a frontend upload flow for production
- Risk: network failures could leave the UI stuck or duplicate actions

Expected output:
- Add retry handling and explicit error recovery
- Confirm loading and disabled states prevent duplicate submissions
- Document the rollback or disablement path

## Guardrails

- Do not treat hardening as a substitute for missing core functionality
- Do not add protections that break the user contract without documenting the tradeoff
- Do not ship public UI without checking for secrets, PII, and authorization gaps

## Optional Tools / Resources

- Security review notes and threat models
- Browser performance tooling and accessibility audits
- Deployment tooling and feature flags
- Incident runbooks and rollback procedures
