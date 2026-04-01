---
name: naming-and-taxonomy
description: Define names and labels so concepts, navigation, and settings stay coherent.
trigger: When terminology or IA wording needs deliberate design.
primary_mcp: notion
fallback_tools: search_query, reference/reuse
best_guess_output: A naming and taxonomy proposal with rationale.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: naming-and-taxonomy"
done_when: Labels are distinct, durable, and understandable.
---

# Naming And Taxonomy

## Purpose

Define names and labels so concepts, navigation, and settings stay coherent.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: naming-and-taxonomy`, include:
- `### Naming criteria`: State the criteria the winning names must satisfy.
- `### Options considered`: List the strongest candidate names or label systems and why they were considered.
- `### Recommended naming system`: Present the recommended names and how they relate to each other.
- `### IA labels`: Show the applied labels for navigation, settings, or surface-specific taxonomy.
- `### Terms to retire`: Call out ambiguous or conflicting terms that should be removed.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/reuse`.
- If both paths fail, produce the best-guess output described as: A naming and taxonomy proposal with rationale.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for long-term coherence rather than one-off cleverness.
- Keep the naming system understandable to both new and existing users.
- Explain why the final system wins, not just what it is.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: naming-and-taxonomy`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Labels are distinct, durable, and understandable.
