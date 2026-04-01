---
name: content-review
description: Review an existing content surface for clarity, consistency, and voice.
trigger: When the product copy exists but quality is in doubt.
primary_mcp: repository, notion
fallback_tools: search_query, reference/ground
best_guess_output: A content review with issues, recommendations, and priorities.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: content-review"
done_when: The team knows what to rewrite and why.
---

# Content Review

## Purpose

Review an existing content surface for clarity, consistency, and voice.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: content-review`, include:
- `### Findings summary`: Summarize the surface reviewed and the overall content health.
- `### Clarity issues`: List places where users may misunderstand what is happening or what to do.
- `### Consistency issues`: Call out terminology, tone, and structure drift.
- `### Rewrite priorities`: Rank the fixes by impact and urgency.
- `### Suggested rewrites`: Provide concrete rewrite examples for the highest-priority problems.

## Tool Path

- Start with `repository, notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A content review with issues, recommendations, and priorities.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Anchor the review in real strings, screens, or repo locations whenever available.
- Separate factual copy defects from stylistic suggestions.
- Preserve product, legal, or technical terms that must remain exact.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: content-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows what to rewrite and why.
