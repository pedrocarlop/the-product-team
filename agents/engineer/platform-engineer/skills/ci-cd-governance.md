---
name: ci-cd-governance
description: Define or improve delivery controls by modeling the pipeline first, then turning policy into enforceable checks, approvals, provenance requirements, and exception handling.
trigger: When releases need stronger automation, control, or governance across CI/CD.
analysis_framework: delivery governance synthesis across controls, provenance, and exception paths
primary_mcp: repository, logs
fallback_tools: reference/reuse, search_query
required_inputs:
  - pipeline provider and scope under review
  - branch, environment, or release surface being governed
  - current required checks, approvals, and deployment protections when known
  - artifact provenance, signing, or promotion requirements when relevant
  - exception owners, escalation path, and rollout constraints when known
recommended_passes:
  - control inventory and scope framing
  - enforcement gap review
  - provenance and deployment protection review
  - exception path and ownership review
  - adoption risk synthesis
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [github, gitlab, azure_devops, buildkite, circleci]
  controls:
    primary: [github_rulesets, github_deployment_protection, gitlab_compliance_frameworks, gitlab_mr_approvals, azure_branch_policies, azure_release_gates, buildkite_block_steps, circleci_approval_jobs]
    secondary: [github_artifact_attestations, sigstore_cosign, azure_artifact_signing, open_policy_agent, kyverno]
  portable_pipelines:
    primary: [dagger, earthly]
    notes: Use when portable, reproducible pipeline definitions are the governance objective — both Dagger and Earthly run identically locally and in CI, making policy-as-code easier to test and verify.
  iac_governance:
    primary: [spacelift, atlantis, env0]
    notes: Use when IaC changes (Terraform, OpenTofu, Pulumi) need approval gates, drift detection, or OPA/Sentinel policy enforcement before apply. Spacelift supports push/plan/approval/task policies; Atlantis enforces PR-level apply locks; env0 adds cost governance and ready-to-use policies.
  supply_chain:
    primary: [slsa_framework, tekton_chains, sigstore_cosign, openssf_scorecard]
    secondary: [in_toto, gittuf, syft, guac]
    notes: Use when artifact provenance, attestation, SBOM generation, or SLSA level compliance is the primary control objective. Tekton Chains produces SLSA Provenance v1 attestations; OpenSSF Scorecard enforces repo security posture as a CI gate; in-toto and gittuf add cryptographic policy binding across pipeline steps.
  artifacts:
    primary: [reference/reuse, search_query]
  fallback:
    primary: [reference/reuse, search_query]
tool_routing:
  - if: live repo config and pipeline logs are available
    use: [repository, logs]
  - if: branch protection, required checks, or environment approvals are the main control surface
    use: [github_rulesets, gitlab_compliance_frameworks, azure_branch_policies]
  - if: deployment pause or manual promotion is the main question
    use: [github_deployment_protection, azure_release_gates, buildkite_block_steps, circleci_approval_jobs]
  - if: artifact signing, attestations, or provenance are the main question
    use: [github_artifact_attestations, sigstore_cosign, tekton_chains, azure_artifact_signing]
  - if: SLSA compliance level or supply chain integrity is the main question
    use: [slsa_framework, tekton_chains, openssf_scorecard, in_toto]
  - if: IaC changes need approval gates, drift detection, or policy enforcement before apply
    use: [spacelift, atlantis, env0]
  - if: policy-as-code enforcement across pipelines or Kubernetes is the main question
    use: [open_policy_agent, kyverno]
  - if: portable, reproducible pipeline definitions are needed to make governance testable
    use: [dagger, earthly]
  - if: only static docs or historical pipeline examples exist
    use: [reference/reuse, search_query]
best_guess_output: A CI/CD governance proposal or implementation with controls, exceptions, and rollout guidance.
output_artifacts: knowledge/platform-engineer-ci-cd-governance.md
done_when: Delivery rules are concrete enough to enforce repeatedly, with owners, exception paths, and enforcement points identified.
---

# CI/CD Governance

## Purpose

Define or improve delivery controls by modeling the pipeline first, then turning policy into enforceable checks, approvals, provenance requirements, and exception handling.

