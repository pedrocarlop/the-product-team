# QA Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `git-workflow`

- Description: Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes.
- Trigger: Missing trigger.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: Missing best_guess_output.
- Output: Missing output_artifacts.
- Done when: Missing done_when.

## `regression-triage`

- Description: Triage regressions by building a regression model, validating reproduction status, and separating user impact, scope, evidence strength, and release impact instead of collapsing them into raw bug counts.
- Trigger: When a build, feature, or release candidate has defects and the team needs a structured blocking versus non-blocking decision.
- Primary MCP/tool: repository, chrome_devtools
- Fallback: reference/verify, open
- Best guess: A regression triage with evidence-tagged severity, blocking status, and next-action routing.
- Output: knowledge/reviews/qa-reviewer.md
- Done when: Blocking and non-blocking regressions are clearly separated with evidence, rationale, confidence, and next action, and duplicate or systemic issues are grouped instead of counted loosely.

## `release-gate`

- Description: Make a release recommendation by building a release-readiness model and weighing blockers, residual risk, evidence quality, rollback posture, and operating readiness instead of treating test completion as automatic safety.
- Trigger: When work is nearing release and needs a structured ship, conditional-ship, or no-ship QA gate.
- Primary MCP/tool: repository, logs
- Fallback: qa-reviewer/runtime-network-audit, qa-reviewer/test-plan-review
- Best guess: A release gate recommendation with blocking issues, residual risk, and explicit confidence.
- Output: knowledge/reviews/qa-reviewer.md
- Done when: The release recommendation is unambiguous, evidence-based, explicit about residual risk, and clear about what must happen before or after ship.

## `requirements-trace-review`

- Description: Trace delivered behavior back to stated requirements and constraints by building a requirement model and an evidence matrix that separates confirmed matches, gaps, ambiguities, and unverified assumptions.
- Trigger: When implementation, design, or release readiness must be validated against upstream requirements, acceptance criteria, or policy constraints.
- Primary MCP/tool: repository, logs
- Fallback: reference/verify, open
- Best guess: A requirements trace review with explicit matches, gaps, ambiguities, and unverified areas.
- Output: knowledge/reviews/qa-reviewer.md
- Done when: The team can see where delivery matches intent, where it drifts, which constraints are unverified, and which gaps matter most for sign-off or release.

## `runtime-network-audit`

- Description: Audit runtime behavior by building a flow-and-dependency model first, then tracing requests, failures, degraded states, and observability gaps across the strongest available runtime evidence path.
- Trigger: When release confidence, incident triage, or QA sign-off depends on real runtime and network evidence rather than static reasoning.
- Primary MCP/tool: chrome_devtools
- Fallback: repository, reference/trace
- Best guess: A runtime and network audit with evidence-tagged failures, dependency context, and observability gaps.
- Output: knowledge/reviews/qa-reviewer.md
- Done when: The main runtime issues are identified with reproducible evidence, request context, dependency mapping, and explicit limits on what could not be observed directly.

## `security-scan`

- Description: Inspects code changes and configuration for vulnerabilities, hardcoded secrets, and permission regressions before release.
- Trigger: Before a release gate, or when explicitly asked to verify the security posture of an implementation.
- Primary MCP/tool: repository
- Fallback: reference/ground
- Best guess: A QA security triage report identifying vulnerabilities or granting passage.
- Output: knowledge/runs/<run-id>/qa-security-scan.md
- Done when: All changed files within the release scope have been audited against basic security constraints.

## `test-plan-review`

- Description: Review a test strategy by building a risk model and a coverage matrix that separates missing coverage, shallow coverage, environment blind spots, and residual uncertainty instead of treating test type counts as adequacy.
- Trigger: When a feature, milestone, or release needs a structured review of whether the proposed test plan covers the real risks.
- Primary MCP/tool: repository, logs
- Fallback: reference/trace, search_query
- Best guess: A test plan review with explicit risk coverage, gaps, and priority recommendations.
- Output: knowledge/reviews/qa-reviewer.md
- Done when: Critical risks have explicit coverage mapping, missing depth is visible, blind spots are named, and the highest-value additions are prioritized.
