---
name: verify
description: Prove that a security fix actually blocks the issue and does not introduce a new regression.
activation_hints:
  - "Use when a security fix, mitigation, or configuration change needs proof after implementation."
  - "Use when the team needs to confirm a vulnerability is closed before release or sign-off."
  - "Do not use before the underlying issue and fix path are already defined."
---

# Verify

## Purpose

Use this skill to confirm that the remediation really closes the security gap and that the surrounding behavior still works as intended. Verification should answer whether the issue is gone, how it was tested, and what risk remains.

## When to Use

- After a security patch, config change, or mitigation lands
- When a finding needs proof before closure
- When a scan, test, or manual check must confirm that the fix holds in practice

## When Not to Use

- When the vulnerability has not yet been fixed
- When the task is still investigation or review
- When the ask is to design a new mitigation instead of checking an existing one

## Required Inputs

- The original finding or incident being verified
- The fix that was applied
- The expected secure behavior and acceptance criteria
- The environment, build, or deployment where verification happens
- Any baseline evidence from before the change, if available

## Workflow

1. Reproduce the original issue or confirm the exact path that was vulnerable.
2. Run the same check against the fixed build, config, or deployment.
3. Test the negative case that should now fail and the positive case that should still work.
4. Recheck nearby security properties such as auth, authorization, logging, or headers.
5. Confirm the fix survives the relevant environment and deployment settings.
6. Record whether the issue is closed, partially closed, or still open.

## Design Principles / Evaluation Criteria

- Verification must test the actual failure path, not just a related path
- Passing means the weakness is blocked in the real environment
- Regression checks matter even when the original bug is fixed
- Evidence should be repeatable by another engineer

## Output Contract

- Verification result: pass, partial, or fail
- The method used to test the fix
- What behavior changed and what still works
- Any remaining risk, follow-up check, or re-test condition

## Guardrails

- Do not declare success without exercising the vulnerable path
- Do not rely on a single observation when the behavior is environment-sensitive
- Do not ignore adjacent regressions while checking the fix
- Do not blur verification with implementation or redesign work
