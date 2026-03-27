---
name: pipeline
description: Design and maintain CI/CD pipelines that build, test, scan, and promote infrastructure or delivery changes safely.
activation_hints:
  - "Use when a change affects GitHub Actions, build stages, branch protections, or artifact promotion."
  - "Route here when the task is about delivery flow, not runtime operations or incident response."
---

# Pipeline

## Purpose

Use this skill to create or improve delivery pipelines that produce traceable artifacts, separate validation stages, and safe promotion paths from commit to deployment.

## When to Use

- When building or refactoring GitHub Actions workflows
- When a release needs separated lint, test, build, scan, and deploy stages
- When branch protections, required checks, or artifact promotion need to be enforced

## When Not to Use

- When the main problem is a broken production system or incident
- When the task is primarily rollout strategy for an already-built change
- When the work is only observability or alerting

## Required Inputs

- The repo, branch, or workflow that needs change
- The systems involved, such as GitHub Actions, Terraform, containers, or release automation
- The required validation stages and any quality gates
- The artifact that should be promoted, such as an image digest or plan file

## Workflow

1. Identify the commit-to-production path and where validation should split into independent stages.
2. Define the artifact produced by each successful build step and how later stages consume it.
3. Separate checks so failed test, build, or scan steps can rerun independently.
4. Enforce required status checks and branch protection so stale or unverified changes cannot merge.
5. Confirm the pipeline behaves the same across environments and does not rebuild untracked artifacts.
6. Verify the final path to deploy is deterministic, auditable, and easy to rerun.

## Design Principles / Evaluation Criteria

- Promote artifacts, not assumptions
- Keep stages small enough to rerun without redoing unrelated work
- Require explicit passing checks before merge or deploy
- Make pipeline state visible enough for another engineer to trust

## Output Contract

- A concise pipeline summary with the stages and gates that now exist
- The artifact promoted by the deploy stage
- Any required checks, branch protection, or rerun behavior that changed
- Open risks or remaining manual steps

## Examples

### Example 1

Input:
- Task: Split a single deploy workflow into safe stages
- Concern: Failed tests currently still allow deploy reruns from the same job

Expected output:
- Separate lint, test, scan, and deploy jobs
- Publish the build artifact once and reuse it in deploy
- Require the test and scan jobs before merge

## Guardrails

- Do not collapse validation and deploy into one monolithic job
- Do not rebuild a different artifact for deploy than the one that passed validation
- Do not add required checks that are impossible to rerun independently

## Optional Tools / Resources

- MCP: GitHub MCP, Sentry MCP, Linear MCP, Notion MCP
- Websites: [Docker Docs](https://docs.docker.com/), [Kubernetes Docs](https://kubernetes.io/docs/home/), [Terraform Docs](https://developer.hashicorp.com/terraform/docs), [AWS Documentation](https://docs.aws.amazon.com/), [Google Cloud Docs](https://cloud.google.com/docs)
- GitHub Actions workflow files
- Branch protection settings
- Build artifacts and release metadata
- CI timing or failure history
