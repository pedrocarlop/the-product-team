---
name: implement
description: Build backend services, handlers, migrations, and integrations from an agreed model without drifting from the contract.
---

# Implement

## Purpose

Use this skill to turn a backend model into working code that is cleanly layered, testable, and aligned with the agreed contract.

## When to Use

- When the API, schema, or service design is already decided
- When writing handlers, services, repositories, migrations, or queue workers
- When a bug fix needs code changes rather than more analysis

## When Not to Use

- When the main problem is still unclear and needs modeling first
- When the work is primarily production verification or rollout observation
- When the task is only about security hardening or operational resilience

## Required Inputs

- The agreed model or contract
- The target files, modules, or service area
- Testing expectations and any repo-specific conventions
- Any existing code paths that must stay compatible

## Workflow

1. Trace the request through the handler, service, persistence, and external boundary layers.
2. Keep validation at the edge and business rules in the service layer.
3. Implement the smallest change that satisfies the contract and preserves existing behavior.
4. Add or update migrations, handlers, workers, and integration points together when they are coupled.
5. Write tests that prove the behavior, including failure cases and authorization or idempotency checks where relevant.
6. Confirm the implementation matches the model and does not introduce hidden coupling.

## Design Principles / Evaluation Criteria

- Keep layers narrow and single-purpose
- Prefer explicit inputs and outputs over shared mutable state
- Make the success path and failure path equally testable
- Preserve backwards compatibility unless the change is intentionally breaking

## Output Contract

- The code change itself, scoped to the agreed backend behavior
- Tests that demonstrate the new or changed behavior
- Any migration, config, or fixture updates required for the change
- A short note on anything intentionally deferred or left unchanged

## Examples

### Example 1

Input:
- Task: Add a POST endpoint for task completion
- Model: Endpoint must reject duplicate completions and record an audit event

Expected output:
- Handler validates the request and delegates to a service
- Service enforces duplicate protection and writes the audit record
- Tests cover success, duplicate rejection, and malformed input

## Guardrails

- Do not put business logic in the route handler if a service layer exists
- Do not skip tests for behavior that is easy to regress
- Do not change persistence or auth semantics without checking the model first

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Sentry MCP, Linear MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [Node.js Docs](https://nodejs.org/en/docs), [Python Docs](https://docs.python.org/3/), [PostgreSQL Docs](https://www.postgresql.org/docs/), [Martin Fowler](https://martinfowler.com/)
- Repo search and code navigation tools
- Migration tooling for the project
- Test runner and fixture setup
- Existing integration patterns in nearby backend code
