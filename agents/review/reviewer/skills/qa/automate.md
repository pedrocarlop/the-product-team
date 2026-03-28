---
name: automate
description: Turn QA coverage into reliable automated tests, fixtures, and CI checks that run with strong signal and low maintenance cost.
---

# Automate

## Purpose

Use this skill to convert QA intent into automated checks that are stable, readable, and useful in CI.

## When to Use

- When a test case should become automated
- When test data, fixtures, or mocks need to be created or refactored
- When a regression should be locked in with repeatable coverage
- When CI needs stronger detection for a known failure mode

## When Not to Use

- When the request is only to decide what should be covered
- When the output should be a manual test plan or exploratory charter
- When the main decision is whether the build passes the gate
- When the test is likely too volatile to automate well right now

## Required Inputs

- The behavior to verify and the expected result
- The preferred test layer and why it was chosen
- The environments, dependencies, and data the test needs
- Existing test patterns, helpers, or suite conventions
- Stability constraints such as flake risk, runtime budget, or selector rules

## Workflow

1. Identify the observable behavior the test must prove.
2. Choose the smallest automation layer that gives trustworthy signal.
3. Create isolated test data and mock only what the test does not need to prove.
4. Write the test with clear setup, action, and assertion boundaries.
5. Keep selectors, fixtures, and helpers resilient to UI or implementation changes.
6. Wire the test into the right suite and CI path.
7. Verify that the test adds signal without making the suite slower or flakier.

## Design Principles / Evaluation Criteria

- Automation should verify behavior, not implementation trivia
- Tests should be deterministic and isolated
- Suite runtime and flake risk matter as much as coverage count
- Good helpers reduce repetition without hiding intent
- Automated checks should fail for the right reason and only the right reason

## Output Contract

- Automated test code or a precise implementation plan for it
- Fixtures, factories, or helper updates when needed
- Suite placement and CI integration details
- Notes on flake risk, maintenance risk, or follow-up work

## Examples

### Example 1

Input:
- Request: "Automate the refund flow regression we found in staging."

Expected output:
- Tests: stable regression coverage for the bug and the key recovery path
- Fixtures: isolated test data and any required mocks
- CI: the suite and job where the regression should run

## Guardrails

- Do not automate unstable behavior without first reducing the flake risk
- Do not assert on implementation details when user-visible behavior is enough
- Do not let helper abstractions hide what the test is proving
- Do not add tests that only pass because of shared state

## Optional Tools / Resources

- Existing test suites and helper libraries
- Fixture factories and seed data
- CI configuration and failure history
- Browser automation or API test tooling
