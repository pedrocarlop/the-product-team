---
name: frame
description: "Turn a vague product request into a precise problem statement, boundary, and explicit decision to be made. Use when a request is ambiguous, when success criteria are missing, or when the team disagrees on what problem is actually being solved."
---

# Frame

## Overview

"Framing" is the most critical upstream skill. A poorly framed request leads to wasted design and engineering cycles solving the wrong problem. A well-framed request turns a vague idea ("We need a dashboard") into a precise, scoped problem statement ("Operators need to identify and retry failed payments within 5 minutes without writing SQL").

## When to Use

- When a new feature request comes in with a proposed solution but no documented problem.
- When an initiative's scope feels "leaky" or unbounded.
- When leadership, design, and engineering disagree on what success looks like.
- When you need to decide if an initiative is actually worth staffing.

## When Not to Use

- When the problem is already explicitly defined, the boundaries are locked, and the task is pure execution.
- When the task is a known bug fix or technical debt item.
- When the expected output is a full PRD (use `specify` instead).

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Extract the Core Decision

Identify what action this work will ultimately drive:
- **Good**: "Should we invest in a native mobile app or optimize the responsive web experience?"
- **Bad**: "We need to research mobile usage." (Not a decision).

### Step 2: Define the Problem Statement

State the user or business pain in under two sentences.
- Use the format: *[Who] is struggling to [Do What] because [Why], which results in [Impact].*
- **Example**: "Customer Success Managers are struggling to identify churning accounts early because health scores update weekly, resulting in preventable revenue loss."

### Step 3: Set Scope Boundaries (In/Out)

Explicitly define what the team will *not* do:
- **In Scope**: The exact personas, use cases, or platforms being targeted.
- **Out of Scope**: Adjacent problems, future features, or edge cases that will be deliberately ignored for now. *If the "Out of Scope" list is empty, the frame is too weak.*

### Step 4: Define Success Criteria

State how the team will know if the problem is solved:
- **Quantitative**: "Activation rate increases from 20% to 25%."
- **Qualitative**: "Users can complete the onboarding flow without contacting support."

### Step 5: Identify the 'Next Step' Output

Define what artifact will close this framing exercise:
- A 1-pager for leadership approval.
- A "How Might We" brief for design exploration.
- A kill decision (stopping the work because the problem isn't worth solving).

## Decision Tree: Is the Frame Strong Enough?

```
Is the Problem Statement focused on a user/business pain (not a missing feature)?
├── YES → Does the "Out of Scope" list explicitly forbid at least one related idea?
│   ├── YES → Are the Success Criteria measurable?
│   │   ├── YES → The frame is strong. Proceed.
│   │   └── NO → Rewrite Success Criteria (Step 4).
│   └── NO → The scope is too leaky. Define what we won't do (Step 3).
└── NO → You are building a solution in search of a problem. Go back to Step 2.
```

## Worked Examples

### Example 1: "Add AI to the Editor" (Vague Request)

**Input:** Leadership asks, "Can we add an AI writing assistant to our text editor?"
**Workflow Application:**
- **Problem Statement**: Users are abandoning drafts because they struggle to format raw meeting notes into structured project updates.
- **In Scope**: Reformatting existing text, extracting action items.
- **Out of Scope**: Generating novel content from scratch, AI image generation, chatbot interfaces.
- **Success Criteria**: 30% increase in draft completion rate.
- **Output**: A 1-page scoping brief for the design team.

### Example 2: "Churn Dashboard" (Feature-first Request)

**Input:** Support team asks for a "churn dashboard."
**Workflow Application:**
- **Core Decision**: How should we route accounts that are at risk of non-renewal?
- **Problem Statement**: Account managers don't know which accounts to call today because renewal data lives in Stripe while usage data lives in Mixpanel.
- **Out of Scope**: Predicting churn with machine learning; building custom charting UI.
- **Success Criteria**: AMs can view a daily list of at-risk accounts in their existing CRM.

## Guardrails

- **Never accept a feature as a problem statement.** "We lack a dashboard" is not a problem. "Users cannot see their data" is the problem.
- **Always force a constraint.** If everything is in scope, nothing will ship.
- **Do not write a full PRD during framing.** Keep it under 1 page. If it takes 5 pages, you are designing the solution, not framing the problem.

## Troubleshooting

### Issue: The team ignores the framing and builds everything anyway
**Cause**: The "Out of Scope" section was too vague or missing.
**Solution**: Make the exclusions painful and explicit. Write "We will explicitly NOT build X, even if users ask for it."

### Issue: Leadership rejects the framing
**Cause**: The Core Decision (Step 1) didn't align with business strategy.
**Solution**: Re-interview the stakeholder. Ask: "If this project succeeds perfectly, what metric on your dashboard moves?"

### Issue: The problem statement is too broad
**Cause**: "Boiling the ocean" (e.g., "Users want the product to be easier").
**Solution**: Narrow the persona. Narrow the usecase. Change "Users" to "First-time administrators setting up SAML."
