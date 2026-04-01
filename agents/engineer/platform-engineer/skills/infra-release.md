---
name: infra-release
description: Plan or implement an infrastructure or platform release with operational safeguards.
trigger: When infra or deployment changes must be executed safely.
primary_mcp: repository
fallback_tools: search_query, reference/verify
best_guess_output: An infra release plan or implementation summary.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: infra-release"
done_when: The release path and rollback posture are explicit.
---

# Infra Release

## Purpose

Plan or implement an infrastructure or platform release with operational safeguards.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: infra-release`, include:
- `### Release scope`: Define what infrastructure or platform change is being released.
- `### Preconditions`: List the checks or dependencies required before release starts.
- `### Execution plan`: Describe the release sequence and critical steps.
- `### Rollback posture`: Explain rollback options and triggers.
- `### Operational safeguards`: Capture monitoring, gating, or human-in-the-loop protections.
- `### Verification and follow-up`: State how success is confirmed after release.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/verify`.
- If both paths fail, produce the best-guess output described as: An infra release plan or implementation summary.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep release order and rollback thinking explicit so operators can act under pressure.
- Distinguish pre-release assumptions from post-release verification.
- Preserve exact environment or deployment touchpoints where the release path depends on them.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: infra-release`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The release path and rollback posture are explicit.
