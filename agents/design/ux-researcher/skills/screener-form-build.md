---
name: screener-form-build
description: Prepare the participant screener or intake form needed to recruit the right people.
trigger: When a study needs recruitment or intake filtering.
primary_mcp: google_forms
fallback_tools: notion, ux-researcher/research-plan
best_guess_output: A screener form or equivalent structured questionnaire.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: screener-form-build"
done_when: Recruiting can start with clear inclusion and exclusion criteria.
---

# Screener Form Build

## Purpose

Prepare the participant screener or intake form needed to recruit the right people.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: screener-form-build`, include:
- `### Recruitment criteria`: Define the inclusion and exclusion criteria clearly.
- `### Screening questions`: List the actual screener questions in order.
- `### Inclusion and exclusion logic`: Explain how answers qualify or disqualify participants.
- `### Ops notes`: Capture compensation, cadence, and handling notes needed for recruiting.
- `### Backup plan`: State what to do if the ideal sample is hard to recruit.

## Tool Path

- Start with `google_forms`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `notion, ux-researcher/research-plan`.
- If both paths fail, produce the best-guess output described as: A screener form or equivalent structured questionnaire.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use `ux-researcher/research-plan` as the fallback support instead of an undocumented questionnaire alias.
- Make qualification logic explicit so recruiters do not have to infer intent.
- Keep the screener short enough to complete, but precise enough to filter well.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: screener-form-build`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Recruiting can start with clear inclusion and exclusion criteria.
