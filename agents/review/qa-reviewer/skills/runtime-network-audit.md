---
name: runtime-network-audit
description: Inspect runtime behavior as a system of flows, requests, failures, and observability gaps rather than isolated console messages.
trigger: When release confidence depends on real runtime evidence.
primary_mcp: chrome_devtools
fallback_tools: repository, reference/trace
best_guess_output: A runtime and network audit with key findings.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
section_anchor: "## Skill: runtime-network-audit"
done_when: The main runtime issues are identified with reproducible evidence, request context, and remaining observability gaps.
---

# Runtime Network Audit

## Purpose

Inspect runtime behavior as a system of flows, requests, failures, and observability gaps rather than isolated console messages.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: runtime-network-audit`, include:
- `### Review framing`: Define the environment, flow, and runtime conditions inspected.
- `### Runtime scope and environment`: Record device assumptions, auth state, data state, feature flags, and any setup needed for reproduction.
- `### Runtime flow map`: Summarize the key user or system flows executed during the audit.
- `### Request and dependency graph`: Capture important requests, downstream dependencies, statuses, retries, and sequence relationships.
- `### Failures and anomalies`: Record visible failures, degraded behavior, slow paths, or suspicious request patterns.
- `### Reproduction evidence`: Provide the exact steps, request context, and evidence needed to reproduce each confirmed issue.
- `### Observability gaps`: Note missing logs, opaque errors, hidden retries, or unclear dependency boundaries that made diagnosis harder.
- `### Priority risks`: Highlight the runtime issues with the highest user or release impact.
- `### Limits and unknowns`: Explain what could not be observed directly or reproduced reliably.

## Tool Path

- Start with `chrome_devtools`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository, reference/trace`.
- If both paths fail, produce the best-guess output described as: A runtime and network audit with key findings.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Audit by flow first and by request second so the network evidence stays connected to user-visible behavior.
- Capture dependency chains, not just failing requests in isolation.
- Distinguish confirmed runtime failures from suspicious but unresolved anomalies.
- Treat missing observability as a real QA finding when it blocks reliable diagnosis or release confidence.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/qa-reviewer.md`.
- Keep all work for this skill inside `## Skill: runtime-network-audit`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The main runtime issues are identified with reproducible evidence, request context, and remaining observability gaps.
