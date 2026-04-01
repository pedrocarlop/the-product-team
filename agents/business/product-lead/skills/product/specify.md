---
name: specify
description: "Convert an agreed product direction into precise requirements, business rules, and acceptance criteria that can be built and tested. Use when handing off work to engineering, or when a high-level concept needs rigorous functional definition."
---

# Specify

## Overview

"Specify" translates a framed problem into a strict contract for execution. While framing defines *why* we are doing something and *what* the boundaries are, specification defines *exactly how it must behave* under all conditions. Ambiguous specs lead to engineer-assumption, which leads to bugs, rework, and missed requirements.

## When to Use

- When a problem is fully framed and approved for implementation.
- When handing off work to engineering and design.
- When an epic needs to be broken down into testable user stories or tickets.
- When business rules (e.g., compliance, permissions) need to be explicitly documented.

## When Not to Use

- When the problem statement is still debated (use `frame` instead).
- When the work is a pure technical refactor owned entirely by engineering.
- When the project is still in the early discovery or prototyping phase.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Deconstruct into Functional Capabilities

Break the high-level feature into independent capabilities:
- **Feature**: "Team Billing Hub"
- **Capabilities**: 1) View invoice history, 2) Change credit card, 3) Add billing emails.

### Step 2: Define the Business Rules

List the logic that must be true regardless of the UI:
- **Permissions**: "Only users with the `Admin` role can view invoices."
- **Constraints**: "A team must always have at least one active payment method."
- **Defaults**: "Invoices are emailed to the account owner by default."

### Step 3: Write the Requirements / User Stories

For each capability, write testable requirements:
- Use standard phrasing: *As a [Persona], I want to [Action] so that [Value].*
- **Example**: "As an Admin, I want to download past invoices as PDFs so I can expense them."

### Step 4: Write Strict Acceptance Criteria

Define exactly how QA and Engineering will prove the requirement is done.
- Use Given/When/Then (BDD) format for clarity.
- **Happy Path**: Expected successful outcome.
- **Edge Cases**: Empty states, error conditions, boundary limits.

### Step 5: Document Telemetry and Tracking

Specify what needs to be measured:
- "Fire event `billing_method_updated` when a new card is successfully saved."

## Decision Tree: Is the Spec Ready for Handoff?

```
Is every requirement paired with Acceptance Criteria?
├── YES → Are the Business Rules (Permissions, Constraints) explicitly listed?
│   ├── YES → Are edge cases (failures, empty states) documented?
│   │   ├── YES → The spec is ready for Engineering/Design review.
│   │   └── NO → Add error handling criteria (Step 4).
│   └── NO → Document the rules (Step 2). Engineering cannot guess permissions.
└── NO → Write Acceptance Criteria (Step 4) for the missing requirements.
```

## Worked Examples

### Example 1: Specify a Password Reset Flow

**Input:** "We need a way for users to reset their passwords."
**Workflow Application:**
- **Business Rules**: Reset links expire after 1 hour. Passwords must be 12+ chars.
- **Requirement**: As a logged-out user, I want to request a reset link via email.
- **Acceptance Criteria (Happy Path)**:
  - *Given* I am on the login page, *When* I click "Forgot Password" and submit a valid email, *Then* a success message appears and an email is dispatched.
- **Acceptance Criteria (Edge Case)**:
  - *Given* I submit an email not in the system, *Then* the system shows the exact same success message (to prevent email enumeration).

### Example 2: Specify a Pricing Tier Gate

**Input:** "Lock the advanced reporting feature to Pro users."
**Workflow Application:**
- **Business Rules**: 'Free' and 'Basic' users cannot access the `/reports` route.
- **Requirement**: As a Free user clicking a report link, I should see an upgrade prompt.
- **Acceptance Criteria**:
  - *Given* I am a Free user, *When* I navigate to `/reports`, *Then* I am redirected to `/upgrade` and see the "Pro Required" banner.
- **Telemetry**: Fire event `upgrade_wall_hit` with property `source=reports`.

## Guardrails

- **Never write specs that dictate the UI layout.** Specify the *data* and *behavior*, let Design solve the screen. (e.g., Use "User selects an option" not "User clicks the blue dropdown").
- **Always include negative/error criteria.** The happy path is only 20% of the work.
- **Never use words like "fast", "easy", or "intuitive" in Acceptance Criteria.** They cannot be tested. Use exact metrics (e.g., "Loads in < 2 seconds").

## Troubleshooting

### Issue: Engineers constantly ask for clarification during sprints
**Cause**: Missing edge cases or implicit business rules.
**Solution**: Require engineers to actively review and sign off on the Acceptance Criteria *before* the sprint starts. Add an "Unresolved Questions" section to the spec.

### Issue: QA rejects the ticket because "it doesn't work right"
**Cause**: The Acceptance Criteria were written after the code was built, or they were too vague.
**Solution**: Enforce Given/When/Then format. If a condition isn't in the AC, it's a new feature request, not a bug.

### Issue: Design feels restricted by the spec
**Cause**: The spec prescribes UI components (e.g., "Add a modal with a red button").
**Solution**: Strip UI terminology. Focus on intent: "Provide a high-friction confirmation step before deletion."
