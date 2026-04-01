---
name: positioning-brief
description: Define how the product should be positioned against alternatives for a target audience.
trigger: When a market-facing message needs sharpening.
primary_mcp: notion
fallback_tools: search_query, reference/ground
best_guess_output: A positioning brief with audience, alternatives, and message pillars.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: positioning-brief"
done_when: The team can reuse the positioning consistently.
---

# Positioning Brief

## Purpose

Define how the product should be positioned against alternatives for a target audience.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: positioning-brief`, include:
- `### Target audience`: Define the primary audience and any priority segments.
- `### Problem and alternatives`: Explain the job to be done and the alternatives the audience compares against.
- `### Differentiated promise`: State the core promise or market position in a concise form.
- `### Message pillars`: Break the positioning into reusable supporting pillars.
- `### Proof points`: List the evidence, examples, or capabilities that make the promise credible.
- `### Objections and caveats`: Capture the most likely pushback or conditions where the message weakens.
- `### Reuse guidance`: Explain how downstream GTM or sales work should reuse this positioning.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A positioning brief with audience, alternatives, and message pillars.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the differentiated promise distinct from generic value statements.
- Preserve exact competitor, alternative, or customer language when it matters to message fidelity.
- Write message pillars so adjacent skills can reuse them without reinterpreting the thesis.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: positioning-brief`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can reuse the positioning consistently.
