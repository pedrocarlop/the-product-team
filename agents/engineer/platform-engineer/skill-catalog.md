# Platform Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `ci-cd-governance`

- Description: Define or improve the quality gates and governance around delivery pipelines.
- Trigger: When releases need better automation and control.
- Primary MCP/tool: repository
- Fallback: reference/reuse, search_query
- Best guess: A CI/CD governance proposal or implementation.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: Delivery rules are concrete enough to enforce repeatedly.

## `infra-release`

- Description: Plan or implement an infrastructure or platform release with operational safeguards.
- Trigger: When infra or deployment changes must be executed safely.
- Primary MCP/tool: repository
- Fallback: search_query, reference/verify
- Best guess: An infra release plan or implementation summary.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: The release path and rollback posture are explicit.

## `performance-investigation`

- Description: Diagnose a platform or system performance issue and localize the bottleneck.
- Trigger: When performance is degraded and root cause is unclear.
- Primary MCP/tool: repository
- Fallback: search_query, reference/trace
- Best guess: A performance investigation with bottleneck and next step.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: The main performance constraint is identified credibly.

## `pipeline-orchestration`

- Description: Design or improve platform pipelines and long-running processing flows.
- Trigger: When data or build pipelines need clearer orchestration.
- Primary MCP/tool: repository
- Fallback: reference/ground, search_query
- Best guess: A pipeline orchestration design or implementation.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: The sequence, retries, and ownership are explicit.

## `schema-migration`

- Description: Design and implement schema changes with migration and rollback awareness.
- Trigger: When persistent data models must change safely.
- Primary MCP/tool: repository
- Fallback: reference/trace, search_query
- Best guess: A migration plan or implementation with rollback considerations.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: Schema changes are bounded and operationally safe.

## `security-hardening`

- Description: Identify and implement a concrete security improvement or remediation.
- Trigger: When the system needs a specific security fix or hardening step.
- Primary MCP/tool: repository
- Fallback: search_query, reference/verify
- Best guess: A security hardening change or remediation plan.
- Output: logs/active/<project-slug>/deliverables/platform-engineer.md
- Done when: The security issue and fix path are explicit.
