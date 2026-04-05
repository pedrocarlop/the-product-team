---
name: integration-flow-build
description: Build integration flows by modeling cross-system boundaries first, then validating contracts, timing, retries, idempotency, compensations, observability, and rollout risk.
trigger: When data or actions must move across system boundaries, especially through APIs, queues, webhooks, brokers, or long-running workflows.
required_inputs:
  - the systems, services, vendors, queues, topics, or jobs involved
  - the trigger that starts the flow and the expected downstream effect
  - the request, event, payload, or schema contract at each boundary
  - retry, timeout, ordering, deduplication, and idempotency expectations
  - compensation or rollback behavior for partial failure
  - runtime environment, auth state, and deployment stage when known
recommended_passes:
  - integration map and boundary inventory
  - contract and payload inspection
  - failure-path and retry analysis
  - idempotency and compensation review
  - observability and rollout review
  - synthesis and prioritized findings
primary_mcp: repository
fallback_tools:
  - reference/trace
  - search_query
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [temporal, hookdeck, svix, testcontainers]
  contracts:
    primary: [asyncapi, openapi, buf, redocly_cli]
  artifacts:
    primary: [diagrams, docs]
  fallback:
    primary: [reference/trace, search_query]
tool_routing:
  - if: the flow is long-running, multi-step, or requires durable retries, heartbeats, or compensation
    use: [temporal]
  - if: the boundary is event-driven or asynchronous
    use: [asyncapi]
  - if: inbound webhooks must be captured, replayed, or forwarded locally
    use: [hookdeck]
  - if: outbound webhooks need signing, delivery tracking, or retry management
    use: [svix]
  - if: the integration depends on real downstream services or broker/database parity
    use: [testcontainers]
  - if: protobuf or gRPC contracts are part of the flow
    use: [buf]
  - if: HTTP contracts need linting, bundling, or reference docs validation
    use: [redocly_cli]
  - if: the primary runtime path is unavailable or the repository is missing needed evidence
    use: [reference/trace, search_query]
best_guess_output: An integration implementation or flow design with explicit contracts, retries, failure handling, and boundary notes.
output_artifacts: knowledge/backend-engineer-integration-flow-build.md
done_when: The integration path, contract boundaries, retries, idempotency, compensations, observability, and rollout constraints are explicit enough to implement and verify.
---

# Integration Flow Build

## Purpose

Build and reason about backend integration flows across service boundaries.

This skill constructs an integration model before any implementation judgment: who initiates the flow, what crosses the boundary, how failures propagate, what must be retried or compensated, and how operators will observe the result.

This skill does not replace API implementation or domain modeling. It focuses on the cross-system path, the timing semantics, and the operational edge cases that make integrations durable.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/backend-engineer-integration-flow-build.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: integration-flow-build`, include:
- `### Systems involved`: Identify the services, vendors, jobs, or boundaries in the flow.
- `### Trigger and flow`: Describe what starts the integration and the key steps in sequence.
- `### Payload or contract boundaries`: Explain the important payloads, schemas, or contract edges.
- `### Failure handling`: Capture retries, compensating actions, and failure behavior.
- `### Observability needs`: State the signals needed to debug or operate the integration.
- `### Rollout notes`: Note rollout order, gating, or compatibility concerns.

## Required Inputs and Assumptions

Required inputs:
- The systems, services, vendors, queues, topics, or jobs involved
- The trigger that starts the flow and the expected downstream effect
- The payload, schema, or contract at each boundary
- Retry, timeout, ordering, deduplication, and idempotency expectations
- Compensation, rollback, or replay behavior for partial failure
- Runtime environment, auth state, deployment stage, and data shape when known

If inputs are missing, infer provisional values and prefix each with `Assumed context:`.

Known vs unknown:
- The systems involved are usually known from code, tickets, or docs.
- Delivery semantics, retry behavior, and ownership boundaries are often under-specified and must be surfaced before conclusions are written.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live or current runtime evidence from logs, traces, queues, brokers, webhook captures, or running workflow state.
2. Structured repository evidence from code, tests, migrations, configs, and generated contracts.
3. Contract and design artifacts such as AsyncAPI, OpenAPI, protobuf, ADRs, runbooks, or flow diagrams.
4. Screenshots, static payload examples, or issue attachments.
5. Inference from conventions, naming, or surrounding code.

Declare which path was used and state its limits. Prefer live evidence when the goal is to validate real delivery behavior; prefer repository evidence when the goal is to understand intended implementation.

## Tool Stack

**Runtime - primary:**

- `repository`: source code, configs, tests, and generated contracts
- `logs`: runtime evidence, failures, and boundary behavior

**Runtime - secondary:**

- `temporal`: durable workflow orchestration, retries, heartbeats, and compensation
- `hookdeck`: inbound webhook capture, replay, and local forwarding
- `svix`: outbound webhook delivery, signing, retries, and delivery tracking
- `testcontainers`: real dependency parity for local or CI integration tests

**Contracts - primary:**

- `asyncapi`: event and message contracts
- `openapi`: HTTP contract and schema surfaces
- `buf`: protobuf and gRPC contract evolution
- `redocly_cli`: OpenAPI linting, bundling, and contract docs

**Artifacts - primary:**

- `diagrams`
- `docs`

**Fallback:**

- `reference/trace`
- `search_query`

## Tool Routing

