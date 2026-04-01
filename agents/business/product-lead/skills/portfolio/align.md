---
name: align
description: Align the organization around product strategy by translating portfolio-level decisions into narratives that executives, the board, and cross-functional leaders can act on.
---

# Align

## Purpose

Use this skill to ensure that product strategy decisions are understood and adopted across the executive team, the board, and the functional leaders who must execute them — not just the product organization.

## When to Use

- When a strategic bet, portfolio shift, or multi-quarter commitment needs organizational buy-in
- When the board or investors need a clear narrative connecting product direction to business outcomes
- When cross-functional leaders (engineering, sales, marketing, finance) need to understand how the strategy changes their priorities
- When a prior alignment is breaking down and the organization is drifting from the agreed direction

## When Not to Use

- When the strategy itself has not been decided
- When the alignment need is within a single product team, not across the organization
- When the task is tactical prioritization rather than strategic narrative

## Required Inputs

- The strategic decision, portfolio bet, or direction shift being communicated
- The audiences: board, executive team, functional leaders, or all of the above
- The business context: market position, competitive pressure, financial constraints
- Known objections, competing priorities, or organizational tensions
- The outcomes the strategy must produce and the timeline for evaluation

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

1. Frame the strategic decision in terms of business outcomes, not product features.
2. Map each audience's existing mental model and the gap between it and the new direction.
3. Build audience-specific narratives: board-level (ROI, risk, competitive position), executive-level (resource allocation, timeline, accountability), functional-level (what changes for their team).
4. Surface the tradeoffs explicitly — what the company is choosing not to do and why.
5. Define the evaluation criteria and timeline so alignment includes a built-in checkpoint.
6. Identify the follow-up mechanisms that prevent drift: review cadence, decision logs, and escalation paths.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Strategic alignment should change behavior, not just produce agreement
- The narrative should connect product decisions to business outcomes, not technical milestones
- Tradeoffs should be stated at the same altitude as the strategy
- Different audiences need different framings of the same decision
- Alignment without follow-through is just a meeting

## Output Contract

- A strategic alignment memo or narrative with audience-specific framings
- Explicit tradeoffs and non-goals at the portfolio level
- Evaluation criteria and review timeline
- Follow-up mechanisms to prevent organizational drift

## Examples

### Example 1

Input:
- Decision: Shift investment from horizontal platform features to a vertical-specific product line

Expected output:
- Board narrative: "This vertical focus improves our path to profitability by concentrating GTM spend on a segment where we have demonstrated product-market fit. Horizontal investment pauses for two quarters."
- Engineering narrative: "Two platform teams will be reallocated. Current commitments that conflict will be deprioritized with specific dates."
- Sales narrative: "New vertical positioning and pricing will be ready by Q2. Existing pipeline on horizontal deals should be managed to close or transitioned."

## Guardrails

- Do not align on strategy that has not been decided — alignment is not a substitute for decision-making
- Do not flatten disagreement into consensus language when real tensions exist
- Do not present portfolio tradeoffs as temporary workarounds if they are structural choices
- Do not skip the follow-up mechanisms that keep the organization on course

## Optional Tools / Resources

- Board decks and investor materials
- Strategic planning documents and portfolio reviews
- Executive meeting agendas and decision logs
- Financial models and market analysis

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Harvard Business Review (hbr.org)](https://hbr.org/), [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [McKinsey Insights (mckinsey.com)](https://www.mckinsey.com/featured-insights)
