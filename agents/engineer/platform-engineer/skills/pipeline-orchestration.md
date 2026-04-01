---
name: pipeline-orchestration
description: Design or improve platform pipelines and long-running processing flows.
trigger: When data or build pipelines need clearer orchestration.
primary_mcp: repository
fallback_tools: reference/ground, search_query
best_guess_output: A pipeline orchestration design or implementation.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: pipeline-orchestration"
done_when: The sequence, retries, and ownership are explicit.
---

# Pipeline Orchestration

## Purpose

Design or improve platform pipelines and long-running processing flows.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: pipeline-orchestration`, include:
- `### Pipeline scope`: Define what pipeline or processing flow is in scope.
- `### Execution sequence`: Describe the step order and dependencies.
- `### Retry and failure policy`: Explain retries, backoff, dead-lettering, or failure behavior.
- `### Ownership and handoffs`: Capture which systems or teams own which stages.
- `### Observability`: State the signals required to operate and debug the flow.
- `### Open risks`: Call out unresolved design or operational risks.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A pipeline orchestration design or implementation.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat retries, ownership, and observability as first-class parts of the design rather than afterthoughts.
- Keep the sequence concrete enough that implementation or review work can follow it directly.
- Preserve exact queue, job, or scheduler identifiers when they matter to the real flow.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: pipeline-orchestration`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The sequence, retries, and ownership are explicit.
