---
name: infra-release
description: Execute a rollback-first infrastructure release by building a release model, selecting the narrowest safe tool path, and verifying rollout, rollback, and operational readiness from present-state evidence.
trigger: When infra, platform, IaC, or deployment changes must be released safely.
mesh:
  inputs:
    - platform-engineer:pipeline-orchestration
    - qa-reviewer:test-plan-review
  next:
    - go-to-market:launch-plan
  context: "Deploys the necessary infrastructure to support the feature."
decision_framework: rollback-first infra release execution
primary_mcp: repository
fallback_tools:
  - search_query
  - reference/verify
required_inputs:
  - the exact infra or platform change, target environment, and expected outcome
  - the deployment surface: cloud resource, cluster object, pipeline, release controller, or GitOps path
  - rollback constraints, blast radius, maintenance window, and ownership context
  - available evidence such as diffs, plans, logs, release notes, manifests, or runtime status
  - known dependencies or blockers such as secrets, approvals, data migrations, or policy gates
recommended_passes:
  - release scope and dependency mapping
  - plan or manifest parity check
  - rollout and rollback path validation
  - operational safeguard review
  - post-release verification and residual risk review
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [reference/verify, open]
  iac:
    primary: [terraform, opentofu, pulumi]
    secondary: [cloudformation, crossplane, terragrunt, cdktf]
  iac_governance:
    primary: [spacelift, env0]
    secondary: [atlantis]
  release_execution:
    primary: [helm, kubectl]
    secondary: [argo-rollouts, flagger]
  gitops:
    primary: [argocd, flux]
    secondary: [kustomize, kargo]
  progressive_delivery:
    primary: [argo-rollouts, flagger]
    secondary: [spinnaker]
  fallback:
    primary: [search_query]
    secondary: [reference/verify]
tool_routing:
  - if: the change is described by code, manifests, or repository state and real evidence is available
    use: [repository, logs]
  - if: the release is managed as infrastructure code with a plan/apply or preview/apply loop
    use: [terraform, opentofu, pulumi, cloudformation]
  - if: the IaC stack uses Terragrunt for module orchestration or DRY config management
    use: [terragrunt]
  - if: the IaC release requires policy gates, cost controls, or team-level governance
    use: [spacelift, env0]
  - if: the release targets Kubernetes objects directly
    use: [kubectl, helm]
  - if: the release is GitOps-managed or reconciled from a repository controller
    use: [argocd, flux, kustomize]
  - if: multi-environment promotion pipelines or stage-gated GitOps workflows are involved
    use: [kargo]
  - if: progressive delivery, canary, or blue-green rollout logic is involved
    use: [argo-rollouts, flagger, kubectl]
  - if: the progressive delivery strategy requires automated metric analysis and traffic shifting
    use: [flagger]
  - if: multi-cloud or enterprise CD pipelines with manual approval gates are required
    use: [spinnaker]
  - if: the strongest evidence is a previous validation artifact or a linked runbook
    use: [reference/verify]
  - if: tool behavior or rollout semantics are unclear
    use: [search_query]
best_guess_output: A release runbook or implementation summary with scope, prereqs, execution, rollback, verification, and residual risk.
output_artifacts: knowledge/platform-engineer-infra-release.md
done_when: The release path, rollback posture, verification evidence, and remaining unknowns are explicit enough for safe execution or audit.
---

# Infra Release

## Purpose

Execute or plan an infrastructure or platform release with operational safeguards, using the narrowest evidence-backed tool path available.

This skill builds a release model before action, prefers deterministic previews and current runtime evidence, and keeps rollback and verification on equal footing with deployment steps.

