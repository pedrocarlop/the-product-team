---
name: review
description: Inspect implemented code, configuration, and architecture for security weaknesses before merge or release.
---

# Review

## Purpose

Use this skill to find security issues in a concrete change and turn them into actionable findings. The goal is to decide whether the change is safe enough to ship, what must be fixed first, and what risk remains if it is not.

## When to Use

- When reviewing a pull request, patch, migration, or infrastructure change
- When checking a dependency bump, auth flow, secrets change, or permission change
- When a feature is ready for security sign-off and needs a hard look before merge

## When Not to Use

- When no implementation exists yet
- When the job is to design the threat model from scratch
- When the task is to apply the fix after the review has already identified the issue

## Required Inputs

- The changed files, diff, or deployed configuration
- The intended behavior of the change
- Any existing threat model, security assumptions, or acceptance criteria
- The deployment context, including environment and privilege level
- Relevant test results or scan output, if available

## Workflow

1. Read the change in context and identify what trust boundary or privilege path it touches.
2. Check authentication, authorization, input validation, secrets handling, and data exposure first.
3. Inspect dependency, crypto, logging, header, and configuration changes for silent regressions.
4. Ask whether the change is reachable, exploitable, and material in the current environment.
5. Separate definite vulnerabilities from concerns, and rank the definite issues by severity.
6. Write findings in terms of impact, exploit path, and exact remediation needed.
7. Confirm whether the change can ship as-is or whether it needs blocking fixes.

## Design Principles / Evaluation Criteria

- Reviews should focus on exploitability and user impact, not cosmetic policy violations
- Findings should point to concrete code or config, not vague architectural unease
- A secure implementation must still be secure after deployment defaults and environment differences
- The best review outcome is a specific fix, not a generalized warning

## Output Contract

- Ordered findings with severity, rationale, and the affected file or config path
- Clear note on whether each issue blocks merge, needs follow-up, or is informational
- Any assumptions that affect the severity call
- A short overall recommendation on ship readiness

## Guardrails

- Do not call something a vulnerability without a plausible attack path
- Do not ignore environment-specific exposure just because the code looks correct in isolation
- Do not bury the highest-severity issue below lower-value notes
- Do not replace concrete findings with generic best practices
