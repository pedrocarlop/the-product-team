---
name: security-hardening
description: Analyze a concrete security weakness, choose the least-invasive effective control, and verify that the remediation measurably reduces risk.
trigger: When the system needs a specific security fix, guardrail, or hardening step.
hardening_framework: threat-to-control remediation loop
primary_mcp: repository, logs
fallback_tools:
  - reference/verify
  - search_query
required_inputs:
  - specific weakness, incident, or target control gap
  - affected service, path, image, cluster, or pipeline surface
  - evidence artifacts such as code, configs, manifests, logs, scans, or screenshots
  - environment and rollout context when the change touches production or shared infra
  - constraints on compatibility, compliance, or downtime when known
recommended_passes:
  - weakness normalization and blast-radius mapping
  - control selection and lowest-cost effective remediation
  - environment and reproducibility check
  - verification and rollback review
  - residual-risk prioritization
tool_stack:
  synthesis:
    primary: [repository, logs]
    secondary: [reference/verify]
  enrichment:
    primary: [search_query]
  fallback:
    primary: [reference/verify, search_query]
tool_routing:
  - if: code, infra config, manifests, or runtime evidence are accessible
    use: [repository, logs]
  - if: the strongest context lives in docs, tickets, scan output, or prior reviews
    use: [reference/verify]
  - if: external guidance, scanner behavior, or control-specific implementation details matter
    use: [search_query]
best_guess_output: A security hardening change or remediation plan with evidence, residual risk, and verification steps.
output_artifacts: knowledge/platform-engineer-security-hardening.md
done_when: The weakness, remediation, evidence path, and residual risk are explicit enough to implement and review.
---

# Security Hardening

## Purpose

Analyze a concrete security weakness, choose the least-invasive effective control, and verify that the remediation measurably reduces risk.

This skill applies threat-to-control reasoning across dependency, container, secret, policy, signing, supply chain, and runtime boundaries.

This skill does not invent threats, replace formal security review, or claim safety without evidence.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/platform-engineer-security-hardening.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Inputs and Assumptions

Before starting analysis, confirm or record the following:

**Required inputs:**
- The specific weakness, incident, or control gap being addressed (not a general category — name the exact surface)
- The affected service, image, namespace, cluster, path, or pipeline stage
- Evidence artifacts: code, configs, manifests, scan output, runtime logs, or screenshots
- Environment and rollout context when the change touches production or shared infrastructure
- Constraints on compatibility, compliance, or downtime when known

**Known vs unknown:**
- Distinguish what was directly observed from what was inferred or assumed
- When a required input is missing, record it as an unknown and state the assumption made in its place

**Assumption rule:** When proceeding without a required input, prefix the assumption with `Assumed context:` so reviewers can identify unverified conditions. Example: `Assumed context: the cluster runs Kubernetes 1.29 with Pod Security Admission enforced in restricted mode.`

## Input Mode and Evidence Path

Choose the strongest available evidence path and label the output accordingly:

1. **Current implementation or runtime evidence** — live cluster state, runtime logs, admission controller decisions, Falco or Tetragon alerts, audit logs. Use `repository` and `logs`. Label as `sourced`.
2. **Structured repository and log evidence** — code, manifests, CI pipeline configs, Dockerfile layers, policy files, prior scan output committed to the repo. Use `repository`. Label as `sourced`.
3. **Linked scans or docs** — scan reports, vulnerability advisories, compliance audit exports, linked tickets. Use `reference/verify`. Label as `fallback`.
4. **Screenshots or visual artifacts** — dashboard screenshots, terminal output images. Use `reference/verify`. Label as `fallback`.
5. **Inference** — reasoning from patterns, conventions, or analogous systems when no direct evidence is accessible. Label as `inferred` and state the basis.

Do not mix levels silently. If a finding draws on level 4 or 5, say so in the finding's evidence field.

## Environment and Reproducibility

