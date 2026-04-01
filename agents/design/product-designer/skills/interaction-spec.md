---
name: interaction-spec
description: Specify the important interaction rules, state changes, and transitions.
trigger: When implementation needs behavior-level clarity.
primary_mcp: figma, repository
fallback_tools: paper, reference/trace
best_guess_output: An interaction spec tied to states and user actions.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer.md
section_anchor: "## Skill: interaction-spec"
done_when: An engineer can implement the interaction without guessing behaviors.
---

# Interaction Spec

## Purpose

Specify the important interaction rules, state changes, and transitions.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: interaction-spec`, include:
- `### Trigger map`: List the user actions, system events, and entry conditions in scope.
- `### State transitions`: Describe the state changes in sequence, including exit conditions.
- `### Interaction rules`: Specify deterministic behavior that must remain true.
- `### Edge cases`: Document exceptions, failures, or race conditions that change behavior.
- `### Non-obvious behaviors`: Call out interaction details an implementer would likely miss.

## Tool Path

- Start with `figma, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/trace`.
- If both paths fail, produce the best-guess output described as: An interaction spec tied to states and user actions.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Describe behavior in a way an engineer can implement without inventing missing rules.
- Prefer explicit state change language over vague intent statements.
- Keep interaction details tied to actual user triggers and system responses.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/product-designer.md`.
- Keep all work for this skill inside `## Skill: interaction-spec`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: An engineer can implement the interaction without guessing behaviors.
