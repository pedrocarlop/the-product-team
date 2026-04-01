---
name: token-architecture
description: Define or refine the token model for color, typography, spacing, and semantic usage.
trigger: When the system needs a durable token foundation.
primary_mcp: figma
fallback_tools: paper, repository
best_guess_output: A token architecture proposal tied to system usage.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md
section_anchor: "## Skill: token-architecture"
done_when: Tokens are structured well enough to scale consistently.
---

# Token Architecture

## Purpose

Define or refine the token model for color, typography, spacing, and semantic usage.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: token-architecture`, include:
- `### Token layers`: Define the token stack such as raw, semantic, and component-level tokens.
- `### Naming conventions`: Document how tokens are named and grouped.
- `### Semantic aliases`: Explain how semantic tokens map to raw primitives.
- `### Cross-platform mapping`: Note any constraints or naming differences that affect implementation.
- `### Migration notes`: Describe how existing tokens or styles should be normalized into the new model.

## Tool Path

- Start with `figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, repository`.
- If both paths fail, produce the best-guess output described as: A token architecture proposal tied to system usage.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Optimize for long-term semantic clarity, not only current file cleanliness.
- Keep token layers shallow enough that teams can reason about them.
- Document which token decisions are stable foundations versus transitional compromises.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Keep all work for this skill inside `## Skill: token-architecture`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Tokens are structured well enough to scale consistently.
