---
name: tooling-audit
description: Encode expert workflow for assessing tool sprawl, gaps, and ownership using TCO, ROI, and Shadow AI Detection.
trigger: When systems or tools are slowing execution down or during annual operating rhythm reviews.
best_guess_output: A comprehensive SaaS inventory with TCO analysis, ROI justification, and a keep/change/remove roadmap.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops-tooling-audit.md
done_when: The stack decision is actionable, justified by TCO/ROI benchmarks, and identifies Shadow AI risks.
---

# Tooling Audit

## Purpose
Assess tool sprawl, gaps, and ownership across the operating stack using financial and operational metrics. This skill identifies redundancy, calculates Total Cost of Ownership (TCO), evaluates Return on Investment (ROI), and detects Shadow AI usage to optimize the organization's tech stack.

## Required Inputs and Assumptions
Define the following before analysis:
- **Core Inventory**: List of tools from SaaS Management Platforms (SMP) or finance records.
- **Spend Data**: Monthly/Annual costs.
- **Utilization Data**: Active user counts and seat allocation.
- **Assumptions**: If spend is unknown, use 2026 industry benchmarks from Vertice. Assume unmanaged AI tools exist if no formal AI governance is documented.

## Input Mode and Evidence Path
Gather evidence hierarchically:
1. **Live Interaction**: Access to Zylo, CloudEagle, or Vertice dashboards.
2. **Structured System Access**: Finance records (ERP), SSO logs (Okta/Azure AD), and vendor invoices.
3. **Design Artifacts**: Tech stack diagrams or procurement documentation.
4. **Inference**: Market rates for enterprise SaaS in 2026 for unpriced tiers.

## Tool Stack (Capabilities)
Define access layers:
- **Inventory Layer**: Zylo (SaaS Management, lifecycle tracking).
- **Governance Layer**: CloudEagle (AI Governance, Shadow AI detection).
- **Optimization Layer**: Vertice (SaaS Spend Optimization, TCO/ROI benchmarking).

## Tool Routing (Decision System)
- **IF** spend > $100k **USE** [Vertice] for deep spend optimization.
- **IF** AI apps are detected in logs **USE** [CloudEagle] for Shadow AI compliance checks.
- **FOR** general inventory/lifecycle **USE** [Zylo] to identify overlapping software.

## Environment and Reproducibility
- **Platform**: SaaS Management and Procurement Platforms.
- **State**: Current active subscriptions and user auth state.
- **Reproducibility**: Analysis must be reproducible using the same data snapshot from the SMP stack.

## Model Building (Before Analysis)
Before evaluating the stack, the agent must construct:
1. **Stack Capability Model**: Mapping tools to business capabilities (e.g., CRM, Project Management).
2. **Lifecycle Map**: Categorizing tools (Acquisition, Deployment, Active, At-Risk, Sunsetting).
3. **Integration Graph**: Mapping data flows between tools to find silos.

## Core Method Execution
1. **Shadow AI Detection**: Scan logs for unauthorized AI subscriptions and risk-level categorization.
2. **TCO Analysis**: Calculate Direct (License) and Indirect (Management, Training, Integration) costs.
3. **ROI Evaluation**: Map tool usage to business outcomes (e.g., efficiency gains) and compare against 2026 benchmarks.
4. **Rationalization**: Identify overlaps (e.g., Zoom vs Teams) and draft a Keep/Change/Remove matrix.

## Structured Findings
Each finding must include:
- **Observation**: Description of sprawl, gap, or risk.
- **Evidence**: Specific dashboard data or log entry.
- **TCO Impact**: Combined direct/indirect cost impact.
- **ROI Score**: 1-10 based on value vs cost.
- **Confidence**: High/Medium/Low.

## Prioritization Logic
- **Critical (P0)**: Shadow AI risks (security) or massive overspend (>25% waste).
- **High (P1)**: Redundant tools with high TCO.
- **Medium (P2)**: Underutilized seats or minor integration friction.

## Pattern Detection
Identify recurring failures:
- **"Horizontal Bloat"**: Departments buying different tools for the same capability.
- **"AI Fragmentation"**: Individual AI seats instead of enterprise licenses.
- **"Zombie SaaS"**: Automatic renewals for tools with zero logins in 90 days.

## Recommendations
- **Directional Fixing**: Consolidation or negotiation before termination.
- **Strategic Scaling**: Moving towards enterprise licenses for fragmented AI usage.
- **Governance**: Implementing Intake-to-Procure workflows.

## Coverage Map
- **Deeply Analyzed**: Core departments (Sales, Marketing, Engineering).
- **Partially Analyzed**: Shadow IT, small departmental apps.
- **Not Analyzed**: Hardware and on-premise infrastructure.

## Limits and Unknowns
- **User Sentiment**: Qualitative value of a tool vs quantitative ROI.
- **Hidden Growth**: Free-tier usage that may scale exponentially.

## Workflow Rules
- Build the **Stack Capability Model** before making "Remove" recommendations.
- Distinguish between "Waste" (unused) and "Redundancy" (overlap).
- Check the 2026 Vertice benchmark for any replacement tool.

## Output Contract
- **Target**: `logs/active/<project-slug>/deliverables/business-ops-tooling-audit.md`.
- **Merge Rules**: Standalone deliverable.
- **Artifacts**: Stack Rationalization Matrix; TCO/ROI Chart.
