---
name: measure
description: Define marketing metrics, tracking, and attribution so campaign performance can be trusted and acted on.
---

# Measure

## Purpose

Use this skill to turn marketing activity into a trustworthy measurement system: clear definitions, correct tracking, and reporting that supports decisions instead of noise.

## When to Use

- When defining campaign KPIs or channel success metrics
- When UTMs, conversion events, or attribution logic need to be set up or checked
- When reported performance feels inconsistent or hard to trust
- When leadership needs a credible view of pipeline or demand contribution

## When Not to Use

- When the issue is still unclear audience, message, or channel strategy
- When the work is mainly creative execution
- When the result is a one-off number without a decision attached

## Required Inputs

- The campaign or channel being measured
- The business outcome the team cares about
- The tracking stack, source of truth, and reporting surface
- The time window, cohort, or comparison period
- Known instrumentation gaps, data quality risks, or attribution rules

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Define the decision the metric should support.
2. Write the metric definition before looking at results.
3. Confirm the source of truth and the event or field that will be used.
4. Check that tracking is in place and that the numbers can be reproduced.
5. Validate the result against a simpler check, benchmark, or secondary source.
6. Note any caveats that change how the result should be interpreted.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Definitions must be reproducible
- Measurement should be tied to a decision, not just a dashboard
- Validation is part of the work
- Attribution should be explicit about what it can and cannot prove
- The simplest correct measurement method is usually the best one

## Output Contract

- Metric definitions and tracking assumptions
- Validation checks and notable discrepancies
- Attribution or reporting notes that explain interpretation limits
- A short conclusion on whether the result is ready to use

## Examples

### Example 1

Input:
- Question: "Did the campaign generate qualified pipeline?"
- Data: HubSpot campaign records, GA4 events, and Salesforce opportunities

Expected output:
- Metric definition that separates lead volume, qualified lead volume, and pipeline contribution
- Validation checks for duplicate contacts, source attribution gaps, and date-window alignment
- Caveat that pipeline attribution depends on the selected model and tracking completeness

## Guardrails

- Do not report numbers that have not been validated
- Do not compare periods or cohorts that are not comparable
- Do not hide attribution assumptions
- Do not use a metric that cannot be reproduced by someone else

## Optional Tools / Resources

- HubSpot, GA4, CRM, or warehouse reporting
- UTM taxonomy and campaign naming conventions
- Dashboard docs or metric definitions
- Data quality or tracking implementation notes

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Marketing Blog (hubspot.com)](https://blog.hubspot.com/marketing), [Ahrefs Blog (ahrefs.com)](https://ahrefs.com/blog/), [Google Ads Help (support.google.com)](https://support.google.com/google-ads/), [Think with Google (thinkwithgoogle.com)](https://www.thinkwithgoogle.com/), [Content Marketing Institute (contentmarketinginstitute.com)](https://contentmarketinginstitute.com/articles/)
