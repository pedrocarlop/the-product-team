---
name: interview-guide-build
description: Write the interview or discussion guide with sequencing, probes, and evidence goals.
trigger: When live research sessions need a structured guide.
primary_mcp: notion
fallback_tools: search_query, ux-researcher/research-plan
best_guess_output: An interview guide that supports comparable sessions.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: interview-guide-build"
done_when: A moderator can run sessions without improvising the core script.
---

# Interview Guide Build

## Purpose

Write the interview or discussion guide with sequencing, probes, and evidence goals.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: interview-guide-build`, include:
- `### Research objective`: State the decision or uncertainty the interviews must illuminate.
- `### Session structure`: Lay out the flow of the session from intro to close.
- `### Questions and probes`: Provide the main questions plus follow-up probes.
- `### Evidence goals`: State what evidence each section of the guide is meant to surface.
- `### Moderator notes`: Capture facilitation cautions, transitions, or bias risks.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, ux-researcher/research-plan`.
- If both paths fail, produce the best-guess output described as: An interview guide that supports comparable sessions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Write for a moderator who should not have to improvise the core flow.
- Keep questions neutral and connected to the study objective.
- Separate mandatory questions from optional probes so the guide stays usable under time pressure.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: interview-guide-build`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A moderator can run sessions without improvising the core script.
