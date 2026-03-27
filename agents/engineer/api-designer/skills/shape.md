---
name: shape
description: Shape API contracts so resources, endpoints, methods, and schemas are consistent, consumer-friendly, and ready for implementation.
---

# Shape

## Purpose

Use this skill to define the structure of an API contract so the first version is understandable, coherent, and easy for consumers to use without reverse engineering implementation details.

## When to Use

- When designing new endpoints, resources, or request and response schemas
- When deciding whether a capability should be modeled as REST, GraphQL, gRPC, or async events
- When endpoint naming, resource boundaries, or field structure are still open questions
- When the contract needs to be specified before any implementation work starts

## When Not to Use

- When the contract shape is already settled and the main work is versioning or documentation
- When you are only checking for breaking changes or compatibility impact
- When the task is mostly about writing OpenAPI examples, Postman collections, or catalog entries

## Required Inputs

- The consumer use case and the job the API must support
- The resources, commands, or events the API needs to expose
- Any known constraints on transport, latency, caching, or internal versus external use
- Existing naming conventions, auth patterns, and resource models the team already follows
- Any edge cases, states, or relationships that must be represented explicitly

## Workflow

1. Identify the primary consumer and the narrowest useful contract that solves the job.
2. Choose the right interaction style, then model the domain as resources, events, or operations rather than implementation steps.
3. Define endpoint names, methods, identifiers, and relationships using consistent API conventions.
4. Shape request and response schemas so required fields, optional fields, and nested objects are intentional.
5. Account for pagination, filtering, sorting, and state transitions before the shape is considered stable.
6. Check whether the contract can be implemented without hidden coupling to internal services or database structure.

## Design Principles / Evaluation Criteria

- Model nouns and durable resources, not implementation verbs
- Make consumer success the default path
- Prefer clear, explicit schemas over clever shortcuts
- Keep relationships and ownership boundaries legible
- Optimize for predictable behavior across clients and over time

## Output Contract

- Proposed endpoints, methods, and resource boundaries
- Request and response schema outline with required and optional fields
- Notes on identifiers, relationships, pagination, filtering, and state transitions
- Any unresolved modeling questions that need consumer or engineering input

## Examples

### Example 1

Input:
- Need an endpoint for a customer to submit a refund request
- The refund is a state transition, not a new resource type

Expected output:
- `PATCH /refunds/{refundId}` or `POST /refund-requests` depending on lifecycle
- A schema that includes the refund amount, reason, and status transition explicitly
- A note that the design should avoid `POST /issueRefund`

## Guardrails

- Do not hide domain decisions inside implementation details
- Do not use action names in paths when a resource model is clearer
- Do not define fields just because the backing service already has them
- Do not leave identifiers, relationships, or collection behavior implicit

## Optional Tools / Resources

- MCP: Postman MCP, GitHub MCP, Notion MCP
- Websites: [OpenAPI Specification](https://www.openapis.org/), [Swagger Docs](https://swagger.io/docs/), [Stoplight API Design Guides](https://blog.stoplight.io/), [REST API Tutorial](https://restfulapi.net/), [MDN HTTP Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- Existing OpenAPI specs or API style guides
- Consumer feedback, support tickets, or product requirements
- Domain models, event catalogs, or service boundaries
- Mock requests or example payloads from adjacent systems
