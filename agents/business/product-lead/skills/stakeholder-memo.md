---
name: stakeholder-memo
description: Prepare a concise decision memo or update for stakeholders.
trigger: When a product decision needs alignment or reporting.
primary_mcp: notion
fallback_tools: search_query, reference/verify
best_guess_output: A stakeholder memo with recommendation, risks, and asks.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: stakeholder-memo"
done_when: A stakeholder can read once and know the decision required.
---

# Stakeholder Memo

## Purpose

Prepare a concise decision memo or update for stakeholders.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: stakeholder-memo`, include:
- `### Audience and purpose`: Name who the memo is for and what decision or update it supports.
- `### Recommendation`: State the recommended action or conclusion up front.
- `### Why now`: Explain the timing, urgency, or forcing function.
- `### Evidence`: Summarize the key facts, signals, or sources backing the recommendation.
- `### Risks and tradeoffs`: Spell out the downside, uncertainty, and competing options.
- `### Asks or decisions needed`: List what approvals, choices, or support are being requested.
- `### Next steps`: Define the immediate follow-through after the memo lands.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/verify`.
- If both paths fail, produce the best-guess output described as: A stakeholder memo with recommendation, risks, and asks.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for one-pass comprehension; stakeholders should not have to infer the ask.
- Keep the memo decision-oriented even when the trigger is a status update.
- Distinguish confirmed facts from assumptions or in-flight work.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: stakeholder-memo`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A stakeholder can read once and know the decision required.
