---
name: lint-knowledge
description: Run periodic health checks on the knowledge base — detect stale files, contradictions, orphans, missing cross-references, knowledge gaps, and entity drift.
trigger: After every 3-5 projects, on explicit request, or when knowledge/index.md grows significantly.
primary_mcp: repository, knowledge files
fallback_tools: repository review
best_guess_output: A structured lint report with actionable findings per category.
output_artifacts: knowledge/orchestrator-lint.md
done_when: Every check category has run and findings are logged with severity and recommended fix.
---

# Lint Knowledge

## Purpose

Run a periodic health check on `knowledge/` to keep the wiki accurate, cross-linked, and free of drift. This skill detects six categories of problems and produces an actionable report.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header

```yaml
---
role: orchestrator
project: <slug-or-maintenance>
run_id: <run-id>
deliverable: orchestrator-lint.md
confidence: <0.0-1.0>
inputs_used: [knowledge/index.md, knowledge/changelog.md, knowledge/*.md]
evidence_mode: sourced|fallback|inferred
related: []
---
```

### Step 2: Load the Knowledge State

1. Read `knowledge/index.md` to get the full catalog of known deliverables.
2. Read the tail of `knowledge/changelog.md` (last 30 entries) to understand recent mutations.
3. List all `.md` files in `knowledge/` (top-level) and `knowledge/entities/`.
4. For each file, read the YAML frontmatter and `## TL;DR` section only.

### Step 3: Run the Six Checks

#### Check 1: Stale Deliverables

- For each deliverable in `knowledge/`, check whether it appears in any `reads_from` or `related` field of deliverables updated in the last 3 months (use `changelog.md` dates).
- Flag files with no references and no changelog activity in 3+ months.
- Severity: `warning`.

#### Check 2: Contradictions

- Compare TL;DR sections across deliverables in the same domain category (from `index.md`).
- Flag cases where two deliverables make conflicting claims about the same metric, decision, or recommendation.
- Severity: `error` (contradictions degrade downstream decisions).

#### Check 3: Orphan Files

- Compare the list of files on disk in `knowledge/` against entries in `knowledge/index.md`.
- Flag any file that exists on disk but is not listed in the index.
- Severity: `warning`.

#### Check 4: Missing Cross-References

- For each deliverable, check its `reads_from` / `inputs_used` list.
- If file A lists file B in `inputs_used`, file B should list file A in `related` (or vice versa).
- Flag missing backlinks.
- Severity: `info`.

#### Check 5: Knowledge Gaps

- Check each domain category in `index.md`.
- Flag categories with zero deliverables, or where all deliverables use `evidence_mode: inferred`.
- Severity: `warning`.

#### Check 6: Entity Drift

- For each entity page in `knowledge/entities/`, check its `sources` list.
- If any source deliverable has been superseded (per `changelog.md`), the entity page is stale.
- Flag with the superseding deliverable path.
- Severity: `warning`.

### Step 4: Produce the Lint Report

Write findings to `knowledge/orchestrator-lint.md` in this format:

```markdown
## TL;DR

<1-3 sentence summary: N errors, M warnings, P info items found.>

## Findings

### Stale Deliverables
| File | Last Referenced | Severity | Recommended Action |
|---|---|---|---|

### Contradictions
| File A | File B | Conflict | Severity | Recommended Action |
|---|---|---|---|---|

### Orphan Files
| File | Severity | Recommended Action |
|---|---|---|

### Missing Cross-References
| Source | Should Reference | Severity |
|---|---|---|

### Knowledge Gaps
| Domain | Issue | Severity |
|---|---|---|

### Entity Drift
| Entity | Stale Source | Superseded By | Severity |
|---|---|---|---|
```

If a check category has no findings, write "No issues found." under its heading.

### Step 5: Update Index and Changelog

- If new findings require index.md updates (orphan files that should be added), note them but do not auto-fix — list them as recommendations.
- Append a `lint` entry to `knowledge/changelog.md`:
  ```
  ## [YYYY-MM-DD] lint | <run-id> | orchestrator-lint.md | <summary of findings>
  ```

### Step 6: Mandatory Reflection

End the deliverable with a `## Reflection` section:
- **What worked**: checks that surfaced real issues.
- **What didn't**: checks that were inconclusive or had false positives.
- **Next steps**: specific remediation actions ranked by severity.
