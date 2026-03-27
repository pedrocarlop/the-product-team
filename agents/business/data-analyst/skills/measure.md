---
name: measure
description: Define, compute, and validate metrics so the numbers are correct, reproducible, and fit for decision-making.
activation_hints:
  - "Use when a task requires metric definition, SQL validation, funnel analysis, cohort logic, or data quality checks."
  - "Route here after the question is framed and before results are reported."
  - "Do not use for final storytelling or for broad scoping without a clear measurement target."
---

# Measure

## Purpose

Use this skill to turn the framed question into a trustworthy measurement plan: exact metric definitions, correct SQL or model logic, and validation that the numbers are real.

## When to Use

- When you need to define numerators, denominators, time windows, or cohort rules
- When you are writing SQL to compute a metric or compare periods
- When data quality, duplication, or null handling could change the result
- When a dashboard, funnel, or experiment result depends on precise metric logic

## When Not to Use

- When the question still needs to be framed
- When the work is mainly explanation or presentation of an already-validated result
- When no measurable outcome or dataset has been identified yet

## Required Inputs

- The framed analytical question
- The metric or metrics under review
- The authoritative data source or model
- Time window, cohort, and segment definitions
- Known data quality risks or instrumentation caveats

## Workflow

1. Write the metric definition before querying data.
2. Specify the numerator, denominator, window, and null handling.
3. Choose the simplest valid SQL or model path to answer the question.
4. Validate row counts, joins, duplicates, and null rates.
5. Compare results against a simpler check or expected benchmark.
6. Record any data quality limitations that affect interpretation.

## Design Principles / Evaluation Criteria

- Definitions must be reproducible by another analyst
- Validation is part of the analysis, not a separate afterthought
- Use the simplest query that can still answer the question correctly
- Favor readable CTEs and explicit logic over clever shortcuts
- Never publish a number that has not been checked for plausibility

## Output Contract

- Exact metric definitions
- The SQL, model logic, or calculation method used
- Validation checks and results
- Any caveats, anomalies, or data quality issues
- A short note on whether the metric is ready for use

## Examples

### Example 1

Input:
- Question: "Did activation improve after launch?"
- Context: Product launch on March 1

Expected output:
- Metric definition: "Activation rate = activated users / eligible signups within 7 days of signup"
- Validation: Compare signup counts, activation event counts, and duplicate user joins across the pre/post window
- Caveat: Exclude users with missing signup timestamps

## Guardrails

- Do not define a metric ad hoc in a one-off query if a source-of-truth model exists
- Do not ignore duplicate joins, nulls, or unexpected row inflation
- Do not compare cohorts that are not comparable by construction
- Do not treat a returned result as correct without validation

## Optional Tools / Resources

- SQL warehouse or semantic layer
- dbt models or metric definitions
- Spreadsheet for validation logs
- Data quality or instrumentation notes

- Shared MCP servers: Notion MCP, GitHub MCP, Linear MCP
- Reference websites: [Mode SQL Tutorial (mode.com)](https://mode.com/sql-tutorial/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/), [Looker Documentation (cloud.google.com)](https://cloud.google.com/looker/docs), [Tableau Learning (tableau.com)](https://www.tableau.com/learn), [Kaggle Learn (kaggle.com)](https://www.kaggle.com/learn)
