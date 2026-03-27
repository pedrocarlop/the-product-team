---
name: apply-patch
tool: apply_patch
description: Write the Copy Reviewer plan and review artifacts inside `/logs`.
---

# Apply Patch

Use this skill to write the Copy Reviewer's plan and review artifacts in `logs/active/<project-slug>/`. The review output should be structured, decisive, and easy for the orchestrator to route.

## When to Use

- After the role has accepted reviewer ownership and needs to write `plans/copy-reviewer.md`
- After completing the review of the relevant design artifacts and live product copy
- When documenting findings with severity levels, remediation guidance, and the overall verdict

## How to Use

Invoke `apply_patch` targeting one of these files:

- `logs/active/<project-slug>/plans/copy-reviewer.md`
- `logs/active/<project-slug>/reviews/copy-reviewer.md`

The plan must include objective, assumptions, scope, steps, deliverables, dependencies, risks, and status.

The review must:
1. Include a summary verdict
2. List findings grouped by severity (blocker, major, minor, suggestion)
3. Make each finding actionable by naming the exact string, the problem, and the suggested fix

## What to Produce

Structure each finding as:
- **Location**: Which screen, component, or state
- **Current copy**: The exact string as it appears
- **Issue**: What is wrong (unclear, too long, inconsistent terminology, wrong tone)
- **Suggested fix**: A concrete alternative or directive

## Notes for Copy Reviewer

Do not write vague findings like "copy could be improved." Every finding must name the exact string and explain precisely why it fails clarity, brevity, actionability, or consistency. A suggestion without a concrete fix is not actionable, and the review should stand on its own inside `/logs`.
