---
name: problem-framing
description: Translate product goals, evidence, user context, and delivery constraints into a design-ready frame by building an actor-job-constraint-success model before exploring solutions.
trigger: When design work needs a stable problem definition, bounded scope, and evidence-backed success criteria before flows or screens are produced.
analysis_framework: JTBD-informed problem framing with assumption mapping, constraint analysis, and success-signal definition
primary_mcp: notion, repository
fallback_tools:
  - reference/ground
  - search_query
required_inputs:
  - product goal, opportunity, or request
  - target users or segments
  - existing evidence, research, or feedback signals
  - delivery constraints, dependencies, or non-negotiables
  - current experience or workflow context when known
recommended_passes:
  - evidence inventory
  - actor and job model construction
  - problem boundary and anti-goal definition
  - constraints and risk mapping
  - success signal definition
tool_stack:
  workspace:
    primary: [notion, repository]
    secondary: [reference/ground]
  research_repositories:
    primary: [dovetail]
    secondary: [miro, productboard]
  enrichment:
    primary: [search_query]
  fallback:
    primary: [reference/ground, search_query]
tool_routing:
  - if: product briefs, strategy docs, and repo context are accessible
    use: [notion, repository]
  - if: tagged research evidence, transcripts, or insight repositories exist
    use: [dovetail]
  - if: continuous customer feedback or feature evidence is centralized in planning tools
    use: [productboard]
  - if: collaborative synthesis or workshop framing artifacts are the strongest evidence source
    use: [miro]
  - if: external domain constraints or category norms materially affect the framing
    use: [search_query]
  - if: only static notes or partial artifacts exist
    use: [reference/ground, search_query]
best_guess_output: A design framing artifact with explicit users, jobs, constraints, risks, success criteria, and decision-driving unknowns.
output_artifacts:
  - knowledge/runs/<run-id>/product-designer-problem-framing.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: The design problem is bounded, evidence-tagged, and stable enough that downstream flow and wireframe work can proceed without rediscovering the brief.
---

# Problem Framing

## Purpose

Translate product goals, evidence, user context, and delivery constraints into a design-ready framing before solution work begins.

This skill applies JTBD-informed framing, assumption mapping, and constraint analysis to define what problem the design work is actually solving.

This skill does not jump ahead to detailed UI solutions, treat opinions as evidence, or hide uncertainty behind vague problem statements.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/product-designer-problem-framing.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/runs/<run-id>/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

## Required Deliverable Sections

Within `## Skill: problem-framing`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Framing objective`: Define what decision this framing must support and why the work needs framing before solutioning.
- `### Required inputs and assumptions`: State the known product goal, target users, evidence, constraints, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live product and current work context, structured workspace artifacts, research repositories or workshop artifacts, static screenshots or exports, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record the current project state, relevant builds, feature flags, market or platform assumptions, and doc or repo versions when known.
- `### Problem model`: Build the actor -> context -> job -> friction -> constraint -> success model before writing conclusions.
- `### Framing passes`: List the passes used such as evidence inventory, actor and job model construction, problem boundary and anti-goal definition, constraints and risk mapping, and success signal definition.
- `### Problem statement`: State the bounded design problem in one crisp statement.
- `### Users, context, and jobs`: Define the primary actors, their context, and the job they are trying to complete.
- `### Current friction and evidence`: Summarize the strongest evidence showing why the current state is not good enough.
- `### Constraints, dependencies, and anti-goals`: Make non-negotiables, exclusions, and delivery realities explicit.
- `### Risks and assumption map`: Separate proven constraints from assumptions that still need validation.
- `### Success criteria and leading signals`: Define what would indicate the framing is correct and the design work is solving the right problem.
- `### Framing findings`: Record findings using the required finding schema below.
- `### Prioritized framing risks`: Include all major framing risks as standalone findings and group lower-risk uncertainty into patterns.
- `### Systemic patterns`: Group recurring uncertainty such as goal ambiguity, user mismatch, missing operational constraints, or success-measure gaps.
- `### Recommendations`: Offer directional next steps that reduce framing uncertainty without pretending the solution is already known.
- `### Coverage map`: State what was deeply framed, partially framed, and not framed.
- `### Limits and unknowns`: Explain what could not be validated and what still requires real user or business confirmation.

For each finding inside `### Framing findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Affected actor or job:
- Constraint or risk:
- Impact on design scope:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest evidence path available: live product and current context -> structured workspace artifacts -> research repositories or workshop synthesis -> static artifacts -> inference.
- Start with `notion, repository` when the assignment has product briefs, tickets, existing strategy notes, or implementation context that can anchor the frame.
- Use `dovetail` when tagged research evidence, transcripts, or insight clustering are the best available source of user truth.
- Use `productboard` when continuous customer evidence, feature-level insight links, or trend summaries materially sharpen the problem boundary.
- Use `miro` when workshop synthesis, framing canvases, or collaborative clustering materially shape the problem definition.
- Use `search_query` only when external domain expectations, competitive norms, or market constraints materially affect the problem boundary.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A design framing artifact with explicit users, jobs, constraints, risks, success criteria, and decision-driving unknowns.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-source framing pass.

## Workflow Notes

- Build the actor-job-constraint-success model before analysis. Do not jump straight to UI ideas or solution recommendations.
- Treat `required_inputs` as real prerequisites. If the goal, users, or evidence are missing, infer a provisional set, prefix each inferred item with `Assumed context:`, and lower confidence for downstream findings that depend on it.
- Use JTBD-style language when it clarifies user motivation, but keep the framing grounded in the actual assignment rather than abstract aspiration.
- Separate observed evidence from inferred explanation and from recommendation direction.
- Make anti-goals explicit. Good framing says what the design work is not trying to solve in this pass.
- Prefer exact product or business language when it materially affects scope, commitments, or metrics.
- After all passes, consolidate repeated uncertainty into systemic patterns before prioritization.
- Do not present open assumptions as settled truth just because the team needs momentum.

