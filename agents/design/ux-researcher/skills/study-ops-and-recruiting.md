---
name: study-ops-and-recruiting
description: Define the operational plan for scheduling, recruiting, consent, and study logistics.
trigger: When research needs a concrete execution plan beyond the study design.
primary_mcp: notion, google_forms
fallback_tools: ux-researcher/screener-form-build, open
best_guess_output: A study ops plan with recruiting flow and logistics.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: study-ops-and-recruiting"
done_when: The study can be scheduled and staffed cleanly.
---

# Study Ops And Recruiting

## Purpose

Define the operational plan for scheduling, recruiting, consent, and study logistics.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: study-ops-and-recruiting`, include:
- `### Study schedule`: Lay out the timeline and sequencing for recruiting and sessions.
- `### Recruiting flow`: Describe how participants are sourced, screened, and confirmed.
- `### Consent and logistics`: Capture consent, tools, scheduling, and communication logistics.
- `### Staffing and ownership`: State who owns each operational step.
- `### Risks and contingencies`: List the main failure modes and the fallback plan for each.

## Tool Path

- Start with `notion, google_forms`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `ux-researcher/screener-form-build, open`.
- If both paths fail, produce the best-guess output described as: A study ops plan with recruiting flow and logistics.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat study ops as a real delivery plan, not just a list of admin tasks.
- Keep recruiting dependencies and staffing handoffs explicit.
- Use the screener build as fallback support only when it materially helps close the ops gap.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: study-ops-and-recruiting`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The study can be scheduled and staffed cleanly.
