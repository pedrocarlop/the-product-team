---
name: allocate
description: Distribute product investment across the portfolio with explicit rationale, trade-offs, and review cadence.
---

# Allocate

## Purpose

Use this skill to decide how product capacity should be distributed so the portfolio supports strategy instead of drifting into default spending.

## When to Use

- When quarterly or annual planning needs a resource split across initiatives
- When platform, growth, retention, and maintenance work are competing for the same people
- When leadership needs a defensible funding mix for product areas or teams

## When Not to Use

- When the question is whether an idea is worth pursuing at all
- When the issue is only how to present the plan to executives or the board
- When the problem is local priority ordering inside one already-funded area

## Required Inputs

- The current product portfolio and its strategic goals
- Available capacity in headcount, budget, and time
- Any fixed commitments, dependencies, or operating constraints
- The expected return or strategic purpose of each investment bucket

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

1. List the portfolio buckets that need funding.
2. Estimate the minimum and target investment needed for each bucket.
3. Compare allocation against strategy, risk, and expected return.
4. Identify overfunded and underfunded areas.
5. Make the trade-offs explicit, including what gets slower or smaller as a result.
6. Set a review cadence for revisiting the allocation.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Funding should reflect strategy, not historical precedent
- Every allocation should have a reason tied to a business outcome
- Platform and maintenance work should be funded consciously, not by accident
- The portfolio should preserve room for new bets
- Rebalancing should be expected, not exceptional

## Output Contract

- A portfolio allocation summary
- The rationale for the chosen split
- The areas that are funded, limited, or deferred
- The cadence for reviewing and adjusting the allocation

## Examples

### Example 1

Input:
- Portfolio pressure: growth asks are crowding out platform work

Expected output:
- Allocation: "60% growth, 20% retention, 15% platform, 5% maintenance"
- Rationale: Growth remains the main strategic push, but platform investment is preserved so future delivery speed does not erode.

## Guardrails

- Do not allocate by political pressure alone
- Do not starve platform or maintenance until they become emergencies
- Do not make the split so rigid that the portfolio cannot adapt
- Do not confuse allocation with prioritization inside a team

## Optional Tools / Resources

- Planning docs and headcount plans
- Financial or capacity models
- Product scorecards and OKRs
- Delivery and dependency maps

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Harvard Business Review (hbr.org)](https://hbr.org/), [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [McKinsey Insights (mckinsey.com)](https://www.mckinsey.com/featured-insights)