This skill does not replace incident command, product approval, or hands-on execution by the owner of the target system.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/platform-engineer-infra-release.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: infra-release`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Release framing`: Define the exact release candidate, target environment, and success criteria.
- `### Required inputs and assumptions`: State what was known, what was missing, and which assumptions were made.
- `### Input mode and evidence path`: Declare whether the path was sourced, fallback, or inferred, and what the evidence can and cannot prove.
- `### Tool selection rationale`: Explain why the chosen tools fit the change, and what alternative tools would cover the same capability.
- `### Environment and reproducibility`: Record environment, version, auth, data, and parity details needed to reproduce the release.
- `### Release model`: Map dependencies, blast radius, rollback triggers, operational checks, and validation points before judging readiness.
- `### Execution plan`: Describe the ordered release sequence and any hold points or approvals.
- `### Rollback posture`: Explain the rollback mechanism, reversibility limits, and abort triggers.
- `### Verification and follow-up`: State how success will be confirmed and what must happen after release.
- `### Structured findings`: Document each confirmed issue using the finding schema.
- `### Pattern detection`: Identify recurring release failures, systemic rollback issues, and structural environment gaps.
- `### Recommendations`: Provide directional, finding-linked improvements without overstating confidence.
- `### Coverage map`: Declare which areas were deeply analyzed, partially covered, and not analyzed.
- `### Prioritization logic`: Explain how blockers, risk, and cleanup items were ordered.
- `### Limits and unknowns`: Call out what remains unproven or environment-specific.

## Required Inputs and Assumptions

Required inputs:
- The exact infra, platform, or deployment change and the target environment.
- The expected release outcome, including whether the change is a safe edit, replacement, migration, or progressive rollout.
- The current implementation surface: code, manifests, pipeline, controller, or deployment artifact.
- The rollback boundary, blast radius, and owner or approver for the release.
- Available evidence: plans, diffs, logs, release notes, runbooks, or runtime status.

If inputs are missing, infer a provisional release frame and label it clearly as `Assumed context:`. Lower confidence for any claim that depends on inference.

Known vs unknown:
- The change may be fully codified in IaC, partially managed by a controller, or executed through a release pipeline.
- Reversibility is often constrained by data migrations, provider-side side effects, or controller reconciliation, so it must be checked rather than assumed.
- Environment parity may differ across local, CI, staging, and production-like targets.

## Input Mode and Evidence Path

Use this hierarchy:

1. Live or current runtime evidence: deployed state, controller status, rollout health, or release output.
2. Structured system access: repository diffs, plans, manifests, logs, CI output, or deployment metadata.
3. Linked artifacts and specifications: runbooks, tickets, release notes, or architecture notes.
4. Static samples: captured manifests, screenshots, command output, or exported logs.
5. Inference: use only when stronger evidence is unavailable.

State which path was used and what it cannot prove. Do not present a preview, plan, or controller status as a confirmed release.

## Tool Selection Rationale

- `terraform` and `opentofu` fit release work that needs explicit preview/apply semantics, drift awareness, and infrastructure-as-code parity. OpenTofu is the CNCF-backed open-source fork of Terraform 1.5 with a fully compatible HCL surface and active community development; prefer it for teams avoiding HashiCorp's BSL licensing.
- `terragrunt` fits IaC stacks that need DRY module orchestration, multi-account or multi-region composition, and dependency-ordered applies across many root modules. It wraps Terraform or OpenTofu without replacing their plan/apply semantics.
- `pulumi` fits teams authoring infrastructure in general-purpose languages (TypeScript, Python, Go) where type safety, testing frameworks, and programmatic composition are stronger than HCL.
- `cloudformation` fits AWS-native infrastructure releases that depend on change-set style review and stack-managed updates.
- `cdktf` (CDK for Terraform) fits teams who want Terraform provider coverage with a programming-language abstraction layer instead of HCL.
- `spacelift` and `env0` fit platform teams that need centralized IaC governance: policy-as-code gates, cost controls, audit trails, approval workflows, and self-service for many teams running Terraform, OpenTofu, Terragrunt, or Pulumi. Spacelift is stronger for complex stack dependency graphs and multi-IaC environments; env0 is stronger for cost visibility and self-service standardization.
- `kubectl` fits direct Kubernetes inspection, rollout status, and rollback control for live cluster objects.
- `helm` fits charted application or platform releases that need template, upgrade, and rollback semantics.
- `argocd` and `flux` fit GitOps-managed releases where reconciliation, sync state, and drift are the primary release signals.
- `kargo` fits teams that need structured, GitOps-centered promotion across multiple environments with stage-gated pipelines and promotion policies. It builds on top of Argo CD and treats environment promotion as a first-class workflow rather than a manual git operation.
- `crossplane` fits composed infrastructure or platform releases where managed resources and composite resources are the source of truth.
- `argo-rollouts` fits canary or blue-green progressive delivery where analysis, promotion, abort, and rollback are release controls.
- `flagger` fits automated progressive delivery where canary, blue-green, or A/B strategies are driven by metric analysis against Prometheus, Datadog, CloudWatch, or similar observability backends. Flagger integrates natively with Flux and supports Istio, Linkerd, NGINX, and Gateway API for traffic shifting.
- `spinnaker` fits multi-cloud or enterprise CD pipelines where manual approval stages, baked image promotion, and multi-cluster rollout choreography are required at scale.
- `reference/verify` and `search_query` are fallback aids when the primary execution path is blocked or tool semantics need confirmation.

