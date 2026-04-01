---
name: frontend-verify
description: Verify the implemented UI against behavior, layout, and basic quality expectations.
trigger: When frontend work is ready for validation before handoff.
primary_mcp: repository, chrome_devtools
fallback_tools: reference/verify, figma
best_guess_output: A frontend verification result with any remaining risks.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: frontend-verify"
done_when: The UI is verified or residual issues are explicit.
---

# Frontend Verify

## Purpose

Verify the implemented UI against behavior, layout, and basic quality expectations.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: frontend-verify`, include:
- `### Verification scope`: Define what surface, flow, or component was verified.
- `### Behavior checks`: Record the key behavioral checks and whether they passed.
- `### Layout and responsive checks`: Summarize layout fidelity and breakpoint behavior.
- `### Accessibility or quality checks`: Capture basic accessibility, interaction, or polish checks.
- `### Findings`: List defects, mismatches, or confirmations.
- `### Residual risk`: State what still remains uncertain or unverified.

## Tool Path

- Start with `repository, chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, figma`.
- If both paths fail, produce the best-guess output described as: A frontend verification result with any remaining risks.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep verification findings tied to observable evidence rather than general impressions.
- Separate confirmed passes from assumed behavior.
- Preserve any exact visual or interaction mismatches that should survive into review or fix work.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: frontend-verify`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The UI is verified or residual issues are explicit.
