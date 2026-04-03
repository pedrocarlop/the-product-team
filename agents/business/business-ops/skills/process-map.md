---
name: process-map
description: Engineering expert-grade process maps using AI-driven mining, generative diagramming, and value-based governance.
trigger: When a workflow is inefficient, undergoing transformation, or needs formal governance and optimization.
best_guess_output: A high-fidelity BPMN 2.0 process model, SIPOC framework, and Value Stream Mapping (VSM) analysis.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops-process-map.md
done_when: A complete SIPOC, BPMN 2.0 current/target state, and VSM analysis with validated ownership and handoffs are documented.
---

# Process Map

## Purpose
Map, analyze, and optimize business processes using modern process intelligence and modeling standards (BPMN 2.0, SIPOC, VSM). This skill transforms raw operational data and stakeholder inputs into actionable, governed process models that eliminate waste and clarify ownership.

## Required Inputs and Assumptions
Define the following before analysis:
- **Raw process logs**: CSV/XES from ERP/CRM or detailed stakeholder walkthroughs.
- **Key Actors**: List of humans and AI agents involved.
- **Business Goals**: Specific objectives (e.g., reduce cycle time by 20%).
- **Assumptions**: If detailed logs are missing, the agent will infer the flow from documentation and label as "Inferred Current State."

## Input Mode and Evidence Path
Gather evidence hierarchically:
1. **Live System Logs**: Direct access to Celonis/SAP logs (Highest Confidence).
2. **DTO (Digital Twin)**: Real-time monitoring data from SAP Signavio.
3. **Structured Interviews**: Stakeholder testimony on handoffs and edge cases.
4. **Static Documentation**: Existing SOPs or old flowcharts.
5. **Inference**: Based on standard industry patterns for the specific process type.

## Tool Stack (Capabilities)
Define access layers:
- **Mining Layer**: Celonis (Process Mining), SAP Signavio (DTO Monitoring).
- **Modeling Layer**: Lucidchart AI (Generative BPMN), SAP Signavio Process Manager.
- **Visualization Layer**: Mermaid.js (Structured diagramming).

## Tool Routing (Decision System)
- **IF** event logs are available **USE** [Celonis] for automated discovery.
- **IF** governance and compliance are priorities **USE** [SAP Signavio] for DTO setup.
- **IF** rapid visualization from text is needed **USE** [Lucidchart AI].

## Environment and Reproducibility
- **Platform**: Process Intelligence Clouds (Celonis/Signavio).
- **State**: Snapshot dates, log versions, and stakeholder participant list.
- **Reproducibility**: Models must be exportable in BPMN 2.0 XML or standard formats.

## Model Building (Before Analysis)
Before evaluating the process, the agent must construct:
1. **SIPOC Framework**: Define Suppliers, Inputs, Process (high-level), Outputs, and Customers.
2. **Actor Profile**: Catalog all humans and AI agents involved.
3. **Object Model**: Map the data entities (e.g., Invoice, SKU) and their transformations.

## Core Method Execution
1. **SIPOC Scoping**: Align on the start and end points of the process.
2. **Process Discovery**: Run Celonis mining to find the "Happy Path" and all "Variants."
3. **BPMN 2.0 Modeling**: Create the **Current State** map using standard notation.
4. **Value Stream Mapping (VSM)**: Calculate Cycle Time (CT), Lead Time (LT), and Value-Added vs. Non-Value-Added (NVA) time.
5. **Gap & Bottleneck Analysis**: Identify handoff friction and "shadow AI" usage.
6. **Target State Engineering**: Design the optimized flow in Lucidchart AI.
7. **Governance Implementation**: Set up automated approval flows in SAP Signavio.

## Structured Findings
Each finding must include:
- **Observation**: Detailed description of the process deviation or bottleneck.
- **Evidence**: Specific log entry or stakeholder quote.
- **Impact**: Efficiency loss, compliance risk, or financial cost.
- **Confidence**: High/Medium/Low.

## Prioritization Logic
- **Critical**: Compliance violations or complete process blocks.
- **High**: Bottlenecks adding >30% delay to the happy path.
- **Medium**: Redundant handoffs or minor tool inefficiencies.
- **Low**: Aesthetic or minor documentation discrepancies.

## Pattern Detection
Identify recurring failures:
- **"Systemic Waste"**: Recurring NVA activities across variants.
- **"Handoff Silos"**: Where data requires manual re-entry between tools.
- **"Governance Drift"**: Gaps between the "Designed" and "Executed" process.

## Recommendations
- **Directional Fixing**: Link to specific VSM or BPMN findings.
- **Strategic Scaling**: Prioritize automation where predictive AI suggests high ROI.
- **Governance**: Define clear RACI for the target state.

## Coverage Map
- **Deeply Analyzed**: Modules with log evidence.
- **Partially Analyzed**: Modules with stakeholder input only.
- **Not Analyzed**: Explicitly excluded scope.

## Limits and Unknowns
- **Data Gaps**: Missing logs for legacy systems.
- **Human Factor**: Variability in manual steps that cannot be tracked.
- **External Dependencies**: Third-party APIs or vendor delays.

## Workflow Rules
- Build the SIPOC before the BPMN.
- Distinguish between the "Happy Path" and "Exception Paths."
- Use standard BPMN 2.0 symbols only.

## Output Contract
- **Target**: `logs/active/<project-slug>/deliverables/business-ops-process-map.md`.
- **Merge Rules**: Standalone deliverable.
- **Artifacts**: BPMN 2.0 diagram and SIPOC table.
