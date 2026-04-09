---
name: verify
description: Re-open evidence and confirm that the chosen conclusion still holds before handoff or approval.
trigger: Before finalizing a decision that depends on repo or tool evidence.
primary_mcp: repository, deliverables
fallback_tools: reference/trace, search_query
best_guess_output: A pass/fail/unresolved verification result with cited evidence.
output_artifacts: knowledge/reference-verify.md
done_when: The claimed conclusion is defended by present-state evidence.
---

# Verify

## Purpose

Re-open evidence and confirm that the chosen conclusion still holds before handoff or approval.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/reference-verify.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

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

