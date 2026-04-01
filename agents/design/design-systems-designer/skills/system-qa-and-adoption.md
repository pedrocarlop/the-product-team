---
name: system-qa-and-adoption
description: Validate the live system for consistency and define how teams should adopt it.
trigger: When the system exists but adoption or QA is weak.
primary_mcp: repository, figma
fallback_tools: chrome_devtools, reference/verify
best_guess_output: A system QA and adoption plan with key issues and rollout guidance.
output_artifacts: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
section_anchor: "## Skill: system-qa-and-adoption"
done_when: System issues and adoption blockers are concrete and prioritized.
---

# System QA And Adoption

## Purpose

Validate the live system for consistency and define how teams should adopt it.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: system-qa-and-adoption`, include:
- `### QA checklist`: Define the checks used to verify system consistency.
- `### Adoption blockers`: List what prevents teams from using the system cleanly today.
- `### Rollout guidance`: Describe how teams should adopt or re-adopt the system.
- `### Verification method`: Explain how future QA should be run and evidenced.
- `### Exit criteria`: State what must be true before the adoption push is considered complete.

## Tool Path

- Start with `repository, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `chrome_devtools, reference/verify`.
- If both paths fail, produce the best-guess output described as: A system QA and adoption plan with key issues and rollout guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat adoption as an operational problem, not only a design-quality problem.
- Treat `project-ds-spec.md` as the canonical adoption artifact teams should consume before the product DS folder or code implementation.
- Tie QA checks to concrete surfaces or implementation evidence.
- Make the rollout path realistic for teams with existing product commitments.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/design-systems-designer.md`.
- Also update `logs/active/<project-slug>/deliverables/project-ds-spec.md`.
- Keep all work for this skill inside `## Skill: system-qa-and-adoption`.
- In `project-ds-spec.md`, update `## Governance And Adoption` and `## QA Notes And Open Questions`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: System issues and adoption blockers are concrete and prioritized.
