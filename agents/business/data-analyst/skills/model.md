---
name: model
description: Build analytic models that structure the data correctly, expose the drivers behind a result, and keep assumptions explicit.
activation_hints:
  - "Use when an analysis needs cohorting, segmentation, decomposition, or a reusable analytical structure."
  - "Route here when you need to transform raw data into a reliable table, view, or analysis model."
  - "Do not use for final presentation copy or for first-pass question framing."
---

# Model

## Purpose

Use this skill to build the analytical structure that makes a question answerable: cohort logic, decomposition, segmentation, and clear assumptions about how the data should behave.

## When to Use

- When the answer depends on how users, events, or periods are grouped
- When you need to decompose a metric into drivers or components
- When you are building reusable tables, views, or analysis layers
- When a result could change materially based on cohort or segment design

## When Not to Use

- When the problem is only metric calculation or validation
- When the analysis structure already exists and only a number needs to be produced
- When the task is purely narrative or dashboard communication

## Required Inputs

- The framed question and metric definition
- The raw tables or models available
- The grouping logic for cohorts, segments, or periods
- Any assumptions about user identity, event ordering, or attribution
- The comparison logic needed for decomposition or trend analysis

## Workflow

1. Identify the unit of analysis: user, account, event, session, or cohort.
2. Choose the minimal structure that can express the question clearly.
3. Build the analysis around explicit grouping and comparison rules.
4. Surface the key drivers, segment splits, or component parts.
5. Check that the model is stable, interpretable, and reusable.
6. Document assumptions that materially affect the answer.

## Design Principles / Evaluation Criteria

- Analytical structure should make the answer easier to trust
- Cohort and segment logic must be explicit, not implied
- Driver decomposition should explain the result without overfitting it
- Reusable models are better than one-off structures when the pattern repeats
- Assumptions must be visible enough for someone else to challenge them

## Output Contract

- The chosen analytical structure
- Cohort, segment, or decomposition logic
- A reusable model, table, or clear query pattern
- Assumptions and limitations
- The driver view that explains the result

## Examples

### Example 1

Input:
- Question: "What is driving the retention drop?"
- Context: Retention fell after a product release

Expected output:
- Structure: Retention by activation cohort, acquisition channel, and platform
- Decomposition: Separate new-user and returning-user retention
- Assumption: Activation date is the cohort anchor, not signup date

## Guardrails

- Do not hide important grouping logic inside opaque query layers
- Do not treat a correlation as causation without evidence
- Do not change cohort rules midway through the analysis without noting it
- Do not overcomplicate the model when a simpler decomposition answers the question

## Optional Tools / Resources

- SQL warehouse or dbt
- Notebook for exploratory driver analysis
- Dashboard or semantic layer for reusable structures
- Metric and cohort definitions from prior work

- Shared MCP servers: Notion MCP, GitHub MCP, Linear MCP
- Reference websites: [Mode SQL Tutorial (mode.com)](https://mode.com/sql-tutorial/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/), [Looker Documentation (cloud.google.com)](https://cloud.google.com/looker/docs), [Tableau Learning (tableau.com)](https://www.tableau.com/learn), [Kaggle Learn (kaggle.com)](https://www.kaggle.com/learn)
