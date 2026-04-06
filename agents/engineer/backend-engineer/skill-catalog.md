# Backend Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `api-design`

- Description: REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.
- Trigger: Missing trigger.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: Missing best_guess_output.
- Output: Missing output_artifacts.
- Done when: Missing done_when.

## `api-implementation`

- Description: Implement or extend backend APIs by modeling the contract, invariants, compatibility boundaries, and verification path before changing code.
- Trigger: When product or platform work requires backend endpoints, handlers, RPCs, queue consumers, or service-call surfaces.
- Primary MCP/tool: repository
- Fallback: reference/trace, search_query
- Best guess: A backend API implementation or change plan with a contract model, implementation touchpoints, compatibility notes, and verification status.
- Output: knowledge/backend-engineer-api-implementation.md
- Done when: The API contract is implemented with clear behavior and constraints, compatibility risks are explicit, and the contract can be verified from the deliverable and the codebase.

## `backend-observability`

- Description: Add or refine backend telemetry by building a signal model first, then using logs, traces, metrics, and error data to expose actionable operational insight with explicit cost and privacy tradeoffs.
- Trigger: When debugging or operations depend on better backend visibility.
- Primary MCP/tool: repository
- Fallback: search_query, reference/reuse
- Best guess: An observability change or backend diagnostics plan with a signal model, instrumentation inventory, verification notes, and explicit residual risk.
- Output: knowledge/backend-engineer-backend-observability.md
- Done when: Important backend behavior can be inspected after deployment by the intended operators, with the signal path, consumers, and remaining blind spots documented.

## `backend-verify`

- Description: Build a verification model for backend changes, then confirm contract, failure-path, and operational behavior against present-state evidence.
- Trigger: When backend work needs a final verification pass before handoff or release.
- Primary MCP/tool: repository
- Fallback: reference/verify, search_query
- Best guess: A backend verification report with contract checks, failure-path checks, operational checks, residual risk, and confidence.
- Output: knowledge/backend-engineer-backend-verify.md
- Done when: The team can see which backend behaviors were validated, which risks remain, and whether any unresolved issues block release.

## `domain-model-build`

- Description: Model backend entities, invariants, state transitions, persistence boundaries, and transformation rules before implementing or changing domain behavior.
- Trigger: When business rules, lifecycle changes, authorization relationships, or backend data transformations must be encoded.
- Primary MCP/tool: repository
- Fallback: reference/ground, reference/trace
- Best guess: A backend domain model implementation or design with explicit entities, rules, transitions, transformations, and open risks.
- Output: knowledge/backend-engineer-domain-model-build.md
- Done when: Core rules are explicit, mapped to a clear source of truth, and any unresolved ambiguities, edge cases, or data-shape risks are documented.

## `integration-flow-build`

- Description: Build integration flows by modeling cross-system boundaries first, then validating contracts, timing, retries, idempotency, compensations, observability, and rollout risk.
- Trigger: When data or actions must move across system boundaries, especially through APIs, queues, webhooks, brokers, or long-running workflows.
- Primary MCP/tool: repository
- Fallback: reference/trace, search_query
- Best guess: An integration implementation or flow design with explicit contracts, retries, failure handling, and boundary notes.
- Output: knowledge/backend-engineer-integration-flow-build.md
- Done when: The integration path, contract boundaries, retries, idempotency, compensations, observability, and rollout constraints are explicit enough to implement and verify.

## `tdd-workflow`

- Description: Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration, and E2E tests.
- Trigger: Missing trigger.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: Missing best_guess_output.
- Output: Missing output_artifacts.
- Done when: Missing done_when.
