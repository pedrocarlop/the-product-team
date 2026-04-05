# `/logs` — Execution Trail

`/logs` records what agents were asked, what they reasoned, and what decisions they made. It is the execution trail — not the output surface.

Agent deliverables (research, strategies, designs) go to `/knowledge`. Code outputs go to `/app`.

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
      runs/
        <run-id>-<YYYYMMDD-HHMM>/
          prompt.md
          trace.md
          feedback.md
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
- **trace.md**: Agent reasoning, tool usage, key decisions, and what was produced. Must reference the knowledge paths where deliverables were written.
- **feedback.md**: User feedback or review notes (when applicable).

Run logs are the execution record. They do NOT contain deliverables — those live in `/knowledge`.

## TIMELINE.md

Chronological index of all projects.

| Column | Content |
|---|---|
| Date | Project start date (YYYY-MM-DD) |
| Slug | Project slug |
| Objective | One-line goal |
| Roles | Comma-separated staffed roles |
| Status | planning / in-progress / blocked / complete / archived |

## Archive

Move projects from `active/` to `archive/` when complete, abandoned, or inactive for 30+ days. Update `context.md` before archiving.
