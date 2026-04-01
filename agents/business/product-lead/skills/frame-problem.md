---
name: frame-problem
description: Turn a raw request into a clear product problem, constraints, success criteria, and decision frame.
trigger: When the request is vague or outcome-first.
primary_mcp: notion, repository
fallback_tools: search_query, reference/ground
best_guess_output: A framing brief with objective, constraints, and success criteria.
output_artifacts: logs/active/<project-slug>/deliverables/product-lead.md
section_anchor: "## Skill: frame-problem"
done_when: The team can tell what problem is being solved and what is out of scope.
---

# Frame Problem

## Purpose

Turn a raw request into a clear product problem, constraints, success criteria, and decision frame.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: frame-problem`, include:
- `### Problem statement`: State the core problem in one crisp, bounded sentence.
- `### Objective and success criteria`: Define the intended outcome and the measures that would make the team call this successful.
- `### Constraints and non-goals`: Capture constraints, dependencies, and what should explicitly stay out of scope.
- `### Decision frame`: Explain the decision the team must make next and the tradeoffs that matter.
- `### Open questions`: List unresolved issues that still affect product direction or execution.

## Tool Path

- Start with `notion, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A framing brief with objective, constraints, and success criteria.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Preserve exact language for goals, constraints, and decision asks when those details will shape downstream design, analysis, or engineering work.
- Make non-goals explicit so later roles do not quietly expand scope.
- Call out any ambiguity that should be escalated before the team commits to delivery.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-lead.md`.
- Keep all work for this skill inside `## Skill: frame-problem`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team can tell what problem is being solved and what is out of scope.
