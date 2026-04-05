---
name: execution-tracker
description: Create a predictive, AI-enhanced tracking model for operational accountability, resource optimization, and risk-adjusted forecasting.
trigger: When a project requires deep execution visibility, predictive delay tracking, and structured accountability.
best_guess_output: A predictive execution model with CPM logic, RACI assignments, and risk-adjusted milestone forecasts.
output_artifacts: knowledge/business-ops-execution-tracker.md
section_anchor: execution-tracker
done_when: All workstreams have clear owners, critical paths are identified, and the system can predict delays based on resource load.
---

# Execution Tracker

## Purpose
This skill encodes a high-fidelity execution tracking method combining predictive analytics with expert accountability frameworks. It moves beyond static status reporting to a dynamic, risk-aware model that identifies bottlenecks before they occur. It explicitly does NOT perform basic manual data entry without a structured model.

## Required Inputs and Assumptions
Define the following before analysis:
- **Project Scope/Milestones**: What must be tracked.
- **Resource Pool**: List of executors and their theoretical capacity.
- **Historical Velocity**: Past completion rates (if available).
- **Assumptions**: If velocity is unknown, apply a 20% "Cold Start" buffer.

## Input Mode and Evidence Path
Gather evidence hierarchically:
1. **Live System Interaction**: Direct queries to ClickUp Brain or Asana Intelligence via primary tools.
2. **Predictive Analytics Access**: Ingesting Fever Charts and Future Load Graphs from Epicflow.
3. **Documentation Review**: Cross-referencing PRDs and Project Manifests in the repository.
4. **Inference**: Determining logical dependencies (e.g., 'A must precede B') when not explicitly stated.

## Tool Stack (Capabilities)
Define access layers:
- **Knowledge Layer**: ClickUp Brain (AI Project Manager/Knowledge Manager).
- **Workflow Layer**: Asana Intelligence (Goal tracking, Workflow automation).
- **Predictive Layer**: Epicflow (Risk-adjusted forecasting, CPM visualization).
- **Documentation Layer**: Notion, Linear (Artifact storage).

## Tool Routing (Decision System)
- **If resource overloading is suspected**: Route through **Epicflow** for Future Load analysis.
- **If finding specific task status in large datasets**: Use **ClickUp Brain**'s semantic search.
- **If automating multi-thread status updates**: Synchronize via **Asana Intelligence**.

## Environment and Reproducibility
- **Platform**: Modern 2026 SaaS PM Ecosystem.
- **State**: Auth-dependent; requires access to relevant workspaces.
- **Reproducibility**: Analysis must be reproducible using the same data snapshot from the tool stack.

## Model Building (Before Analysis)
Before evaluating execution, the agent must construct:
1. **The Critical Path Method (CPM) Graph**: Mapping the dependency chain that determines the finish line.
2. **The RACI Assignment Matrix**: Defining Responsibility, Accountability, Consulted, and Informed roles.
3. **Risk-Adjusted Capacity Model**: Overlaying resource availability on CPM tasks to find bottleneck intersections.

## Core Method Execution
1. **Dependency Mapping**: identify the critical path (CPM) to find non-slack tasks.
2. **Accountability Layering**: Apply RACI to every milestone. If one task has >1 'A', flag as an accountability risk.
3. **Predictive Forecasting**: Apply risk-adjusted estimates (P50 vs P90) to durations.
4. **Fever Chart Analysis**: Plot buffer consumption vs. work completion.
5. **Load Balancing**: Use Epicflow analytics to suggest resource shifts for "Red" workstreams.

## Structured Findings
Each finding must include:
- **Observation**: What is happening in the tracker.
- **Evidence**: Specific data point (e.g., "Resource X is at 140% load").
- **CPM Impact**: Impact on the critical path (in days/hours).
- **RACI Implication**: Who is accountable for the fix.

## Prioritization Logic
- **P0**: Delays on the Critical Path or missing Accountable owners.
- **P1**: Buffer consumption exceeding 50% without commensurate progress.
- **P2**: Resource overallocation for non-critical path tasks.

## Pattern Detection
Identify recurring failures:
- **"Bottlenecking"**: A single resource appearing in the critical path of multiple workstreams.
- **"Buffer Bleed"**: Consistent use of P90 estimates indicating systemic underestimation.
- **"Ghost Work"**: Tasks with progress but no updates in the AI knowledge manager.

## Recommendations
- **Directional Fixing**: Reassigning accountability or re-sequencing non-critical tasks.
- **Strategic Scaling**: Recommending resource additions based on future load clusters.
- **Automation**: Offloading administrative reporting to AI agents.

## Coverage Map
- **Deeply Analyzed**: Critical Path, Resource Load, RACI integrity.
- **Partially Analyzed**: Secondary stakeholders, informal communication channels.
- **Not Analyzed**: External dependencies not logged in the tool stack.

## Limits and Unknowns
- Accuracy depends on data freshness in ClickUp/Asana.
- Model cannot predict external "Black Swan" events outside the tracked domain.

## Workflow Rules
- Build the CPM model first.
- Fact vs. Inference labeling for all status summaries.
- Never declare "On Track" if the P90 forecast exceeds the deadline.

## Output Contract
- **Target**: `knowledge/business-ops-execution-tracker.md`.
- **Merge Rules**: Standalone deliverable. Do not modify the core project manifest.
- **Artifacts**: Must include a Mermaid-formatted CPM diagram and a RACI table.
