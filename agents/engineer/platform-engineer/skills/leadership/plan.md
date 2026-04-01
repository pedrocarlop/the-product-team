---
name: plan
description: Turn an engineering objective into an execution plan with sequencing, owners, milestones, and measurable success criteria.
---

# Plan

## Purpose

Use this skill to turn an engineering objective into an executable plan that the team can own, schedule, and review.

## When to Use

- When the team needs a plan for a product or platform objective
- When milestones, dependencies, and owners need to be made explicit
- When capacity needs to be translated into commitments
- When leadership needs a plan that can be reviewed without the author present

## When Not to Use

- When the decision or objective is still unclear
- When the main need is staffing rather than sequencing
- When the work is blocked and needs immediate escalation
- When the task is mainly about calibration or feedback

## Required Inputs

- The agreed objective or outcome
- Time horizon, deadline, and audience
- Capacity, dependencies, and non-negotiables
- Known risks, unknowns, and coordination needs
- Existing commitments that constrain what can be planned

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

1. Restate the objective and define what success looks like.
2. Break the work into milestones, workstreams, and owners.
3. Sequence the work by dependency, risk, and value.
4. Match the plan to actual capacity, not theoretical capacity.
5. Surface decision points, risks, and fallback options.
6. Set review checkpoints and success measures.
7. Write the plan so another person can execute or review it without extra explanation.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- The plan should be specific enough to assign ownership
- Sequencing should reflect dependencies and risk
- The plan should fit the capacity that actually exists
- Success criteria should measure outcomes, not just activity
- Review points should be early enough to change course

## Output Contract

- Engineering plan with milestones, owners, and sequencing
- Success measures or checkpoints
- Risks, dependencies, and decision points
- Review cadence or milestone dates when relevant

## Examples

### Example 1

Input:
- Request: "Plan the next quarter for the platform team"
- Constraints: two engineers, one hard dependency on infrastructure work

Expected output:
- Plan: milestones by month, owners, and dependency order
- Measures: what will tell us the plan is on track
- Risks: the assumptions that need monitoring

## Guardrails

- Do not create a plan before the objective is clear
- Do not confuse an activity list with an executable plan
- Do not ignore dependency risk just to make the schedule look neat
- Do not plan beyond the capacity that has been demonstrated

## Optional Tools / Resources

- MCP: GitHub MCP, Linear MCP, Notion MCP, Sentry MCP
- Websites: [Atlassian Team Playbook](https://www.atlassian.com/team-playbook), [Linear Docs](https://linear.app/docs), [DORA / DevOps Research](https://cloud.google.com/devops), [GitHub Engineering Blog](https://github.blog/engineering/), [InfoQ Engineering Culture](https://www.infoq.com/)
- Roadmaps, project trackers, and milestone docs
- Capacity, throughput, or velocity data
- Dependency maps and cross-functional commitments
- Retro notes and prior execution plans
