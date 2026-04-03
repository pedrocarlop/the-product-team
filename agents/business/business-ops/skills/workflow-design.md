---
name: workflow-design
description: Architect high-fidelity operational workflows using Design Thinking and DMAIC methodologies.
trigger: When a team requires a repeatable, scalable, and automated operating model.
best_guess_output: A comprehensive workflow architecture deliverable with automation logic and role definitions.
output_artifacts: logs/active/<project-slug>/deliverables/business-ops-workflow-design.md
done_when: The workflow is mapped, prototyped in high-fidelity, and ready for automation deployment.
---

# Workflow Design

## Purpose
Design and architect end-to-end business workflows. This skill applies **IDEO Design Thinking** for human-centricity and **Lean Six Sigma (DMAIC)** for operational excellence. It produces high-fidelity prototypes and automation specifications using 2026-standard tools.

## Required Inputs and Assumptions
Define the following before analysis:
- **Business Objective**: Primary goal of the new or redesigned workflow.
- **Stakeholder Map**: Roles, DRIs, and impact.
- **Constraints**: Compliance, tool access, and budget.
- **Assumptions**: If the "As-Is" state is missing, the agent will infer an industry-standard baseline for the organizational type.

## Input Mode and Evidence Path
Gather evidence hierarchically:
1. **System Audit**: Direct review of Notion/Linear/GitHub for existing task patterns.
2. **Artifact Analysis**: Review of meeting notes, PRDs, or legacy process documentation.
3. **Prototype Testing**: Observational data from low-fidelity flow testing.
4. **Inference**: Applying best practices from similar organizational scale or industry benchmarks.

## Tool Stack (Capabilities)
Define access layers:
- **Cognitive Layer**: Vellum AI (Prompt Engineering & Agent Reasoning lifecycle).
- **Orchestration Layer**: Bika.ai (Automation Orchestration, state management).
- **Execution Layer**: Make (Visual Logic, API connectivity).

## Tool Routing (Decision System)
- **IF** complex reasoning or agent-led tasks are required **USE** [Vellum AI].
- **IF** the workflow requires sophisticated cross-tool state management **USE** [Bika.ai].
- **IF** high-volume visual logic and data sync are needed **USE** [Make].

## Environment and Reproducibility
- **Version Control**: Vellum prompt versions and Make blueprint snapshots.
- **State**: Current tool integrations and database schemas.
- **Reproducibility**: Must be reproducible using the exported logic/blueprint in the designated tool.

## Model Building (Before Analysis)
Before designing the workflow, the agent must construct:
1. **Workflow Topology Model**: Mapping distinct States (e.g., Draft, Review, Live) and Triggers (Webhook, Time, Manual).
2. **Value Stream Mapping**: Identifying the "ValuePath" that directly contributes to the objective.
3. **I/O Schema**: Defining data input/output requirements for every node.

## Core Method Execution
1. **Empathize & Define (DMAIC-D)**: Conduct "Voice of the Business" analysis and define specific KPIs.
2. **Measure & Analyze (DMAIC-M/A)**: Map current friction and perform Root Cause Analysis on failures.
3. **Ideate & Prototype (Design Thinking)**: Design the TO-BE logic using **Make** for flow and **Vellum AI** for reasoning.
4. **Hifi-Modeling**: Create high-fidelity wireflows with explicit integration points.
5. **Improve & Control (DMAIC-I/C)**: Design error-handling sub-flows and define the maintenance operating rhythm.

## Structured Findings
Each finding must include:
- **Observation**: Specific friction point or gap in the current flow.
- **Automation Logic**: Tool, Logic (Pseudo-code), and Prerequisite data.
- **Bottleneck Score**: 1-10 based on impact.
- **Confidence**: High/Medium/Low.

## Prioritization Logic
- **P1**: Core value-delivery steps (the "Golden Path").
- **P2**: Automation of high-frequency manual administrative tasks.
- **P3**: Edge case handling and executive reporting.

## Pattern Detection
Identify recurring failures:
- **"Silent Failures"**: Work stalls without notification.
- **"Shadow Work"**: Critical steps occurring in Slack/Email outside of the system of record.
- **"Linearity Traps"**: Workflows that fail because they don't account for recursive loops.

## Recommendations
- **Logic Specifications**: Directional logic for Make/Bika blueprints.
- **Agentic Integration**: Suggesting where Vellum AI reasoning can replace human review checkpoints.
- **Governance**: Recommendation for data integrity rules at the entry/exit points.

## Coverage Map
- **Deeply Analyzed**: Core value-stream steps and primary automation triggers.
- **Partially Analyzed**: Exception handling and edge cases.
- **Not Analyzed**: External vendor-side workflows.

## Limits and Unknowns
- **API Capacity**: Rate limits for Make/Bika.ai integrations.
- **Human Adoption**: Psychological friction points in new workflow adoption.

## Workflow Rules
- Build the **Topology Model** before proposing steps.
- Distinguish between **Deterministic Automation** (Make) and **Agentic Reasoning** (Vellum).
- No workflow should be "Live" without an error-handling path.

## Output Contract
- **Target**: `logs/active/<project-slug>/deliverables/business-ops-workflow-design.md`.
- **Merge Rules**: Standalone deliverable.
- **Artifacts**: Wireflow diagram; I/O Schema table; Automation blueprint specs.
