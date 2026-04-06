---
name: backend-verify
description: Build a verification model for backend changes, then confirm contract, failure-path, and operational behavior against present-state evidence.
trigger: When backend work needs a final verification pass before handoff or release.
mesh:
  inputs:
    - backend-engineer:integration-flow-build
    - backend-engineer:api-implementation
  next:
    - qa-reviewer:requirements-trace-review
  context: "Final check of backend logic before QA and release gating."
primary_mcp: repository
fallback_tools:
  - reference/verify
  - search_query
required_inputs:
  - the service, endpoint, job, queue, or integration flow under verification
  - the intended contract, acceptance criteria, or release expectation
  - the implementation surface and any related tests or specs
  - available runtime evidence such as logs, traces, CI output, or deployed URLs
  - known risk areas such as auth, retries, idempotency, data integrity, or rollout constraints
recommended_passes:
  - verification model construction
  - contract and schema checks
  - failure-path and recovery checks
  - operational readiness checks
  - residual risk synthesis
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [reference/verify, open]
  contract_testing:
    primary: [schemathesis, pact]
    secondary: [dredd, microcks]
  environment_parity:
    primary: [testcontainers]
    secondary: [redocly, buf]
  observability:
    primary: [search_query]
    secondary: [open]
tool_routing:
  - if: the backend surface is described by OpenAPI or GraphQL and broad input exploration is needed
    use: [schemathesis]
  - if: consumer/provider expectations are the main risk
    use: [pact]
  - if: the API description needs a lightweight implementation check against live behavior
    use: [dredd]
  - if: the implementation needs mocks or contract tests across APIs and events
    use: [microcks]
  - if: the verification depends on real database, cache, broker, SMTP, or other infra dependencies
    use: [testcontainers]
  - if: the contract source is OpenAPI and the spec itself needs linting or bundling before verification
    use: [redocly]
  - if: the contract source is protobuf or gRPC and compatibility matters
    use: [buf]
  - if: runtime behavior, telemetry, or deployment health must be confirmed
    use: [repository, logs]
  - if: primary tools are unavailable or blocked
    use: [reference/verify, search_query]
best_guess_output: A backend verification report with contract checks, failure-path checks, operational checks, residual risk, and confidence.
output_artifacts: knowledge/backend-engineer-backend-verify.md
done_when: The team can see which backend behaviors were validated, which risks remain, and whether any unresolved issues block release.
---

# Backend Verify

## Purpose

Verify backend behavior against the intended contract and operational risk using present-state evidence first, then targeted contract-testing tools, then fallback inference only when needed.

This skill applies structured verification reasoning across implementation surfaces, schema and contract checks, negative-path behavior, and deployment readiness.

This skill does not assume a passing unit test suite proves release readiness, does not treat happy-path checks as sufficient, and does not hide unresolved risk behind generic approval language.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/backend-engineer-backend-verify.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: backend-verify`, include:
- `### Verification scope`: Define what service, endpoint, job, or flow was verified.
- `### Contract checks`: Record checks against the intended contract or spec.
- `### Failure-path checks`: Capture negative-path, validation, or recovery checks.
- `### Operational checks`: Note runtime, observability, or deployment-related checks.
- `### Findings`: Summarize the issues found or key passes.
- `### Residual risk`: State what remains unresolved or unverified.

## Required Inputs and Assumptions

Required inputs:
- The backend surface under verification: service, endpoint, job, queue consumer, webhook, or integration flow.
- The intended contract or release expectation: API spec, ticket, acceptance criteria, or prior design note.
- The implementation surface: code, tests, deployment artifact, or runtime target.
- Evidence sources available for the current state: logs, traces, CI output, API responses, or deployed environment access.
- The main risk areas: auth, validation, retries, idempotency, data integrity, observability, rollout, or backward compatibility.

If inputs are missing, infer a provisional scope and prefix it with `Assumed context:`. Lower confidence for any claim that depends on an inferred input.

