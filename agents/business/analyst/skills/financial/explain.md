---
name: explain
description: Turn financial analysis into clear, decision-ready language that helps stakeholders understand what happened, why it matters, and what to do next.
---

# Explain

## Purpose

Use this skill to translate financial analysis into a concise narrative that non-finance stakeholders can understand and act on.

## When to Use

- When a model, forecast, or variance analysis needs a written readout
- When stakeholders need the business implication, not just the numbers
- When a board, leadership team, or cross-functional partner needs an executive summary

## When Not to Use

- When the task is only to compute or update the numbers
- When the main need is model design or stress testing
- When the user has not yet confirmed the audience or decision context

## Required Inputs

- The financial output to explain
- Intended audience and decision moment
- The key changes, drivers, or deltas that need to be communicated
- Any constraints on tone, length, or format

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

1. Identify who the explanation is for and what they need to decide or understand.
2. Extract the few numbers or drivers that actually matter.
3. State the result, the cause, and the implication in direct language.
4. Avoid jargon unless the audience clearly expects it and the term is already defined.
5. Check that the narrative matches the underlying model and does not overstate certainty.
6. End with the action or decision the audience should take, if one exists.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Clear before clever
- Decision-oriented
- Matches the underlying analysis exactly
- Uses business language the audience already understands
- Keeps the story focused on the material drivers

## Output Contract

- Short narrative summary or executive readout
- Key drivers and implications in plain language
- Recommended action or decision framing, when applicable

## Guardrails

- Do not introduce new numbers that are not in the analysis
- Do not bury the conclusion under too much context
- Do not explain every line item when only a few drivers matter


## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Investopedia Finance and Accounting (investopedia.com)](https://www.investopedia.com/), [Corporate Finance Institute Resources (corporatefinanceinstitute.com)](https://corporatefinanceinstitute.com/resources/), [SEC Filings and Forms (sec.gov)](https://www.sec.gov/edgar/search-and-access), [IFRS Accounting Standards (ifrs.org)](https://www.ifrs.org/issued-standards/list-of-standards/), [McKinsey Corporate Finance (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights)
