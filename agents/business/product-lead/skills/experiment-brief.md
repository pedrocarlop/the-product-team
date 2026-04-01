---
name: experiment-brief
description: Define a product experiment with hypothesis, metrics, scope, and decision rules.
trigger: When the team wants to validate an idea before full commitment.
primary_mcp: notion, linear
fallback_tools: analyst/experiment-readout, search_query
best_guess_output: An experiment brief with metrics and stop/go criteria.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: experiment-brief"
done_when: The experiment can be run and judged without inventing criteria later.
---

# Experiment Brief

## Purpose

Define a product experiment with hypothesis, metrics, scope, and decision rules.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: experiment-brief`, include:
- `### Hypothesis`: State the change being tested and the expected outcome.
- `### Audience and scope`: Define who is included, what surfaces are affected, and what stays outside the test.
- `### Primary metric`: Name the success metric and how it will be evaluated.
- `### Guardrails`: List secondary metrics or constraints that protect against harm.
- `### Decision rules`: Spell out the stop, continue, or scale rules before the experiment runs.
- `### Rollout or instrumentation notes`: Capture launch details, instrumentation requirements, or sample-size considerations.
- `### Risks`: Call out major execution, measurement, or interpretation risks.

## Tool Path

- Start with `notion, linear`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `analyst/experiment-readout, search_query`.
- If both paths fail, produce the best-guess output described as: An experiment brief with metrics and stop/go criteria.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Pre-commit the decision rules so the experiment cannot be retrofitted to whatever result arrives later.
- Separate product intent from measurement design; both need to be explicit.
- Note any instrumentation dependencies that could invalidate the readout if left unresolved.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: experiment-brief`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The experiment can be run and judged without inventing criteria later.
