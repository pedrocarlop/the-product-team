---
name: handoff-spec
description: Prepare the structured design handoff for downstream UI, content, and engineering work.
trigger: When discovery and flow work must be handed downstream.
primary_mcp: notion, figma
fallback_tools: paper, reference/verify
best_guess_output: A handoff spec linking flow, structure, and open questions.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: handoff-spec"
done_when: A downstream role can continue without reopening the design problem.
---

# Handoff Spec

## Purpose

Prepare the structured design handoff for downstream UI, content, and engineering work.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: handoff-spec`, include:
- `### Assignment type`: Classify the work as `new design` or `extension of existing pattern`.
- `### Experience summary`: Summarize the user job, flow, and intended outcome.
- `### Flow and screen inventory`: List the screens, states, and flow stages the downstream team must preserve.
- `### Downstream contracts`: Call out what UI, content, and engineering each need to deliver.
- `### Exploration prerequisites`: For `new design`, point to the exploration and comparison sections required before concrete UI production.
- `### Open questions`: List unresolved decisions that still need explicit follow-up.

## Tool Path

- Start with `notion, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/verify`.
- If both paths fail, produce the best-guess output described as: A handoff spec linking flow, structure, and open questions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Make the handoff specific enough that downstream roles do not need to rediscover the problem.
- When the assignment is `new design`, explicitly require divergent exploration before screen production.
- Preserve edge cases, dependencies, and assumptions that could be lost in a compressed summary.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: handoff-spec`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A downstream role can continue without reopening the design problem.
