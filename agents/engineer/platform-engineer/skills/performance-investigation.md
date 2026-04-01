---
name: performance-investigation
description: Diagnose a platform or system performance issue and localize the bottleneck.
trigger: When performance is degraded and root cause is unclear.
primary_mcp: repository
fallback_tools: search_query, reference/trace
best_guess_output: A performance investigation with bottleneck and next step.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: performance-investigation"
done_when: The main performance constraint is identified credibly.
---

# Performance Investigation

## Purpose

Diagnose a platform or system performance issue and localize the bottleneck.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: performance-investigation`, include:
- `### Performance symptom`: Describe the degraded behavior or SLO problem.
- `### Measurement or evidence`: Capture the metrics, traces, logs, or observations supporting the investigation.
- `### Bottleneck hypothesis`: State the leading explanation for the slowdown.
- `### Localization findings`: Explain where the bottleneck appears to live.
- `### Recommended next step`: Give the next highest-leverage action.
- `### Confidence and unknowns`: State how certain the localization is and what remains unclear.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/trace`.
- If both paths fail, produce the best-guess output described as: A performance investigation with bottleneck and next step.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep evidence and hypothesis distinct so the artifact remains trustworthy as investigation continues.
- Prefer bottleneck localization over vague performance commentary.
- Preserve exact metrics, paths, or subsystems where the performance story depends on them.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: performance-investigation`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The main performance constraint is identified credibly.
