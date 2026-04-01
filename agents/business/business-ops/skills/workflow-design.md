---
name: workflow-design
description: Define a new operational workflow with roles, triggers, and artifacts.
trigger: When work needs a repeatable operating model.
primary_mcp: notion, repository
fallback_tools: business-ops/process-map, reference/reuse
best_guess_output: A workflow definition with triggers, owners, and outputs.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
section_anchor: "## Skill: workflow-design"
done_when: A team can follow the workflow without inventing steps.
---

# Workflow Design

## Purpose

Define a new operational workflow with roles, triggers, and artifacts.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: workflow-design`, include:
- `### Trigger`: Define what starts the workflow and any prerequisites.
- `### Roles and responsibilities`: Assign who owns which part of the flow.
- `### Workflow steps`: Describe the ordered steps in the process.
- `### Artifacts and systems`: Identify the deliverables, tools, or systems touched along the way.
- `### Failure modes`: Call out common breakdown points and how to handle them.
- `### Adoption notes`: Explain what teams need to change to adopt the workflow successfully.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `business-ops/process-map, reference/reuse`.
- If both paths fail, produce the best-guess output described as: A workflow definition with triggers, owners, and outputs.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the workflow specific enough that new operators do not have to invent missing steps.
- Distinguish mandatory steps from optional guidance.
- Reuse proven patterns where possible, but record where the new workflow intentionally diverges.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Keep all work for this skill inside `## Skill: workflow-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A team can follow the workflow without inventing steps.
