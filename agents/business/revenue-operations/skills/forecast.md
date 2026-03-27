---
name: forecast
description: Build revenue forecasts that connect pipeline, stage conversion, bookings, and timing into a defensible outlook.
---

# Forecast

## Purpose

Use this skill to build or refresh revenue forecasts that tie pipeline and historical conversion patterns to future bookings, with assumptions that leadership can inspect and challenge.

## When to Use

- When a quarter or month needs a forward-looking bookings or pipeline outlook
- When the forecast needs to be tied to conversion, deal size, and close timing
- When actuals have changed enough that the current forecast is no longer credible
- When leadership needs confidence ranges or risk flags, not just a point estimate

## When Not to Use

- When the task is only to model capacity or territory math
- When the main need is to define routing or ownership rules
- When the forecast source data is missing and the work is really data cleanup

## Required Inputs

- The forecast horizon and cadence
- Current actuals, open pipeline, and historical conversion benchmarks
- Deal-level assumptions for stage, size, and timing
- Source data freshness and any gaps or caveats
- The audience and decision the forecast will support

## Workflow

1. Reconcile the starting point to the latest actuals before projecting forward.
2. Build the forecast from deal-level drivers rather than blended guesses.
3. Separate committed, upside, and downside cases if the business needs scenario clarity.
4. Compare the forecast against historical conversion and cycle-time patterns.
5. Surface the biggest assumptions, risks, and leading indicators.
6. Present the forecast with enough context that a reviewer can reproduce the logic.

## Design Principles / Evaluation Criteria

- Tied to actuals and current pipeline
- Assumptions are visible and traceable
- Confidence ranges are clearer than false precision
- Forecast logic should be simple enough to audit
- Leading indicators should explain the risk, not just the outcome

## Output Contract

- A forecast table or model with period-by-period outputs
- Assumptions summary with source and date
- Confidence range or scenario framing
- Short note on the biggest drivers, risks, and deltas

## Examples

### Example 1

Input:
- Request: "Forecast Q3 bookings using the current pipeline."
- Context: The team wants a manager-ready view with risk flags

Expected output:
- Structure: Stage-weighted forecast with timing adjustments
- Assumptions: Conversion by segment and historical slip rates
- Output: Base case, upside, downside, and key risk notes

## Guardrails

- Do not publish a forecast without stating the assumptions behind it
- Do not bury timing changes inside an unexplained blended rate
- Do not forecast from stale actuals if a newer source exists
- Do not present a point estimate when the range of outcomes is material

## Optional Tools / Resources

- Google Sheets or Excel
- Salesforce or HubSpot pipeline reports
- SQL warehouse for historical conversion analysis
- Notion for assumption documentation

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Revenue Operations resources (hubspot.com)](https://www.hubspot.com/revenue-operations), [Salesforce Revenue Intelligence resources (salesforce.com)](https://www.salesforce.com/resources/), [Gartner Sales Operations insights (gartner.com)](https://www.gartner.com/en/sales), [McKinsey Growth, Marketing & Sales Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights), [Winning by Design Resources (winningbydesign.com)](https://winningbydesign.com/resources/)
