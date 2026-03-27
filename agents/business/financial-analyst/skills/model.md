---
name: model
description: Build reproducible financial models with explicit assumptions, clean logic, and outputs that can be audited and reused.
---

# Model

## Purpose

Use this skill to construct financial models that are clear, auditable, and reusable across planning, reporting, and decision support.

## When to Use

- When building a new model from scratch
- When refactoring a spreadsheet that is hard to audit or maintain
- When adding driver logic, schedules, or linked statements

## When Not to Use

- When the task is mostly about forecasting outcomes from existing assumptions
- When the task is primarily about downside analysis or scenario stress testing
- When the task is mostly to explain the model to stakeholders

## Required Inputs

- Model purpose and intended audience
- Required outputs and decision use case
- Source data and any existing spreadsheet structure
- Assumption list, business rules, and definition of key metrics
- Tooling constraints such as Sheets, Excel, or shared reporting surfaces

## Workflow

1. Define the model objective and the exact outputs it must produce.
2. Separate inputs, calculations, and outputs into distinct model areas.
3. Encode assumptions clearly and avoid burying constants in formulas.
4. Build formulas so that outputs roll up from supporting schedules rather than being manually forced.
5. Add checks, controls, and reconciliation lines where the model could drift or break.
6. Review the model for traceability, consistency, and ease of updating.

## Design Principles / Evaluation Criteria

- Inputs are separated from calculations
- Formulas are readable and auditable
- Checks catch broken logic early
- Outputs can be traced back to sources
- The model can be updated without rewriting it

## Output Contract

- Working model or spreadsheet structure
- Assumptions and definitions tab or equivalent
- Control checks or reconciliation notes
- Brief explanation of model structure and any key design choices

## Guardrails

- Do not mix inputs and formulas in the same place without a clear convention
- Do not optimize for compactness at the expense of auditability
- Do not leave key assumptions undocumented


## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Investopedia Finance and Accounting (investopedia.com)](https://www.investopedia.com/), [Corporate Finance Institute Resources (corporatefinanceinstitute.com)](https://corporatefinanceinstitute.com/resources/), [SEC Filings and Forms (sec.gov)](https://www.sec.gov/edgar/search-and-access), [IFRS Accounting Standards (ifrs.org)](https://www.ifrs.org/issued-standards/list-of-standards/), [McKinsey Corporate Finance (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights)