Record the following before producing findings so that the remediation is reproducible:

- **Platform:** cloud provider, region, node OS and kernel version (relevant for eBPF-based controls like Tetragon or KubeArmor)
- **Cluster or runtime:** Kubernetes version, container runtime (containerd, CRI-O), admission plugins active
- **Build and image digests:** base image name and digest (e.g. `cgr.dev/chainguard/node@sha256:...`), Dockerfile or build config ref
- **Policy versions:** OPA Gatekeeper or Kyverno policy version, Conftest policy bundle ref, seccomp profile version
- **Auth and data assumptions:** whether the workload handles PII, holds elevated IAM roles, or is reachable from the internet
- **Version-specific caveats:** note when a control requires a minimum Kubernetes version, kernel version, or feature gate

If any of these are unknown, state `Assumed context:` and proceed with the best available information.

## Model Building (Threat-Control Model)

Build the threat-control model before proposing any changes. Do not move from a finding to a fix without completing this map:

**Mapping method — for each weakness, answer in order:**

1. **Normalize the weakness:** What is the precise failure? (e.g. "container runs as UID 0 with no seccomp profile", not "bad security posture")
2. **Name the trust boundary:** What boundary does the weakness cross or erode? (e.g. container-to-host, namespace-to-namespace, CI-to-registry, developer-to-secret)
3. **Trace the exploit path:** How would an adversary move from the weakness to impact? Be specific about steps. (e.g. "attacker escapes container via privileged mode → access host filesystem → read node credentials → lateral movement to other namespaces")
4. **Map blast radius:** What is the scope of harm if the exploit path succeeds? (e.g. single pod, all pods in namespace, all nodes, secrets across cluster, downstream consumers of signed artifacts)
5. **Select control family:** Which control family closes the root cause at the widest applicable scope? Options: image hardening, admission policy, runtime enforcement, secret management, supply chain integrity, network segmentation, identity and workload attestation, IaC policy gate.
6. **Validate enforcement path:** Where is the control enforced and how would you verify it? (e.g. OPA Gatekeeper webhook blocks admission, Falco alert fires on syscall, CI gate fails on Trivy HIGH+)

The `### Threat-control model` deliverable section is the output of this method — one entry per weakness.

## Core Method Execution

Execute these steps in order. Record the output of each step in the corresponding deliverable section.

1. **Normalize the weakness** — restate the weakness in precise, non-generic terms. Strip vague language. Identify the exact config key, image layer, policy gap, or runtime behavior at issue.
2. **Map blast radius and trust boundary** — determine what an adversary can reach from this weakness and what boundary it crosses. Use the model building method above.
3. **Select control family** — choose the control family that closes root cause at the widest applicable scope. Prefer enforcement over detection alone where both are available.
4. **Evaluate the lowest-cost effective control** — among controls in the selected family, choose the one with the least blast from rollout, fewest dependencies, and smallest operational burden, while still closing the root cause. Document trade-offs for higher-cost alternatives.
5. **Verify enforcement path** — confirm how the control is enforced (admission, CI gate, runtime agent, hook) and what evidence would confirm it is working. Do not recommend a control without a verification step.
6. **Check residual risk** — after the control is applied, what risk remains? Is detection still needed alongside enforcement? Are there bypass paths?
7. **Synthesize** — write findings, recommended controls, and residual risk sections. Link each recommendation to the finding it addresses.

## Pattern Detection

When reviewing multiple services, namespaces, or workloads, look for recurring anti-patterns that indicate a systemic gap rather than an isolated incident. Systemic gaps require a control-family fix (admission policy, image standard) rather than a per-workload patch.

**Common anti-patterns to identify:**

