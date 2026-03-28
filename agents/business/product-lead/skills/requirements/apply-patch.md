---
name: apply-patch
tool: apply_patch
description: Write and iterate on the Product Lead plan and requirements deliverable artifacts inside `/logs`.
---

# Apply Patch

Use this skill to write the Product Lead's plan and deliverable artifacts inside `logs/active/<project-slug>/`. Within the `requirements/` discipline group, the Product Lead records both its working plan and its authored requirements package in `/logs`.

## When to Use

- After the orchestrator has staffed the Product Lead and the role has accepted ownership
- When drafting `plans/product-lead.md` before any substantial execution
- When iterating on `deliverables/product-lead.md` in response to review findings or new constraints

## How to Use

Invoke `apply_patch` targeting one of these files:

- `logs/active/<project-slug>/plans/product-lead.md`
- `logs/active/<project-slug>/deliverables/product-lead.md`

The plan must cover:

- Objective
- Assumptions
- Scope
- Steps
- Deliverables
- Dependencies
- Risks
- Status

The deliverable should contain the complete, design-ready, implementation-aware requirements package. It must cover:

- Problem statement and business objective
- Target users and user needs
- In-scope and out-of-scope items
- Assumptions, open questions, edge cases, dependencies, and risks
- Functional and non-functional requirements with `REQ-*` identifiers
- Acceptance criteria with `AC-*` identifiers
- Success metrics
- Design-system and source-system dependencies explicitly named

## What to Produce

Every requirement must be:
- **Specific**: One requirement per `REQ-*` entry — no compound requirements
- **Testable**: The acceptance criteria can be verified without interpretation
- **Traceable**: Linked back to a user need or business objective

## Notes for Product Lead

Expose ambiguity explicitly. A requirements package that silently invents answers is less useful than one that names what still needs a decision. Keep the plan and deliverable aligned so the orchestrator can reconcile ownership, approvals, and downstream work quickly.

## Optional Tools / Resources

- Shared MCP servers: Notion MCP, Linear MCP, GitHub MCP, Slack MCP
- Reference websites: [Atlassian Product Requirements Guide (atlassian.com)](https://www.atlassian.com/agile/product-management/requirements), [Google Technical Writing Resources (developers.google.com)](https://developers.google.com/tech-writing), [Microsoft Writing Style Guide (learn.microsoft.com)](https://learn.microsoft.com/en-us/style-guide/welcome/), [ProductPlan Guides (productplan.com)](https://www.productplan.com/learn/), [NN/g UX Documentation Articles (nngroup.com)](https://www.nngroup.com/)
