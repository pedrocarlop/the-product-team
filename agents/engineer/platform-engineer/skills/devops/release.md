---
name: release
description: Plan and execute safe releases, rollouts, and rollback paths for infrastructure and platform changes.
---

# Release

## Purpose

Use this skill to move approved changes through environments safely and predictably, with clear rollout controls and a known path back out.

## When to Use

- When promoting a change from staging to production
- When choosing between rolling, canary, or blue/green release strategies
- When a rollout needs feature flags, gates, or a documented rollback

## When Not to Use

- When the pipeline itself is broken before release
- When the production issue is already active and needs observation or stabilization
- When the task is only adding telemetry or alerts

## Required Inputs

- The release target, affected services, and environments
- The change risk level and any dependencies or migrations
- The acceptable rollout strategy and rollback expectations
- Any feature flags, health checks, or approval steps that must be honored

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

1. Classify the change by blast radius, dependency risk, and rollback complexity.
2. Choose a rollout pattern that matches the risk: rolling, canary, or blue/green.
3. Verify the promoted artifact is the same one that passed previous validation.
4. Confirm health checks, alarms, and automated gates are ready before traffic shifts.
5. Define the rollback path so it is a documented, low-friction operation.
6. Validate the release order across environments and call out any manual steps.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Smaller exposure windows are safer than broad launches
- Rollback should be simple enough to use under pressure
- Promotion should preserve artifact identity across environments
- Release control beats release speed when the blast radius is high

## Output Contract

- A release plan with the chosen rollout strategy
- The rollback path and any preconditions for using it
- Environment, artifact, and gate details that matter for execution
- Any risks that remain after the release plan is defined

## Examples

### Example 1

Input:
- Task: Move a Kubernetes service to production
- Concern: The service is stateful and a bad deploy needs a fast rollback

Expected output:
- Use a staged rollout with explicit health gates
- Keep the image digest unchanged between staging and production
- Document the rollback command and decision trigger

## Guardrails

- Do not release without a rollback path
- Do not let staging and production use different artifacts for the same commit
- Do not choose a rollout strategy that hides the service from alerting or manual recovery

## Optional Tools / Resources

- Deployment manifests
- Feature flag controls
- Release checklists and runbooks
- Environment promotion records
