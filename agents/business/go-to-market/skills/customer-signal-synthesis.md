---
name: customer-signal-synthesis
description: Turn customer conversations, escalations, or feedback into market-ready insights.
trigger: When field signals need to be distilled into GTM action.
primary_mcp: notion, github
fallback_tools: search_query, reference/ground
best_guess_output: A synthesis of customer signals tied to GTM implications.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: customer-signal-synthesis"
done_when: The team knows what to change in message, launch, or enablement.
---

# Customer Signal Synthesis

## Purpose

Turn customer conversations, escalations, or feedback into market-ready insights.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: customer-signal-synthesis`, include:
- `### Sources reviewed`: List the customer inputs or source types reviewed.
- `### Recurring themes`: Summarize the strongest repeated patterns.
- `### Signal strength`: Distinguish strong, weak, or anecdotal signals.
- `### Customer impact`: Explain what the signals suggest about customer pain, value, or urgency.
- `### GTM implications`: Translate the findings into messaging, launch, or enablement implications.
- `### Recommended actions`: Suggest the highest-leverage next moves for the GTM team.
- `### Unknowns`: Note questions the current signal set cannot yet answer.

## Tool Path

- Start with `notion, github`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A synthesis of customer signals tied to GTM implications.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep noisy one-off anecdotes separate from repeatable themes.
- Translate signals into GTM action instead of stopping at a feedback summary.
- Preserve source context where severity or customer segment materially changes the meaning.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: customer-signal-synthesis`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows what to change in message, launch, or enablement.
