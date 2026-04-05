---
name: api-implementation
description: Implement or extend backend APIs by modeling the contract, invariants, compatibility boundaries, and verification path before changing code.
trigger: When product or platform work requires backend endpoints, handlers, RPCs, queue consumers, or service-call surfaces.
primary_mcp: repository
fallback_tools:
  - reference/trace
  - search_query
required_inputs:
  - the API surface in scope: endpoint, handler, RPC, job, queue consumer, or webhook
  - the contract reference when available: OpenAPI, AsyncAPI, protobuf, schema, spec, or ADR
  - the expected request, response, and error behavior
  - the auth, authorization, and rate-limit expectations
  - the downstream systems, data stores, or external dependencies involved
recommended_passes:
  - contract and surface model construction
  - request/response and invariant mapping
  - compatibility and rollout review
  - implementation touchpoint selection
  - runtime and contract verification
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [testcontainers]
  api_spec:
    primary: [redocly_cli, buf]
    secondary: [prism, microcks]
  api_client:
    primary: [bruno, hoppscotch]
    secondary: [postman]
  contract_testing:
    primary: [schemathesis, pact]
    secondary: [dredd]
  fallback:
    primary: [reference/trace, search_query]
tool_routing:
  - if: the contract is OpenAPI or AsyncAPI and needs linting, bundling, or drift checks
    use: [redocly_cli]
  - if: the contract is protobuf or gRPC and compatibility matters
    use: [buf]
  - if: request or response reproduction needs a git-tracked collection
    use: [bruno]
  - if: quick manual API exploration or shareable ad hoc requests are needed
    use: [hoppscotch]
  - if: the change needs spec-driven fuzzing or negative-path coverage
    use: [schemathesis]
  - if: consumer-driven compatibility is the main risk
    use: [pact]
  - if: a contract should be replayed or checked against live behavior
    use: [dredd]
  - if: dependent services, databases, or brokers need isolated verification
    use: [testcontainers]
  - if: a mock server or temporary contract endpoint is needed
    use: [prism, microcks]
  - if: only repository code and runtime logs are available
    use: [repository, logs]
  - if: primary tools are unavailable, blocked, or incomplete
    use: [reference/trace, search_query]
best_guess_output: A backend API implementation or change plan with a contract model, implementation touchpoints, compatibility notes, and verification status.
output_artifacts: knowledge/backend-engineer-api-implementation.md
done_when: The API contract is implemented with clear behavior and constraints, compatibility risks are explicit, and the contract can be verified from the deliverable and the codebase.
---

# API Implementation

## Purpose

Implement or extend backend APIs using a contract-first workflow: model the surface, state the invariants, identify compatibility risks, then change code and verify behavior against the strongest available evidence.

This skill applies backend implementation reasoning: request and response design, validation, error mapping, idempotency, auth boundaries, rollout compatibility, and runtime verification.

This skill does not decide product scope, invent unsupported endpoints, or collapse domain logic into transport concerns.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/backend-engineer-api-implementation.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: api-implementation`, include:
- `### API surface`: Define the endpoint, handler, RPC, queue consumer, or webhook surface being changed.
- `### Inputs and outputs`: Describe request inputs, response outputs, and any contract boundaries.
- `### Behavior and invariants`: Capture the intended behavior, constraints, and invariants.
- `### Error handling`: Explain expected failures, validation, and fallback behavior.
- `### Code touchpoints`: Identify the files, modules, or services involved.
- `### Rollout or compatibility notes`: Note compatibility concerns, versioning, or rollout implications.

## Required Inputs and Assumptions

Required inputs:
- The API surface in scope: endpoint, handler, RPC, job, queue consumer, or webhook
- The contract reference when available: OpenAPI, AsyncAPI, protobuf, schema, spec, or ADR
- The expected request, response, and error behavior
- Auth, authorization, and rate-limit expectations
- The downstream systems, data stores, or external dependencies involved

If any required input is missing, infer a provisional value and prefix it with `Assumed context:`.

Known vs unknown:
- Known: the codebase, existing route names, runtime logs, and any published contract artifacts
- Often unknown: edge-case validation, consumer compatibility, rollout order, and whether an apparent API behavior is intentional or accidental

