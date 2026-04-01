---
name: threat-model
description: Map attack surface, trust boundaries, and realistic threats before implementation so security decisions are explicit instead of implicit.
---

# Threat Model

## Purpose

Use this skill to identify what can go wrong before code is written or while the design is still cheap to change. A good threat model clarifies what is protected, who can attack it, where trust boundaries exist, and which mitigations are required versus optional.

## When to Use

- When a new feature introduces user data, credentials, money movement, or access control
- When a service integrates with external systems, queues, webhooks, or third-party APIs
- When a design adds new trust boundaries, roles, or privileged actions
- When the team needs documented security assumptions before implementation or launch

## When Not to Use

- When the task is a code review for an already-implemented change
- When the issue is a concrete vulnerability that needs a fix plan instead of first-pass analysis
- When the design and data flows are already fully documented and unchanged

## Required Inputs

- The feature or system being modeled
- The data types, secrets, and permissions the system touches
- The main actors, including users, admins, services, and external parties
- The high-level architecture or flow diagram, if available
- Any known compliance, legal, or platform constraints

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Define the asset or user outcome that must be protected.
2. Inventory the data, privileges, and integrations involved in the flow.
3. Identify trust boundaries and the places where input crosses from untrusted to trusted space.
4. Walk the design with STRIDE and note plausible abuse cases, not just obvious bugs.
5. Rank the threats by likelihood and impact in the current product context.
6. Choose mitigations that remove the risk or reduce it to an accepted residual level.
7. Document what is in scope, what is out of scope, and what must be rechecked later.
8. Review the result with the implementing engineer so assumptions are shared, not hidden.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Threat models should be specific to the actual system, not generic checklists
- Trust boundaries matter more than abstract component names
- Mitigations should be testable, not just aspirational
- Residual risk should be explicit when a perfect fix is not practical

## Output Contract

- A concise list of assets, actors, and trust boundaries
- Threats organized by category or flow, with severity and rationale
- Recommended mitigations and the owner or implementation path for each
- Accepted residual risks and any follow-up questions

## Guardrails

- Do not stop at listing threats without proposing mitigations
- Do not assume a mitigation exists unless the team can actually ship it
- Do not overstate likelihood without grounding it in the current architecture
- Do not hide accepted risk; document it clearly

## Optional Tools / Resources

- MCP: GitHub MCP, Sentry MCP, Notion MCP, Linear MCP
- Websites: [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/), [OWASP Top 10](https://owasp.org/www-project-top-ten/), [NIST Computer Security Resource Center](https://csrc.nist.gov/), [CWE List](https://cwe.mitre.org/), [Snyk Learn](https://learn.snyk.io/)
- Architecture diagrams and trust-boundary docs
- Incident history and vuln reports
- Compliance or policy constraints
