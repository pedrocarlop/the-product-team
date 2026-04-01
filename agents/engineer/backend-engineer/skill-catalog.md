# Backend Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `api-implementation`

- Description: Implement or extend backend APIs to support the product behavior safely.
- Trigger: When product or platform work requires backend endpoints or handlers.
- Primary MCP/tool: repository
- Fallback: reference/trace, search_query
- Best guess: A backend API implementation or change plan.
- Output: logs/active/<project-slug>/deliverables/backend-engineer.md
- Done when: The API contract is implemented with clear behavior and constraints.

## `backend-observability`

- Description: Add or refine logging, metrics, and diagnostics around backend behavior.
- Trigger: When debugging or operations depend on better backend visibility.
- Primary MCP/tool: repository
- Fallback: search_query, reference/reuse
- Best guess: An observability change or backend diagnostics plan.
- Output: logs/active/<project-slug>/deliverables/backend-engineer.md
- Done when: Important backend behavior can be inspected after deployment.

## `backend-verify`

- Description: Verify backend behavior against the intended contract and operational risk.
- Trigger: When backend work needs a final verification pass.
- Primary MCP/tool: repository
- Fallback: reference/verify, search_query
- Best guess: A backend verification result with open risks if any.
- Output: logs/active/<project-slug>/deliverables/backend-engineer.md
- Done when: The backend behavior is validated or unresolved issues are explicit.

## `domain-model-build`

- Description: Implement the core backend domain logic and data transformations for a feature.
- Trigger: When business rules or backend state transitions must be encoded.
- Primary MCP/tool: repository
- Fallback: reference/ground, reference/trace
- Best guess: A backend domain model implementation or design.
- Output: logs/active/<project-slug>/deliverables/backend-engineer.md
- Done when: Core rules are explicit and live in a clear source of truth.

## `integration-flow-build`

- Description: Build the integration flow between internal services or external systems.
- Trigger: When data or actions must move across system boundaries.
- Primary MCP/tool: repository
- Fallback: search_query, reference/trace
- Best guess: An integration implementation or flow design.
- Output: logs/active/<project-slug>/deliverables/backend-engineer.md
- Done when: The integration path, failures, and key boundaries are explicit.
