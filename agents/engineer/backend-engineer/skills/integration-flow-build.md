---
name: integration-flow-build
description: Build the integration flow between internal services or external systems.
trigger: When data or actions must move across system boundaries.
primary_mcp: repository
fallback_tools: search_query, reference/trace
best_guess_output: An integration implementation or flow design.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer.md
section_anchor: "## Skill: integration-flow-build"
done_when: The integration path, failures, and key boundaries are explicit.
---

# Integration Flow Build

## Purpose

Build the integration flow between internal services or external systems.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: integration-flow-build`, include:
- `### Systems involved`: Identify the services, vendors, jobs, or boundaries in the flow.
- `### Trigger and flow`: Describe what starts the integration and the key steps in sequence.
- `### Payload or contract boundaries`: Explain the important payloads, schemas, or contract edges.
- `### Failure handling`: Capture retries, compensating actions, and failure behavior.
- `### Observability needs`: State the signals needed to debug or operate the integration.
- `### Rollout notes`: Note rollout order, gating, or compatibility concerns.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/trace`.
- If both paths fail, produce the best-guess output described as: An integration implementation or flow design.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep system boundaries explicit so ownership is not lost across the flow.
- Separate happy-path flow from operational failure handling.
- Preserve exact contract names or queue/topic identifiers where they matter to implementation.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/backend-engineer.md`.
- Keep all work for this skill inside `## Skill: integration-flow-build`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The integration path, failures, and key boundaries are explicit.
