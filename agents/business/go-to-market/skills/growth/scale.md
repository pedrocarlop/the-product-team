---
name: scale
description: Turn proven growth wins into repeatable systems, rollouts, and operating habits that compound safely.
---

# Scale

## Purpose

Use this skill to convert a validated growth insight into a repeatable process, broader rollout, or operating system that can sustain the gain.

## When to Use

- When a test winner needs phased rollout or production hardening
- When a process needs to be repeated across channels, segments, or markets
- When the team wants to codify a working growth motion into a playbook

## When Not to Use

- When the idea has not yet been validated
- When the work is still about finding the bottleneck or designing the test
- When the problem is a measurement gap rather than an execution gap

## Required Inputs

- The proven change or winning experiment result
- The segment where the win was observed
- Rollout constraints, risks, and guardrails
- Dependencies on engineering, marketing, sales, or ops
- Any operational metrics that must remain stable during expansion

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Confirm what was proven and the boundary of the evidence.
2. Identify the smallest safe rollout path that preserves the observed lift.
3. Translate the win into a repeatable process, rule, or automation.
4. Define guardrails that detect regressions during expansion.
5. Expand the rollout in phases and monitor for segment-specific degradation.
6. Document the playbook so another team member can reproduce the result.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Scale only what has evidence behind it
- Preserve the conditions that made the original win work
- Expand in controlled steps rather than all at once
- Build repeatable systems instead of one-off heroics
- Watch for degradation in segments that were not in the original test

## Output Contract

- The validated insight being scaled
- The rollout or operating model
- Guardrails and monitoring plan
- Dependencies and ownership
- The documented playbook or repeatable process

## Examples

### Example 1

Input:
- Result: A simplified onboarding path improved activation by 12%
- Need: Roll out across all acquisition channels

Expected output:
- Rollout plan: Ship in phases, starting with the most similar cohort to the test audience
- Guardrails: Activation rate, support tickets, and drop-off by device
- Playbook: Define when to use the simplified path and when to keep the standard flow

## Guardrails

- Do not scale before the win is validated
- Do not remove monitoring once rollout begins
- Do not assume a win in one segment will hold everywhere
- Do not codify a process before the underlying behavior is stable

## Optional Tools / Resources

- LaunchDarkly or equivalent rollout controls
- Analytics dashboards for monitoring
- Notion or docs for playbooks and handoffs
- Engineering and ops coordination channels

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Mixpanel Blog (mixpanel.com)](https://mixpanel.com/blog/), [Andrew Chen Essays (andrewchen.com)](https://andrewchen.com/)
