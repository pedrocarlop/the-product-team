---
name: trace
description: Trace a behavior through files, systems, or deliverables until the real source of truth is clear.
trigger: When implementation paths or ownership boundaries are unclear.
primary_mcp: repository, deliverables
fallback_tools: reference/ground, open
best_guess_output: A traced path from entry point to source of truth.
output_artifacts: logs/active/<project-slug>/deliverables/reference.md
section_anchor: "## Skill: trace"
done_when: A downstream implementer knows exactly where the change lands.
---

# Trace

## Purpose

Trace a behavior through files, systems, or deliverables until the real source of truth is clear.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: trace`, include:
- `### Entry point`: State the starting symptom, component, or question.
- `### Trace path`: Record the path through files, systems, or artifacts.
- `### Source of truth`: Name the final source of truth reached.
- `### Ownership boundary`: Clarify who owns the relevant change surface.
- `### Downstream action`: State what the next role should do with the trace result.

## Tool Path

- Start with `repository, deliverables`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, open`.
- If both paths fail, produce the best-guess output described as: A traced path from entry point to source of truth.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the trace ordered so another specialist can replay it quickly.
- Distinguish confirmed path steps from inferred jumps.
- Preserve exact handoff boundaries when the final action belongs to another role or system.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/reference.md`.
- Keep all work for this skill inside `## Skill: trace`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A downstream implementer knows exactly where the change lands.
