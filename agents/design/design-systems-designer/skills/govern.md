---
name: govern
description: Define contribution paths, ownership, lifecycle policy, and deprecation rules so the design system evolves without chaos.
activation_hints:
  - "Use when the system needs ownership, review, versioning, or deprecation rules."
  - "Route here when multiple contributors are changing the system and guardrails are needed."
  - "Do not use for asset authoring, token naming, or documentation writing."
---

# Govern

## Purpose

Use this skill to define how design system changes are proposed, reviewed, approved, versioned, deprecated, and communicated.

## When to Use

- When a new component or token needs a contribution path
- When ownership or decision authority is unclear
- When versioning, changelogs, or migration guidance need to be established
- When a component, token, or pattern is being deprecated or replaced

## When Not to Use

- When the task is authoring the component or token itself
- When the request is mainly about usage guidance or documentation content
- When the issue is composing the asset rather than managing its lifecycle

## Required Inputs

- The asset or change being governed
- The relevant owners, reviewers, and approvers
- The current release, versioning, or migration state
- Any existing contribution process or policy to preserve
- The communication channel or audience that needs the decision

## Workflow

1. Identify the lifecycle stage of the asset: proposal, review, release, adoption, or retirement.
2. Define who can propose, who reviews, who approves, and who communicates the change.
3. Set versioning and change-log expectations proportional to the impact.
4. Establish deprecation and migration rules for anything being replaced.
5. Document escalation paths for conflicting requests or ambiguous ownership.
6. Verify that the policy can be followed consistently by the teams using the system.

## Design Principles / Evaluation Criteria

- Governance should make change safe, not slow for its own sake
- Ownership must be explicit enough to avoid silent drift
- Deprecation should come with a path forward
- Release notes should tell adopters what changed and why
- Policy should be documented, repeatable, and easy to find

## Output Contract

- A contribution or governance policy for the asset or system area
- Defined reviewers, approvers, and escalation paths
- Versioning, changelog, and migration expectations
- Deprecation timing, replacement guidance, and communication plan

## Examples

### Example 1

Input:
- A token rename would affect multiple components and downstream coded usage
- Teams need a safe path to adopt the change

Expected output:
- A governance decision that requires review and versioning
- A migration plan with timing and ownership
- A communication note for adopters

## Guardrails

- Do not approve changes without clear ownership and impact assessment
- Do not deprecate assets without a replacement and migration path
- Do not let verbal agreements stand in for documented policy
- Do not apply the same governance weight to trivial and breaking changes
- Do not use governance to mask unresolved design or token decisions

## Optional Tools / Resources

- Notion or policy docs for contribution and deprecation rules
- GitHub or other review systems for change tracking
- Changelogs, release notes, and migration guides
- Asset inventories and adoption metrics