- If the flow is long-running, multi-step, or requires durable retries, heartbeats, or compensation, use `temporal`.
- If the boundary is event-driven or asynchronous, use `asyncapi` before making implementation claims.
- If inbound webhooks must be captured, replayed, or forwarded locally, use `hookdeck`.
- If outbound webhooks need signing, delivery tracking, or retry management, use `svix`.
- If the integration depends on real downstream services or broker/database parity, use `testcontainers`.
- If protobuf or gRPC contracts are part of the flow, use `buf` to inspect compatibility and breaking change risk.
- If HTTP contracts need linting, bundling, or reference-doc validation, use `redocly_cli`.
- If live runtime evidence is missing, fall back to `reference/trace` and `search_query`, and label the result as `fallback`.

## Tool Path

- Start with `repository, logs`.
- If the flow is long-running or compensation-heavy, use `temporal`.
- If the boundary is event-driven, use `asyncapi`.
- If inbound webhook capture or replay is required, use `hookdeck`.
- If outbound webhook delivery, signing, or retry management is the main concern, use `svix`.
- If realistic downstream parity is required, use `testcontainers`.
- If gRPC or protobuf contracts are involved, use `buf`.
- If HTTP contracts need linting, bundling, or drift checks, use `redocly_cli`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: An integration implementation or flow design with explicit contracts, retries, failure handling, and boundary notes.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Environment and Reproducibility

Record the following when known:

- repository commit or build hash
- environment name and stage
- auth state and tenant or account context
- queue, topic, endpoint, or workflow identifiers
- sample payload IDs, correlation IDs, or trace IDs
- dependency versions and container images
- feature flags, rollout gates, and configuration knobs
- date and time of inspection

If any of the above is unknown, state it explicitly. Do not present test-environment behavior as equivalent to production unless that was actually verified.

## Model Building

Before analysis, construct an integration map with these elements:

- actors and owning systems
- trigger and start condition
- synchronous versus asynchronous segments
- payloads, schemas, and contract edges
- delivery guarantees and retry semantics
- idempotency keys, deduplication, and ordering rules
- compensation, replay, and rollback paths
- observability points and operator actions
- blast radius and ownership boundaries

Do not write findings before this model exists.

## Core Method Execution

Follow this sequence:

1. Clarify scope. Identify the exact integration and the boundary being reviewed.
2. Build the integration map. Separate the trigger, transport, receiver, and downstream side effects.
3. Inspect contracts. Confirm schema shape, versioning expectations, and compatibility constraints.
4. Analyze failure paths. Enumerate timeout, retry, duplicate delivery, poison message, and partial failure cases.
5. Check idempotency and compensation. Verify what prevents double-apply and how recovery works after a partial success.
6. Review observability. Confirm logs, metrics, traces, correlation IDs, replay hooks, and alertability.
7. Review rollout risk. Check compatibility, sequencing, gating, and rollback implications.
8. Synthesize. Merge duplicate observations and separate implementation facts from inferred risk.

## Workflow Notes

- Keep system boundaries explicit so ownership is not lost across the flow.
- Separate happy-path sequencing from failure handling, retries, and compensation.
- Preserve exact contract names, queue or topic identifiers, and workflow names when they matter to implementation.
- Never assume exactly-once delivery unless the evidence proves it.
- Make rollback and replay posture explicit whenever the flow crosses teams or vendors.

## Structured Findings

Every finding must use this exact schema. No free-form output.

```text
#### Finding <id>
Observation: [What was seen, without interpretation]
Evidence: [Tool used + source path, log, trace, or artifact reference]
Repro steps: [Exact steps to reproduce or confirm the issue]
Cause: [Why this issue likely exists, labeled as inferred if not confirmed]
Impact: [Effect on correctness, reliability, or operability]
Confidence: [High / Medium / Low + rationale]
```

## Prioritization Logic

Prioritize findings by user and system impact:

1. Critical - duplicate side effects, lost events, data corruption, unrecoverable failures, broken compensation, or security/privacy exposure at a boundary.
2. Significant - brittle retries, weak idempotency, partial delivery risk, missing observability, or compatibility gaps that threaten reliability.
3. Minor - naming drift, documentation gaps, or non-blocking operational roughness.

Do not include more than ten standalone findings. Group small issues that share a root cause.

## Pattern Detection

After analysis, identify recurring integration patterns such as:

- repeated retry failure across multiple boundaries
- idempotency gaps or duplicate-delivery risk
- contract drift between producers and consumers
- timeout mismatch between caller and callee
- ownership ambiguity across service boundaries
- missing correlation IDs or replay hooks
- compensation logic that is incomplete or untestable

Surface system-level causes when several findings point to the same boundary weakness.

## Recommendations

Recommendations must:

- link to a specific finding by ID
- be directional, not implementation-detailed
- distinguish between code changes, contract changes, and operational changes
- note when the recommendation depends on inferred evidence

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly in the deliverable:

- Fully implemented: boundaries, failure paths, or observability pieces that are complete and evidenced.
- Partially implemented: pieces that exist but are incomplete, unverified, or only present in one direction.
- Not implemented: deliberate gaps or missing contract pieces.
- Not analyzed: adjacent surfaces that were out of scope.

## Limits and Unknowns

Mandatory section. State:

- what could not be validated from the available evidence
- what requires real-world replay, load, or production-like validation
- where confidence is low because delivery semantics or ownership are unclear
- which third-party guarantees were assumed rather than verified

Do not collapse this section into a single line.

## Workflow Rules

The agent must:

- build the integration model before analysis
- distinguish observed fact from inference
- keep happy-path flow separate from failure handling
- preserve exact contract, queue, topic, endpoint, or workflow names when they matter
- merge duplicates and avoid redundant findings
- never assume exactly-once delivery unless the evidence proves it
- label evidence as `sourced`, `fallback`, or `inferred`

