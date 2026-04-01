---
name: experiment-readout
description: Interpret an experiment and translate the result into a decision.
trigger: When an experiment has completed and the team needs a decision-ready summary.
primary_mcp: notion, repository
fallback_tools: analyst/metric-definition, search_query
best_guess_output: An experiment readout with result, confidence, and next step.
output_artifacts: logs/active/<project-slug>/deliverables/analyst.md
section_anchor: "## Skill: experiment-readout"
done_when: The team can tell what happened, how confident to be, and what to do next.
---

# Experiment Readout

## Purpose

Interpret an experiment and translate the result into a decision.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: experiment-readout`, include:
- `### Experiment setup`: Summarize the test, population, and timing.
- `### Observed results`: Describe the headline results and any meaningful splits.
- `### Metric impact`: Explain the effect on the primary and important secondary metrics.
- `### Confidence and validity`: Assess sample size, quality, confounders, and how trustworthy the outcome is.
- `### Decision`: State the recommended decision clearly.
- `### Recommended follow-up`: List the next steps, including any re-test or rollout actions.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `analyst/metric-definition, search_query`.
- If both paths fail, produce the best-guess output described as: An experiment readout with result, confidence, and next step.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the readout separate from the original hypothesis so the evidence can contradict expectations cleanly.
- State confidence limits directly instead of burying them in footnotes.
- Tie the decision back to the pre-committed criteria when available.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/analyst.md`.
- Keep all work for this skill inside `## Skill: experiment-readout`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can tell what happened, how confident to be, and what to do next.
