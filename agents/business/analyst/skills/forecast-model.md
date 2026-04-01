---
name: forecast-model
description: Create a forecast with assumptions, ranges, and sensitivity analysis.
trigger: When planning depends on future volume, revenue, or adoption.
primary_mcp: notion
fallback_tools: search_query, analyst/metric-definition
best_guess_output: A forecast model summary with assumptions and scenarios.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
section_anchor: "## Skill: forecast-model"
done_when: The forecast is decision-usable and assumption-driven.
---

# Forecast Model

## Purpose

Create a forecast with assumptions, ranges, and sensitivity analysis.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: forecast-model`, include:
- `### Forecast question`: State the business question the forecast is meant to answer.
- `### Assumptions`: List the core assumptions, including any external inputs or planned changes.
- `### Driver model`: Explain the main forecast drivers and how they connect.
- `### Base/upside/downside scenarios`: Give scenario ranges rather than a single unqualified number.
- `### Sensitivity analysis`: Identify which assumptions change the result the most.
- `### Decision implication`: Translate the forecast into what the team should do or watch.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, analyst/metric-definition`.
- If both paths fail, produce the best-guess output described as: A forecast model summary with assumptions and scenarios.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the model assumption-driven instead of presenting a single-point estimate as fact.
- Make sure the drivers can be traced back to known metrics or explicit judgment calls.
- Emphasize what would most likely invalidate the forecast.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Keep all work for this skill inside `## Skill: forecast-model`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The forecast is decision-usable and assumption-driven.