- Secrets injected as environment variables across multiple services (systemic: migrate to External Secrets Operator, Vault agent injector, or Sealed Secrets)
- Missing `securityContext` (or `runAsNonRoot: false`) across most or all Deployments (systemic: Kyverno/OPA Gatekeeper policy at admission)
- Images running as UID 0 consistently across the workload fleet (systemic: base image standard — adopt Wolfi/Chainguard distroless or enforce `USER` in Dockerfile policy)
- No RBAC least-privilege pattern — service accounts with wildcard verbs or cluster-admin bindings for workloads (systemic: RBAC audit with kubeaudit or Kubescape NSA framework check)
- Images without digests in manifests, relying on mutable tags (systemic: pin digests in CI, enforce with Kyverno mutating policy)
- No image signing or verification gate — unsigned images admitted to production (systemic: Sigstore Cosign + Kyverno `verify-images` policy or Sigstore policy-controller)
- No seccomp or AppArmor profile applied to any workload (systemic: default seccomp profile enforcement via Pod Security Admission `restricted` mode or Kyverno)
- IaC configs without policy gate — Terraform or Helm changes merged without Checkov/KICS scan (systemic: add CI gate)
- No runtime threat detection deployed — workloads have no Falco, Tetragon, or KubeArmor policy active (systemic: runtime security layer gap)
- Container images built from unverified upstream base images with no SBOM or provenance (systemic: supply chain gap — adopt Syft for SBOM generation, Grype for CVE scanning, Rekor for transparency)

When three or more instances of the same anti-pattern appear, call it a systemic finding and recommend the systemic control alongside any per-instance fixes.

## Recommendations

Recommendations must be grounded in findings. Do not add recommendations without a linked finding ID.

**Format:** Each recommendation must include:
- The finding ID it addresses
- The concrete change (exact config key, policy name, admission mode, tool and flag)
- The enforcement point (CI gate, admission webhook, runtime agent, image build step)
- The verification step (how to confirm the control is working)
- The trade-off or caveat (what this control does not cover)

**Directional, not overconfident:** When evidence is incomplete (level 4 or 5), state the recommendation as directional: "Based on observed pattern, recommend X — validate against actual cluster state before enforcing." Do not present inferred controls as confirmed fixes.

**Prefer systemic controls over per-instance patches** when a pattern is detected. A Kyverno policy that blocks root containers at admission is worth more than patching five Dockerfiles individually, if the root cause is a missing policy gate.

## Prioritization Logic

Rank findings by combining severity and blast radius. Do not use CVSS score alone — a medium CVE in a public-facing service with cluster-admin access is higher priority than a critical CVE in an isolated internal batch job.

**Priority factors (all must be considered):**

- **Public exposure:** Is the affected workload reachable from the internet or from untrusted networks?
- **Privilege escalation path:** Does the weakness allow an attacker to gain higher privilege within the cluster or on the host?
- **Secret or credential disclosure:** Could the weakness expose secrets, tokens, certificates, or credentials?
- **Unsigned or unverified artifacts:** Is the supply chain integrity of images or build outputs unverifiable?
- **Policy bypass:** Does the weakness allow workloads to evade admission policies or runtime controls?
- **Blast radius:** How many pods, namespaces, nodes, or downstream consumers are affected?
- **Exploit maturity:** Is a public exploit known? Is active exploitation observed in the wild?

**Priority tiers:**
- **Critical:** Public exposure + privilege escalation or secret disclosure. Address before the next deployment.
- **High:** One of the above factors plus broad blast radius. Address within the current sprint.
- **Medium:** Isolated blast radius, no active exploit, policy enforcement available. Schedule within two sprints.
- **Low:** Defense-in-depth gap, no known exploit path, low blast radius. Track and address in hardening backlog.

## Coverage Map

State explicitly what was reviewed and at what depth. Do not omit this section.

**Structure:**
- **Deeply reviewed:** Surfaces where direct evidence was examined (code read, manifest inspected, scan output analyzed, runtime log reviewed)
- **Partially reviewed:** Surfaces where indirect evidence was used (doc referenced, ticket linked, screenshot examined, analogous system inferred from)
- **Not reviewed:** Surfaces that are in scope but were not examined due to missing access, missing tooling, or time constraint — name them

