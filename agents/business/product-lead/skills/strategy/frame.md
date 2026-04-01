---
name: frame
description: Turn ambiguous strategic problems into a decision-ready frame with the real question, constraints, success criteria, and testable hypotheses.
---

# Frame

## Purpose

Use this skill to define the strategic problem clearly enough that analysis can answer it and leadership can make a decision without re-litigating the premise.

## When to Use

- When the request mixes multiple questions into one strategy ask
- When the decision-maker, deadline, or success criteria are unclear
- When the team is collecting data before agreeing on the hypothesis
- When a board, executive, or planning discussion needs a crisp question and scope

## When Not to Use

- When the strategic question has already been framed and approved
- When the task is primarily market scanning, competitor comparison, or plan assembly
- When the only need is summarizing an existing analysis or deck

## Required Inputs

- The business decision that must be made
- The decision-maker and deadline
- The business context and why the question matters now
- Known constraints, assumptions, and non-goals
- Any existing research, notes, metrics, or prior decisions

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

1. Restate the decision in one sentence and name the person who owns it.
2. Separate the core question from adjacent questions that should be parked.
3. Define the scope boundary: what is in, what is out, and what would make the answer unusable.
4. Write the key hypotheses that analysis must prove or disprove.
5. List the minimum evidence needed to answer the question well.
6. Capture risks, dependencies, and the assumptions most likely to break the recommendation.
7. Confirm the frame with the decision-maker before anyone invests in deeper analysis.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- One question, one owner, one deadline
- Hypotheses before data collection
- Clear boundaries over broad, unfocused exploration
- Decision usefulness over intellectual completeness
- Explicit assumptions and risk points
- Shared language that the whole team can repeat consistently

## Output Contract

- A one-page problem frame
- A single-sentence decision question
- Scope, constraints, and non-goals
- Hypotheses and evidence required
- Risks, assumptions, and open questions

## Examples

### Example 1

Input:
- Request: "Should we enter enterprise?"
- Context: Leadership is debating growth options
- Deadline: Board review next month

Expected output:
- Frame: "Should we enter enterprise in FY26, and if so, which segment, with what offer, and under what success thresholds?"
- Scope: target segment, timing, resource envelope, and entry criteria
- Hypotheses: enterprise demand exists, we can win efficiently, and the economics justify the investment

## Guardrails

- Do not start with research when the question itself is unstable
- Do not bundle separate decisions into one frame unless they truly share the same decision owner and timing
- Do not hide tradeoffs behind broad language like "strategic fit"
- Do not overstate certainty when the frame still depends on untested assumptions

## Optional Tools / Resources

- Prior strategy memos and board materials
- Decision logs and planning calendars
- Metrics dashboards and operating reviews
- Workshop notes or stakeholder interviews

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP, GitHub MCP
- Reference websites: [Harvard Business Review Strategy (hbr.org)](https://hbr.org/topic/strategy), [McKinsey Strategy & Corporate Finance Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights), [Bain Strategy Insights (bain.com)](https://www.bain.com/insights/), [BCG Insights (bcg.com)](https://www.bcg.com/publications), [a16z Market and Product Essays (a16z.com)](https://a16z.com/news-content/)
