---
name: frame
description: Turn a vague product request into a precise decision question, scope, and output that the team can act on.
---

# Frame

## Purpose

Use this skill to turn a messy product ask into a crisp product question: what decision needs to be made, what problem is actually being solved, what scope is in or out, and what output will support the next step.

## When to Use

- When the request is vague, multi-part, or comes in as a feature idea without a clear problem statement
- When different interpretations of the same ask would lead to different product decisions
- When the owner, audience, or success criteria are not yet explicit

## When Not to Use

- When the problem statement is already clear and the work is mainly prioritization or specification
- When the task is to choose among known options rather than define the decision itself
- When the work is final messaging or execution handoff

## Required Inputs

- The request in the stakeholder's own words
- The product decision this work should inform
- The audience or decision maker who will use the answer
- Known constraints on timing, scope, dependencies, or delivery format
- Any existing context, metrics, or prior decisions that shape the ask

## Workflow

1. Restate the request as a decision-oriented question.
2. Identify the decision maker and the action the answer should change.
3. Split broad asks into smaller questions that can actually be answered.
4. Define the minimum scope needed to answer the question credibly.
5. State the expected output format, such as a memo, table, recommendation, or PRD input.
6. Call out assumptions, exclusions, and open questions before moving forward.

## Design Principles / Evaluation Criteria

- Specific beats broad
- Decision-first framing over feature-first thinking
- Smallest scope that still supports the decision
- Clear boundaries around what this work will and will not claim
- Outputs should be easy to act on, not just easy to read

## Output Contract

- A rewritten product question
- The decision it supports and the intended audience
- Scope, assumptions, and exclusions
- The expected output format
- Any open questions that must be resolved next

## Examples

### Example 1

Input:
- Stakeholder ask: "Can we add a dashboard for churn?"
- Context: Leadership wants to understand whether churn is being caused by activation or by usage drop-off

Expected output:
- Framed question: "Among newly activated users in the last 90 days, what is the main driver of churn, and which segment shows the largest drop?"
- Decision: Whether to invest in activation, retention, or reporting
- Scope: New users only, with comparison by cohort and segment

## Guardrails

- Do not jump into solution ideas before the question is specific
- Do not expand scope just because more data or more features are available
- Do not silently choose a metric or segment when the decision context is ambiguous
- Do not hide uncertainty; surface it explicitly

## Optional Tools / Resources

- Notion for documenting the question and decision frame
- Existing product briefs, PRDs, or decision logs
- Metrics dashboards or customer evidence
- Stakeholder notes and prior launch reviews

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Mind the Product (mindtheproduct.com)](https://www.mindtheproduct.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Product School Resources (productschool.com)](https://productschool.com/resources)
