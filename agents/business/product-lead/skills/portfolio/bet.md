---
name: bet
description: Frame strategic product bets with clear hypotheses, evidence, upside, downside, and the signals that will prove or disprove them.
---

# Bet

## Purpose

Use this skill to turn an ambiguous opportunity into a deliberate product bet with an explicit thesis, expected return, and kill criteria.

## When to Use

- When deciding whether to enter a market, wedge into a segment, or pursue a capability
- When leadership needs a concise investment case for a meaningful product move
- When the team needs to understand what must be true for the strategy to work

## When Not to Use

- When the issue is only sequencing work that is already approved
- When the main question is how to allocate people across the portfolio
- When the work is about communicating an already chosen strategy to others

## Required Inputs

- The opportunity or problem the bet addresses
- The customer, market, or business hypothesis behind the move
- The expected upside, downside, and timeline to learn
- The evidence currently supporting the bet
- The signals that would confirm, weaken, or kill it

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: product-lead
project: <slug>
deliverable: product-lead.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Name the bet in plain language.
2. Write the core hypothesis and what must be true for it to pay off.
3. Identify the customer value, business value, and strategic value separately.
4. List the strongest evidence and the biggest unknowns.
5. Define how success will be measured and how long the team has to learn.
6. Write the decision boundary so the team knows when to double down, adjust, or stop.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Every bet should be legible as a hypothesis, not a wish
- The upside must justify the cost and opportunity cost
- The risk should be explicit rather than buried in optimism
- The learning loop should be short enough to change course in time
- The bet should connect to strategy, not just feature novelty

## Output Contract

- A one-paragraph bet thesis
- The evidence, assumptions, and open questions
- Success and failure signals
- A decision point or review horizon

## Examples

### Example 1

Input:
- Opportunity: Expand into mid-market teams using a lighter onboarding path

Expected output:
- Bet: "If we reduce time-to-value to under one week for mid-market teams, we can increase activation enough to justify a dedicated expansion motion."
- Signals: Activation rate, time-to-value, conversion to paid expansion, churn in the segment

## Guardrails

- Do not confuse a roadmap item with a strategic bet
- Do not skip the failure case or the learning horizon
- Do not make the hypothesis so broad that it cannot be tested
- Do not claim certainty when the evidence is still directional

## Optional Tools / Resources

- Product analytics and cohort data
- Market research and customer interviews
- Financial modeling inputs
- Strategy docs and planning artifacts

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Harvard Business Review (hbr.org)](https://hbr.org/), [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [McKinsey Insights (mckinsey.com)](https://www.mckinsey.com/featured-insights)
