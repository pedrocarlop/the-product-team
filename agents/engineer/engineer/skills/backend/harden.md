---
name: harden
description: Strengthen backend services for data integrity, concurrency safety, operational resilience, and incident readiness before they handle production traffic.
---

# Harden

## Purpose

Use this skill to make backend services safe to run under production load — handling concurrency hazards, data integrity risks, dependency failures, and operational blind spots that only surface at scale or under stress.

## When to Use

- Before releasing a service that writes to shared state, processes payments, or manages authorization
- When a code path involves retries, queues, or external service calls that can fail or duplicate
- When the service needs rate limiting, backpressure, or circuit breakers to survive dependency failures
- When incident response depends on observability that has not been wired yet

## When Not to Use

- When the service design is still being shaped
- When the work is frontend or client-side code
- When the task is pure feature development with no production-readiness concern

## Required Inputs

- The service or code path being hardened
- The risk surface: data mutations, authorization boundaries, external integrations, async processing
- Concurrency model: shared state, locking strategy, idempotency requirements
- Dependency map: databases, queues, caches, third-party APIs, and their failure modes
- Team standards for secrets management, logging levels, and alerting thresholds

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Trace the code path for data integrity risks: race conditions, partial writes, missing transactions, and unguarded upserts.
2. Verify idempotency for any operation that can be retried by clients, queues, or infrastructure.
3. Add resilience controls for external dependencies: timeouts, circuit breakers, backoff, and fallback behavior.
4. Check authorization at every trust boundary — not just the API edge, but internal service calls and queue consumers.
5. Wire observability: structured logs at decision points, metrics for latency and error rates, alerts for anomalous behavior.
6. Confirm deployment safety: migration ordering, feature flags, rollback steps, and health-check endpoints.
7. Validate that the hardening does not change the service contract or introduce performance regressions.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Data integrity comes first — a correct slow path beats a fast corrupt one
- Every side effect must be idempotent or explicitly documented as non-idempotent
- Dependency failures should be contained, not cascaded
- Authorization must be enforced at trust boundaries, not assumed from context
- The service should be operable by someone who did not write it

## Output Contract

- A hardening review covering data integrity, concurrency, resilience, auth, and observability
- Specific fixes applied or recommended, with severity and rationale
- Residual risks that require follow-up or monitoring
- Confirmation of deployment safety and rollback path

## Examples

### Example 1

Input:
- Service: Payment processing worker consuming from a message queue
- Risk: Duplicate messages could trigger double charges

Expected output:
- Add idempotency key check before processing each message
- Add dead-letter queue routing for messages that fail after max retries
- Wire alerts for duplicate-detection rate and processing latency
- Document the manual replay procedure for stuck messages

## Guardrails

- Do not treat hardening as optional when the service touches money, PII, or authorization
- Do not add retry logic without idempotency protection
- Do not ship services without health checks, structured logging, and alerting
- Do not assume infrastructure retries are safe without verifying side-effect behavior

## Optional Tools / Resources

- Load testing and chaos engineering tools
- APM and observability platforms (Datadog, Grafana, PagerDuty)
- Database migration tooling and schema versioning
- Incident runbooks and post-mortem templates