If a surface is not reviewed, say so. Do not let gaps hide in silence.

## Limits and Unknowns

State what could not be validated and where confidence is low. This section is required even when the analysis is well-evidenced.

**Required entries:**
- What evidence was missing or unavailable
- Which findings rest on inference (level 5) rather than direct observation
- Where the recommended control has not been tested in the specific environment
- What follow-up is needed to close the confidence gap (e.g. "Validate Falco rule triggers in staging before enabling in production")
- Any assumptions that, if wrong, would change the priority or recommendation

## Required Deliverable Sections

Within `## Skill: security-hardening`, include:

- `### Security framing`: Define the weakness, trust boundary, and why it matters now.
- `### Required inputs and assumptions`: State the known issue, affected surface, and any assumptions made when evidence is incomplete. Use `Assumed context:` prefix for unverified conditions.
- `### Input mode and evidence path`: State which evidence level (1–5) was used and label the section `sourced`, `fallback`, or `inferred`.
- `### Tool selection rationale`: State which tools were used, why they fit the surface, what they validated well, and what they could not validate. Mention candidate controls or scanners only as alternatives, not mandates.
- `### Environment and reproducibility`: Record platform, cluster or runtime, build or image digests, policy versions, auth/data assumptions, and any version-specific caveats.
- `### Threat-control model`: Build the model first by mapping each weakness to its trust boundary, exploit path, blast radius, and control family. One entry per weakness.
- `### Hardening passes`: List the passes executed: weakness normalization, blast-radius mapping, control selection, verification planning, residual-risk prioritization.
- `### Evidence reviewed`: Summarize the code, config, scan output, runtime logs, docs, or screenshots that informed the recommendation. Note evidence level for each.
- `### Findings`: Record findings using the required finding schema below.
- `### Pattern detection`: Note any recurring anti-patterns observed across services or workloads. Flag systemic gaps.
- `### Prioritization logic`: State how severity was ranked for this engagement, applying the priority factors above.
- `### Recommended controls`: List the concrete remediation steps with enforcement point and verification step for each. Link each to a finding ID.
- `### Residual risk`: Capture what risk remains after the change and what would still need monitoring or follow-up.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed.
- `### Limits and unknowns`: Explain what could not be validated and where confidence is low.

For each finding inside `### Findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Evidence level: (1 sourced / 2 sourced / 3 fallback / 4 fallback / 5 inferred)
- Affected surface:
- Validation path:
- Risk type:
- Impact:
- Severity:
- Blast radius:
- Confidence:
- Recommendation direction:
- Systemic pattern: (yes / no — if yes, name the pattern)

## Tool Path

- Prefer the strongest security evidence path available: current implementation or runtime evidence -> structured repository and log evidence -> linked scans or docs -> inference.
- Start with `repository, logs` when the weakness, config, build, or runtime evidence are accessible.
- Use `repository` to inspect code, manifests, CI, policy, image, and deployment surfaces.
- Use `logs` when recent runtime behavior, alerts, or execution records materially affect exposure or validation.
- Use `search_query` only to consult official docs for scanner behavior, policy semantics, or runtime hardening guidance.
- Use `reference/verify` when the best evidence is in prior reviews, scan reports, or linked artifacts.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/verify, search_query`.
- If both paths fail, produce the best-guess output described as: A security hardening change or remediation plan.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

**Tool candidates by capability — use when the surface matches:**

