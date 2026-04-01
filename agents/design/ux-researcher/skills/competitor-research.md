---
name: competitor-research
description: Benchmark adjacent products and patterns to inform UX decisions.
trigger: When the team needs external pattern or competitor evidence.
primary_mcp: refero
fallback_tools: search_query, open
best_guess_output: A benchmark report with patterns, screenshots, and implications.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher.md
section_anchor: "## Skill: competitor-research"
done_when: Relevant competitor patterns are documented with evidence or clearly marked inference.
---

# Competitor Research

## Purpose

Benchmark adjacent products and patterns to inform UX decisions.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: competitor-research`, include:
- `### Comparison set`: List the products, surfaces, or patterns benchmarked.
- `### Pattern inventory`: Summarize the relevant patterns each competitor uses.
- `### Screens and evidence`: Link the evidence, screenshots, or citations supporting the benchmark.
- `### Implications`: Explain what the benchmark means for the current product decision.
- `### Gaps in evidence`: Call out what could not be verified directly.

## Tool Path

- Start with `refero`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, open`.
- If both paths fail, produce the best-guess output described as: A benchmark report with patterns, screenshots, and implications.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Distinguish sourced evidence from inference clearly.
- Benchmark the parts of the market that actually matter to the current decision.
- Avoid turning the output into a gallery dump without product implications.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ux-researcher.md`.
- Keep all work for this skill inside `## Skill: competitor-research`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Relevant competitor patterns are documented with evidence or clearly marked inference.
