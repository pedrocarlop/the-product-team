# Product Team for Codex

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
- Global fallback rule: `primary MCP -> alternative tool/MCP -> best guess inferred output`.
- Deliverables must label the actual evidence path as `sourced`, `fallback`, or `inferred`.
- Shared role deliverables use stable skill-owned anchors in the form `## Skill: <skill-name>` and one trailing `## Reflection` footer.
- For net-new design work, the design flow must diverge before it converges: explore materially different directions first, compare them explicitly, and only then move into concrete production design.
- For greenfield product work, `ui-designer` seeds `logs/active/<project-slug>/deliverables/project-ds-spec.md` from up to 3 inspiration-only company references in `.codex/product-team/references/reference-design-systems/`; `design-systems-designer` then operationalizes that shared spec for tokens, components, widget layouts, governance, and QA.
- Escalate only for setup, account access, destructive actions, or external publishing/sharing.
- Staff the minimum viable set of roles and keep one explicit repo-write owner per stage by default.
- Read installed role definitions in `.codex/agents/product-team-<discipline>/<role>/`.
- Use `.codex/product-team/references/role-catalog.md` as the canonical staffing reference.

## Verification

- Before considering any task complete, verify that all required checks and acceptance criteria are satisfied.
- Every project `context.md` must include a `Done when` section with concrete, verifiable completion criteria.
- Frontend implementation should be verified on both desktop and mobile when the scoped work affects responsive behavior.