| Capability | Tools |
|---|---|
| Container image CVE scanning | Trivy, Grype, Docker Scout |
| SBOM generation | Syft, Trivy (with `--format cyclonedx`) |
| Container image hardening (base) | Wolfi/Chainguard images (distroless, minimal attack surface, CVE-free base) |
| Kubernetes posture and CIS benchmarks | Kubescape (NSA, MITRE ATT&CK, CIS frameworks), kube-bench (CIS Kubernetes Benchmark) |
| Runtime threat detection | Falco (syscall-based, alerting), Tetragon (eBPF kernel-level, Cilium project, <1% overhead, detection + enforcement), KubeArmor (eBPF + LSM enforcement, CNCF Sandbox) |
| Automated runtime response | Falco Talon (automated response actions triggered by Falco alerts) |
| Kubernetes admission policy | OPA Gatekeeper (Rego), Kyverno (YAML-native, supports `verify-images`, mutating policies), Kubernetes Pod Security Admission (built-in, no CRD) |
| IaC security scanning | Checkov (1,000+ policies, graph-based cross-resource checks), KICS (2,400+ Rego queries, 22+ IaC platforms), Trivy (absorbed tfsec check library), Snyk IaC, Semgrep |
| Policy as code (generic) | Conftest (OPA Rego for any structured format), OPA |
| Secret scanning (git/repo) | Gitleaks (fast, pre-commit), TruffleHog (live credential verification, 800+ types), detect-secrets (baseline methodology, low false-positive rate) |
| Secret scanning (built-in) | GitHub secret scanning, GitLab secret detection |
| Secret management | HashiCorp Vault, External Secrets Operator (ESO — syncs from Vault/AWS SSM/GCP Secret Manager to Kubernetes Secrets), Sealed Secrets (Bitnami — encrypted secrets committed to git) |
| Workload identity | SPIFFE/SPIRE (platform-agnostic workload identity, used by Sigstore Fulcio for keyless signing) |
| Image signing and verification | Sigstore Cosign (keyless and key-based signing), Sigstore policy-controller (admission enforcement of image signatures) |
| Supply chain transparency | Rekor (Sigstore transparency log, immutable signing record), in-toto (supply chain attestation framework, SLSA provenance uses in-toto format) |
| SAST / code scanning | Semgrep, Bearer (privacy-focused SAST) |
| seccomp / AppArmor | Kubernetes seccomp profiles, `securityContext.seccompProfile`, AppArmor annotations, KubeArmor LSM policies |
| Network segmentation | Kubernetes NetworkPolicy, Cilium NetworkPolicy (eBPF-based) |

Note on tool status: Terrascan was archived in November 2025 — migrate existing Terrascan users to Checkov, KICS, or Trivy. tfsec is now absorbed into Trivy and its check library is carried forward there.

## Workflow Notes

- Build the threat-control model before proposing changes. Do not jump from a finding to a fix without naming the boundary it crosses.
- Treat scanners, policy, signing, and runtime controls as complementary layers. Prefer the control that closes root cause across the widest applicable surface.
- Keep the remediation concrete: exact config keys, policy names, image digests, namespaces, flags, or admission points matter.
- Prefer controls that are enforceable automatically in CI, admission, or runtime over one-off manual review.
- Do not overfit the fix to one symptom if a higher-level control family would prevent recurrence.
- Distinguish observed evidence from inference, and avoid claiming a control works where it was not validated.
- When selecting between Falco and Tetragon: prefer Falco for detection-first alerting pipelines; prefer Tetragon for enforcement (kernel-level, <1% overhead); combine them where detection breadth and enforcement depth are both needed.
- When selecting between OPA Gatekeeper and Kyverno: prefer Kyverno for teams that want YAML-native policy without Rego; prefer Gatekeeper for teams already invested in OPA and needing audit-mode across fleet.
- When selecting secret management: prefer External Secrets Operator for teams syncing from existing secret stores (Vault, AWS SSM, GCP); prefer Sealed Secrets for teams that need encrypted secrets committed to git without an external secret store.
- When selecting base images: prefer Wolfi/Chainguard minimal images when CVE surface reduction is the primary goal; verify the image provides the runtime dependencies the workload needs before enforcing fleet-wide.

