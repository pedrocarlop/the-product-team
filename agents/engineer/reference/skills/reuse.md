---
name: reuse
description: Prefer existing approved patterns, helpers, and components over inventing new ones when solving a task.
---

# Reuse

## Purpose

Use this skill to choose the safest existing building block for the job. Reuse means matching the repository's approved patterns as closely as possible while minimizing new surface area and avoiding accidental divergence.

## When to Use

- When an existing component, helper, or module already covers the need
- When a feature should align with a shared system or established implementation pattern
- When adapting a known solution is lower risk than creating a new abstraction
- When a task needs reuse guidance after grounding and tracing are complete

## When Not to Use

- When the area has no viable existing pattern
- When the problem is deliberately novel and needs a new abstraction
- When the task is only to discover or trace, not to choose a reusable path

## Required Inputs

- The user goal and the exact capability being added or changed
- The grounded patterns or traced implementation paths already found
- Constraints that affect compatibility, such as platform, framework, or version
- Any nearby reusable modules, utilities, or components that may fit

## Workflow

1. List the existing options that could satisfy the need.
2. Compare them against the repository's established patterns and constraints.
3. Choose the option with the least change surface that still meets the requirement.
4. Call out any adaptation needed to fit the existing primitive into the new context.
5. Record why the reused path was chosen over inventing something new.

## Design Principles / Evaluation Criteria

- Reuse should reduce risk, not create hidden coupling
- Minimal change surface is usually the best first choice
- Approved patterns are stronger than personal preference
- Adapting a real existing primitive is better than copying its shape loosely

## Output Contract

- The reusable option or options considered
- The chosen path and the reason for choosing it
- Any adaptations, wrappers, or tradeoffs required to make reuse safe

## Examples

### Example 1

Input:
- Task: Add a confirmation dialog to a destructive action
- Context: The repo already has a shared modal and a standardized button set

Expected output:
- Reuse decision: Use the shared modal component and existing destructive button variant
- Adaptation: Add a local header and body message only
- Reason: Matches established interaction patterns and avoids new dialog primitives

## Guardrails

- Do not create a new abstraction when the codebase already has a suitable one
- Do not reuse a pattern that conflicts with the grounded source of truth
- Do not copy code blindly without checking whether it is still the approved pattern
- Do not reuse something just because it is nearby if it is the wrong fit

## Optional Tools / Resources

- MCP: Notion MCP, GitHub MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [DevDocs](https://devdocs.io/), [GitHub Docs](https://docs.github.com/), [RFC Editor](https://www.rfc-editor.org/), [IETF Datatracker](https://datatracker.ietf.org/)
- Search results for existing components, helpers, and utilities
- Design-system or source-system repository references
- Tests, stories, examples, and usage docs
- Repository conventions captured during grounding and tracing
