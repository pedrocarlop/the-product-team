---
name: requirements-trace-review
description: Trace delivered behavior back to stated requirements, surfaces, and constraints using an explicit evidence matrix.
trigger: When implementation or design must be validated against upstream intent.
primary_mcp: repository, logs
fallback_tools: reference/verify, open
best_guess_output: A requirements trace review with gaps and mismatches.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: requirements-trace-review"
done_when: The team knows where delivery matches intent, where it drifts, and which gaps remain unverified.
---

# Requirements Trace Review

## Purpose

Trace delivered behavior back to stated requirements, surfaces, and constraints using an explicit evidence matrix.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: requirements-trace-review`, include:
- `### Review framing`: Define the source requirements, scope reviewed, and what artifacts count as evidence.
- `### Requirement matrix`: Map each major requirement or constraint to its current status, evidence, and confidence.
- `### Surface and flow mapping`: Show which screens, APIs, flows, or system behaviors implement each requirement.
- `### Confirmed matches`: Record where delivered behavior clearly satisfies stated intent.
- `### Gaps and mismatches`: Capture missing behavior, contradictory behavior, or partial delivery.
- `### Ambiguities and unverified assumptions`: Note where the requirement is vague, conflicting, or only inferred.
- `### Priority risks`: Highlight the highest-impact traceability gaps for product, engineering, or release decisions.
- `### Limits and unknowns`: Explain what could not be verified from the available evidence.

## Tool Path

- Start with `repository, logs`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both paths fail, produce the best-guess output described as: A requirements trace review with gaps and mismatches.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Build the trace matrix first. Do not collapse multiple requirements into a loose summary paragraph.
- Distinguish clearly between unmet requirements, ambiguous requirements, and unverified requirements.
- Preserve upstream wording when it matters so the team can resolve drift without reinterpretation.
- Treat constraints such as security, performance, rollout, or policy rules as requirements when they materially affect release readiness.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: requirements-trace-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows where delivery matches intent, where it drifts, and which gaps remain unverified.
