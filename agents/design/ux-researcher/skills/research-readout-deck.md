---
name: research-readout-deck
description: Package research findings into a readout that aligns stakeholders quickly.
trigger: When research must be socialized to decision-makers.
primary_mcp: notion
fallback_tools: ux-researcher/research-synthesis, open
best_guess_output: A research readout deck or memo with findings and actions.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: research-readout-deck"
done_when: A stakeholder can understand the key findings in one pass.
---

# Research Readout Deck

## Purpose

Package research findings into a readout that aligns stakeholders quickly.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: research-readout-deck`, include:
- `### Audience and decision`: State who the readout is for and what decision they need to make.
- `### Key findings`: Present the headline findings in a stakeholder-friendly structure.
- `### Evidence highlights`: Include the strongest supporting evidence and examples.
- `### Recommendations`: Translate findings into clear recommendations or implications.
- `### Stakeholder asks`: List the decisions, approvals, or follow-up actions needed after the readout.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `ux-researcher/research-synthesis, open`.
- If both paths fail, produce the best-guess output described as: A research readout deck or memo with findings and actions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Package the story for fast comprehension rather than exhaustive note-dumping.
- Keep recommendations traceable back to evidence.
- Make the stakeholder ask explicit so the readout leads to action.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: research-readout-deck`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A stakeholder can understand the key findings in one pass.
