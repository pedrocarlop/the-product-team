<!-- Generated from product-team.fragment.template.md — edit the template, then run scripts/generate-fragments.sh -->
# Product Team for Antigravity

This repository has the Product Team workflow installed.

## Entry Point

- Route every request in this repository through `product-team-orchestrator` by default.
- Only bypass Product Team when the user explicitly says not to use Product Team or not to use the orchestrator for that request.
- The orchestrator may still choose direct execution for clearly single-role work, but that decision happens inside the workflow.
- Route by real job function first, then assign exact `skill_paths`.
- Do not staff a role without naming the core action it will execute.

## Workflow Rules

- On every request, the orchestrator must scan its own `skill-catalog.md`, open the matching orchestrator skills, and use them.
- Each staffed specialist must read its `skill-catalog.md`, open the assigned `skill_paths`, and execute that workflow directly.
- Every staffed assignment must define `assignment_mode`, `owned_outputs`, `reads_from`, `repo_write_owner`, `repo_write_scope`, `return_expected`, `skill_paths`, `primary_tools`, `fallback_policy`, and `evidence_mode`.
- Specialists do not ask whether to use the required MCP/tool path. They use it automatically when the skill requires it.
- **Lossless Handoff**: Prioritize fidelity over conciseness. Specialists must produce at least one standalone deliverable per assigned skill (formatted as `knowledge/<role>-<skill>.md`, with a snapshot in `knowledge/runs/<run-id>/`).
- **Execution Manifest**: The orchestrator curates a central `orchestrator.md` as an index/map of all specialist source outputs. It does not compress or summarize away their detail.
- **Direct Consumption**: Implementation owners (e.g., engineers) must read every relevant original skill output from the manifest before acting.
- **Global Fallback Rule**: `primary MCP -> alternative tool/MCP -> best guess inferred output`.
- For net-new design work, the design flow must diverge before it converges: explore materially different directions first, compare them explicitly, and only then move into concrete production design.
- **Knowledge Continuity**: Before every assignment, the orchestrator follows progressive disclosure: (1) read `knowledge/index.md` for relevant domain categories, (2) read tail of `knowledge/changelog.md` for recent changes, (3) read TL;DR sections of relevant deliverables, (4) read full files only when directly relevant, (5) follow `related` links. Include relevant files in `reads_from`. Decisions compound across projects.
- **Knowledge Wiki Maintenance**: Every knowledge mutation must append to `knowledge/changelog.md`. After project completion, the orchestrator updates `knowledge/index.md` with new deliverables. Every deliverable must include a `## TL;DR` section and a `related` field in its YAML header for cross-references. Cross-cutting concepts (competitors, personas, patterns) get dedicated entity pages in `knowledge/entities/`.
- **Output Routing**: Intelligence outputs (research, strategies, designs) go to `knowledge/`. Code outputs go to `app/`. Execution records (prompts, reasoning) go to `logs/`.
- For greenfield product work, `ui-designer` seeds `knowledge/project-ds-spec.md` from up to 3 inspiration-only company references in `.antigravity/product-team/references/reference-design-systems/`; `design-systems-designer` then operationalizes that shared spec for tokens, components, widget layouts, governance, and QA.
- When `project-ds-spec.md` recommends shadcn/ui for a blank or near-empty frontend, only the explicit engineering repo-write owner may initialize it, and the install must follow the product's recorded implementation-foundation decisions instead of generic shadcn defaults.
- Escalate only for setup, account access, destructive actions, or external publishing/sharing.
- Staff the minimum viable set of roles and keep one explicit repo-write owner per stage by default.
- Read installed role definitions in `.antigravity/agents/product-team-<discipline>/<role>/`. Each role has a `skill-catalog.md`; skills are at `.antigravity/agents/product-team-<discipline>/<role>/skills/<skill-name>.md` — construct the path, do not list the directory.
- Use `.antigravity/product-team/references/role-catalog.md` as the canonical staffing reference.

## Verification

- Before considering any task complete, verify that all required checks and acceptance criteria are satisfied.
- Every project `context.md` must include a `Done when` section with concrete, verifiable completion criteria.
- Frontend implementation should be verified on both desktop and mobile when the scoped work affects responsive behavior.
