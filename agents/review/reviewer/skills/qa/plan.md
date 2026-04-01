---
name: plan
description: "Turn a QA request into a structured test strategy with scope, risk boundaries, coverage targets, and executable matrices. Use when an epic or feature needs a defensible verification approach before it hits production."
---

# Plan (QA Review)

## Overview

"Plan" creates a structured framework for verifying quality. Abstract testing ("poke around and see if it breaks") is insufficient. A rigorous QA Plan maps requirements to specific test methodologies (Unit, Integration, E2E, Manual), defines the boundaries of testing, and systematically targets high-risk code paths before release.

## When to Use

- When a new, complex feature or epic requires a comprehensive test strategy before engineering handoff.
- When organizing a pre-release regression cycle.
- When transitioning an ad-hoc QA request into a structured matrix.
- When determining which checks should be automated versus manual exploratory.

## When Not to Use

- When writing the actual line-by-line automated code (Cypress, Playwright).
- When merely executing an already-established test plan (use an execution skill).
- When the task is a simple typo/copy fix with near-zero regression risk.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: reviewer
project: <slug>
deliverable: reviewer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: Define the Scope and Risk Profile

Explicitly state the boundaries of the test plan based on the product requirements.
- **In Scope**: The exact feature, API routes, or UI components.
- **Out of Scope**: Unrelated systems not touched by the PR.
- **High-Risk Subsystems**: E.g., "Billing calculation logic", "Auth token generation."

### Step 3: Extract Acceptance Criteria into Test Scenarios

Convert each PRD requirement into a testable scenario.
- Break them down by Functional vs. Non-Functional (Performance, Accessibility, Security).
- Include Negative Paths: What happens when the database is unreachable?

### Step 4: Assign the Test Pyramid Layers

Determine *where* each scenario should be tested to ensure speed and stability.
- **Unit (Eng)**: Algorithm edge cases, mathematical validations.
- **Integration (Eng/QA)**: API endpoints, database transactions, service boundaries.
- **End-to-End (QA)**: Critical user flows via UI automation (e.g., checkout).
- **Exploratory (QA)**: Visual edge cases, accessibility quirks, unique device inputs.

### Step 5: Define Test Data and Environment Needs

List the exact prerequisites for execution:
- "Need an AWS staging environment with Stripe sandbox keys."
- "Need a mock database seeded with 10k 'Expired Trial' user accounts."

### Step 6: Create the Execution Matrix

Produce a structured grid or list that maps: 
`[Scenario ID]` | `[Description]` | `[Type (Happy/Edge)]` | `[Execution Method]`

### Step 7: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Decision Tree: Is the Test Plan complete?

```
Are all Product Acceptance Criteria mapped to at least one Test Scenario?
├── YES → Have you explicitly defined the Negative/Error paths?
│   ├── YES → Is every scenario assigned a layer (Unit, API, E2E, Manual)?
│   │   ├── YES → The QA Plan is ready for review.
│   │   └── NO → Assign layers (Step 3). Do not default to 100% manual UI testing.
│   └── NO → Add edge case scenarios (Step 2).
└── NO → Map the missing ACs. A plan without full coverage is incomplete.
```

## Worked Examples

### Example 1: Payment Gateway Integration

**Input:** "Engineer finished the new Stripe Checkout flow. Please QA."
**Workflow Application:**
- **Risk Profile**: High. Financial data loss possible.
- **Test Scenarios (Happy)**: User completes purchase with a valid card.
- **Test Scenarios (Negative)**: Card declined, expired card, network timeout during processing.
- **Test Layers**: 
  - Unit: Calculate tax totals.
  - Integration: Stripe webhook payload handling.
  - E2E: Full UI checkout flow with sandbox cards.
- **Matrix Output**: A 15-row test matrix defining inputs, expected states, and verification methods.

### Example 2: Marketing Page Update

**Input:** "Added a new 'Enterprise Solutions' landing page."
**Workflow Application:**
- **Risk Profile**: Low. Static content.
- **Test Scenarios**: Responsive layout checks, broken links, SEO tags, dark mode support.
- **Test Layers**: 100% Exploratory/Manual visual review and Lighthouse auditing.

## Guardrails

- **Never default to "100% E2E UI testing".** UI tests are slow and brittle. Push logic tests down to the API or Unit layer.
- **Always require explicit Test Data definitions.** "Log in as user" is bad. "Log in as user with `role=admin` and `status=banned`" is good.
- **Do not plan tests for unspecified requirements.** If the PRD doesn't mention something, clarify it rather than inventing a strict test for it.

## Troubleshooting

### Issue: The test plan takes 3 weeks to execute manually
**Cause**: Overuse of UI-driven exploratory testing, or testing every micro-permutation manually.
**Solution**: Shift testing left. Move 80% of data-driven permutations to the API/Integration layer.

### Issue: New bugs constantly reported in production that weren't in the plan
**Cause**: The QA plan only mapped the "Happy Path" supplied by the Product Lead.
**Solution**: Instantiate a mandatory "Destructive Testing" session in every plan (e.g., simulating 500 errors, null inputs, and concurrent clicks).

### Issue: Engineers ignore the test plan because "it's QA's job"
**Cause**: The plan was created in a silo after development finished.
**Solution**: Shift the plan upstream. The QA plan must be written and agreed upon during the `Specify` phase, before coding begins.
