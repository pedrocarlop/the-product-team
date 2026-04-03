---
name: interaction-spec
description: Specify interaction behavior by modeling triggers, states, rules, feedback, and exceptional conditions so implementation can reproduce the intended behavior without guessing.
trigger: When implementation needs behavior-level clarity across user actions, system responses, states, and recovery paths.
analysis_framework: microinteraction framing plus state-machine reasoning
primary_mcp: figma, repository
fallback_tools:
  - paper
  - reference/trace
required_inputs:
  - target flow, screen, or component
  - states and triggers in scope
  - platform or device context
  - dependency systems or APIs when known
  - accessibility, timing, or motion constraints when known
recommended_passes:
  - trigger inventory
  - state model construction
  - rule and guard review
  - feedback and timing review
  - exception and recovery review
tool_stack:
  design_behavior:
    primary: [figma, repository]
    secondary: [protopie, axure, uxpin]
  runtime_validation:
    primary: [chrome_devtools]
  fallback:
    primary: [paper, reference/trace]
tool_routing:
  - if: source designs and implementation context are both accessible
    use: [figma, repository]
  - if: complex transitions, conditions, or variables need to be simulated before specification
    use: [protopie, axure, uxpin]
  - if: live runtime behavior can resolve ambiguity around state, timing, or feedback
    use: [chrome_devtools]
  - if: only notes, traces, or static references remain
    use: [paper, reference/trace]
best_guess_output: An interaction spec tied to triggers, state transitions, rules, and clearly labeled ambiguities.
output_artifacts: logs/active/<project-slug>/deliverables/product-designer-interaction-spec.md
done_when: An engineer can implement the interaction without guessing behaviors, hidden state rules, or recovery logic.
---

# Interaction Spec

## Purpose

Define behavior precisely enough that implementation does not invent missing rules.

This skill applies microinteraction thinking and state-machine reasoning to specify what triggers an interaction, how state changes, what feedback appears, and how exceptions behave.

This skill does not finalize pixel-perfect visuals or assume runtime behavior is correct unless it has been checked.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/product-designer-interaction-spec.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: interaction-spec`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Interaction framing`: Define the target flow, screen, or component and what implementation decision this spec must support.
- `### Required inputs and assumptions`: State the known triggers, states, platform context, dependencies, and inferred assumptions required to complete the spec.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live interaction, structured system access, design or documentation artifacts, screenshots or static input, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and what they could not validate.
- `### Environment and reproducibility`: Record platform, browser or device, build or prototype version, auth state, and artifact dates when known.
- `### Interaction model`: Build the model first by listing actors, interface objects, triggers, states, and system dependencies before specifying rules.
- `### Specification passes`: List the passes used such as trigger inventory, state model construction, rule and guard review, feedback and timing review, and exception and recovery review.
- `### Trigger map`: List user actions, system events, entry conditions, and prerequisites in scope.
- `### State transition model`: Describe states, transitions, exit conditions, and illegal or blocked transitions.
- `### Rules, guards, and dependencies`: Specify deterministic rules, validation logic, permissions, and dependency checks that govern behavior.
- `### Feedback, timing, and motion expectations`: Define response timing, loading feedback, confirmations, errors, and motion behavior when relevant.
- `### Failure, recovery, and accessibility behaviors`: Call out failure states, retry behavior, focus behavior, keyboard behavior, and assistive-tech-relevant expectations when known.
- `### Interaction gaps and ambiguities`: Record the highest-signal missing rules or unclear transitions using the required finding schema below.
- `### Prioritized implementation risks`: Include all implementation-blocking ambiguities as standalone findings, group lower-impact details into patterns, and prefer no more than 12 standalone findings by default unless more are materially distinct.
- `### Systemic interaction patterns`: Group recurring issues such as missing feedback, ambiguous guards, incomplete state coverage, or inconsistent transitions.
- `### Coverage map`: State what states and interaction paths were deeply specified, lightly specified, or not specified.
- `### Directional implementation guidance`: Translate the behavior into implementation guidance without pretending code details are fully designed.
- `### Limits and unknowns`: Explain what still requires runtime validation, accessibility verification, or upstream product clarification.

For each finding inside `### Interaction gaps and ambiguities`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Trigger:
- Expected state change:
- Missing or ambiguous rule:
- Impact:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest evidence path available: live interaction -> structured systems -> design or documentation artifacts -> screenshots or static inputs -> inference.
- Start with `figma, repository` when source designs and implementation context are both accessible.
- Use `protopie`, `axure`, or `uxpin` when conditional transitions, variables, or richer interaction logic need to be simulated before specification.
- Use `chrome_devtools` when live runtime behavior can confirm or disambiguate timing, state changes, or feedback logic.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/trace`.
- If both paths fail, produce the best-guess output described as: An interaction spec tied to triggers, state transitions, rules, and clearly labeled ambiguities.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Use named external tools only when they are connected or explicitly available in the environment.

## Workflow Notes

- Build the interaction model first. Do not start by writing vague behavior notes.
- Treat `required_inputs` as real prerequisites. If the trigger set, state scope, or dependency model is missing, infer a provisional set, prefix each inferred item with `Assumed interaction input:`, and lower confidence for dependent findings.
- Start with triggers and states, then define rules and guards, then add feedback and timing, then layer failure and recovery behavior.
- Prefer explicit transition language over intent language. Use phrases such as `when X happens, state changes from A to B` instead of vague outcome statements.
- Make hidden system behavior visible. Many implementation errors come from undocumented loading, disabled, rate-limited, expired, or error states.
- Distinguish clearly between observed behavior, inferred rule, and recommendation direction.
- Group small behavioral clarifications into patterns when they point to the same missing rule family.
- Do not treat default browser or framework behavior as sufficient unless it matches the intended experience.

