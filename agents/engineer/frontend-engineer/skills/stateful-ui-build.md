---
name: stateful-ui-build
description: Implement the async, error, empty, and interactive state model for a surface.
trigger: When a frontend feature depends on robust state behavior.
primary_mcp: repository
fallback_tools: chrome_devtools, reference/trace
best_guess_output: A stateful UI implementation with clear behavior across critical states.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: stateful-ui-build"
done_when: Key states are implemented and verifiable in code.
---

# Stateful UI Build

## Purpose

Implement the async, error, empty, and interactive state model for a surface.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: stateful-ui-build`, include:
- `### Surface and state model`: Define the surface and the states it must handle.
- `### Loading state`: Describe loading behavior and any skeleton, pending, or optimistic patterns.
- `### Error and recovery state`: Capture failure handling and recovery behavior.
- `### Empty state`: Explain the empty or first-run experience.
- `### Interactive transitions`: Describe how the UI transitions between states during user interaction.
- `### Verification notes`: State how the critical states should be verified in code or runtime.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `chrome_devtools, reference/trace`.
- If both paths fail, produce the best-guess output described as: A stateful UI implementation with clear behavior across critical states.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat state coverage as a behavioral contract, not a checklist of vague UI states.
- Make transitions explicit enough that downstream reviewers can test them.
- Preserve exact runtime dependencies or API assumptions that affect state handling.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: stateful-ui-build`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Key states are implemented and verifiable in code.
