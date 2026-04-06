# `/knowledge` — Business Intelligence

`/knowledge` is the persistent knowledge base for the business. It accumulates across projects and is organized flat (no project slug nesting) so agents and humans can find what matters.

Agent execution records go to `/logs`. Code outputs go to `/app`.

## Wiki Model

Knowledge is a **persistent, compounding wiki** maintained by agents. Unlike retrieval systems that rediscover knowledge on each query, knowledge files are compiled once and kept current. Cross-references exist between deliverables, contradictions are flagged, and synthesis reflects everything consumed across all projects.

The orchestrator maintains the wiki structure. Specialists produce deliverables. The orchestrator indexes, cross-links, and health-checks them.

## Directory Layout

```text
knowledge/
  index.md                           # Topic-oriented catalog (maintained by orchestrator)
  log.md                             # Append-only chronological mutation log
  raw/                               # Immutable curated collection of source documents
    assets/                          # Images and visual materials
  summaries/                         # Synthesized overviews of raw documents
  concepts/                          # Deep dives into specific domain concepts
  <role>-<skill>.md                  # Latest stable deliverables
  project-ds-spec.md                 # Shared cross-role deliverables
  orchestrator.md                    # Execution manifest
  entities/                          # Cross-cutting concept pages
    <entity-type>-<name>.md          # e.g., competitor-acme.md, persona-admin.md
  reviews/
    <reviewer>.md
  runs/                              # Lossless history
    <run-id>-<YYYYMMDD-HHMM>/
      <role>-<skill>.md              # Snapshot from this run
```

## Special Files

### `index.md` — Knowledge Catalog

A content-oriented catalog organized by **domain** (not by role or date). Updated by the orchestrator after every project completion or significant knowledge change. Enables the orchestrator to find relevant knowledge without scanning every file.

Structure:

```markdown
# Knowledge Index

## Market & Product
- [analyst-market-analysis.md](analyst-market-analysis.md) — TAM/SAM for B2B analytics (2026-03)
- [product-lead-prd.md](product-lead-prd.md) — Dashboard MVP requirements

## User Research
- [ux-researcher-synthesis.md](ux-researcher-synthesis.md) — Async collaboration pain points

## Design & Visual
- [ui-designer-concept-direction.md](ui-designer-concept-direction.md) — Glassmorphic dark theme
- [project-ds-spec.md](project-ds-spec.md) — Design system specification

## Engineering & Architecture
- [backend-engineer-api-design.md](backend-engineer-api-design.md) — REST API v1

## Entities
- [entities/competitor-acme.md](entities/competitor-acme.md) — Acme Corp competitive profile
- [entities/persona-enterprise-admin.md](entities/persona-enterprise-admin.md) — Enterprise admin persona
```

The index is the **first file the orchestrator reads** when scanning knowledge for a new assignment. It replaces the need to `ls knowledge/` and read every file.

### `log.md` — Knowledge Mutation Log

Append-only chronological record of every knowledge change. Parseable format:

```markdown
# Knowledge Log

## [2026-03-15] created | 20260315-analytics-mvp | analyst-market-analysis.md | TAM/SAM analysis for B2B analytics vertical
## [2026-03-16] created | 20260315-analytics-mvp | ux-researcher-synthesis.md | Async collaboration pain point synthesis
## [2026-03-20] updated | 20260320-dashboard-v2 | analyst-market-analysis.md | Added SMB segment sizing from new survey data
## [2026-03-20] created | 20260320-dashboard-v2 | entities/competitor-acme.md | Competitive profile from market analysis + user interviews
## [2026-04-01] superseded | 20260401-rebrand | ui-designer-concept-direction.md | Visual direction replaced by rebrand initiative
```

Actions: `created`, `updated`, `superseded`, `archived`.

This lets the orchestrator quickly see what changed since the last project without re-reading every file.

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
related: [<file-paths>]
---
```

- `related` lists other knowledge files that this deliverable informs or was informed by. This creates **cross-reference trails** between deliverables. Example: a market analysis lists `related: [ui-designer-concept-direction.md, product-lead-prd.md]` because those deliverables used its findings.

Shared cross-role deliverables may use `role: shared-design` and an `owners: [<role-name>, ...]` field.

## Mandatory TL;DR (Progressive Disclosure)

Every deliverable must include a `## TL;DR` section immediately after the YAML header, before any other content. This is 1-3 sentences summarizing the key finding, decision, or output.

```markdown
---
role: analyst
project: 20260315-analytics-mvp
...
---

## TL;DR

B2B analytics TAM is $4.2B with 12% CAGR. SMB segment (60% of market) is underserved by current tools. Primary opportunity: async-first analytics with Slack integration.

## Full Analysis
...
```

The TL;DR enables the orchestrator to scan knowledge quickly during the knowledge continuity check. Read TL;DR first; read the full deliverable only when it is directly relevant to the current assignment.

## Entity Pages

For concepts that span multiple projects — competitors, user personas, design patterns, architectural decisions, market segments — create dedicated entity pages in `knowledge/entities/`.

Naming convention: `<entity-type>-<name>.md` where entity-type is one of: `competitor`, `persona`, `pattern`, `decision`, `segment`, `technology`.

Entity pages are updated by the orchestrator when relevant knowledge is discovered across projects. They aggregate findings from multiple deliverables and link back to their sources via `related`.

```yaml
---
role: orchestrator
entity_type: competitor
entity_name: acme-corp
last_updated: 2026-03-20
sources: [analyst-market-analysis.md, ux-researcher-synthesis.md]
---

## TL;DR

Acme Corp is the market leader in sync-first analytics. Weak in async workflows and SMB pricing.
```

## Lossless History Policy

When an agent "updates" a deliverable:
1. It **MUST** write the new version to `knowledge/runs/<run-id>/` first.
2. It **MAY** then update the canonical file at `knowledge/<deliverable>.md` to reflect the latest state.
3. It **MUST NOT** overwrite previous versions in the `runs/` history.
4. It **MUST** append an entry to `log.md`.

## Knowledge Continuity Rule (CRITICAL)

The orchestrator MUST read `knowledge/index.md` before every assignment. When staffing an agent, the `reads_from` field must include any knowledge files that inform the agent's work — across all projects, not just the current one.

**Scan order** (progressive disclosure):
1. Read `index.md` to identify relevant domain categories.
2. Read `log.md` tail to see recent changes.
3. Read TL;DR sections of relevant deliverables.
4. Read full deliverables only for files directly relevant to the current assignment.
5. Follow `related` links for additional context.

**Example**: A market analysis from Project A must be included in `reads_from` when staffing a UI designer for Project B's brand work. Decisions compound across projects.

## Lint (Periodic Health Check)

The orchestrator runs the `lint-knowledge` skill periodically (after every 3-5 projects, or on request) to check for:

- **Stale deliverables** — Files not referenced by any project in the last 3 months.
- **Contradictions** — Two deliverables making conflicting claims about the same topic.
- **Orphan files** — Files in `knowledge/` not listed in `index.md`.
- **Missing cross-references** — Files referenced in `reads_from` but without a corresponding `related` backlink.
- **Knowledge gaps** — Domains in `index.md` with no deliverables or only inferred-mode evidence.
- **Entity drift** — Entity pages whose `sources` list references deliverables that have been superseded.

Lint results go to `knowledge/orchestrator-lint.md`.

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