This skill is for pipeline governance, not product release judgment, incident response, or app-code review. It does not own deployment decisions — it governs the rules that make those decisions consistent and auditable.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/platform-engineer-ci-cd-governance.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: ci-cd-governance`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Governance goal`: State the control objective, the pipeline surface, and the decision the control should enable or block.
- `### Required inputs and assumptions`: State what was known, what was missing, and which assumptions were necessary.
- `### Input mode and evidence path`: Declare the evidence path used as `sourced`, `fallback`, or `inferred`.
- `### Environment and reproducibility`: Record provider, repo or org scope, branch or environment scope, build or run identifiers, and parity caveats.
- `### Model building`: Build the delivery model before judgment: actors, protected refs, jobs, environments, promotions, artifacts, trust roots, and bypass paths.
- `### Evidence reviewed`: Summarize the repo, pipeline, policy, log, or documentation evidence that informed the control model.
- `### Current gaps`: List the missing controls, weak enforcement points, duplicate gates, or bypass paths that justify the change.
- `### Core method execution`: Show the sequence used to inventory controls, map enforcement, and test exception handling.
- `### Proposed gates or rules`: Describe the gates, checks, policies, or provenance requirements to add or refine.
- `### Enforcement points`: Identify where each rule is enforced in the workflow.
- `### Exception path`: Explain how exceptions are requested, approved, time-boxed, and audited.
- `### Adoption risks`: Capture rollout risk, developer friction, bypass pressure, and operational downsides.
- `### Structured findings`: Record findings with the required schema below.
- `### Prioritization logic`: Explain how control gaps are ranked and grouped.
- `### Pattern detection`: Identify recurring failure modes, systemic policy drift, and broken mental models across the delivery pipeline.
- `### Coverage map`: Declare what was deeply analyzed, partially analyzed, and not analyzed.
- `### Tool path`: Record which tools were used and why the chosen path fit the evidence.
- `### Workflow notes`: Capture any method constraints, reuse rules, or operator assumptions.
- `### Output contract`: State where the deliverable is written and what must not be modified.
- `### Limits and unknowns`: State what could not be validated and what needs live confirmation.

## Required Inputs and Assumptions

Required inputs:
- The CI/CD provider, repo, or delivery surface in scope.
- The branch, environment, or release path under review.
- The current checks, approvals, deployment protections, or signing controls when known.
- The exception owners, escalation path, and rollout constraints when relevant.

Known vs unknown:
- Known: the exact control surface that should become more enforceable.
- Often unknown: whether the same rule applies everywhere, who can bypass it, and which control is the source of truth.

Assumption rule:
- If key inputs are missing, infer a provisional scope and prefix each inferred item with `Assumed context:`.
- Lower confidence for any finding that depends on an inferred provider, environment, or owner.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live runtime and delivery evidence - current pipeline runs, job logs, deployment events, and active protection behavior.
2. Structured system access - repository config, CI/CD provider settings, branch rules, environment checks, approval rules, and artifact metadata.
3. Design artifacts or documentation - policy docs, runbooks, compliance standards, and delivery conventions.
4. Screenshots or static snapshots - exported settings pages, pipeline views, or policy summaries.
5. Inference - config patterns and naming conventions when nothing live is available.

Declare which path was used in the deliverable and state its limitations. Prefer live delivery evidence when it exists, and combine repository review with provider settings when the control behavior needs to be validated end to end.

## Environment and Reproducibility

Record the following when known:

- CI/CD provider, repo, org, and environment scope.
- Branch, tag, or release candidate under review.
- Build number, run ID, deployment ID, or artifact digest.
- Runner image, agent version, or orchestration version when enforcement depends on it.
- Protected branch rules, environment checks, required reviews, or approval policies in effect.
- Feature flags, manual gates, or trust roots that affect whether the rule can be enforced.
- Region, workspace, or project scope when the same policy behaves differently across environments.

If any of the above is unknown, state it explicitly. Do not assume staging policy matches production policy without noting the gap.

## Model Building

Build the delivery model before analysis. No conclusions about governance quality should be written before the model exists.

Model the following:

