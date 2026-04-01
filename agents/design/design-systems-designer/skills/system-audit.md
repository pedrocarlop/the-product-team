---
name: system-audit
description: Assess the current design system for gaps, drift, duplication, and adoption risks.
trigger: When the system needs a baseline before extension or cleanup.
primary_mcp: figma, repository
fallback_tools: paper, reference/ground
best_guess_output: A system audit with prioritized gaps and recommendations.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md
section_anchor: "## Skill: system-audit"
done_when: The team knows the real system health and next moves.
---

# System Audit

## Purpose

Assess the current design system for gaps, drift, duplication, and adoption risks.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: system-audit`, include:
- `### Audit scope`: State which products, libraries, files, or surfaces were audited.
- `### Findings table`: Summarize the major findings with severity and affected areas.
- `### Duplication and drift`: Call out redundant patterns and design/code divergence.
- `### Adoption risks`: Explain what makes the system hard to use or trust today.
- `### Recommended next moves`: List the highest-leverage cleanup or investment steps.

## Tool Path

- Start with `figma, repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/ground`.
- If both paths fail, produce the best-guess output described as: A system audit with prioritized gaps and recommendations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Prioritize evidence-backed findings over broad opinions.
- Separate cosmetic inconsistency from structural system failure.
- Make the next moves small enough to act on, not just admire.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Keep all work for this skill inside `## Skill: system-audit`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows the real system health and next moves.
