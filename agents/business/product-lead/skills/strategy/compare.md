---
name: compare
description: Compare strategic options with explicit criteria, tradeoffs, risks, and decision consequences so the best path is visible.
---

# Compare

## Purpose

Use this skill to turn a set of plausible strategic options into a clear comparison that makes tradeoffs, risks, and decision consequences visible.

## When to Use

- When leadership is choosing between markets, motions, investments, or operating models
- When the decision requires balancing upside, confidence, speed, cost, and risk
- When the team needs a recommendation with explicit alternatives
- When a board or executive audience needs the reasoning behind a choice

## When Not to Use

- When the question is still being framed
- When external evidence is still missing or too thin to compare honestly
- When the task is simply documenting one chosen path

## Required Inputs

- The approved problem frame
- The option set to compare
- The criteria that matter for the decision
- The evidence available for each option
- The time horizon, resource constraints, and risk tolerance

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

1. Define the comparison criteria before scoring anything.
2. List the viable options and exclude false choices that do not deserve equal attention.
3. Compare each option on strategic fit, upside, confidence, cost, speed, and reversibility.
4. Make assumptions and evidence explicit for each criterion.
5. Identify the tradeoffs the decision-maker is actually choosing between.
6. Stress-test the weakest assumption behind each option.
7. Convert the comparison into a recommendation with clear reasons and caveats.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Criteria should be explicit before options are scored
- Similar options should be compared with the same level of rigor
- Confidence matters as much as upside
- A good comparison shows what is being given up
- The recommendation should be explainable to a busy executive quickly

## Output Contract

- A comparison table or decision memo
- Criteria, evidence, and assumptions for each option
- Relative strengths, weaknesses, and failure modes
- A clear recommendation or ranking

## Examples

### Example 1

Input:
- Request: "Should we prioritize enterprise expansion, SMB expansion, or geographic expansion?"

Expected output:
- Compare: the three options across market attractiveness, execution complexity, time to signal, and capital intensity
- Recommendation: the best option given current evidence and risk tolerance
- Caveat: the assumptions that would change the ranking

## Guardrails

- Do not hide uncertain assumptions inside a score
- Do not use the comparison to justify a decision already made
- Do not overfit to a single metric like TAM or payback
- Do not compare options that are not actually viable under the same constraints

## Optional Tools / Resources

- Decision matrices and scoring sheets
- Financial and operating models
- Market scan outputs and customer evidence
- Executive and board decision criteria

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP, GitHub MCP
- Reference websites: [Harvard Business Review Strategy (hbr.org)](https://hbr.org/topic/strategy), [McKinsey Strategy & Corporate Finance Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights), [Bain Strategy Insights (bain.com)](https://www.bain.com/insights/), [BCG Insights (bcg.com)](https://www.bcg.com/publications), [a16z Market and Product Essays (a16z.com)](https://a16z.com/news-content/)
