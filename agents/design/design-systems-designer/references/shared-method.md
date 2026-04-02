# Design Systems Shared Method

Read this file at the start of any `design-systems-designer` assignment before opening the task-specific skill.

## Shared Deliverable Contract

- Update only the section named by the active skill's `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, the skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.
- Label the skill section as `sourced`, `fallback`, or `inferred` to match the strongest evidence path actually used.
- Keep `logs/active/<project-slug>/deliverables/project-ds-spec.md` as the canonical shared design-system handoff artifact whenever the active skill is allowed to update it.

## Required Inputs And Assumptions

- Start from the assignment contract plus `logs/active/<project-slug>/context.md`.
- Prefer concrete system evidence over aspirational docs.
- If a required input is missing, infer the minimum needed to continue and prefix it with `Assumed context:`.
- Lower confidence for every finding that depends on assumed context.

## Evidence Hierarchy

Use the strongest path available in this order and name the chosen path explicitly in the deliverable:

1. Live product or live design-system interaction
2. Structured system access such as repository, APIs, tokens exports, logs, or MCP tools
3. Design artifacts or workspace documentation
4. Screenshots, exports, or static captures
5. Inference

Rules:

- State which path was used and what it could not validate.
- Do not present documentation-only claims as proof that runtime behavior or implementation parity exists.
- Combine sources when needed, but always say which source established the decisive evidence.

## Environment And Reproducibility

Capture all known context that would let another agent rerun the same pass:

- Product, platform, and surface audited
- Repository branch, commit, or file snapshot when available
- Figma, Penpot, Storybook, zeroheight, or Supernova workspace/version context when available
- Theme, mode, density, locale, accessibility settings, or breakpoint assumptions
- Auth, permissions, or tooling constraints that limited access

If unknown, say `Unknown at time of analysis`.

## Model Building Rule

Build the system model before analysis. Every skill must define its own model, but the model should at minimum identify:

- System primitives
- Composition layers
- Ownership boundaries
- Runtime or documentation surfaces involved
- Where evidence comes from for each part of the model

No conclusions before the model exists.

## Finding Schema

Use this exact mini-template for every standalone finding:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Cause:
- Impact:
- Confidence:
- Recommendation direction:

Rules:

- Keep observation separate from explanation.
- Merge duplicates into one finding with broader evidence.
- Group minor issues into patterns instead of flooding the deliverable with low-signal standalone findings.

## Prioritization Rules

- Always surface critical blockers and systemic drift as standalone findings.
- Group low-impact repeats into pattern summaries.
- Prioritize by user impact, adoption impact, implementation blast radius, and reversibility.
- Prefer directional recommendations tied to findings over prescriptive redesigns without evidence.

## Coverage Map

Every skill section must end with:

- `### Coverage map`
- `Deeply analyzed:`
- `Partially analyzed:`
- `Not analyzed:`

## Limits And Unknowns

Every skill section must end with:

- `### Limits and unknowns`

State:

- What could not be validated
- What needs real-world confirmation
- Which findings have lowered confidence because of missing access or missing evidence

## Recommendation Rules

- Recommendations must map back to findings or patterns.
- Recommendations should be directional and implementation-aware.
- If a recommendation depends on a tool or process the team does not currently use, say so explicitly.

