---
name: observe
description: Verify infrastructure and service health using logs, metrics, traces, alerts, and deployment checks after a change ships to production.
---

# Observe

## Purpose

Use this skill to confirm that a deployed infrastructure or service change is healthy, measurable, and producing the signals needed to operate it safely in production.

## When to Use

- After a deployment, infrastructure change, or configuration update needs validation
- When creating or updating dashboards, alerts, SLOs, or on-call runbooks
- When diagnosing service-level issues: latency degradation, error rate spikes, resource saturation, or cascading failures
- When validating that a new service, scaling change, or failover path is observable

## When Not to Use

- When no change has been deployed and the next step is planning or architecture
- When the main problem is rollout sequencing or feature flag coordination rather than runtime behavior
- When the task is incident command or active stabilization rather than post-deploy verification

## Required Inputs

- The service, infrastructure component, or deployment being verified
- The expected healthy signals: latency targets, error rate baselines, resource utilization thresholds
- The observability stack: logging platform, metrics system, tracing backend, alerting rules
- Any SLOs, SLAs, or operational thresholds that define success
- The deployment method and any canary, blue-green, or rolling update state

## Workflow

1. Define the evidence that would prove the deployment is healthy across the infrastructure layer.
2. Check service-level metrics: request rate, error rate, latency percentiles, and resource utilization.
3. Inspect logs for the deployed version: structured format, appropriate log levels, no sensitive data exposure.
4. Verify distributed traces cover the critical request paths through the changed service.
5. Confirm alerts are configured for the failure modes that matter: threshold breaches, anomaly detection, and dependency failures.
6. Compare post-deploy metrics against the pre-deploy baseline and flag any regression.
7. Document findings and any observability gaps that need follow-up.

## Design Principles / Evaluation Criteria

- Production visibility is infrastructure, not a feature request
- Every deployed service must be observable enough to diagnose without SSH access
- Alerts should fire for conditions the on-call engineer can act on, not for noise
- Missing telemetry in a critical path is a deployment risk, not a backlog item
- SLO-aligned measurement beats vanity metrics

## Output Contract

- A deployment health verification summary with metrics evidence
- Service-level indicator status: latency, error rate, availability, and resource utilization
- Alert and dashboard coverage assessment for the changed path
- Any observability gaps, missing traces, or inadequate log structure that need remediation
- A clear pass/fail statement on deployment health with the evidence supporting it

## Examples

### Example 1

Input:
- Task: Validate a newly deployed microservice behind a load balancer
- Concern: No baseline metrics exist and alerting has not been configured

Expected output:
- Establish baseline: capture p50/p95/p99 latency, error rate, and CPU/memory utilization for 30 minutes post-deploy
- Configure alerts: error rate > 1% for 5 minutes, p99 latency > 500ms for 5 minutes, pod restart count > 2
- Gap: No distributed tracing configured; request path from gateway to service is not traceable
- Status: Conditionally healthy; tracing gap must be resolved before the service handles production traffic

## Guardrails

- Do not declare a deployment healthy without checking metrics, logs, and traces
- Do not treat the absence of alerts firing as evidence of health
- Do not configure alerts that the on-call engineer cannot diagnose or act on
- Do not expose secrets, tokens, or PII in logs or traces
- Do not skip baseline comparison when a meaningful pre-deploy baseline exists

## Optional Tools / Resources

- Prometheus, Grafana, Datadog, or equivalent metrics and dashboards
- ELK, Loki, or equivalent log aggregation
- Jaeger, Tempo, or equivalent distributed tracing
- PagerDuty, OpsGenie, or equivalent alerting
- Infrastructure-as-code definitions for the deployed service
- Incident history or prior debugging notes for the affected service
