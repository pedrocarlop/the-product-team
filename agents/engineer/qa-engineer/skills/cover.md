---
name: cover
description: Design risk-based test coverage across layers, scenarios, and environments so the QA plan proves the feature behaves as intended.
---

# Cover

## Purpose

Use this skill to decide what quality coverage is needed, where it should live, and what gaps still remain.

## When to Use

- When a feature needs a coverage matrix by risk and user path
- When the team must balance unit, integration, E2E, and manual coverage
- When coverage gaps need to be identified before implementation begins
- When a release needs a focused checklist of what must be exercised

## When Not to Use

- When the only task is implementing a known test case
- When the release gate decision is already the main question
- When the request is about test automation plumbing rather than coverage design
- When the work is mainly bug triage or issue reporting

## Required Inputs

- The feature scope and acceptance criteria
- The major user journeys and failure modes
- The current test suite and known coverage gaps
- Browser, device, locale, or environment constraints
- Any release risks or historical regressions relevant to the change

## Workflow

1. List the user journeys, behaviors, and failure states that matter most.
2. Rank them by impact, likelihood, and ease of detection.
3. Choose the lightest test layer that still gives strong signal for each case.
4. Separate required coverage from nice-to-have coverage.
5. Identify gaps that cannot be covered now and make them explicit.
6. Check for redundant tests that add maintenance cost without new signal.
7. Package the coverage view so the team can see what is covered and what is still missing.

## Design Principles / Evaluation Criteria

- High-risk behavior deserves first-class coverage
- Coverage should be layered, not duplicated by default
- Every important path should have a clear detection point
- Tests should maximize signal per minute of execution
- Gaps should be visible instead of implied

## Output Contract

- Coverage matrix or checklist organized by risk and path
- Coverage recommendations by test layer
- Explicit gaps, assumptions, and tradeoffs
- Prioritized list of cases to cover first

## Examples

### Example 1

Input:
- Request: "Make sure the checkout change is covered well enough to ship."

Expected output:
- Coverage matrix: happy path, payment failure, retry, and edge states
- Layering: unit for business rules, integration for API behavior, E2E for the core checkout path
- Gaps: any browser, device, or data cases still untested

## Guardrails

- Do not duplicate coverage just because multiple layers feel safer
- Do not ignore edge states that are likely to fail in real use
- Do not call coverage complete when the highest-risk paths are still untested
- Do not trade away maintainability for marginally more coverage

## Optional Tools / Resources

- Coverage reports and flaky test logs
- Prior incidents, bugs, and support tickets
- Browser/device matrices and release checklists
- Existing test suite maps or QA matrices
