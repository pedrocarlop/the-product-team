---
name: apply-patch
tool: apply_patch
description: Write the Reviewer plan and requirements-review artifacts inside `/logs`.
---

# Apply Patch

Use this skill to write the Reviewer's plan and requirements-review artifacts in `logs/active/<project-slug>/`. The review must be structured, decisive, and actionable.

## When to Use

- After the reviewer has accepted ownership of the requirements review pass and needs to write `plans/reviewer.md`
- After completing a full review of the requirements package against the agreed review dimensions
- When the requirements package has been revised and the reviewer needs to update its findings

## How to Use

Invoke `apply_patch` targeting one of these files:

- `logs/active/<project-slug>/plans/reviewer.md`
- `logs/active/<project-slug>/reviews/reviewer.md`

The plan must include objective, assumptions, scope, steps, deliverables, dependencies, risks, and status.

The review must include:
1. **Verdict**: `pass`, `pass_with_notes`, or `fail`
2. **Summary**: One paragraph explaining the verdict
3. **Findings**: Grouped by severity — blockers, major issues, minor notes
4. **Remediation actions**: For each blocker and major issue, an explicit actionable directive

## What to Produce

Each finding must include:
- **Dimension**: Which review area (clarity, completeness, acceptance criteria quality, etc.)
- **Issue**: The specific problem with a citation to the relevant PRD section
- **Impact**: Why this is a design or engineering risk if not resolved
- **Action**: The specific change the owning archetype must make

## Notes for Reviewer

Do not write vague findings like "requirements need more detail." Name the specific `REQ-*` or `AC-*` item, describe the exact gap, and state the exact action required. Keep the review reusable by the orchestrator and future specialists without requiring the original conversation.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Engineering Practices: Reviewing Design Docs (google.github.io)](https://google.github.io/eng-practices/), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
