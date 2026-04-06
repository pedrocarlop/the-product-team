name: wireframe-structure
description: Build low-to-mid fidelity structural wireframes by converting an approved flow into screen-level hierarchy, navigation, and content scaffolding before visual polish begins.
trigger: When teams need screen structure, hierarchy, and task flow clarity before detailed visual design or implementation.
mesh:
  inputs:
    - product-designer:journey-and-flow-design
  next:
    - ui-designer:ui-concept-direction
    - content-designer:microcopy-flow-design
  context: "Converts behavioral flows into structural screen layouts."
analysis_framework: information architecture plus task-flow and hierarchy modeling
primary_mcp: figma
fallback_tools:
  - paper
  - reference/ground
required_inputs:
  - approved or provisional flow in scope
  - target platform, viewport, or device family
  - key tasks, content, and actions that must be supported
  - relevant design-system or product-pattern constraints
  - known technical or delivery limitations when they affect structure
recommended_passes:
  - screen inventory
  - hierarchy and priority mapping
  - navigation model construction
  - repeated pattern identification
  - structural gap review
tool_stack:
  design_system_aligned:
    primary: [figma]
    secondary: [repository]
  low_fidelity_exploration:
    primary: [balsamiq, whimsical]
    secondary: [miro]
  advanced_structural_prototyping:
    primary: [axure]
  fallback:
    primary: [paper, reference/ground]
tool_routing:
  - if: the work must stay aligned to an existing design system or downstream Figma workflow
    use: [figma]
  - if: rapid low-fidelity exploration and fast structural iteration matter more than polish
    use: [balsamiq, whimsical]
  - if: the wireframes need conditional structure, richer states, or inspectable structural documentation
    use: [axure]
  - if: the work starts as collaborative whiteboard structure before becoming screens
    use: [miro]
  - if: only notes, screenshots, or rough references exist
    use: [paper, reference/ground]
best_guess_output: A wireframe set aligned to the flow, with explicit hierarchy, navigation logic, and unresolved structural gaps.
output_artifacts:
  - knowledge/runs/<run-id>/product-designer-wireframe-structure.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Screen structure is clear enough that reviewers can assess hierarchy and task completion without needing visual polish to infer intent.
mesh:
  inputs:
    - product-designer:journey-and-flow-design # Wireframes are the structural realization of the journey flows
  next:
    - ui-designer:ui-concept-direction
    - product-designer:prototype-and-usability-validation
  context: "Wireframing is the structural bridge between flow logic and visual interaction, defining the hierarchy and navigation that the UI designer will then skin."
---

# Wireframe Structure

## Purpose

Build structural wireframes that make task flow, hierarchy, and navigation explicit before high-fidelity design begins.

This skill applies information-architecture and task-flow reasoning to transform an approved flow into screen-level structure.

This skill does not finalize visual styling, substitute for interaction specification, or hide unresolved structural dependencies behind polished mockups.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/product-designer-wireframe-structure.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/runs/<run-id>/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/runs/<run-id>/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

## Required Deliverable Sections

Within `## Skill: wireframe-structure`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Wireframe framing`: Define the assignment type, target user task, scope boundary, and why structural wireframes are needed now.
- `### Required inputs and assumptions`: State the source flow, known constraints, missing content or state details, and any inferred structural assumptions.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: design source and flow artifacts, low-fidelity structural tools, static references, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they supported well, and what they could not validate.
- `### Environment and reproducibility`: Record platform, viewport, device class, orientation, design-system version, and any code or runtime constraints when known.
- `### Screen inventory`: List the screens, panels, overlays, and states covered by the wireframe set.
- `### Structural model`: Build the model first by naming the primary task on each screen, the major content regions, action zones, navigation elements, and repeated placeholders before judging quality.
- `### Content hierarchy`: Explain how information, controls, and supporting context are prioritized on each screen.
- `### Navigation and task flow`: Describe how users move between screens and what structural cues support forward progress, backtracking, and recovery.
- `### Repeated patterns and placeholders`: Identify reusable modules, content slots, tables, cards, forms, or system messages that should stay consistent across the set.
- `### Structural gaps`: Call out missing screens, unresolved content dependencies, state gaps, and structural unknowns.
- `### Structural decisions`: Record the most important structural choices using the required finding schema below.
- `### Prioritized review points`: Highlight the hierarchy decisions or missing elements most likely to affect downstream UI or prototyping work.
- `### Systemic layout patterns`: Group recurring patterns such as action overload, weak scannability, buried primary actions, or inconsistent navigation models.
- `### Directional next moves`: Suggest what should happen next, such as content definition, interaction specification, or divergent visual exploration.
- `### Coverage map`: State which screens were fully structured, partially structured, or left unresolved.
- `### Limits and unknowns`: Explain what could not be decided because of missing flow, content, interaction, or business context.

For each finding inside `### Structural decisions`, use this exact mini-template:

#### Wireframe decision <id>
- Observation:
- Evidence:
- Screen or state:
- Structural choice:
- Tradeoff:
- Impact:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest structural path available: Figma or aligned design source -> low-fidelity wireframing tools -> static references -> inference.
- Start with `figma` when the work must stay anchored to a live design-system workflow or when downstream teams expect screen artifacts there.
- Use `balsamiq` when the team needs fast, low-fidelity structure, editable flows, or sketch-to-wireframe speed without visual overcommitment.
- Use `whimsical` when quick structural collaboration, lightweight wireframes, and simple overlays are more useful than component-level polish.
- Use `axure` when conditional states, richer structural behaviors, annotations, or inspectable handoff detail materially improve the result.
- Use `miro` when the work is still at the whiteboard or architecture stage and not ready for formal screen structure.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `paper, reference/ground`.
- If both paths fail, produce the best-guess output described as: A wireframe set aligned to the flow, with explicit hierarchy, navigation logic, and unresolved structural gaps.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing the whole workflow into a single canvas.

## Workflow Notes

- Build the structural model before commenting on quality. First identify what each screen is responsible for and how users move through it.
- Treat `required_inputs` as real prerequisites. If the flow, platform, or content priorities are missing, infer a provisional version, prefix each inferred item with `Assumed wireframe context:`, and lower confidence for downstream decisions that depend on it.
- Keep the wireframes structural. If a choice is mainly about branding or visual polish, leave it for downstream visual design.
- Prefer explicit hierarchy over exhaustive detail. The point is to make task completion and information order obvious.
- Make state coverage visible. Empty, loading, confirmation, and error states belong in the structural model when they change layout or task flow.
- Reuse patterns deliberately. Repeated elements should only diverge when the task or context truly changes.
- If the assignment is `new design`, leave room for later divergent visual exploration instead of collapsing every screen into a single obvious pattern.
- Group low-impact structural rough edges into systemic patterns instead of overproducing isolated findings.

