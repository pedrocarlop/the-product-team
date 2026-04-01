---
name: stress-test
description: Test financial plans and models under adverse conditions, expose weak assumptions, and quantify downside risk before decisions are made.
---

# Stress Test

## Purpose

Use this skill to pressure-test a financial model or forecast so the team understands downside risk, breakpoints, and decision thresholds.

## When to Use

- When a decision depends on identifying the riskiest assumptions
- When leadership needs sensitivity analysis, scenario analysis, or break-even analysis
- When a forecast or investment case needs a downside view before approval

## When Not to Use

- When the task is only to build the base model
- When the task is mainly to summarize or explain the result
- When the user has not yet defined the decision or the key uncertainties

## Required Inputs

- Base model or forecast
- Key assumptions to vary and the direction of downside
- Decision threshold or approval criterion
- Scenario definitions, if already agreed
- Any non-negotiable business constraints

## Workflow

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

1. Identify the assumptions that most influence the decision.
2. Define realistic downside and upside ranges for those assumptions.
3. Run sensitivities or scenarios against the base model.
4. Highlight the assumptions that create the largest change in outcome.
5. Surface breakpoints where the decision no longer holds.
6. Summarize the downside risk in plain language for the decision-maker.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Focuses on the assumptions that matter most
- Shows the range of outcomes, not only a single downside case
- Identifies breakpoints and failure modes
- Keeps scenario definitions distinct and understandable
- Links financial impact to the business assumption causing it

## Output Contract

- Sensitivity table, scenario summary, or downside case comparison
- List of the assumptions stressed and the ranges used
- Short readout of breakpoints, decision thresholds, and key risks

## Guardrails

- Do not confuse stress testing with a forecast refresh
- Do not reuse the same assumptions under different scenario labels
- Do not present a downside case without explaining what business condition causes it


## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Investopedia Finance and Accounting (investopedia.com)](https://www.investopedia.com/), [Corporate Finance Institute Resources (corporatefinanceinstitute.com)](https://corporatefinanceinstitute.com/resources/), [SEC Filings and Forms (sec.gov)](https://www.sec.gov/edgar/search-and-access), [IFRS Accounting Standards (ifrs.org)](https://www.ifrs.org/issued-standards/list-of-standards/), [McKinsey Corporate Finance (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights)
