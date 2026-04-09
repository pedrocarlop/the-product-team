# `/knowledge` — Business Intelligence (LLM Wiki)

`/knowledge` is the persistent, compounding knowledge base for the business. It aligns with the **LLM Wiki** pattern: a structured, interlinked collection of markdown files that sits between the agent and raw sources. Unlike retrieval systems that rediscover knowledge on each query, this wiki is compiled once and kept current.

Agent execution records go to `/logs`. Code outputs go to `/app`.

## Directory Layout

```text
knowledge/
  index.md                           # Content-oriented catalog (Knowledge Index)
  log.md                             # Chronological record of wiki evolution
  <role>-<skill>.md                  # Synthesized deliverables
  entities/                          # Cross-cutting entity pages (competitors, personas)
  reviews/                           # Quality assurance records
  assets/                            # Visual artifacts (screenshots, mockups)
```

## Rules for Agents

1.  **Write to `knowledge/`**: Every task produces its deliverable at `knowledge/<role>-<skill>.md`. Git provides version history — no manual snapshots needed.
2.  **Log Requirement**: Every meaningful change (ingest, query, lint) must be appended to `knowledge/log.md`.
3.  **TL;DR Sections**: Every synthesized page must include a `## TL;DR` section at the top for fast scanning.
4.  **Direct File Tools**: If specialized MCPs are missing, use direct filesystem tools (`write_to_file`) to maintain the structure.

## Operations

### Ingest
Processing a new source into the wiki. This involves reading the source, writing/updating deliverables and entity pages, and updating `index.md` and `log.md`.

### Query
Answering questions against the wiki. Agents should synthesize answers with citations. **Good answers must be filed back into the wiki** as new pages or updates to existing ones.

### Lint (Health Check)
Periodically auditing the wiki for contradictions, stale claims, orphan pages, and gaps.

## Special Files

### `index.md` — Knowledge Index

A content-oriented catalog organized by **domain**. Updated after every ingest or significant change. Enables agents to find relevant pages without scanning the entire directory.

### `log.md` — Knowledge Log

Append-only chronological record. Parseable format:
`## [YYYY-MM-DD] <type> | <description>` (e.g., `## [2026-04-05] ingest | Market Report`)

Types: `ingest`, `query`, `lint`, `created`, `updated`, `superseded`.

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

## Version History

Git is the version history for all deliverables. When an agent updates a deliverable, it writes directly to `knowledge/<deliverable>.md`. Previous versions are available through `git log` and `git diff`.

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
