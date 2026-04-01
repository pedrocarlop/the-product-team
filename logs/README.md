# `/logs` — Project Memory

`/logs` is the persistent memory surface for the product team workflow.

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
      deliverables/
      decisions/
  archive/
```

## context.md

One file per project. It records the project context in a structured form:

- **Goal**: What we're building and why
- **Constraints**: Timelines, technical limits, dependencies
- **Decisions**: Key choices made and rationale
- **Roles**: Who is working on what (when orchestrated)
- **State**: Current status (planning / in-progress / blocked / complete / archived)
- **Deliverables**: Detailed list of outputs with linked paths
- **Open questions**: Unresolved items

### context.md Metadata (YAML Header)
Each `context.md` must start with a YAML block for programmatic verification:
```yaml
---
slug: <project-slug>
objective: <one-line-goal>
confidence_score: <0.0-1.0>
last_sync: <YYYY-MM-DD-HH:MM>
status: <planning|executing|blocked|complete>
---
```

## deliverables/

Deliverables are the primary output of specialists. They must follow a structured **"Artifact Handshake"** format.

### Deliverable Header (YAML)
Every deliverable file (`logs/active/<slug>/deliverables/*.md`) must begin with:
```yaml
---
role: <role-name>
project: <slug>
deliverable: <file-basename>
confidence: <0.0-1.0>
inputs_used: [<file-paths>]
---
```

### Mandatory Reflection
Every deliverable must end with a `## Reflection` section where the executor self-critiques the result:
- **What worked**: Successful implementation details.
- **What didn't**: Trade-offs, shortcuts, or known limitations.
- **Next steps**: Specific guidance for downstream roles (e.g., "Reviewer should check the X module specifically for Y").

Keep it concise. This is a continuity reference, not a process artifact.

## TIMELINE.md

Chronological index of all projects. Newest entries at the bottom.

| Column | Content |
|---|---|
| Date | Project start date (YYYY-MM-DD) |
| Slug | Project slug, linked to the project folder |
| Objective | One-line project goal |
| Roles | Comma-separated list of staffed roles |
| Status | planning / in-progress / blocked / complete / archived |

## Orchestration

Routing, staffing, planning, and approval happen in the context window. The orchestrator does not need separate files for those steps. Persist only project context and deliverables.

## Archive

Move projects from `active/` to `archive/` when complete, abandoned, or inactive for 30+ days. Update `context.md` state before archiving.
