---
name: verify
description: Re-open evidence and confirm that the chosen conclusion still holds before handoff or approval.
trigger: Before finalizing a decision that depends on repo or tool evidence.
primary_mcp: repository, deliverables
fallback_tools: reference/trace, search_query
best_guess_output: A pass/fail/unresolved verification result with cited evidence.
output_artifacts: logs/active/<project-slug>/deliverables/reference.md
section_anchor: "## Skill: verify"
done_when: The claimed conclusion is defended by present-state evidence.
---

# Verify

## Purpose

Re-open evidence and confirm that the chosen conclusion still holds before handoff or approval.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: verify`, include:
- `### Claim under review`: State the claim, decision, or conclusion being verified.
- `### Evidence checked`: List the repo, tool, or artifact evidence revisited.
- `### Pass/fail/unresolved result`: Record the result clearly.
- `### Contradictions or gaps`: Call out mismatches, stale assumptions, or missing evidence.
- `### Recommended follow-up`: Explain the next action required after verification.

## Tool Path

- Start with `repository, deliverables`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A pass/fail/unresolved verification result with cited evidence.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Treat verification as a present-state check, not a summary of what used to be true.
- Make contradictions explicit even when the final result is still mostly favorable.
- Keep the follow-up recommendation concrete so downstream roles know whether to proceed, pause, or reroute.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/reference.md`.
- Keep all work for this skill inside `## Skill: verify`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The claimed conclusion is defended by present-state evidence.
