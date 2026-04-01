---
name: localization-prep
description: Prepare content for translation, expansion, and locale-sensitive adaptation.
trigger: When user-facing text must survive localization cleanly.
primary_mcp: notion, figma
fallback_tools: reference/verify, search_query
best_guess_output: A localization-ready content pack with notes on constraints.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: localization-prep"
done_when: Strings and content patterns are ready for localization work.
---

# Localization Prep

## Purpose

Prepare content for translation, expansion, and locale-sensitive adaptation.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: localization-prep`, include:
- `### String inventory`: Identify the strings, surfaces, and content groups in scope.
- `### Expansion risks`: Call out truncation, concatenation, and layout-sensitive copy risks.
- `### Locale-sensitive rules`: Document dates, units, cultural phrasing, and regulatory sensitivities.
- `### Terminology lockups`: List product terms that should stay stable across locales.
- `### Translator notes`: Provide context needed for accurate translation without guesswork.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, search_query`.
- If both paths fail, produce the best-guess output described as: A localization-ready content pack with notes on constraints.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Flag strings that depend on hardcoded punctuation, variable order, or plural handling.
- Keep the output actionable for both design and localization teams.
- Document unresolved copy dependencies instead of masking them.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: localization-prep`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Strings and content patterns are ready for localization work.
