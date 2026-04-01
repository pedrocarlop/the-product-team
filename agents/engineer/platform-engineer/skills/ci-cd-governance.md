---
name: ci-cd-governance
description: Define or improve the quality gates and governance around delivery pipelines.
trigger: When releases need better automation and control.
primary_mcp: repository
fallback_tools: reference/reuse, search_query
best_guess_output: A CI/CD governance proposal or implementation.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: ci-cd-governance"
done_when: Delivery rules are concrete enough to enforce repeatedly.
---

# CI/CD Governance

## Purpose

Define or improve the quality gates and governance around delivery pipelines.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: ci-cd-governance`, include:
- `### Governance goal`: State the delivery problem or control objective.
- `### Current gaps`: List the important weaknesses in the current pipeline or process.
- `### Proposed gates or rules`: Describe the gates, checks, or governance rules to add or refine.
- `### Enforcement points`: Identify where those rules should be enforced in the workflow.
- `### Exception path`: Explain how exceptions should be handled.
- `### Adoption risks`: Capture rollout risks, developer friction, or operational downsides.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/reuse, search_query`.
- If both paths fail, produce the best-guess output described as: A CI/CD governance proposal or implementation.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep governance tied to enforceable pipeline behavior, not only policy prose.
- Reuse existing quality gates where possible instead of layering duplicate controls.
- Make exception handling explicit so the process remains operable under real delivery pressure.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: ci-cd-governance`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Delivery rules are concrete enough to enforce repeatedly.
