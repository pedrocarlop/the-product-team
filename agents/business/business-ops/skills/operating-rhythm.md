---
name: operating-rhythm
description: Design the recurring meetings, checkpoints, and decision cadence for a team.
trigger: When the team needs a clearer operating system.
primary_mcp: notion, linear
fallback_tools: business-ops/process-map
best_guess_output: An operating rhythm proposal with ceremonies and decision points.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops.md
section_anchor: "## Skill: operating-rhythm"
done_when: The cadence is concrete enough to run next week.
---

# Operating Rhythm

## Purpose

Design the recurring meetings, checkpoints, and decision cadence for a team.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: operating-rhythm`, include:
- `### Cadence table`: List the recurring rituals, frequency, owners, and participants.
- `### Purpose of each ceremony`: Explain why each touchpoint exists.
- `### Inputs and outputs`: Define what each ceremony consumes and produces.
- `### Decision rights`: Clarify who decides what inside the rhythm.
- `### Escalation path`: Explain how blocked or cross-cutting issues get raised.
- `### Risks`: Note failure modes or overload risks in the proposed cadence.

## Tool Path

- Start with `notion, linear`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `business-ops/process-map`.
- If both paths fail, produce the best-guess output described as: An operating rhythm proposal with ceremonies and decision points.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the rhythm runnable by a real team with real calendars; avoid over-instrumented ceremony sprawl.
- Tie the cadence to actual decision and execution needs rather than generic management patterns.
- Note which existing meetings can be repurposed instead of creating net-new load.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/business-ops.md`.
- Keep all work for this skill inside `## Skill: operating-rhythm`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The cadence is concrete enough to run next week.
