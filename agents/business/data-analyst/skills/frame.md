---
name: frame
description: Turn a vague business question into a precise analytical question, a decision it will inform, and a scoped plan for answering it.
activation_hints:
  - "Use when a stakeholder asks a broad or ambiguous question that needs sharpening before analysis starts."
  - "Route here before opening data, writing SQL, or defining metrics for a new analysis."
  - "Do not use for metric calculation, validation, or final reporting once the question is already clear."
---

# Frame

## Purpose

Use this skill to turn a messy business question into a specific analysis frame: what decision is being supported, what question is actually answerable, what scope is in or out, and what the output should look like.

## When to Use

- When the request is vague, multi-part, or outcome-focused without a clear analytical question
- When multiple interpretations of the same ask could lead to different answers
- When the audience, decision owner, or success criteria are not yet explicit

## When Not to Use

- When the question is already specific and the work is mainly computation or validation
- When the task is to define exact metric logic or check data quality
- When the work is final narrative or dashboard packaging

## Required Inputs

- The stakeholder ask in their own words
- The decision this analysis should inform
- The audience who will use the answer
- Known constraints on time window, segment, data source, or delivery format
- Any related metrics, prior analyses, or business context

## Workflow

1. Restate the ask as a decision-oriented question.
2. Identify the primary decision maker and the action the answer should change.
3. Split broad asks into a smaller set of answerable subquestions.
4. Define the minimum scope needed to answer the question credibly.
5. Write down the intended output form, such as a number, table, chart, or memo.
6. Call out assumptions, exclusions, and open questions before analysis starts.

## Design Principles / Evaluation Criteria

- Specific beats broad
- Decision-first framing over curiosity-driven exploration
- Smallest answerable scope that still serves the decision
- Clear boundaries around what the analysis will and will not claim
- Outputs should be easy for the stakeholder to act on

## Output Contract

- A rewritten analytical question
- The decision it supports and the intended user
- Scope, assumptions, and exclusions
- The expected output format
- Any remaining open questions that must be resolved before analysis

## Examples

### Example 1

Input:
- Stakeholder ask: "Why is retention down?"
- Context: Leadership wants to know whether the latest product change hurt activation cohorts

Expected output:
- Framed question: "Among users who activated in the last 90 days, did D30 retention change after the product update, and which acquisition segment explains the difference?"
- Decision: Whether to roll back, keep, or iterate on the change
- Scope: Activation cohorts only, with comparison to the prior 90-day cohort

## Guardrails

- Do not jump into SQL or dashboards before the question is specific
- Do not expand scope just because more data is available
- Do not silently choose a metric or segment when the decision context is ambiguous
- Do not pretend uncertainty is resolved; surface it explicitly

## Optional Tools / Resources

- Notion for documenting the question and scope
- Prior analysis notes or metric definitions
- Stakeholder briefs, PRDs, or experiment plans
- Existing dashboards or dbt docs for context

- Shared MCP servers: Notion MCP, GitHub MCP, Linear MCP
- Reference websites: [Mode SQL Tutorial (mode.com)](https://mode.com/sql-tutorial/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/), [Looker Documentation (cloud.google.com)](https://cloud.google.com/looker/docs), [Tableau Learning (tableau.com)](https://www.tableau.com/learn), [Kaggle Learn (kaggle.com)](https://www.kaggle.com/learn)
