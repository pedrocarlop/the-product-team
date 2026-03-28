---
name: review
description: Review code and designs for correctness, architecture fit, tests, risk, and mentoring value.
---

# Review

## Purpose

Use this skill to evaluate technical work with enough rigor to catch bugs, regressions, and design drift while still helping the author move forward confidently.

## When to Use

- When reviewing pull requests, design docs, or implementation plans
- When checking correctness, test coverage, performance, security, or maintainability
- When feedback should explain the why, not just flag the what
- When a decision needs a technical second look before merge or rollout

## When Not to Use

- When the main task is deciding architecture or technical direction
- When the work is mostly about ordering steps or coordinating dependencies
- When the request is to teach or coach without evaluating a specific artifact

## Required Inputs

- The code, design, or proposal being reviewed
- The intended behavior and acceptance criteria
- Relevant constraints, standards, and prior decisions
- The level of risk tolerance for the change
- Any tests, screenshots, logs, or traces that help validate the work

## Workflow

1. Read the change in context and identify the user-visible or system-visible impact.
2. Check correctness first, then regression risk, then maintainability and consistency.
3. Verify that the solution matches the architecture and does not introduce unnecessary coupling.
4. Inspect the tests and confirm they cover the new behavior and obvious failure modes.
5. Separate blocking issues from suggestions so the author knows what must change.
6. Phrase feedback so it teaches a principle the team can reuse.

## Design Principles / Evaluation Criteria

- Correctness before polish
- Tests for new logic and risky edges
- Architectural consistency over local cleverness
- High-signal comments that explain consequences
- Block on real risk, not preference

## Output Contract

- A list of findings ordered by severity
- Clear callouts for what is blocking versus optional
- Suggested fixes or alternative approaches where useful
- A brief overall assessment if the change is mostly sound

## Examples

### Example 1

Input:
- Change: Adds a new API path
- Observation: No tests cover invalid inputs or backward compatibility

Expected output:
- Finding: Missing tests for error handling and compatibility edge cases.
- Guidance: Add coverage for the new input validation and any callers that rely on the previous contract.

## Guardrails

- Do not collapse review into style preferences that can be handled by linting
- Do not hide the severity of a real issue behind soft language
- Do not over-index on implementation details when the underlying design is the problem
- Do not give vague praise without actionable feedback

## Optional Tools / Resources

- Test runs and failure logs
- Architecture or ADR documents
- Performance traces and security notes
- Code review standards or team checklists
