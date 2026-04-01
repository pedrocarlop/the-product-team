---
name: design-code-mapping
description: Map design system components and tokens to their implementation counterparts.
trigger: When design and code need a reliable bridge.
primary_mcp: figma, repository
fallback_tools: reference/trace, reference/verify
best_guess_output: A design-code mapping with reusable implementation guidance.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md
section_anchor: "## Skill: design-code-mapping"
done_when: Design and engineering can identify the same system primitives reliably.
---

# Design Code Mapping

## Purpose

Map design system components and tokens to their implementation counterparts.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: design-code-mapping`, include:
- `### Mapping table`: Provide a table with exactly these columns: `Design anchor`, `Token/component name`, `Code anchor`, `Status`, `Notes`.
- `### Drift and gap list`: Identify where design and code do not line up yet.
- `### Ownership notes`: State which team or role should close each mismatch.
- `### Follow-up actions`: List the next concrete fixes needed to complete the bridge.

## Tool Path

- Start with `figma, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, reference/verify`.
- If both paths fail, produce the best-guess output described as: A design-code mapping with reusable implementation guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Use concrete Figma identifiers, token names, component names, or code file paths whenever available.
- Do not satisfy this skill with prose alone; the mapping table is mandatory.
- Mark uncertain mappings explicitly instead of guessing silently.
- Do not treat the company reference library or the project ds-spec as proof that a component or token exists in code. This skill must stay grounded in actual design/code evidence.
- When `project-ds-spec.md` recommends shadcn/ui, include the implementation-foundation bridge explicitly in the mapping, such as `components.json`, registry namespaces, generated primitives, wrapper components, and where product-specific tokens diverge from stock shadcn defaults.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Keep all work for this skill inside `## Skill: design-code-mapping`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Design and engineering can identify the same system primitives reliably.
