---
name: govern
description: Set the standards, decision rights, review paths, and exception handling that keep design operations consistent and defensible over time.
activation_hints:
  - "Use when a design ops system needs policy, ownership, or enforcement."
  - "Route here for standards, governance charters, approvals, deprecation, or exceptions."
  - "Do not use for one-off troubleshooting or simple process documentation."
---

# Govern

## Purpose

Use this skill to define how design operations decisions are made, who owns them, and how the team keeps standards consistent as the organization changes.

## When to Use

- When a process or system needs a documented standard
- When people need clarity on who can approve, override, or escalate decisions
- When a workflow needs exception handling or a deprecation path

## When Not to Use

- When the task is mostly about process mapping or scheduling
- When the issue is a local operational gap with no broader policy impact
- When there is no repeatable decision to govern

## Required Inputs

- The object, process, or system that needs governance
- The decision owners and approvers
- The standard, policy, or rule that should apply
- The risks, exceptions, and failure modes that matter most
- The review cadence or enforcement method

## Workflow

1. Define the governed area and the decisions that must be controlled.
2. Write the minimum standard or policy needed to keep behavior consistent.
3. Assign ownership, approval rights, and escalation paths.
4. Define how exceptions are requested, reviewed, approved, and recorded.
5. Set a review cadence to catch drift, outdated rules, or repeated violations.
6. Document the lifecycle for change, retirement, or deprecation of the policy.

## Design Principles / Evaluation Criteria

- Governance should make good decisions easier, not harder
- Every rule needs an owner and a review path
- Exceptions should be explicit, not informal
- Standards should be easy to find and simple to apply
- Policies should evolve without creating confusion

## Output Contract

- Governance charter or policy summary
- Decision rights and approval matrix
- Exception handling and escalation path
- Review cadence and enforcement notes
- Deprecation or change-management guidance

## Examples

### Example 1

Input:
- Need: Decide who can publish a new design workflow template
- Risk: Teams are publishing inconsistent versions

Expected output:
- Policy: Templates require review before publication
- Ownership: Named approver and backup approver
- Exception path: Temporary approval for urgent cases with a documented follow-up review

## Guardrails

- Do not set policies without a clear owner
- Do not create exceptions that are impossible to track
- Do not confuse governance with bureaucracy
- Do not let undocumented exceptions become the real policy

## Optional Tools / Resources

- Notion MCP, Figma MCP, and Chrome DevTools MCP for policy context and operational evidence
- [zeroheight](https://zeroheight.com/)
- [Storybook Docs](https://storybook.js.org/docs)
- [DesignOps Assembly](https://designopsassembly.com/)
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Atlassian Team Playbook](https://www.atlassian.com/team-playbook)