Assumptions to make explicit when undeclared:
- If no contract artifact exists, infer the contract from adjacent handlers, tests, logs, and documented callers.
- If no versioning strategy is declared, assume the existing route or field names are stable unless the codebase shows otherwise.
- If no observability pattern exists, reuse the nearest existing logging and metrics convention instead of introducing a new one.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live or current runtime behavior - inspect the running API, request traces, and logs.
2. Structured system access - repository code, migrations, OpenAPI or protobuf artifacts, and runtime logs.
3. Contract and docs artifacts - API specs, ADRs, collection files, schema docs, and integration notes.
4. Request captures or screenshots - copied responses, curl output, or shared debugging artifacts.
5. Inference - derive the contract from code shape and conventions when nothing else is available.

Declare which path was used and state its limitations in the deliverable. Prefer paths 1 and 2 together when the API is reachable.

## Tool Stack

**Repository (runtime, primary):** Source of truth for routes, handlers, validation, schema definitions, tests, migrations, and call sites.

**Logs (runtime, primary):** Request traces, request IDs, error bodies, latency signals, and deployment-time behavior. Use to confirm the API behaves as expected in a live or staged environment.

**Redocly CLI (api spec, primary):** Lint, bundle, and validate OpenAPI or AsyncAPI contracts before implementation. Use to catch drift, broken refs, or undocumented changes.

**Buf (api spec, primary):** Lint, generate, and check breaking changes for protobuf and gRPC APIs. Use when the surface is schema-driven and compatibility matters.

**Bruno (api client, primary):** Git-friendly API collections for reproducible requests and responses. Use for manual reproduction and shareable request history.

**Hoppscotch (api client, secondary):** Fast interactive API exploration and shareable request captures when a lightweight UI is enough.

**Schemathesis (contract testing, primary):** Property-based testing against OpenAPI or GraphQL contracts. Use for edge-case, invalid-input, and schema-fuzz coverage.

**Pact (contract testing, primary):** Consumer-driven contract testing for service-to-service compatibility.

**Dredd (contract testing, secondary):** Validate implementation against API descriptions by replaying the spec as checks against the live service.

**Testcontainers (isolated runtime, secondary):** Spin up real dependencies in disposable containers for integration verification against databases, queues, caches, or external stubs.

**Prism and Microcks (mocking, secondary):** Mock servers and contract simulators when the implementation needs a controllable dependency boundary.

**Fallback - reference/trace + search_query:** Use when repository or runtime access is incomplete. Label all output as `fallback`.

## Tool Path

- Start with `repository`.
- OpenAPI or AsyncAPI contract needs linting, bundling, or drift checks -> use `redocly_cli`.
- Protobuf or gRPC contract needs compatibility checks -> use `buf`.
- Manual reproduction should be reproducible in git -> use `bruno`.
- Fast ad hoc request exploration or collaborative debugging is needed -> use `hoppscotch`.
- Negative-path coverage or contract fuzzing is needed -> use `schemathesis`.
- Consumer compatibility is the main risk -> use `pact`.
- The implementation must be checked against a published spec -> use `dredd`.
- Dependent services, databases, or queues need isolated verification -> use `testcontainers`.
- A mock server or replayable stub is needed -> use `prism` or `microcks`.
- Only repository code and runtime logs are available -> use `repository, logs`.
- Primary tools are unavailable or the contract is incomplete -> use `reference/trace, search_query`.
- Do not rely on a single tool. Combine contract artifacts, runtime evidence, and repro collections when the change touches a user-visible or consumer-facing API.

## Environment and Reproducibility

Record the following in the deliverable when known:
- Route, handler, RPC, or queue name
- Environment used: localhost, preview, staging, or production
- Build or commit reference
- Auth state and acting principal
- Request payloads, headers, query params, and fixtures used
- Response codes, bodies, and latency where relevant
- Upstream and downstream service versions
- Feature flags, schema versions, and migration state
- Tool versions for Redocly CLI, Buf, Bruno, Hoppscotch, Schemathesis, Pact, or Testcontainers

If any of the above is unknown, state it explicitly. Do not treat one successful request as proof across all consumers or states.

## Model Building

Before changing code, build an API contract model. No implementation conclusions may be written before the model is complete.

### API contract model

1. Surface inventory
- List every route, handler, RPC, queue consumer, webhook, or supporting background action in scope.

