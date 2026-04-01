---
name: partner-thesis
description: Define which partners matter, why, and what structure best fits the opportunity.
trigger: When partnership exploration or prioritization is needed.
primary_mcp: notion
fallback_tools: search_query, go-to-market/positioning-brief
best_guess_output: A partner thesis with targets and rationale.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: partner-thesis"
done_when: The partnership strategy is specific enough to start outreach.
---

# Partner Thesis

## Purpose

Define which partners matter, why, and what structure best fits the opportunity.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: partner-thesis`, include:
- `### Partnership goal`: State what the business wants partnership to unlock.
- `### Target partner types`: Define the categories or examples of partners that fit best.
- `### Why each matters`: Explain the logic behind the priority targets.
- `### Value exchange`: Describe what each side gives and gets.
- `### Operating model`: Recommend the partnership structure or motion to pursue.
- `### Selection risks`: Capture risks, downsides, or disqualifying conditions.
- `### Next steps`: Define the immediate follow-up work needed to pursue the thesis.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, go-to-market/positioning-brief`.
- If both paths fail, produce the best-guess output described as: A partner thesis with targets and rationale.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the thesis selective; a long undifferentiated partner list is not useful.
- Tie the value exchange to concrete business outcomes instead of vague ecosystem language.
- Call out why a seemingly attractive partner type should still be deprioritized if that is part of the analysis.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: partner-thesis`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The partnership strategy is specific enough to start outreach.
