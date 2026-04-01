---
name: backend-verify
description: Verify backend behavior against the intended contract and operational risk.
trigger: When backend work needs a final verification pass.
primary_mcp: repository
fallback_tools: reference/verify, search_query
best_guess_output: A backend verification result with open risks if any.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer.md
section_anchor: "## Skill: backend-verify"
done_when: The backend behavior is validated or unresolved issues are explicit.
---

# Backend Verify

## Purpose

Verify backend behavior against the intended contract and operational risk.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: backend-verify`, include:
- `### Verification scope`: Define what service, endpoint, job, or flow was verified.
- `### Contract checks`: Record checks against the intended contract or spec.
- `### Failure-path checks`: Capture negative-path, validation, or recovery checks.
- `### Operational checks`: Note runtime, observability, or deployment-related checks.
- `### Findings`: Summarize the issues found or key passes.
- `### Residual risk`: State what remains unresolved or unverified.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, search_query`.
- If both paths fail, produce the best-guess output described as: A backend verification result with open risks if any.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Tie each verification claim to a present-state source of truth.
- Keep residual risk explicit so release or follow-up decisions do not overstate confidence.
- Distinguish contract correctness from operational readiness when both are being checked.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/backend-engineer.md`.
- Keep all work for this skill inside `## Skill: backend-verify`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The backend behavior is validated or unresolved issues are explicit.
