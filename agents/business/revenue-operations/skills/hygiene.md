---
name: hygiene
description: Audit, normalize, and maintain CRM and revenue data so routing, reporting, and forecasting stay reliable.
---

# Hygiene

## Purpose

Use this skill to keep revenue data trustworthy by defining required fields, identifying gaps, removing duplicates, and maintaining the standards that downstream reporting depends on.

## When to Use

- When CRM records are incomplete, inconsistent, or duplicated
- When reporting or forecasting is breaking because source data is unreliable
- When the team needs a repeatable audit for lead, contact, account, or opportunity quality
- When field standards, validation rules, or enrichment logic need to be tightened

## When Not to Use

- When the task is primarily to define routing or handoff ownership
- When the main work is to build a revenue forecast or model
- When the data is already trusted and the issue is interpretation rather than quality

## Required Inputs

- The object or dataset to audit
- The required fields, standards, and acceptable values
- The systems of record and any secondary sources used for cross-checks
- The quality thresholds that matter to the business
- The remediation path for missing or invalid records

## Workflow

1. Identify the records and fields that must be trustworthy for downstream work.
2. Compare actual data against the required standards and flag exceptions.
3. Separate missing data, invalid values, duplicates, and stale records.
4. Prioritize fixes by business impact, not just by volume.
5. Document the source of truth, the audit result, and the remediation owner.
6. Confirm the hygiene rules can be repeated on a schedule.

## Design Principles / Evaluation Criteria

- Downstream trust matters more than cosmetic cleanliness
- Required fields should match actual operating needs
- Exceptions should be deliberate and documented
- Audits should be repeatable and measurable
- Remediation should be owned, not just observed

## Output Contract

- A data quality audit with issues grouped by type and severity
- Required-field or validation recommendations
- Deduping or enrichment notes, if relevant
- A repeatable hygiene check or cadence

## Examples

### Example 1

Input:
- Request: "Clean up our open opportunities before the board review."
- Context: Forecasting depends on stage, amount, and close date accuracy

Expected output:
- Audit: Missing close dates, stale stage values, and duplicate accounts
- Remediation: A prioritized cleanup list with owners
- Output: A hygiene report and repeatable validation checklist

## Guardrails

- Do not treat cosmetic cleanup as the same thing as trustworthy data
- Do not change data standards without checking downstream reporting impact
- Do not ignore duplicates or stale records because they are hard to fix
- Do not bundle hygiene work into a forecast or routing task

## Optional Tools / Resources

- Salesforce or HubSpot reports
- SQL queries for audits and dedupe checks
- Enrichment tools
- Notion for data standards and remediation tracking

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Revenue Operations resources (hubspot.com)](https://www.hubspot.com/revenue-operations), [Salesforce Revenue Intelligence resources (salesforce.com)](https://www.salesforce.com/resources/), [Gartner Sales Operations insights (gartner.com)](https://www.gartner.com/en/sales), [McKinsey Growth, Marketing & Sales Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights), [Winning by Design Resources (winningbydesign.com)](https://winningbydesign.com/resources/)