## Tool Path

- Start with `repository, logs` when code, manifests, pipeline state, or runtime evidence are available.
- If the release is infrastructure code, use `terraform`, `opentofu`, or `cloudformation` preview or change-set style checks first. Use `opentofu` as the default for new greenfield IaC stacks unless provider or licensing constraints require Terraform.
- If the IaC stack uses Terragrunt, run `terragrunt plan` or `terragrunt run-all plan` to validate the full dependency graph before apply.
- If the release requires governance gates, policy checks, or cost approval, route through `spacelift` or `env0` before execution.
- If the release targets Kubernetes directly, use `kubectl` and `helm` before broader verification.
- If the release is GitOps-managed, use `argocd` or `flux` reconciliation and status checks as the source of truth.
- If multi-environment promotion is managed by Kargo, check stage health and promotion policy before advancing.
- If the release is composed through Crossplane, check the composite resource and managed resource readiness before applying dependent changes.
- If progressive delivery is involved, use `argo-rollouts` or `flagger` plus platform health signals before promotion or abort decisions. Prefer `flagger` when metric-driven traffic shifting and automated rollback are the primary control plane.
- If multi-cloud or enterprise-scale CD with manual approvals is required, use `spinnaker` pipeline stages as the release control plane.
- If the strongest available evidence is a prior runbook or validation artifact, use `reference/verify`.
- If the primary path is unavailable or tool behavior is unclear, switch to `search_query`.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Environment and Reproducibility

Record the following when known:
- Target environment: local, CI, staging, or production-like.
- Build, image tag, commit, release version, or stack revision.
- Auth and access state: human, service account, controller, or mixed.
- Relevant flags, namespaces, accounts, regions, or migration state.
- Provider or controller version when behavior is version-sensitive.

If any of the above is unknown, state it explicitly. Do not imply parity that was not checked.

## Model Building

Before judging readiness, build a release model with these parts:

- Change map: what is changing and where.
- Dependency map: IaC, cluster, cloud provider, registry, secrets, DNS, or pipeline dependencies.
- Risk map: blast radius, data impact, downtime risk, and rollback limits.
- Validation map: preview, rollout, health, and post-change verification points.
- Environment map: what differs across local, CI, staging, and production-like targets.

No decision about safety should be written before the model is complete.

## Core Method Execution

1. Define the release scope and source of truth for expected behavior.
2. Build the model from repository state, release artifacts, and runtime evidence.
3. Check the narrowest safe preview path first: plan, change set, render, or dry run.
4. Validate release sequencing, including hold points, approvals, and canary or rollout controls.
5. Confirm rollback posture, including triggers, reversibility limits, and owner readiness.
6. Verify operational safeguards: logs, health checks, alerts, and deployment visibility.
7. Compare observed state to expected state and separate confirmed findings from inferred concerns.
8. Group repeated risks into patterns and state the residual risk clearly.

## Structured Findings

Document each confirmed issue using this schema. Do not conflate distinct findings into one entry, and do not subdivide the same weakness into multiple entries.

#### Finding <id>
- Observation: What was observed in the release, plan, manifest, or runtime state.
- Evidence: The specific artifact, log line, plan output, or status that supports the observation.
- Repro steps or validation path: How to reproduce or verify the finding in the same or equivalent environment.
- Cause: The immediate and structural cause, if determinable from available evidence.
- Impact: The release risk, blast radius, or operational consequence if this finding is not addressed.
- Confidence: High (confirmed from direct evidence), Medium (inferred from partial evidence), or Low (speculative).

