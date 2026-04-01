---
name: research-plan
description: Define the research objective, method, sample, risks, and reporting path before the study runs.
trigger: When the team needs a real study plan instead of ad hoc interviews.
primary_mcp: notion
fallback_tools: search_query, reference/ground
best_guess_output: A research plan with question, method, sample, and outputs.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: research-plan"
done_when: A study can be executed without inventing the protocol later.
---

# Research Plan

## Purpose

Define the research objective, method, sample, risks, and reporting path before the study runs.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: research-plan`, include:
- `### Research question`: State the main question and the decision it should unlock.
- `### Method and sample`: Specify the method, sample, and why they fit the question.
- `### Risks and biases`: List the biggest threats to study quality or interpretation.
- `### Outputs`: Define the expected artifacts, readout shape, and timing.
- `### Decision the study should unlock`: State the product or design decision this research is meant to inform.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A research plan with question, method, sample, and outputs.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Make the plan executable without requiring the team to fill in core protocol gaps later.
- Tie the method and sample to the decision, not to generic research best practice.
- Document what the study will not answer so expectations stay honest.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: research-plan`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A study can be executed without inventing the protocol later.
