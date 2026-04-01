---
name: focus
description: Identify the highest-leverage product priorities, cut distractions, and define what the organization should pay attention to now.
---

# Focus

## Purpose

Use this skill to decide what deserves attention now, what should wait, and what must be explicitly declined so the product team can move with conviction.

## When to Use

- When the backlog or roadmap has grown beyond what the team can realistically absorb
- When leadership needs a clear priority stack for the next planning cycle
- When a new request threatens to dilute an already important product direction

## When Not to Use

- When the real question is how to fund work across a portfolio
- When the task is choosing the size or shape of a strategic bet
- When the issue is alignment across teams rather than prioritization itself

## Required Inputs

- The business goal, customer goal, or company outcome the prioritization must support
- The candidate initiatives or themes under consideration
- Known constraints on time, headcount, dependencies, or risk
- Any existing strategy, roadmap, or operating cadence that the decision must respect

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

1. State the decision in one sentence so the scope is explicit.
2. Separate must-do work from nice-to-have work and from speculative work.
3. Rank options by strategic leverage, urgency, reversibility, and confidence.
4. Identify the work that should stop, shrink, or move later so focus is real.
5. Write the priority order in a way that a PM or team lead can act on immediately.
6. Check whether the resulting focus still matches the product vision and current market conditions.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Concentrate effort on the few things that most change outcomes
- Prefer explicit trade-offs over soft compromise
- Optimize for strategic leverage, not just stakeholder volume
- Make the "not now" list visible and defensible
- Keep the output short enough to drive action without interpretation

## Output Contract

- A ranked priority list or focus statement
- The work that is explicitly deferred or cut
- The rationale for the top trade-offs
- Any assumption that could change the order later

## Examples

### Example 1

Input:
- Goal: Improve activation in the next quarter
- Candidates: onboarding redesign, pricing changes, new integrations, analytics cleanup

Expected output:
- Focus: "Prioritize onboarding redesign and analytics cleanup; defer pricing changes and new integrations until activation improves."
- Rationale: The first two most directly affect activation and give faster feedback.

## Guardrails

- Do not turn focus into an everything-is-important compromise
- Do not hide trade-offs behind broad themes
- Do not prioritize based only on the loudest request
- Do not overfit to short-term noise when the strategy points elsewhere

## Optional Tools / Resources

- Roadmaps, planning docs, and intake queues
- Product metrics and funnel data
- Customer feedback and support themes
- Strategy or vision documents

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Harvard Business Review (hbr.org)](https://hbr.org/), [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [McKinsey Insights (mckinsey.com)](https://www.mckinsey.com/featured-insights)
