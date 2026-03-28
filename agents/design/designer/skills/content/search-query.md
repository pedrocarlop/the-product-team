---
name: search-query
tool: search_query
description: Research conversation design patterns, dialogue frameworks, and AI interaction precedents before authoring flows.
---

# Search Query

Use this skill to research conversation design best practices, existing dialogue frameworks, LLM UX patterns, and fallback strategies before committing to a dialogue design approach.

## When to Use

- Before designing dialogue flows for a new domain or interaction type
- When looking for precedents for error recovery, escalation, or tone calibration
- When researching how analogous AI-powered products handle the same conversational challenge
- When validating that a proposed fallback strategy aligns with established dialogue conventions

## How to Use

Call `search_query` with a targeted query. Keep queries specific to the design challenge — avoid broad queries that return generic LLM content.

Good queries:
- `"conversational AI error recovery patterns in customer support"`
- `"LLM chat UI empty-state copy best practices"`
- `"escalation from bot to human handoff UX patterns"`

## What to Extract

- Documented dialogue design frameworks and their decision criteria
- Tone calibration guidance for the target user segment
- Anti-patterns to avoid (over-apologetic bots, vague fallbacks, dead-end recoveries)
- Component or prompt library references from credible sources

## Notes for Conversation Designer

Search before designing, not after. Grounding dialogue decisions in observed patterns prevents inventing broken conventions. Record the sources used in `research-and-rationale.md` alongside the design decisions they informed.
