---
name: regression-triage
description: Triage regressions using reproducibility, user impact, scope, and release impact instead of raw issue counts.
trigger: When a build or feature has defects and they need triage.
primary_mcp: repository, chrome_devtools
fallback_tools: reference/verify, open
best_guess_output: A regression triage with severity and release impact.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: regression-triage"
done_when: Blocking and non-blocking regressions are clearly separated with rationale, confidence, and next action.
---

# Regression Triage

## Purpose

Triage regressions using reproducibility, user impact, scope, and release impact instead of raw issue counts.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: regression-triage`, include:
- `### Review framing`: Define the build, branch, feature area, or release candidate being triaged.
- `### Regression inventory`: List the regressions considered, their origin surface, and current evidence status.
- `### Reproduction status`: Record whether each issue is confirmed, intermittent, suspected, or unresolved.
- `### Affected scope and users`: State who is affected, what flows are impacted, and how broad the blast radius appears to be.
- `### Severity and release impact`: Score severity with rationale and explain how it should influence release decisions.
- `### Frequency and confidence`: Separate how often the issue appears from how confident the triage evidence is.
- `### Blocking vs non-blocking decision`: Classify each issue and justify the classification.
- `### Recommended next actions`: State whether the next step is fix now, monitor, add coverage, clarify scope, or accept temporary risk.
- `### Limits and unknowns`: Explain where missing environment parity or incomplete reproduction weakens the triage.

## Tool Path

- Start with `repository, chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, open`.
- If both paths fail, produce the best-guess output described as: A regression triage with severity and release impact.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Triage is a decision exercise, not just issue documentation.
- Keep severity, frequency, confidence, and release-blocking status separate. They are related but not interchangeable.
- Prefer clear reasoning over false precision, especially when evidence is partial.
- Group regressions that share a root cause or affected surface so the team can fix the real problem instead of managing duplicates.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: regression-triage`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: Blocking and non-blocking regressions are clearly separated with rationale, confidence, and next action.
