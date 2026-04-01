---
name: measure
description: "Define, compute, and validate metrics so the numbers are correct, reproducible, and fit for decision-making. Use when building a new metric, verifying KPI accuracy, or designing analytical logic for a dashboard or report."
---

# Measure

## Overview

"Measure" turns raw questions into a trustworthy metric model. A good measurement is not just a SQL query; it's a precisely defined Numerator, Denominator, Window, and Filter. Without a measurement standard, the same question asked of different datasets often produces conflicting answers, leading to "Data Drift" and loss of decision confidence.

## When to Use

- When a new business goal or KPI needs a baseline or tracking (e.g., "Retention", "LTV").
- When an existing number is "suspicious" or conflicts with another source.
- When designing the analytical logic for a chart, funnel, or cohort analysis.
- When mapping data from a raw source (Log) to a semantic model (Metric).

## When Not to Use

- When the question is still about strategy or framing (use `frame` instead).
- When the data logic is already settled and the task is purely about visual presentation (use `format` or `present`).
- When the data source itself is uninstrumented or missing (request logging/telemetry first).

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: analyst
project: <slug>
deliverable: analyst.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: State the Metric definition in prose

Write the definition before writing any code:
- **Numerator**: The count, sum, or average of occurrences (e.g., "Active Users").
- **Denominator**: The population of interest (e.g., "Total Signups in the last 30 days").
- **Time Window**: The period of measurement (e.g., "Trailing 7 Days", "Last Full Quarter").
- **Filing Rules**: When does the metric "close"? (e.g., "At the end of the month").

### Step 3: Establish the Semantic Layer

Identify the authoritative table, model, or view to use:
- **Primary Source**: The verified table or dbt model (e.g., `fct_orders`, `dim_users`).
- **Grain**: What does one row represent? (e.g., "One user per day").
- **Filters**: Which rows should be excluded? (e.g., `is_internal_user = false`, `test_transactions = false`).

### Step 4: Write the Metric Logic (SQL or Code)

Develop the calculation using clean, readable patterns:
- Use **CTEs** (Common Table Expressions) for clarity over subqueries.
- Explicitly handle **NULLs** in divisions: `SAFE_DIVIDE(numerator, denominator)`.
- Use **Date Truncation** for stable windowing: `DATE_TRUNC(created_at, MONTH)`.

### Step 5: Validate Data Quality and Inflation

Perform mandatory validation checks:
- **Uniqueness**: Are there duplicates after joins? `count(*) vs count(distinct id)`.
- **Null Rates**: Is the primary key or grouping field missing data?
- **Plausibility**: Is the number in the expected ballpark? (e.g., "Retention can't be 150%").

### Step 6: Document Caveats and Context

List anything that affects the metric's "truth":
- **Instrumentation gaps**: "Mobile app versions < 2.0 don't track this event."
- **Definitions shifts**: "The definition of 'Activated' changed on March 1st."
- **Data Freshness**: "This metric has a 24-hour processing lag."

### Step 7: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Decision Tree: Is the metric "production-ready"?

```
Is the logic reproducible by another analyst from the definition alone?
├── YES → Have you validated row inflation after joins?
│   ├── YES → OK (Ready).
│   └── NO → Run a uniqueness check first.
└── NO → Refine the Prose Definition in Step 1.
```

## Worked Examples

### Example 1: 30-Day Active User (DAU)

**Prose Definition:** "The unique count of non-internal users who performed at least one 'Successful Login' or 'Content View' event in the last 30 natural days."
**Metric Logic:**
```sql
WITH user_activity AS (
  SELECT user_id, DATE(event_timestamp) as activity_date
  FROM events_table
  WHERE event_name IN ('login_success', 'view_content')
    AND user_type != 'internal'
)
SELECT COUNT(DISTINCT user_id) as dau_30d
FROM user_activity
WHERE activity_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);
```
**Validation:** Check for `NULL` user_ids and confirm the `events_table` includes all platforms (iOS/Android/Web).

### Example 2: Conversion Rate (First Session)

**Prose Definition:** "Total unique visitors who completed 'Sign Up' within their first session / Total unique visitors."
**Metric Logic:**
```sql
SELECT
  SAFE_DIVIDE(COUNT(DISTINCT signup_visitor_id), COUNT(DISTINCT visitor_id)) as conv_rate
FROM sessions_summary;
```
**Caveat:** Exclude bot traffic identified via the `is_bot` flag.

## Guardrails

- **Never interpret a raw query as "The Truth" without validation.** Inflation or nulls can distort conclusions.
- **Always handle Division by Zero.** Use `NULLIF` or `SAFE_DIVIDE`.
- **Do not define metrics ad-hoc.** Use the project's semantic layer (e.g., dbt metrics, Looker, or central `definitions.sql`).
- **Metric names must be self-documenting.** Avoid generic names like `rate_1`. Use `signup_conversion_rate_v2`.

## Troubleshooting

### Issue: Metric value is unexpectedly high
**Cause**: Row inflation during joins (e.g., Joining `users` to `orders` without grouping).
**Solution**: Use `COUNT(DISTINCT user_id)` or aggregate the table in a CTE before joining.

### Issue: Metric differs across different reports
**Cause**: "Definition Drift." One report uses `created_at`, another uses `paid_at`.
**Solution**: Document the Source-of-Truth field in Step 2. Force all reports to use the same logic.

### Issue: Large volume of NULL values in a grouping
**Cause**: Left join on a missing dimension.
**Solution**: Check for missing records in the dimension table or use `COALESCE(field, 'Unknown')` for reporting.
