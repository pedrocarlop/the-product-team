---
name: prioritize-roadmap
description: Rank work against impact, effort, sequencing, and strategic fit.
trigger: When multiple candidate bets compete for attention.
primary_mcp: notion, linear
fallback_tools: analyst/metric-definition, search_query
best_guess_output: A ranked roadmap or priority decision with rationale.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: prioritize-roadmap"
done_when: The ordering is explicit and tradeoffs are documented.
---

# Prioritize Roadmap

## Purpose

Rank work against impact, effort, sequencing, and strategic fit.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: prioritize-roadmap`, include:
- `### Candidate bets`: List the candidate initiatives, themes, or roadmap items under consideration.
- `### Prioritization criteria`: State the criteria used to compare options.
- `### Scoring or ranking table`: Provide an explicit ranked view, scorecard, or other structured comparison.
- `### Sequencing dependencies`: Note ordering constraints, prerequisite work, or coupling between bets.
- `### Recommendation`: Name the recommended order and why it wins.
- `### Tradeoffs and deferrals`: Capture what is being deprioritized or delayed and the consequences of that choice.

## Tool Path

- Start with `notion, linear`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `analyst/metric-definition, search_query`.
- If both paths fail, produce the best-guess output described as: A ranked roadmap or priority decision with rationale.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Make the ranking legible enough that another role can explain it without re-running the whole analysis.
- Separate evidence-backed ranking logic from leadership preference or strategic judgment.
- When data is thin, state the uncertainty instead of disguising it as precision.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: prioritize-roadmap`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The ordering is explicit and tradeoffs are documented.
