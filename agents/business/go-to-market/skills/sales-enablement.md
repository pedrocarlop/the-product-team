---
name: sales-enablement
description: Produce the core sales narrative, objections, and proof points for the field.
trigger: When sales needs to communicate and defend the product clearly.
primary_mcp: notion
fallback_tools: search_query, go-to-market/positioning-brief
best_guess_output: A sales enablement pack with talk track and objection handling.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market.md
section_anchor: "## Skill: sales-enablement"
done_when: A seller can use it directly in discovery or demo.
---

# Sales Enablement

## Purpose

Produce the core sales narrative, objections, and proof points for the field.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: sales-enablement`, include:
- `### Core pitch`: Give the primary story a seller should lead with.
- `### Ideal use cases`: Define the situations where the product resonates best.
- `### Proof points`: List evidence, examples, or customer outcomes that support the pitch.
- `### Objection-handling matrix`: Pair common objections with grounded responses.
- `### Qualification cues`: Identify signals that suggest strong or weak fit.
- `### Escalation notes`: Explain when sales should pull in product, solutions, or leadership support.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, go-to-market/positioning-brief`.
- If both paths fail, produce the best-guess output described as: A sales enablement pack with talk track and objection handling.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Write for live sales use, not as a marketing summary.
- Keep objection handling concrete enough that a seller can use it in the moment.
- Reconcile proof points with the current product reality instead of aspirational messaging.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/go-to-market.md`.
- Keep all work for this skill inside `## Skill: sales-enablement`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: A seller can use it directly in discovery or demo.
