---
name: browser-debug
description: Reproduce and isolate a frontend issue using browser evidence.
trigger: When UI behavior is wrong and browser evidence is required.
primary_mcp: chrome_devtools
fallback_tools: repository, reference/trace
best_guess_output: A debugging summary with cause and fix direction.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: browser-debug"
done_when: The issue is localized to a concrete source of truth.
---

# Browser Debug

## Purpose

Reproduce and isolate a frontend issue using browser evidence.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: browser-debug`, include:
- `### Observed issue`: State the visible bug or incorrect behavior.
- `### Reproduction steps`: Give the exact steps, environment, or setup needed to reproduce.
- `### Browser evidence`: Capture the relevant console, network, DOM, or runtime evidence.
- `### Suspected source of truth`: Identify the likely file, component, state boundary, or upstream dependency involved.
- `### Fix direction`: Describe the likely correction path or next engineering move.
- `### Open unknowns`: Call out anything still unresolved before a fix can safely land.

## Tool Path

- Start with `chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository, reference/trace`.
- If both paths fail, produce the best-guess output described as: A debugging summary with cause and fix direction.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prefer concrete browser evidence over speculative root-cause guesses.
- Separate what is observed from what is inferred so downstream implementation work can trust the artifact.
- Preserve exact URLs, selectors, requests, or component names when they matter to reproduction.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: browser-debug`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The issue is localized to a concrete source of truth.
