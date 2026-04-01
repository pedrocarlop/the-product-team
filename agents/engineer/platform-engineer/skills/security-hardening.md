---
name: security-hardening
description: Identify and implement a concrete security improvement or remediation.
trigger: When the system needs a specific security fix or hardening step.
primary_mcp: repository
fallback_tools: search_query, reference/verify
best_guess_output: A security hardening change or remediation plan.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer.md
section_anchor: "## Skill: security-hardening"
done_when: The security issue and fix path are explicit.
---

# Security Hardening

## Purpose

Identify and implement a concrete security improvement or remediation.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: security-hardening`, include:
- `### Threat or weakness`: Define the security issue being addressed.
- `### Affected surface`: Identify the systems, paths, or assets affected.
- `### Hardening change`: Describe the remediation or protection being added.
- `### Residual risk`: Capture what risk remains after the change.
- `### Operational impact`: Note deployment, usability, or maintenance implications.
- `### Verification notes`: Explain how the fix should be verified.

## Tool Path

- Start with `repository`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/verify`.
- If both paths fail, produce the best-guess output described as: A security hardening change or remediation plan.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the remediation tied to a concrete threat or weakness, not general hardening aspirations.
- Make residual risk explicit so follow-up work can prioritize correctly.
- Preserve any exact configuration, endpoint, or control names needed for implementation and review.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/platform-engineer.md`.
- Keep all work for this skill inside `## Skill: security-hardening`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The security issue and fix path are explicit.
