---
name: schema-migration
description: Design and implement schema changes with migration and rollback awareness.
trigger: When persistent data models must change safely.
primary_mcp: repository
fallback_tools: reference/trace, search_query
best_guess_output: A migration plan or implementation with rollback considerations.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: schema-migration"
done_when: Schema changes are bounded and operationally safe.
---

# Schema Migration

## Purpose

Design and implement schema changes with migration and rollback awareness.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: schema-migration`, include:
- `### Schema change summary`: Define the structural change being made.
- `### Migration steps`: Describe the migration sequence and any staged rollout.
- `### Compatibility window`: State how old and new schema shapes coexist during transition.
- `### Rollback plan`: Explain rollback conditions and procedure.
- `### Operational risks`: Capture data loss, lock, latency, or deployment risks.
- `### Verification plan`: Explain how the migration outcome should be checked.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A migration plan or implementation with rollback considerations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep migration sequencing concrete enough that operators and reviewers can reason about it safely.
- Treat compatibility and rollback as required design elements, not optional notes.
- Preserve exact table, collection, or schema identifiers where they affect execution safety.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: schema-migration`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Schema changes are bounded and operationally safe.
