---
name: serve
description: Turn a validated model or LLM workflow into a production-ready serving path with clear latency, reliability, and rollback expectations.
activation_hints:
  - "Use after evaluation has shown a candidate is ready to be deployed."
  - "Route here when defining APIs, batching, infrastructure, or release strategy for inference."
  - "Do not use for initial problem framing or offline evaluation work."
---

# Serve

## Purpose

Use this skill to design how a model or LLM workflow is exposed to production systems, including API shape, latency budget, fallback behavior, and release mechanics.

## When to Use

- When building or changing an inference endpoint
- When deciding on batching, caching, async execution, or model versioning
- When shipping the production path for a model, retrieval layer, or prompt workflow

## When Not to Use

- When the solution has not yet been evaluated
- When the main issue is model quality rather than runtime delivery
- When the work is about post-launch drift or monitoring

## Required Inputs

- The approved model or workflow
- The serving contract and consumer requirements
- The latency target, throughput expectations, and cost budget
- Failure behavior, fallback path, and rollback trigger
- Deployment environment, dependencies, and versioning strategy
- Security, privacy, and observability requirements

## Workflow

1. Define the request and response contract for inference.
2. Set the latency, reliability, and cost budget before implementation.
3. Choose the serving pattern, including batching, caching, and async behavior where appropriate.
4. Add health checks, structured logging, and observability around input, output, and errors.
5. Define a safe fallback path and a rollback mechanism for bad releases.
6. Verify the endpoint under realistic load before handing it to consumers.

## Design Principles / Evaluation Criteria

- The serving path should be simple enough to operate under pressure
- Failures must be visible and recoverable
- Latency budgets should be measured, not assumed
- Versioning and rollback are part of the design, not optional extras
- The runtime contract should preserve the offline evaluation intent

## Output Contract

- The serving architecture and API contract
- Latency, throughput, and cost assumptions
- Fallback, rollback, and release plan
- Observability and health-check requirements
- Any deployment risks or operational constraints

## Examples

### Example 1

Input:
- Need to expose a text classifier to internal tools

Expected output:
- Serving plan: FastAPI `/predict` and `/health`, request batching if throughput requires it, model version pinning, and a fallback rule for unavailable inference

## Guardrails

- Do not ship an endpoint without a rollback path
- Do not ignore latency and cost when choosing an architecture
- Do not deploy a model whose runtime behavior differs materially from its evaluated behavior
- Do not hide errors behind silent fallback logic

## Optional Tools / Resources

- FastAPI or similar serving framework docs
- Load testing tools such as k6 or Locust
- Container build and deployment manifests
- Model registry or artifact store
