---
name: scope
description: Define the assistant's boundaries, supported intents, exclusions, and handoff rules for conversation design work.
activation_hints:
  - "Use when the assistant's domain boundaries or intent coverage need to be clarified."
  - "Route here for scope limits, allowed topics, out-of-scope requests, and handoff criteria."
  - "Do not use for script drafting, tone tuning, or post-failure recovery details unless the scope is unclear."
---

# Scope

## Purpose

Use this skill to define what the assistant should handle, what it should refuse, and where human support or another workflow should take over.

## When to Use

- When a new assistant feature needs clear boundaries before conversation design begins
- When user requests span in-scope and out-of-scope tasks
- When escalation criteria or ownership boundaries need to be documented

## When Not to Use

- When the scope is already fixed and the task is to write the dialogue
- When the issue is primarily how the assistant responds to failure
- When the work is about tone, phrasing, or character rather than boundaries

## Required Inputs

- The product goal and business objective
- A list of supported intents or request types
- Known exclusions, safety limits, or policy constraints
- Handoff destinations and ownership rules
- Any upstream or downstream systems that define the boundary

## Workflow

1. Identify the core job the assistant is meant to do.
2. List the tasks and intents that are clearly in scope.
3. List adjacent requests that should be redirected, escalated, or refused.
4. Define handoff rules for unclear, risky, or unsupported requests.
5. Check that the scope matches product, policy, and implementation reality.
6. Record any ambiguities that must be resolved before script or copy work continues.

## Design Principles / Evaluation Criteria

- Scope should be narrow enough to be dependable
- Boundaries should be explicit enough for users and implementers
- Refusals should be consistent and understandable
- Handoffs should be deliberate, not accidental
- Scope should reduce surprise rather than create it

## Output Contract

- A scope statement describing supported and unsupported requests
- A list of in-scope intents and out-of-scope categories
- Handoff and escalation rules for borderline cases

## Examples

### Example 1

Input:
- Goal: AI assistant for order tracking
- Question: Can it also change shipping addresses?

Expected output:
- In scope: order status, delivery estimates, package location
- Out of scope: address changes after shipment, which require a support handoff

## Guardrails

- Do not broaden scope just to make the assistant seem more capable
- Do not hide limitations that affect user trust
- Do not define a boundary that the product cannot enforce
- Do not mix fallback copy into the scope definition

## Optional Tools / Resources

- Product requirements or PRDs
- Policy, safety, or trust guidance
- `search-query` for comparable scope boundaries in similar assistants

