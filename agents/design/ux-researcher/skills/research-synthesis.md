---
name: research-synthesis
description: Turn notes, recordings, or artifacts into findings, themes, and recommendations.
trigger: After interviews, workshops, or other qualitative studies.
primary_mcp: notion, figma
fallback_tools: ux-researcher/research-plan, search_query
best_guess_output: A synthesis with themes, evidence, and design implications.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: research-synthesis"
done_when: The team can act on findings instead of raw notes.
---

# Research Synthesis

## Purpose

Turn notes, recordings, or artifacts into findings, themes, and recommendations.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: research-synthesis`, include:
- `### Source material`: State which notes, recordings, or artifacts were synthesized.
- `### Themes`: Group the core patterns or recurring signals into themes.
- `### Evidence`: Support each theme with concrete evidence.
- `### Implications`: Explain what each theme means for product or design decisions.
- `### Confidence and gaps`: State where the synthesis is strong and where evidence is thin.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `ux-researcher/research-plan, search_query`.
- If both paths fail, produce the best-guess output described as: A synthesis with themes, evidence, and design implications.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Move from raw observation to actionable meaning without skipping the evidence bridge.
- Keep the synthesis grounded in actual source material rather than generalized intuition.
- Document confidence honestly so the team knows where to probe further.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: research-synthesis`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can act on findings instead of raw notes.