Known vs unknown:
- The intended contract is often explicit in an OpenAPI file, protobuf definition, or consumer expectation, but sometimes only implicit in code and tests.
- Runtime readiness may be known from logs or deployment metadata even when the repository is incomplete.
- Operational risk often depends on environment state, feature flags, and data shape, so those must be recorded rather than assumed.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live or current implementation evidence: a running service, deployed environment, or current runtime response.
2. Structured system access: repository code, tests, CI logs, traces, metrics, database state, or deployment metadata.
3. Linked artifacts and specifications: API descriptions, consumer contracts, tickets, runbooks, or design notes.
4. Static samples: screenshots, response bodies, captured logs, or exported fixtures.
5. Inference: derive likely behavior from patterns only when no stronger evidence exists.

State which path was used and what it cannot prove. Do not present inferred behavior as confirmed behavior.

## Tool Stack

**Runtime**
- `repository`: inspect code, tests, specs, and implementation boundaries.
- `logs`: inspect runtime output, failures, and operational evidence.
- `reference/verify`: use linked verification artifacts when they are the strongest source.
- `open`: inspect static docs, specs, or captured artifacts when needed.

**Contract testing**
- `schemathesis`: property-based testing from OpenAPI or GraphQL schemas for edge cases and schema compliance.
- `pact`: consumer-driven contract testing when provider/consumer expectations must be verified explicitly.
- `dredd`: lightweight implementation checks against API descriptions, especially for OpenAPI and API Blueprint.
- `microcks`: mocks and contract testing for APIs and events when dependency simulation is needed.

**Environment parity**
- `testcontainers`: spin up real dependencies for databases, caches, queues, brokers, and other integration targets.
- `redocly`: lint or bundle OpenAPI before verification when the spec itself is part of the risk.
- `buf`: check protobuf and gRPC compatibility when schema drift is a release risk.

**Observability**
- `search_query`: look up current tool behavior, docs, or platform specifics when evidence or setup is unclear.

## Tool Routing

- If the surface is schema-driven and broad input coverage matters, start with `schemathesis`.
- If a consumer/provider contract is the key risk, use `pact` before broader runtime checks.
- If the API description should be replayed against the live service, use `dredd` as a fast implementation check.
- If dependency simulation or mocked external systems are needed, use `microcks`.
- If verification depends on real infrastructure behavior, use `testcontainers`.
- If the OpenAPI file itself is part of the failure surface, run `redocly` linting or bundling before deeper checks.
- If the contract is protobuf or gRPC, use `buf` for compatibility checks before runtime validation.
- If logs, traces, or deployment health must be confirmed, anchor on `repository` and `logs`.
- If the primary path is blocked, switch to `reference/verify` and `search_query`.

## Tool Path

