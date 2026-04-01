---
name: microcopy-flow-design
description: Write the core product copy across a flow so users know what is happening and what to do next.
trigger: When a feature or flow needs coherent UX writing.
primary_mcp: notion, figma
fallback_tools: search_query, reference/ground
best_guess_output: A flow-level microcopy set with key user-facing text.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: microcopy-flow-design"
done_when: The flow can be followed without copy ambiguity.
---

# Microcopy Flow Design

## Purpose

Write the core product copy across a flow so users know what is happening and what to do next.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: microcopy-flow-design`, include:
- `### Flow overview`: Summarize the user path and the moments where copy changes the outcome.
- `### Step-by-step copy table`: Provide the key copy for each step, screen, or UI milestone in order.
- `### Decision points`: Highlight copy at moments where the user must choose or confirm something.
- `### Error and loading dependencies`: Call out supporting copy needed from adjacent states.
- `### Voice rules`: Define tone, terminology, and phrasing rules that should remain consistent.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A flow-level microcopy set with key user-facing text.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Cover the whole flow instead of isolated strings.
- Tie each recommendation to the actual user action or state transition it supports.
- Keep nouns and labels consistent with any established taxonomy.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: microcopy-flow-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The flow can be followed without copy ambiguity.