- The actor set: contributor, reviewer, approver, release manager, bot, or service account.
- The delivery flow: commit, pull request or merge request, build, artifact, promotion, and deploy.
- The enforcement points: required checks, approvals, branch protections, environment gates, signing, and provenance verification.
- The bypass paths: direct pushes, admin overrides, manual promotions, or missing ownership.
- The consumers: developer, release engineer, security, compliance, or oncall.
- The success condition: what control would let a person move forward with confidence.

## Core Method Execution

Follow this sequence:

1. Clarify the governance goal. Name the exact pipeline surface, control objective, and decision the rule should change.
2. Inventory current controls. List the checks, approvals, protections, policy rules, and signing or provenance steps that already exist.
3. Map the runtime path. Identify where the control is enforced, what it blocks, and what can still bypass it.
4. Check control quality. Look for missing required checks, weak ownership, duplicate gates, stale rules, or rules that do not actually block delivery.
5. Check exception handling. Decide whether the exception path is explicit, time-bound, auditable, and owned.
6. Design the smallest enforceable change. Prefer a targeted rule, protection, or approval step over broad policy prose.
7. Verify the change. Confirm that the control is visible, enforceable, and tied to a concrete delivery failure mode.
8. Synthesize the deliverable. Record the path used, what improved, what remains weak, and the residual risk.

Use provider-native controls when they fit the project: GitHub rulesets and deployment protection rules, GitLab compliance frameworks and merge request approvals, Azure DevOps branch policies and release gates, Buildkite block steps, or CircleCI approval jobs.

For supply chain controls, consider SLSA framework levels as a maturity target: SLSA L1 requires provenance generation; L2 adds hosted build platform and signed provenance; L3 requires hardened builds with Tekton Chains or equivalent. Use OpenSSF Scorecard as a CI gate to enforce repo security posture continuously. Use in-toto or gittuf when cryptographic policy binding across pipeline steps is required.

For IaC governance, use Spacelift, Atlantis, or env0 to enforce apply approval gates, detect drift, and encode OPA/Sentinel policies at the plan or promotion stage — not just at deploy time.

For portable pipeline definitions, use Dagger or Earthly when reproducibility across local and CI environments is needed to make governance verifiable before it reaches production.

## Structured Findings

Every finding must use this exact schema. Keep observation separate from interpretation. Every finding must be traceable to a config setting, pipeline run, policy rule, or doc reference.

```text
#### Finding <id>
- Observation:
- Evidence:
- Repro steps or validation path:
- Cause:
- Impact:
- Confidence:
```

## Prioritization Logic

Prioritize findings by enforcement impact and bypassability:

- Always include gaps that allow unsafe merge or deploy paths.
- Elevate controls that are missing, disabled, mis-scoped, or easy to bypass.
- Group low-risk hygiene issues when they share the same root cause.
- Treat missing ownership, missing auditability, or missing provenance as higher risk than cosmetic policy drift.

## Pattern Detection

After structured findings are recorded, identify whether individual gaps reflect a broader system-level problem. Patterns matter because they reveal broken mental models or structural gaps that a list of findings cannot fix on its own.

Look for:

- **Policy drift** — rules that existed but were gradually eroded by exceptions, admin overrides, or permission creep. Treat repeated bypass pressure as a signal that the rule is mismatched with real workflow needs.
- **Phantom controls** — gates that appear configured but do not actually block delivery in practice (e.g., a required check that is never required on the target branch, or a protected branch rule with admin override always enabled).
- **Ownership gaps at scale** — controls defined once and owned by no one. These often appear as stale approval lists, bot accounts with human-level trust, or service accounts with no rotation policy.
- **Provenance dead ends** — artifact signing or attestation configured for part of the pipeline but not verified at promotion or deployment, creating a false sense of supply chain integrity.
- **Inconsistent scope** — production has strong gates, staging does not, and promotion is automatic. This pattern lets weaknesses accumulate invisibly until they reach production.
- **Governance theater** — policy documents exist and manual checklists are signed, but no machine-enforced control matches the stated requirement. Checklist-only governance fails under delivery pressure.

State each detected pattern as a named issue and link it to the findings that evidence it. Do not invent patterns from a single finding.

## Coverage Map

Declare the analysis scope explicitly so that consumers can tell what was and was not examined.

