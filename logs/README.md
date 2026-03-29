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

One file per project. It records the project context in a compact form:

- **Goal**: What we're building and why
- **Constraints**: Timelines, technical limits, dependencies
- **Decisions**: Key choices made and rationale
- **Roles**: Who is working on what (when orchestrated)
- **State**: Current status (planning / in-progress / blocked / complete / archived)
- **Deliverables**: What was produced
- **Open questions**: Unresolved items

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
