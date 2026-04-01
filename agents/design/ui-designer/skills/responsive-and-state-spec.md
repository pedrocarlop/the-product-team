---
name: responsive-and-state-spec
description: Define how the UI behaves across breakpoints and meaningful interface states.
trigger: When a design must survive real devices and async/system states.
primary_mcp: figma
fallback_tools: paper, reference/trace
best_guess_output: A responsive and state specification for the screen or flow.
output_artifacts: logs/active/<project-slug>/deliverables/ui-designer.md
section_anchor: "## Skill: responsive-and-state-spec"
done_when: Desktop, mobile, and critical states are explicitly covered.
---

# Responsive And State Spec

## Purpose

Define how the UI behaves across breakpoints and meaningful interface states.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: responsive-and-state-spec`, include:
- `### Breakpoint matrix`: Specify how the UI changes across breakpoints and screen classes.
- `### State matrix`: List the meaningful interface states and how each one changes the UI.
- `### Exceptions`: Document intentional exceptions or breakpoint/state combinations that are unsupported.
- `### Stress cases`: Call out long text, empty data, loading, errors, and other resilience cases.
- `### Implementation signals`: Note the details engineering must preserve across device and state changes.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/trace`.
- If both paths fail, produce the best-guess output described as: A responsive and state specification for the screen or flow.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat responsive behavior and state behavior as a matrix, not two separate afterthoughts.
- Use `reference/trace` when repository inspection is needed instead of abstract repository wording.
- Make exceptions explicit so they are not mistaken for omissions.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/ui-designer.md`.
- Keep all work for this skill inside `## Skill: responsive-and-state-spec`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Desktop, mobile, and critical states are explicitly covered.
