---
name: api-implementation
description: Implement or extend backend APIs to support the product behavior safely.
trigger: When product or platform work requires backend endpoints or handlers.
primary_mcp: repository
fallback_tools: reference/trace, search_query
best_guess_output: A backend API implementation or change plan.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer.md
section_anchor: "## Skill: api-implementation"
done_when: The API contract is implemented with clear behavior and constraints.
---

# API Implementation

## Purpose

Implement or extend backend APIs to support the product behavior safely.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: api-implementation`, include:
- `### API surface`: Define the endpoint, handler, RPC, or callable surface being changed.
- `### Inputs and outputs`: Describe request inputs, response outputs, and any contract boundaries.
- `### Behavior and invariants`: Capture the intended behavior, constraints, and invariants.
- `### Error handling`: Explain expected failures, validation, and fallback behavior.
- `### Code touchpoints`: Identify the files, modules, or services involved.
- `### Rollout or compatibility notes`: Note compatibility concerns, versioning, or rollout implications.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A backend API implementation or change plan.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the API contract explicit enough that downstream callers or reviewers can reason about it without rereading the code.
- Separate stable invariants from implementation details that may still evolve.
- Preserve exact route, handler, or service names when they affect integration work.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/backend-engineer.md`.
- Keep all work for this skill inside `## Skill: api-implementation`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The API contract is implemented with clear behavior and constraints.
