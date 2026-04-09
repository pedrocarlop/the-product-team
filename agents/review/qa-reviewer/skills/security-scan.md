---
name: security-scan
description: Inspects code changes and configuration for vulnerabilities, hardcoded secrets, and permission regressions before release.
trigger: Before a release gate, or when explicitly asked to verify the security posture of an implementation.
primary_mcp: repository
fallback_tools: reference/ground
best_guess_output: A QA security triage report identifying vulnerabilities or granting passage.
output_artifacts: knowledge/qa-security-scan.md
done_when: All changed files within the release scope have been audited against basic security constraints.
---

# Security Scan

## Purpose

To mimic a proactive security audit (inspired by AgentShield principles). This skill ensures that newly implemented code doesn't introduce common vulnerabilities such as hardcoded credentials, overly permissive configurations, or injection vectors.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: qa-reviewer
project: <slug>
deliverable: qa-security-scan.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
evidence_mode: sourced|fallback|inferred
---
```

### Step 2: Confirm Trigger And Inputs
- Restate the task: Identify vulnerabilities in the current codebase or release scope.
- Enumerate the files that are marked for release (read from the `execution-manifest` if provided by the orchestrator).

### Step 3: Model Building (Threat Surface)
Before analyzing, construct a threat model based on the components:
- Does this code touch a database? -> Look for SQLi or loose ORM bindings.
- Does this code involve authentication? -> Look for hardcoded tokens, secret leakages, or missing auth checks.
- Does this code accept user input? -> Look for XSS, path traversal, and command injection.

### Step 4: Run The Tool Sequence
- Use `repository` tools or grep to search for typical red flags:
  - `grep -r "password ="` or `API_KEY`
  - Ensure `.env` is ignored by `.gitignore`.
  - Check for open CORS configurations or overly permissive IAM/role rules.

### Step 5: Structured Findings
Output the findings using a strict schema:

#### Finding 1: [Short Title]
- **Observation:** [What was found]
- **Location:** [File path and line number]
- **Cause:** [Why this is insecure]
- **Impact:** [Low/Medium/High/Critical]
- **Recommendation:** [How to fix it]

### Step 6: Prioritization Logic
- Critical/High: Block the release gate immediately.
- Medium/Low: Note them as warnings and proceed to the next reviewer if needed, but advise a follow-up ticket.

### Step 7: Limits and Unknowns
- State explicitly that this is a static review and does not replace dynamic application security testing (DAST) or a penetration test.

### Step 8: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: Successful detection paths.
- **What didn't**: Potential false positives.
- **Next steps**: What the `backend-engineer` or `platform-engineer` needs to do to fix the blocked items.
