---
name: observe
description: Verify backend code behavior using tests, logs, query inspection, traces, and profiling to confirm correctness and performance after implementation.
---

# Observe

## Purpose

Use this skill to confirm that a backend code change behaves correctly and performs acceptably by exercising the code path with representative input and inspecting the observable evidence.

## When to Use

- After implementing a backend change that needs correctness or performance validation
- When adding or verifying logging, metrics, or tracing instrumentation in application code
- When diagnosing an unexpected bug, slow query, N+1 pattern, or data inconsistency
- When verifying that a new endpoint, worker, or data pipeline produces the expected results

## When Not to Use

- When no code exists yet and the right next step is modeling or design
- When the task is primarily infrastructure health, scaling, or deployment verification (route to DevOps)
- When the problem is already solved and only documentation needs updating

## Required Inputs

- The code path, endpoint, worker, queue, or query to verify
- The expected correct output for representative inputs
- The expected performance characteristics: query count, response time, memory usage
- The observability tools available: test runner, logging framework, query explain, profiler
- Any data fixtures or staging environment needed for realistic testing

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

1. Identify the specific proof needed: correctness evidence, performance measurement, or both.
2. Exercise the code path with representative and edge-case inputs, capturing all observable signals.
3. Inspect query behavior: check for N+1 patterns, missing indexes, unnecessary joins, and excessive row scans using EXPLAIN or query logs.
4. Verify that application logs are structured, include correlation IDs, and do not leak sensitive data.
5. Profile performance-sensitive paths with realistic data volume, not just trivial test fixtures.
6. Compare observed behavior against expected behavior and document any discrepancies.
7. Turn findings into actionable follow-ups: code fixes, index additions, log improvements, or test additions.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Correctness proof should come from executing the real code path, not just reasoning about it
- Query performance claims must be backed by EXPLAIN output or profiling data, not assumptions
- Structured logging with correlation IDs is a code quality requirement, not an infrastructure concern
- Missing test coverage for a new code path is a delivery risk
- Performance validation must use realistic data volume; toy fixtures hide real problems

## Output Contract

- A verification summary with the evidence gathered for each code path tested
- Query inspection results: EXPLAIN output, query count, and any problematic patterns found
- Log quality assessment: structure, correlation ID presence, sensitive data absence
- Performance measurements for latency-sensitive or data-heavy paths
- A clear pass/fail statement for correctness and performance
- Follow-up items: code fixes, missing tests, index recommendations, or instrumentation gaps

## Examples

### Example 1

Input:
- Task: Verify a new list endpoint that joins orders with customer data
- Concern: May have an N+1 query pattern and lacks request tracing

Expected output:
- Run the endpoint with 100 representative records and capture query log
- EXPLAIN output showing the join strategy and index usage
- Finding: N+1 detected; 101 queries instead of 2. Recommend eager loading or a JOIN refactor.
- Log check: Structured JSON logs present but missing request correlation ID
- Follow-up: Add correlation ID middleware; refactor query to use JOIN; add integration test for the list endpoint with >50 records

## Guardrails

- Do not treat passing unit tests as sufficient when queries, integrations, or external calls changed
- Do not claim performance is acceptable without measuring it with realistic data
- Do not skip query inspection when the code path involves database reads or writes
- Do not expose secrets, PII, or credentials in logs, traces, or test output
- Do not assume the happy path is the only path that needs verification

## Optional Tools / Resources

- Test runner and fixture data for the application
- Database query EXPLAIN and slow query log tools
- Application profiler for CPU and memory hotspots
- Logging framework documentation and structured log conventions
- APM or tracing tools for request-level visibility
- Incident notes or prior debugging history for the affected code area