2. Contract map
- Record method, path or topic, auth requirements, request shape, response shape, error codes, idempotency, pagination, and rate limits.

3. Dependency map
- Identify the databases, services, caches, queues, and external APIs touched by the change.

4. Invariant map
- State the business rules, validation rules, and must-not-break behaviors that define success.

5. Compatibility map
- Capture consumer expectations, versioning assumptions, rollout order, and any backward-compatibility constraints.

6. Verification map
- Choose the runtime, spec, client, and contract checks that can actually prove the change.

If any item is missing, label it as `Assumed context:` and lower confidence on dependent conclusions.

## Workflow Notes

Follow this sequence:

1. Confirm scope and evidence sources.
- Identify the API surface, the contract artifact, and the runtime evidence available.

2. Build the contract model.
- Write the surface inventory, contract map, dependency map, invariant map, compatibility map, and verification map.

3. Trace implementation touchpoints.
- Find the handlers, services, validators, serializers, migrations, and tests that own the change.

4. Select the smallest safe implementation.
- Prefer the least invasive code path that satisfies the contract and preserves existing invariants.

5. Update spec and repro assets.
- Keep OpenAPI, protobuf, collections, mocks, and examples in sync with the implementation.

6. Verify behavior.
- Use runtime evidence, contract tests, and reproducible request captures to confirm success and failure paths.

7. Synthesize findings.
- Summarize behavior, compatibility risk, unresolved assumptions, and residual operational risk.

## Structured Findings

Every implementation gap, contract mismatch, or reusability issue discovered during the work must use this exact schema. No free-form output.

#### Finding <id>
Observation: [What was found - without interpretation]
Evidence: [Source: repository path, log line, request capture, spec artifact, or contract test]
Cause: [Why this gap or issue exists - label as inferred if not confirmed]
Impact: [What breaks or degrades if this is not addressed]
Confidence: [High / Medium / Low + rationale]

## Prioritization Logic

Prioritize findings and implementation decisions by contract risk:

1. Critical - Contract break, auth failure, data loss, idempotency bug, severe consumer regression, or compatibility break.
2. Significant - API shape or validation choice that would become a breaking change later, incomplete error mapping, or missing operational visibility.
3. Minor - Documentation gaps, non-blocking polish, or small consistency issues that do not change consumer behavior.

Do not list more than six standalone findings unless there is a clear release risk. Group low-impact issues into a `### Minor issues` block.

## Pattern Detection

After the implementation and verification pass, identify recurring backend patterns:
- Contract drift between spec, tests, and handlers
- Repeated validation or serialization gaps
- Idempotency or retry-safety weaknesses
- Versioning or compatibility mismatches
- Error-mapping inconsistencies across routes
- Boundary leakage where transport code owns business rules that should live in the domain layer

Distinguish isolated defects from system-level causes. Repeated patterns are usually the real fix target.

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- State the direction of change, not a full solution
- Acknowledge evidence limits when confidence is Medium or Low
- Avoid inventing new API primitives or compatibility guarantees without evidence

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly in the deliverable:
- Fully implemented: routes, validations, success paths, and verified consumers that are complete
- Partially implemented: states, error paths, or migrations that exist but are not fully wired or verified
- Not implemented: behaviors deliberately deferred, with the reason noted
- Not analyzed: adjacent surfaces that were out of scope, such as admin routes, background jobs, or unrelated services

## Limits and Unknowns

Mandatory section. State:
- What contract states could not be sourced from the spec or codebase
- Where contract or schema bindings could not be confirmed
- Where validation was only static and not exercised against a live runtime
- Where the API surface was designed for the current use case only and may not generalize
- Where runtime, contract, or cross-service verification was not captured
- Any framework, version, or deployment constraints that limit portability

Do not collapse this section to a single line. Unconfirmed decisions carry compounding risk in shared backend systems.

## Workflow Rules

- Build the model before analysis.
- Distinguish fact from inference.
- Merge duplicates and avoid redundant endpoint-by-endpoint repetition.
- Keep transport, domain, and integration concerns separate.
- Preserve exact route, handler, topic, and service names when they matter to downstream consumers.
- Label output as `sourced`, `fallback`, or `inferred` to match the actual evidence path.
- Use upstream wording when it reduces ambiguity for reviewers or consumers.
- Do not invent consumers, rate limits, or compatibility guarantees that are not evidenced.