- Start with `repository, logs`.
- If the surface is schema-driven and broad input coverage matters, use `schemathesis`.
- If a consumer and provider contract is the key risk, use `pact`.
- If a published spec should be replayed against the live service, use `dredd`.
- If dependency simulation or mocked external systems are needed, use `microcks`.
- If verification depends on real infrastructure behavior, use `testcontainers`.
- If the OpenAPI file or protobuf contract is part of the risk, run `redocly` or `buf` before deeper checks.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, search_query`.
- If both paths fail, produce the best-guess output described as: A backend verification report with contract checks, failure-path checks, operational checks, residual risk, and confidence.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Environment and Reproducibility

Record the following when known:
- Service name, endpoint, job name, or flow name.
- Build, commit, image tag, or deployment version.
- Environment and access state: local, CI, staging, or production-like.
- Auth state: signed in, service-to-service, unauthenticated, or mixed.
- Relevant feature flags, seed data, or time-based constraints.
- Spec version or contract version, especially for OpenAPI, GraphQL, or protobuf.
- Test harness version, container image, or dependency version when `testcontainers` or similar tooling is used.

If any of the above is unknown, state it explicitly. Do not imply emulator or test-harness behavior is equivalent to the live system unless that was validated.

## Model Building

Before evaluating results, build a verification model with these parts:

- Surface map: which service, endpoint, queue, or integration is under review.
- Contract map: request shape, response shape, status codes, events, or side effects.
- Failure map: invalid input, auth failure, dependency failure, retry, timeout, and partial success behavior.
- Operational map: logs, metrics, traces, alerts, deployment health, and rollback signals.
- Environment map: local, test, staging, or production-like differences that can change conclusions.

No judgment about pass or fail should be written before the model is complete.

## Core Method Execution

1. Define the exact scope and the source of truth for expected behavior.
2. Build the verification model from the contract, code, and runtime evidence.
3. Check contract behavior with the strongest available tool path.
4. Exercise failure paths, including validation errors, dependency failures, retries, and recovery behavior.
5. Confirm operational behavior: logs, traces, metrics, alerts, and deployment readiness.
6. **Evidentiary Eval Harness**: Run the `scripts/eval-harness.sh` script to verify tests systematically before claiming verification success. Output must be exit code 0.
7. Compare observed behavior to expected behavior and separate confirmed findings from inferred concerns.
8. Group repeated issues into patterns and state the residual risk clearly.

## Workflow Notes

- Tie every verification claim to present-state evidence.
- Keep happy-path checks separate from failure-path and operational readiness checks.
- Make residual risk explicit so reviewers do not mistake partial coverage for approval.
- Prefer the strongest available evidence path before falling back to inference.
- Separate contract correctness from deployment health even when both are being assessed.

## Structured Findings

Every finding must use this exact schema. No free-form findings.

```text
#### Finding <id>
Observation: [What was seen, without interpretation]
Evidence: [Tool used + scope + reference, log, or repro anchor]
Repro steps: [Exact steps to reproduce the behavior]
Cause: [Why this issue likely exists; label as inferred if not confirmed]
Impact: [Effect on correctness, safety, operability, or release readiness]
Confidence: [High / Medium / Low + rationale]
```

## Prioritization Logic

Prioritize findings by release impact:

1. Critical: contract breakage, data loss, unsafe side effects, auth bypass, or missing operational visibility for a release-blocking path.
2. Significant: partial contract mismatch, weak failure handling, missing retries or compensation, degraded operability, or unclear compatibility risk.
3. Minor: polish issues, small observability gaps, or edge-case notes that do not block delivery.

Group minor issues into one block when they share the same cause. Do not inflate issue count by splitting duplicates.

## Pattern Detection

Identify recurring patterns such as:

- The same contract drift across multiple endpoints or consumers.
- Happy-path validation without negative-path coverage.
- Retry or idempotency issues that repeat across integrations.
- Missing telemetry that prevents debugging or release confidence.
- Environment-specific divergence that indicates setup or dependency drift.

Patterns matter when they show a system-level verification gap rather than a one-off defect.

## Recommendations

Recommendations must:

- Link to a specific finding by ID.
- Be directional, not a full implementation plan.
- Note when the confidence is limited by inference or missing evidence.

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly:

- Fully verified: checks that were confirmed by strong evidence.
- Partially verified: checks that were only confirmed on a subset of the intended scope.
- Not verified: important behaviors that were not exercised.
- Not analyzed: adjacent surfaces or dependencies outside the current verification scope.

Keep this map honest. Coverage gaps are part of the result, not an error to hide.

## Limits and Unknowns

Mandatory section. State:

- What could not be validated from the available evidence.
- What requires real-world validation before release.
- Where confidence is low and why.
- Which dependencies, environments, or data states were not exercised.
- Which contract assumptions came from inference rather than direct proof.

## Workflow Rules

- Build the verification model before analysis.
- Separate observed fact from interpretation.
- Tie each claim to a source of truth.
- Merge duplicate issues and avoid redundant findings.
- Label evidence as `sourced`, `fallback`, or `inferred`.
- Keep the output concise enough to support release decisions.

