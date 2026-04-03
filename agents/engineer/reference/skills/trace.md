---
name: trace
description: Trace a behavior through files, systems, or deliverables until the real source of truth is clear.
trigger: When implementation paths or ownership boundaries are unclear.
primary_mcp: repository, deliverables
fallback_tools: reference/ground, open
best_guess_output: A traced path from entry point to source of truth.
output_artifacts: logs/active/<project-slug>/deliverables/reference-trace.md
done_when: A downstream implementer knows exactly where the change lands.
---

# Trace

## Purpose

Trace a behavior through files, systems, or deliverables until the real source of truth is clear.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/reference-trace.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

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

