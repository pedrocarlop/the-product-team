---
name: visual-polish-and-consistency
description: Run the final pass on alignment, hierarchy, typography, spacing, and consistency.
trigger: When a design works structurally but needs a ship-ready polish pass.
primary_mcp: figma
fallback_tools: paper, chrome_devtools
best_guess_output: A polished design with corrected visual inconsistencies.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: visual-polish-and-consistency"
done_when: The design reads as deliberate and consistent, not provisional.
---

# Visual Polish And Consistency

## Purpose

Run the final pass on alignment, hierarchy, typography, spacing, and consistency.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: visual-polish-and-consistency`, include:
- `### Visual issues`: List the concrete hierarchy, spacing, alignment, and typography issues found.
- `### Proposed fixes`: Pair each issue with the exact correction to apply.
- `### Consistency checks`: Describe the system-level checks used to confirm the surface aligns with adjacent work.
- `### Risk of over-polish`: Note where further polish would start to distort the chosen concept or consume disproportionate effort.
- `### Final readiness notes`: State what is now ship-ready and what still feels provisional.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, chrome_devtools`.
- If both paths fail, produce the best-guess output described as: A polished design with corrected visual inconsistencies.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use a concrete issue/fix list instead of a vague polish summary.
- Polish should sharpen the chosen direction, not sand it down into something generic.
- Use `project-ds-spec.md` as the system of record for polish decisions. The company reference library is only a sanity check against generic drift.
- Use `chrome_devtools` when real browser evidence is needed for the final consistency pass.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: visual-polish-and-consistency`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The design reads as deliberate and consistent, not provisional.
