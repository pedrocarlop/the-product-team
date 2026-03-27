---
name: plan
description: Turn a QA request into a test strategy and execution plan with scope, risks, coverage targets, and acceptance criteria.
activation_hints:
  - "Use when a feature, fix, or release needs a quality plan before testing starts."
  - "Route here for test strategy, risk assessment, exploratory charters, and coverage planning."
  - "Do not use when the strategy is already set and the work is only about implementing tests."
---

# Plan

## Purpose

Use this skill to turn a QA request into a clear test plan that the team can execute, review, and trust.

## When to Use

- When a feature needs a quality strategy before implementation or release
- When risk, scope, and test layers need to be decided
- When acceptance criteria must be translated into concrete test cases
- When a release needs an explicit QA approach and sign-off path

## When Not to Use

- When the task is already a concrete test implementation
- When the main need is automated execution or CI wiring
- When the work is only about pass/fail gate evaluation
- When the request is broader product planning rather than QA planning

## Required Inputs

- The feature, bug, or release being tested
- The acceptance criteria or expected user behavior
- The known risks, edge cases, and dependencies
- The target environments, devices, or browsers
- Any existing test coverage or prior bugs that matter

## Workflow

1. Restate what must be proven true from a quality perspective.
2. Break the request into risk areas, user paths, and test layers.
3. Decide which checks belong in unit, integration, E2E, exploratory, or manual review.
4. Identify the minimum test data and environment setup needed.
5. Map each acceptance criterion to one or more test cases.
6. Note open questions, assumptions, and gaps before testing begins.
7. Write the plan so another QA engineer or developer can follow it without extra context.

## Design Principles / Evaluation Criteria

- Risk should drive coverage, not habit
- The plan should trace directly back to acceptance criteria
- Test layers should be chosen for signal and maintainability
- Missing assumptions should be visible early
- The plan should be executable by someone other than the author

## Output Contract

- Test strategy with scope, risk areas, and coverage targets
- Test cases mapped to acceptance criteria
- Assumptions, dependencies, and open questions
- Recommended test layers and sequencing

## Examples

### Example 1

Input:
- Request: "QA the new billing update flow before release."

Expected output:
- Plan: high-risk paths, environment needs, and priority test cases
- Coverage: what belongs in automation versus exploratory checks
- Gaps: any missing requirements that need clarification first

## Guardrails

- Do not start testing without a shared understanding of success
- Do not spread coverage evenly when the risk is uneven
- Do not skip edge cases just because the happy path is well understood
- Do not turn a test plan into a change log or implementation checklist

## Optional Tools / Resources

- MCP: Chrome DevTools MCP, GitHub MCP, Notion MCP, Linear MCP
- Websites: [Playwright Docs](https://playwright.dev/docs/intro), [Cypress Docs](https://docs.cypress.io/), [Selenium Documentation](https://www.selenium.dev/documentation/), [Testing Library Docs](https://testing-library.com/docs/), [BrowserStack Guide](https://www.browserstack.com/guide)
- Product requirements and acceptance criteria
- Prior bug reports and incident notes
- Existing test suites and coverage reports
- Release checklists and environment inventories
