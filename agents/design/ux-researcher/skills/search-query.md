---
name: search-query
tool: search_query
description: Research user behavior patterns, existing studies, competitive UX analysis, and domain insights to generate evidence before design decisions are made.
---

# Search Query

Use this skill to gather user research evidence — behavioral patterns, published studies, competitive UX analysis, and domain-specific insights — before design decisions are made. Evidence informs design; it does not replace it.

## When to Use

- When establishing a behavioral baseline for the user segment before the design phase begins
- When looking for published research, usability studies, or benchmark data relevant to the design challenge
- When researching how competitive products handle the same user problem — to understand the solution space
- When validating that a proposed design direction is consistent with established behavioral research

## How to Use

Call `search_query` with targeted research queries. Be specific about what type of evidence you need:
- `"user mental model file organization digital workspace research"` — not `"file management UX"`
- `"form abandonment triggers enterprise SaaS usability study"` — not `"form UX research"`
- `"progressive disclosure vs. upfront disclosure decision-making fatigue"` — not `"disclosure patterns"`

## What to Extract

- Published research findings with citations for `research-and-rationale.md`
- Behavioral patterns documented in usability studies that constrain or inform the design
- Competitive patterns with evidence of why they work (not just that they exist)
- Anti-patterns with documented evidence of failure

## Notes for UX Researcher

Do not present search results as design recommendations. Synthesize evidence into insights, and hand insights to the primary design role with an explicit framing: "Users do X because Y — the design should account for this by doing Z." The research role generates evidence; the design role makes decisions.
