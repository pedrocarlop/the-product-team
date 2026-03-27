---
name: prioritize
description: Rank product opportunities using explicit criteria, tradeoffs, and evidence so the team can decide what to do next.
activation_hints:
  - "Use when multiple product bets compete for time, capacity, or roadmap space."
  - "Route here before committing to a roadmap, sprint goal, or resourcing decision."
  - "Do not use for problem framing, detailed specification, or stakeholder communication."
---

# Prioritize

## Purpose

Use this skill to compare product options and decide what should happen first, what should wait, and what should be dropped. The result should make the tradeoffs visible enough that someone else can challenge the ranking without guessing at hidden reasoning.

## When to Use

- When several initiatives could solve adjacent problems but capacity only allows one or two
- When a roadmap needs an ordering that can be defended with evidence
- When leadership, design, engineering, or support are disagreeing about what matters most right now

## When Not to Use

- When the problem itself is still unclear and needs framing first
- When the task is to write requirements for one already-chosen initiative
- When the work is mostly communication rather than decision-making

## Required Inputs

- The list of candidate initiatives, features, or bets
- The decision horizon, such as sprint, quarter, or half-year
- Relevant goals, constraints, and dependencies
- Evidence available for reach, impact, confidence, effort, or urgency
- Any strategic bets or non-negotiables that should shape the ranking

## Workflow

1. Define the decision horizon and the set of options being compared.
2. Write the criteria that matter for this decision, including user value, business value, effort, risk, and urgency where relevant.
3. Gather the evidence behind each option instead of relying on intuition.
4. Score or compare the options using a visible method, such as RICE, Cost of Delay, or a decision matrix.
5. Surface uncertainty, sensitivities, and any assumptions that materially affect the order.
6. Produce a ranked recommendation with the rationale and the explicit tradeoffs.

## Design Principles / Evaluation Criteria

- Transparent criteria beat hidden intuition
- Prioritization should be explainable, not just plausible
- Urgency, not just size, matters when delay has a cost
- Scores are decision aids, not substitutes for judgment
- The output should make disagreement easier to discuss, not harder

## Output Contract

- A ranked list of options
- The criteria and evidence used to compare them
- Key assumptions and confidence levels
- Any meaningful tradeoffs or second-order effects
- A clear recommendation for what to do next

## Examples

### Example 1

Input:
- Options: improve activation flow, build reporting dashboard, add enterprise export
- Context: Only one initiative can fit in the next quarter

Expected output:
- Ranking: activation flow first, reporting dashboard second, enterprise export third
- Rationale: activation has the highest reach and impact, while export is mostly a segment-specific request with lower urgency
- Notes: confidence is lower on reporting because current usage data is incomplete

## Guardrails

- Do not let seniority override the scoring or comparison method
- Do not use a framework as a post-hoc justification for a decision already made
- Do not collapse important uncertainty into a fake single score
- Do not prioritize without clarifying the decision horizon and constraints

## Optional Tools / Resources

- Google Sheets for scoring tables
- Notion for decision logs and comparison notes
- Product analytics, support data, and research notes
- Roadmap or capacity planning documents

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Mind the Product (mindtheproduct.com)](https://www.mindtheproduct.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Product School Resources (productschool.com)](https://productschool.com/resources)