| Area | Coverage level | Notes |
|---|---|---|
| Branch protection and required checks | | |
| Environment gates and deployment protection | | |
| Approval and reviewer ownership | | |
| Artifact signing and provenance | | |
| Supply chain attestation and SLSA level | | |
| IaC approval gates and drift detection | | |
| Policy-as-code enforcement (OPA, Kyverno, Sentinel) | | |
| Exception path and audit trail | | |
| Runner and build environment trust | | |
| Bot and service account permissions | | |

Coverage levels:
- **Deeply analyzed** — live config inspected, behavior confirmed, findings traceable to specific settings.
- **Partially analyzed** — docs or static config reviewed, behavior not confirmed end-to-end.
- **Not analyzed** — out of scope, access not available, or deferred to a subsequent pass.

## Tool Path

- Start with `repository, logs`.
- Use provider-native settings or docs when branch rules, environment protection, approval flow, or provenance behavior must be confirmed.
- Use GitHub rulesets, deployment protection rules, and artifact attestations when the repository is on GitHub.
- Use GitLab compliance frameworks and merge request approval rules when the repository is on GitLab.
- Use Azure DevOps branch policies, release gates, and approvals when the repository is on Azure DevOps.
- Use Buildkite block steps or CircleCI approval jobs when manual promotion behavior is the main uncertainty.
- Use Open Policy Agent (OPA) or Kyverno when policy-as-code enforcement across pipelines or Kubernetes workloads is required. OPA uses Rego and integrates via REST API at any decision point; Kyverno is YAML-native and integrates directly with Kubernetes and GitOps pipelines.
- Use Spacelift, Atlantis, or env0 when IaC changes (Terraform, OpenTofu, Pulumi, CloudFormation) need pre-apply approval gates, drift detection, or encoded policy enforcement. Prefer Spacelift when multi-IaC support and OPA/Sentinel policy layers are needed; prefer Atlantis for PR-native Terraform locks on self-hosted infrastructure; prefer env0 when cost governance and ready-to-use policies are the priority.
- Use Dagger or Earthly when the goal is to make pipeline definitions portable and reproducible across local and CI environments, enabling governance controls to be tested before reaching production. Both tools produce deterministic build graphs that are CI-provider-agnostic.
- Use SLSA framework levels as a maturity target for provenance and build integrity requirements. Use Tekton Chains to produce SLSA Provenance v1 attestations in Kubernetes-native pipelines. Use OpenSSF Scorecard as a CI gate to enforce repo security posture continuously. Use in-toto or gittuf when cryptographic policy binding and step-level attestation across the full pipeline are required.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/reuse, search_query`.
- If both paths fail, produce the best-guess output described as: A CI/CD governance proposal or implementation with controls, exceptions, and rollout guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single control source.

## Workflow Notes

- Treat governance as executable control, not policy prose.
- Reuse existing checks and protections where possible instead of layering duplicate gates.
- Make exception handling explicit so the process remains operable under real delivery pressure.
- Prefer one canonical owner and one auditable bypass path per control.
- Separate control gaps from repository drift and from platform limitations.
- When adding supply chain controls, confirm the verification step exists at promotion or deployment, not just at build time. Signing without verification is not a control.
- When recommending OPA or Kyverno, identify the decision point where the policy fires — pre-merge, pre-deploy, or runtime admission — and confirm the enforcement mode is deny, not audit-only, before claiming the control is active.
- When recommending Spacelift, Atlantis, or env0, confirm whether the apply gate is hard-blocking or advisory. Advisory drift detection without a blocking apply gate is not enforcement.


## Limits and Unknowns

- Do not claim enforcement that the provider cannot actually apply.
- Do not assume org-wide, enterprise, or environment-level settings are visible unless they are explicitly inspected.
- Do not treat artifact signing or provenance as present unless the trust root and verification path are confirmed.
- Do not treat OPA or Kyverno policies as enforcing unless the mode is confirmed as deny, not audit.
- Do not treat IaC apply gates as blocking unless the approval workflow is confirmed to prevent auto-apply on drift.
- Do not claim SLSA level compliance without confirming which build steps produce attestations and where verification occurs.
- State any missing approval owner, bypass rule, or deployment protection as an open governance gap until it is validated live.
