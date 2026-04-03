# `/logs` — Project Memory

`/logs` is the persistent memory surface for the Product Team workflow.

## Project Slug

- Format: `YYYYMMDD-<kebab-case-objective>`
- Active projects: `logs/active/<project-slug>/`
- Completed projects: `logs/archive/<project-slug>/`

## Directory Layout

```text
logs/
  TIMELINE.md
  active/
    <project-slug>/
      context.md
      deliverables/   <-- Latest stable versions
      runs/           <-- Every prompt run and phase transition
        <run-id>-<YYYYMMDD-HHMM>/
          prompt.md
          deliverables/  <-- Snapshot of outputs from this run
          feedback.md    <-- User feedback or review notes
      decisions/
  archive/
```

## context.md

One file per project. It records:

- Goal and constraints
- Done-when criteria
- Staffed roles
- Exact `skill_paths`
- Primary tools and fallback policy
- Status, blockers, and key decisions

### context.md Metadata (YAML Header)

```yaml
---
slug: <project-slug>
objective: <one-line-goal>
confidence_score: <0.0-1.0>
last_sync: <YYYY-MM-DD-HH:MM>
status: <planning|executing|blocked|complete>
current_run_id: <run-id>
---
```

## Run Logging (MANDATORY)

Every prompt execution and phase transition MUST be logged in `logs/active/<project-slug>/runs/<run-id>-<timestamp>/`.

- **prompt.md**: The exact assignment or prompt given to the agent.
- **deliverables/**: A folder containing the full content of any file created or modified during this run.
- **Feedback/Review**: If a run is a response to user feedback, include `feedback.md`.

### Lossless History Policy
When an agent "updates" a deliverable:
1. It **MUST NOT** overwrite the previous version in the `runs/` history.
2. It **SHOULD** write the new version to the current run's `deliverables/` folder.
3. It **MAY** update the canonical file in the root `deliverables/` folder to reflect the *latest* state, but only if the `runs/` history is already secured. **Preference: Agents should read from the latest run and write to a new run.**

## deliverables/

Deliverables are the primary output of staffed specialists.

When multiple skills for the same role write into one shared deliverable, each skill must own a stable anchored section in the format:

`## Skill: <skill-name>`

Each skill updates only its own anchored section and preserves the rest of the file.

### Deliverable Header (YAML)

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

Shared cross-role deliverables may use `role: shared-design` and an `owners: [<role-name>, ...]` field when the workflow intentionally routes multiple specialists into one canonical artifact such as `project-ds-spec.md`.

### Mandatory Reflection

Every deliverable must end with one trailing `## Reflection` section:

- **What worked**
- **What didn't**
- **Next steps**

For shared role deliverables, each skill should update its own subsection inside that footer:

- `### <skill-name>`
- `What worked`
- `What didn't`
- `Next steps`

For cross-role shared deliverables, define stable section ownership inside the document template itself and update only the owned sections.

## Assignment Contract

When the orchestrator staffs specialists, it assigns work with:

- `run_id`: Unique identifier for the current execution stage.
- `assignment_mode`
- `owned_outputs`
- `reads_from`
- `repo_write_owner`
- `repo_write_scope`
- `output_path`: The specific `runs/<run-id>/deliverables/` path for this run's outputs.
- `return_expected`
- `skill_paths`
- `primary_tools`
- `fallback_policy`
- `evidence_mode`

The global fallback rule is:

`primary MCP -> alternative tool/MCP -> best guess inferred output`

If a role is forced into best-guess mode, the resulting deliverable must be labeled `inferred`.

## TIMELINE.md

Chronological index of all projects.

| Column | Content |
|---|---|
| Date | Project start date (YYYY-MM-DD) |
| Slug | Project slug |
| Objective | One-line goal |
| Roles | Comma-separated staffed roles |
| Status | planning / in-progress / blocked / complete / archived |

## Repo Implementation Ownership

Staffed specialists may always write the `/logs` artifacts listed in their assignment. Repo-tracked app code is stricter:

- The orchestrator assigns repo implementation with an explicit contract.
- Only one explicit `repo_write_owner` should exist per execution stage by default.
- Parallel repo writers are allowed only when `repo_write_scope` values are explicitly disjoint.
- If a role is not the named `repo_write_owner`, it should return a mismatch note instead of editing repo-tracked files.

## Archive

Move projects from `active/` to `archive/` when complete, abandoned, or inactive for 30+ days. Update `context.md` before archiving.
