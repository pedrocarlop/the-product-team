---
name: integrate
description: Design how systems connect through APIs, events, data contracts, sequencing, migration paths, and failure handling.
---

# Integrate

## Purpose

Use this skill to define how systems exchange data and responsibilities in a way that is reliable, compatible, and operable.

## When to Use

- When an architecture depends on APIs, events, batch jobs, or shared data
- When contracts, schemas, or idempotency rules need to be explicit
- When the system must migrate from one interface or platform to another
- When integration failure behavior matters to the business

## When Not to Use

- When the problem is still too broad to design
- When the main need is deciding between options
- When the task is policy, ownership, or standards enforcement

## Required Inputs

- The systems being connected and their owners
- The data that must move between them
- Latency, consistency, and availability expectations
- Security, auth, and compliance constraints
- Existing interface contracts, schemas, or migration limits

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Identify the integration boundary and each side's responsibility.
2. Choose the transport and contract style that fit the use case.
3. Define payloads, versioning, idempotency, retries, and timeout behavior.
4. Map error handling, fallback behavior, and operational alerts.
5. Sequence the rollout or migration so compatibility is preserved.
6. Verify that the integration can be operated and changed safely over time.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Integration should reduce coupling, not increase it
- Contracts must be versioned and explicit
- Failure handling belongs in the design, not the incident runbook
- Migration paths should be reversible where possible
- Operational ownership must be clear

## Output Contract

- Integration design with systems, responsibilities, and data flow
- Contract definition or contract summary
- Error handling, retry, and fallback behavior
- Versioning and migration plan
- Operational notes for monitoring and handoff

## Examples

### Example 1

Input:
- Need: sync customer status from CRM to billing and support systems
- Constraints: near-real-time updates, eventual consistency acceptable

Expected output:
- Design: event-driven integration with versioned event schema and idempotent consumers
- Notes: retries with dead-letter handling and documented backfill path

## Guardrails

- Do not leave failure modes undefined
- Do not design integrations without ownership and support paths
- Do not assume compatibility across versions
- Do not mix transport choice with policy or governance concerns

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Linear MCP, Postman MCP
- Websites: [AWS Architecture Center](https://aws.amazon.com/architecture/), [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework), [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/), [Martin Fowler](https://martinfowler.com/), [C4 Model](https://c4model.com/)
- API specs, schema docs, and event catalogs
- System context diagrams
- Migration plans and rollout notes
- Observability and alerting standards
