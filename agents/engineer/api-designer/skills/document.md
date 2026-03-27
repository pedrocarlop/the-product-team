---
name: document
description: Document API contracts clearly in OpenAPI, examples, and supporting artifacts so consumers can understand and use the interface without extra explanation.
activation_hints:
  - "Use when the contract is ready to be written down for consumers."
  - "Route here for OpenAPI docs, examples, Postman collections, and catalog entries."
  - "Do not use for the first-pass modeling of the API shape."
---

# Document

## Purpose

Use this skill to turn an agreed API design into clear documentation that consumers can follow, test, and compare against implementation.

## When to Use

- When writing or updating OpenAPI documents
- When adding request and response examples
- When publishing API descriptions, changelogs, or consumer handoff notes
- When the design needs to be discoverable in a catalog or shared reference

## When Not to Use

- When the contract itself is still undecided
- When the task is only to validate or critique a draft design
- When the work is mainly about breaking-change policy or versioning strategy

## Required Inputs

- The approved contract shape and behavior
- The audience for the documentation
- Required examples, edge cases, and error scenarios
- Any naming conventions, style rules, or catalog standards to follow
- Related versions, deprecation notes, or migration guidance

## Workflow

1. Translate the contract into the documentation format consumers are expected to use.
2. Include examples that show both the happy path and meaningful failure cases.
3. Make sure the documented behavior matches the approved contract exactly.
4. Document versioning, pagination, auth, error shapes, and any other consumer-facing rules explicitly.
5. Add notes that help consumers understand what the API is for and what it is not for.
6. Check that the finished docs are easy to scan, compare, and reference during implementation.

## Design Principles / Evaluation Criteria

- Documentation should reduce questions, not create them
- Examples should reflect real consumer flows
- The spec is part of the contract, not an afterthought
- Good docs make edge cases visible instead of hiding them
- Consumers should be able to implement from the docs alone

## Output Contract

- Completed OpenAPI or equivalent contract documentation
- Example payloads for success and failure cases
- Version, deprecation, and migration notes where needed
- Supporting references that help consumers find the right contract quickly

## Examples

### Example 1

Input:
- Document a `GET /orders` endpoint with pagination and rate limiting

Expected output:
- OpenAPI entry with query parameters, response schema, and pagination metadata
- Example responses for both a normal page and an empty page
- Notes on rate limit behavior and error responses

## Guardrails

- Do not document behavior that the contract does not guarantee
- Do not leave key consumer rules buried in prose only
- Do not omit failure examples when they matter for implementation
- Do not let the docs drift away from the approved shape

## Optional Tools / Resources

- OpenAPI editor or generator
- Postman collection or request examples
- API catalog, changelog, or migration guide
- Consumer feedback or implementation notes
