---
name: model
description: Build revenue operating models that connect pipeline, bookings, conversion, and capacity into a structure leadership can trust.
activation_hints:
  - "Use when a task requires a revenue model, pipeline model, quota model, or capacity model."
  - "Route here when the user needs the drivers behind revenue performance made explicit."
  - "Do not use for routing decisions, CRM cleanup, or publishing a forecast from an existing model."
---

# Model

## Purpose

Use this skill to build the analytical structure for revenue operations work: pipeline coverage, stage conversion, quota capacity, territory math, and other driver-based models that explain how revenue is produced.

## When to Use

- When pipeline, bookings, or capacity needs to be decomposed into drivers
- When you need a reusable model that can be refreshed as the business changes
- When leadership needs to understand how changes in conversion, deal size, or headcount affect revenue
- When a one-off spreadsheet is not enough and the structure needs to be explicit

## When Not to Use

- When the task is only to clean CRM records or enforce field hygiene
- When the main need is to choose where a lead or account should go
- When the model already exists and the work is only to publish or explain the result

## Required Inputs

- The decision the model must support
- The revenue question being answered and the period or horizon in scope
- Source data, current assumptions, and known gaps
- Definitions for pipeline stages, bookings, quotas, or capacity units
- Any constraints on tool choice, cadence, or output format

## Workflow

1. Translate the business question into a modelable revenue problem.
2. Choose the smallest model structure that still exposes the real drivers.
3. Define the units, periods, and conversion steps the model must preserve.
4. Separate hardcoded assumptions from formulas and note every assumption source.
5. Check whether the model ties to actuals, forecast logic, and capacity constraints.
6. Document what changed, what is still uncertain, and what a reviewer should challenge.

## Design Principles / Evaluation Criteria

- Driver-based instead of guess-based
- Assumptions should be explicit enough to audit
- The structure should be reusable, not one-off
- Revenue math should reconcile across periods and stages
- The model should make risk and leverage points visible

## Output Contract

- The model structure and the question it answers
- Driver definitions and assumption notes
- A reusable spreadsheet, table, or calculation pattern
- Any limitations, gaps, or edge cases that matter

## Examples

### Example 1

Input:
- Question: "How much pipeline do we need per rep to hit the quarter?"
- Context: The team wants a territory-level capacity view

Expected output:
- Structure: Quota divided by close rate, deal size, and stage coverage
- Assumptions: Historical conversion rate by segment and current ramp assumptions
- Output: A reusable capacity model with rep and territory inputs

## Guardrails

- Do not bury assumptions inside opaque spreadsheet logic
- Do not mix routing or hygiene work into the model
- Do not present a revenue model as final if the driver definitions are still unstable
- Do not overcomplicate the structure when a simpler driver tree answers the question

## Optional Tools / Resources

- Google Sheets or Excel
- CRM reports from Salesforce or HubSpot
- SQL warehouse or dbt models
- Notion for documenting assumptions and definitions

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Revenue Operations resources (hubspot.com)](https://www.hubspot.com/revenue-operations), [Salesforce Revenue Intelligence resources (salesforce.com)](https://www.salesforce.com/resources/), [Gartner Sales Operations insights (gartner.com)](https://www.gartner.com/en/sales), [McKinsey Growth, Marketing & Sales Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights), [Winning by Design Resources (winningbydesign.com)](https://winningbydesign.com/resources/)
