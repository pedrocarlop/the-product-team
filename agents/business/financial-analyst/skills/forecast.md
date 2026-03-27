---
name: forecast
description: Build assumption-driven financial forecasts, translate drivers into forward-looking revenue and cash outlooks, and make the assumptions explicit enough to defend.
---

# Forecast

## Purpose

Use this skill to build or refresh forward-looking financial forecasts that connect business drivers to revenue, cost, and cash outcomes.

## When to Use

- When leadership needs a base case, plan case, or growth outlook
- When revenue, expense, cash, or runway assumptions need to be converted into a time-based forecast
- When the business has changed and the current forecast no longer reflects reality

## When Not to Use

- When the task is primarily about model architecture or formula design
- When the main need is scenario stress testing or downside validation
- When the task is only to explain results from an existing forecast

## Required Inputs

- Forecast horizon and cadence
- Decision owner and the decision the forecast supports
- Historical actuals, current plan, and known assumption changes
- Driver definitions for revenue, cost, headcount, and cash
- Source data, date pulled, and any known gaps or limitations

## Workflow

1. Identify the forecast horizon, output cadence, and the decision it supports.
2. Reconcile the starting point to the latest actuals before projecting anything.
3. Convert business drivers into monthly or quarterly assumptions.
4. Build the forecast so that revenue, cost, and cash roll forward cleanly from those drivers.
5. Separate hardcoded assumptions from formulas and document each assumption source.
6. Check that the forecast ties to the prior period, the current plan, and any known operating constraints.

## Design Principles / Evaluation Criteria

- Driver-based, not guess-based
- Reconciled to actuals
- Assumptions are visible and traceable
- Time horizons and cadence are consistent
- Outputs are easy to compare against plan and prior forecasts

## Output Contract

- Forecast model or table with clear period-by-period outputs
- Assumptions summary with source and date
- Short note on the biggest forecast drivers and any material deltas from prior outlooks

## Guardrails

- Do not hide assumption changes inside a blended growth rate
- Do not forecast from stale actuals
- Do not present point estimates without stating the operating assumptions that create them


## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Investopedia Finance and Accounting (investopedia.com)](https://www.investopedia.com/), [Corporate Finance Institute Resources (corporatefinanceinstitute.com)](https://corporatefinanceinstitute.com/resources/), [SEC Filings and Forms (sec.gov)](https://www.sec.gov/edgar/search-and-access), [IFRS Accounting Standards (ifrs.org)](https://www.ifrs.org/issued-standards/list-of-standards/), [McKinsey Corporate Finance (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights)
