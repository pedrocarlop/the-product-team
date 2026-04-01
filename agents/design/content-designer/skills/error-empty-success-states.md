---
name: error-empty-success-states
description: Design the messaging for non-happy-path states so users can recover or proceed confidently.
trigger: When a feature needs state-specific messaging beyond the default path.
primary_mcp: notion, figma
fallback_tools: reference/trace, search_query
best_guess_output: A state-message set for error, empty, loading, and success moments.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: error-empty-success-states"
done_when: Critical states have explicit user-facing messaging.
---

# Error Empty Success States

## Purpose

Design the messaging for non-happy-path states so users can recover or proceed confidently.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: error-empty-success-states`, include:
- `### State inventory`: List the states covered and the user task affected in each one.
- `### Message set`: Provide the actual headline, body, CTA, and helper copy per state.
- `### Recovery actions`: Explain what action the user should take next, if any.
- `### Voice notes`: Capture tone constraints for stressful, celebratory, or ambiguous moments.
- `### Missing states`: Note uncovered states, assumptions, or states that still need product input.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A state-message set for error, empty, loading, and success moments.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Cover error, empty, loading, and success states unless a state genuinely does not exist.
- Make recovery pathways explicit instead of only restating the problem.
- Keep state copy aligned with the product voice and severity of the situation.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: error-empty-success-states`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Critical states have explicit user-facing messaging.
