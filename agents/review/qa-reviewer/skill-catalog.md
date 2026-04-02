# QA Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `regression-triage`

- Description: Triage regressions using reproducibility, user impact, scope, and release impact instead of raw issue counts.
- Trigger: When a build or feature has defects and they need triage.
- Primary MCP/tool: repository, chrome_devtools
- Fallback: reference/verify, open
- Best guess: A regression triage with severity and release impact.
- Output: logs/active/<project-slug>/reviews/qa-reviewer.md
- Done when: Blocking and non-blocking regressions are clearly separated with rationale, confidence, and next action.

## `release-gate`

- Description: Make the ship or no-ship recommendation by weighing blockers, residual risk, evidence quality, and rollback posture.
- Trigger: When work is nearing release and needs a QA gate.
- Primary MCP/tool: repository, logs
- Fallback: qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review
- Best guess: A release gate recommendation with blocking issues and residual risk.
- Output: logs/active/<project-slug>/reviews/qa-reviewer.md
- Done when: The release recommendation is unambiguous, evidence-based, and explicit about residual risk.

## `requirements-trace-review`

- Description: Trace delivered behavior back to stated requirements, surfaces, and constraints using an explicit evidence matrix.
- Trigger: When implementation or design must be validated against upstream intent.
- Primary MCP/tool: repository, logs
- Fallback: reference/verify, open
- Best guess: A requirements trace review with gaps and mismatches.
- Output: logs/active/<project-slug>/reviews/qa-reviewer.md
- Done when: The team knows where delivery matches intent, where it drifts, and which gaps remain unverified.

## `runtime-network-audit`

- Description: Inspect runtime behavior as a system of flows, requests, failures, and observability gaps rather than isolated console messages.
- Trigger: When release confidence depends on real runtime evidence.
- Primary MCP/tool: chrome_devtools
- Fallback: repository, reference/trace
- Best guess: A runtime and network audit with key findings.
- Output: logs/active/<project-slug>/reviews/qa-reviewer.md
- Done when: The main runtime issues are identified with reproducible evidence, request context, and remaining observability gaps.

## `test-plan-review`

- Description: Review the proposed test strategy as risk coverage, not as a checklist of generic test types.
- Trigger: When a release or feature needs a better test strategy review.
- Primary MCP/tool: repository, logs
- Fallback: reference/trace, search_query
- Best guess: A test plan review with risk-based recommendations.
- Output: logs/active/<project-slug>/reviews/qa-reviewer.md
- Done when: Critical risks have explicit coverage, missing depth is visible, and blind spots are named.
