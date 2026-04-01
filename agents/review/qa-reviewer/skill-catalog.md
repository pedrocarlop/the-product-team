# QA Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `regression-triage`

- Description: Classify and prioritize regressions so the team knows what blocks release.
- Trigger: When a build or feature has defects and they need triage.
- Primary MCP/tool: repository, chrome_devtools
- Fallback: reference/verify, open
- Best guess: A regression triage with severity and release impact.
- Output: logs/active/<project-slug>/deliverables/qa-reviewer.md
- Done when: Blocking and non-blocking issues are clearly separated.

## `release-gate`

- Description: Make the final ship/no-ship recommendation based on requirements, testing, and runtime evidence.
- Trigger: When work is nearing release and needs a QA gate.
- Primary MCP/tool: repository, deliverables
- Fallback: qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review
- Best guess: A release gate recommendation with blocking issues and residual risk.
- Output: logs/active/<project-slug>/deliverables/qa-reviewer.md
- Done when: The release recommendation is unambiguous and evidence-based.

## `requirements-trace-review`

- Description: Check that the delivered work still maps to the stated requirements and constraints.
- Trigger: When implementation or design must be validated against upstream intent.
- Primary MCP/tool: repository, deliverables
- Fallback: reference/verify, open
- Best guess: A requirements trace review with gaps and mismatches.
- Output: logs/active/<project-slug>/deliverables/qa-reviewer.md
- Done when: The team knows where delivery drifted from the stated requirement.

## `runtime-network-audit`

- Description: Inspect runtime behavior, requests, failures, and visible client-server issues.
- Trigger: When release confidence depends on real runtime evidence.
- Primary MCP/tool: chrome_devtools
- Fallback: repository, reference/trace
- Best guess: A runtime and network audit with key findings.
- Output: logs/active/<project-slug>/deliverables/qa-reviewer.md
- Done when: The main runtime issues are identified and reproducible.

## `test-plan-review`

- Description: Evaluate whether the proposed testing strategy actually covers the important risks.
- Trigger: When a release or feature needs a better test strategy review.
- Primary MCP/tool: repository
- Fallback: reference/trace, search_query
- Best guess: A test plan review with risk-based recommendations.
- Output: logs/active/<project-slug>/deliverables/qa-reviewer.md
- Done when: Critical risks have a named testing approach.
