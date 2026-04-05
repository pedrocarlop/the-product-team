# `/knowledge` — Business Intelligence

`/knowledge` is the persistent knowledge base for the business. It accumulates across projects and is organized flat (no project slug nesting) so agents and humans can find what matters.

Agent execution records go to `/logs`. Code outputs go to `/app`.

## Directory Layout

```text
knowledge/
  <role>-<skill>.md              # Latest stable deliverables
  project-ds-spec.md             # Shared cross-role deliverables
  orchestrator.md                # Execution manifest
  reviews/
    <reviewer>.md
  assets/                        # Visual artifacts (screenshots, mockups)
  runs/                          # Lossless history
    <run-id>-<YYYYMMDD-HHMM>/
      <role>-<skill>.md          # Snapshot from this run
```

## Deliverable Header (YAML)

Every deliverable file must begin with:

```yaml
---
role: <role-name>
project: <slug>
run_id: <run-id>
deliverable: <file-basename>
confidence: <0.0-1.0>
inputs_used: [<file-paths>]
evidence_mode: <sourced|fallback|inferred>
---
```

Shared cross-role deliverables may use `role: shared-design` and an `owners: [<role-name>, ...]` field.

## Lossless History Policy

When an agent "updates" a deliverable:
1. It **MUST** write the new version to `knowledge/runs/<run-id>/` first.
2. It **MAY** then update the canonical file at `knowledge/<deliverable>.md` to reflect the latest state.
3. It **MUST NOT** overwrite previous versions in the `runs/` history.

## Knowledge Continuity Rule (CRITICAL)

The orchestrator MUST scan `knowledge/` for relevant prior deliverables before every assignment. When staffing an agent, the `reads_from` field must include any knowledge files that inform the agent's work — across all projects, not just the current one.

**Example**: A market analysis from Project A must be included in `reads_from` when staffing a UI designer for Project B's brand work. Decisions compound across projects.

## Mandatory Reflection

Every deliverable must end with one trailing `## Reflection` section:

- **What worked**
- **What didn't**
- **Next steps**

For shared role deliverables, each skill should update its own subsection: `### <skill-name>`

## Deliverable Ownership

Each specialist role writes to:
```
knowledge/<role>-<skill>.md
```

When multiple skills for the same role write into one shared deliverable, each skill must own a stable anchored section: `## Skill: <skill-name>`

## Assignment Contract

When the orchestrator staffs specialists, it assigns work with:

- `run_id`: Unique identifier for the current execution stage.
- `assignment_mode`
- `owned_outputs`: Paths in `knowledge/` this agent will write.
- `reads_from`: Paths in `knowledge/` this agent must read (including relevant prior knowledge from past projects).
- `repo_write_owner`
- `repo_write_scope`: Path in `app/` for code outputs (engineers only).
- `return_expected`
- `skill_paths`
- `primary_tools`
- `fallback_policy`
- `evidence_mode`

The global fallback rule is:

`primary MCP -> alternative tool/MCP -> best guess inferred output`

If a role is forced into best-guess mode, the resulting deliverable must be labeled `inferred`.
