---
name: execution-tracker
description: Create the tracking model for operational follow-through and accountability.
trigger: When a plan needs an execution dashboard or tracker.
primary_mcp: linear, notion
fallback_tools: business-ops/workflow-design
best_guess_output: An execution tracking model with owners, status, and escalation rules.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
section_anchor: "## Skill: execution-tracker"
done_when: The team can track real work without ambiguity.
---

# Execution Tracker

## Purpose

Create the tracking model for operational follow-through and accountability.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: execution-tracker`, include:
- `### Tracking model`: Describe the tracker structure and what it is meant to manage.
- `### Required fields`: Define the minimum fields each tracked item must carry.
- `### Status definitions`: Explain what each status means so the tracker stays consistent.
- `### Owner and escalation rules`: Clarify ownership and when work should escalate.
- `### Update cadence`: Specify how often the tracker should be updated and reviewed.
- `### Reporting views`: Suggest the views or summaries different stakeholders need.

## Tool Path

- Start with `linear, notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `business-ops/workflow-design`.
- If both paths fail, produce the best-guess output described as: An execution tracking model with owners, status, and escalation rules.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Design the tracker around actual operating behavior, not idealized status reporting.
- Keep status definitions tight enough that two operators would classify the same work the same way.
- Make the reporting views specific enough for weekly use without requiring extra interpretation.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Keep all work for this skill inside `## Skill: execution-tracker`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can track real work without ambiguity.