Use one finding block per distinct issue. If a finding was ruled out during analysis, note the ruling-out evidence rather than omitting it silently.

## Pattern Detection

After recording individual findings, review them for recurring themes. State each pattern explicitly.

Patterns to look for:
- Recurring rollback gaps: multiple release stages or environments where rollback posture is absent, incomplete, or untested.
- Systemic preview failures: plans, dry runs, or change sets that consistently miss a class of resource or dependency.
- Structural environment gaps: differences between staging and production-like environments that invalidate verification evidence before every release.
- Controller drift accumulation: GitOps or Crossplane reconciliation states that accumulate drift across cycles without alerting.
- Governance bypass patterns: release paths that skip policy gates, approval workflows, or cost controls under time pressure.
- Tool mismatch patterns: teams using a tool at the edge of its intended scope (e.g., using raw kubectl for progressive delivery instead of a dedicated controller).

If no pattern is detected, state that explicitly rather than leaving the section blank.

## Recommendations

Provide one recommendation per finding or pattern. Recommendations must link back to the finding or pattern ID they address.

Format:
- Finding or pattern reference: which finding or pattern this recommendation addresses.
- Recommendation: the directional action, stated plainly.
- Rationale: why this addresses the root cause, not just the symptom.
- Confidence: High, Medium, or Low, matching the confidence of the linked finding.
- Trade-offs: what the recommendation does not solve or may make harder.

Do not recommend tools or processes as defaults without evidence that they fit the environment. Do not overstate confidence when the finding itself is inferred. Keep recommendations directional — they are not implementation prescriptions.

## Coverage Map

Declare explicitly what was and was not analyzed. Use three tiers:

**Deeply analyzed**: Areas where direct evidence was available and reviewed thoroughly.
- List the specific areas, files, systems, or components covered.

**Partially analyzed**: Areas where evidence was available but incomplete, or where coverage was limited by scope or time.
- State what was checked and what was not.

**Not analyzed**: Areas that were out of scope, inaccessible, or where no evidence was available.
- State why and whether this gap affects confidence in the findings.

Do not imply coverage that was not performed. A small, well-scoped coverage map is more useful than a broad one that overstates depth.

## Workflow Notes

- Keep plan/apply, sync, rollout, and verification steps distinct so operators can stop at the right point.
- Prefer deterministic previews and reconciled state over guesswork.
- Treat rollback limits, data migrations, and reconciliation loops as first-class release constraints.
- If progressive delivery is used, do not treat promotion as complete until post-promotion signals are checked.
- Keep human approvals and automated gates explicit when the environment depends on them.

## Prioritization Logic

Prioritize release issues by execution risk:

1. Critical: destructive or irreversible steps, missing rollback, unsafe blast radius, broken approvals, or absent release visibility.
2. Significant: partial preview coverage, unclear dependency ordering, weak rollback rehearsal, or incomplete rollout verification.
3. Minor: cleanup, documentation, or low-blast-radius follow-up that does not block the release path.

Group minor items when they share the same cause. Do not split the same release weakness into multiple findings.


## Limits and Unknowns

State explicitly what this skill cannot determine from available evidence. Do not omit this section — an empty limits section implies a completeness that is rarely warranted.

Common limits to check and declare:
- Environment parity: whether the staging or preview environment is close enough to production-like to make verification evidence valid.
- Controller behavior under load or during reconciliation lag: GitOps and Crossplane controllers can behave differently under high-churn or degraded conditions.
- Side effects of provider-managed resources: cloud providers may apply changes to dependencies (IAM, networking, DNS) that are not visible in the IaC plan output.
- Data migration irreversibility: database schema changes, data transforms, or state migrations that cannot be rolled back independently of the infrastructure change.
- Authorization scope: whether the available credentials actually cover every resource the plan or manifest touches.
- Preview completeness: terraform plan, helm dry-run, and kubectl diff do not guarantee runtime behavior matches plan output.
- Rollback rehearsal coverage: whether the rollback path has been tested in an environment comparable to the target.
- Third-party dependencies: external registries, DNS providers, certificate authorities, or upstream APIs that are outside the release controller's scope.

If a limit affects a specific finding's confidence, reference the finding explicitly.
