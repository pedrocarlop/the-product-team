---
name: tooling-audit
description: Assess tool sprawl, gaps, and ownership across the operating stack.
trigger: When systems or tools are slowing execution down.
primary_mcp: notion, repository
fallback_tools: search_query, reference/ground
best_guess_output: A tooling audit with keep/change/remove recommendations.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
section_anchor: "## Skill: tooling-audit"
done_when: The stack decision is actionable and justified.
---

# Tooling Audit

## Purpose

Assess tool sprawl, gaps, and ownership across the operating stack.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: tooling-audit`, include:
- `### Tool inventory`: List the relevant tools or systems in the current stack.
- `### Current owner`: Identify the owner or owning team for each important tool or area.
- `### Keep/change/remove recommendation`: Give the recommendation for the major tools or overlaps.
- `### Gap analysis`: Note missing capabilities or unsupported workflows.
- `### Integration issues`: Capture handoff, sync, or duplication problems between tools.
- `### Recommended roadmap`: Suggest a practical sequence for cleanup or change.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A tooling audit with keep/change/remove recommendations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for a decision-ready audit, not a catalog of every tool anyone has ever touched.
- Make ownership gaps explicit because they are often the root cause of tool sprawl.
- Differentiate between replace-now issues and longer-term platform cleanups.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Keep all work for this skill inside `## Skill: tooling-audit`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The stack decision is actionable and justified.
