---
name: component-implementation
description: Build or extend reusable frontend components by constructing the component API surface model first — props, variants, states, composition boundaries — then implementing against the design system spec, primitives layer, and component workshop.
trigger: When implementation needs a reusable component, not just a one-off screen. When a design handoff is ready and the component must integrate into or bootstrap a design system foundation.
required_inputs:
  - the component name and the interaction or UI pattern it must cover
  - the design artifact (Figma frame, spec, or annotated screenshot) for the target component
  - the project design system spec (project-ds-spec.md) when available
  - the existing component library or primitives layer in use (e.g., shadcn/ui, Radix UI, Ark UI, or none)
  - the target framework and styling approach (e.g., React + Tailwind, Vue + CSS Modules)
recommended_passes:
  - component API surface model construction (props, variants, states, composition)
  - design system alignment check (tokens, primitives, existing components)
  - component implementation and story authoring
  - accessibility and interaction state validation
  - visual regression baseline capture
tool_stack:
  runtime:
    primary: [repository, figma]
    secondary: [storybook, chromatic]
  artifacts:
    primary: [figma, project-ds-spec]
  component_primitives:
    primary: [shadcn_ui, radix_ui, ark_ui]
  visual_testing:
    primary: [chromatic]
    secondary: [ladle, histoire]
  component_distribution:
    primary: [bit_dev]
  fallback:
    primary: [reference_reuse, chrome_devtools]
tool_routing:
  - if: design spec is available in Figma and Code Connect is configured
    use: [figma, repository]
  - if: component must be documented and reviewed before merge
    use: [storybook, chromatic]
  - if: project uses React and a shadcn/ui baseline is specified in project-ds-spec.md
    use: [shadcn_ui, radix_ui]
  - if: project targets multiple frameworks (React, Vue, Solid, Svelte) and needs framework-parity primitives
    use: [ark_ui]
  - if: component must be shared across multiple applications or teams
    use: [bit_dev]
  - if: Storybook is too heavy for the project scale
    use: [ladle]
  - if: project is Vue-primary and a Storybook alternative is needed
    use: [histoire]
  - if: primary tools are unavailable, blocked, or out of credits
    use: [reference_reuse, chrome_devtools]
best_guess_output: A reusable component with a defined props API, all required variants and interactive states, a Storybook story covering the key states, and adoption notes for downstream implementers.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: component-implementation"
done_when: The component is reusable, aligned to the design system spec, all variants and states are implemented and documented in Storybook stories, and downstream consumers can adopt it without inferring unsupported patterns.
---

# Component Implementation

## Purpose

Build or extend reusable frontend components that align with the design system — constructing the component API surface model before writing any code, then implementing against design artifacts, the primitives layer, and an agreed token foundation.

This skill applies component engineering reasoning: API surface design, composability analysis, design system alignment, accessibility compliance, and documentation. It produces production-ready, adoptable components — not one-off screen implementations.

This skill does not design the component from scratch (that is the product-designer or ui-designer's responsibility), does not write full page layouts or routing logic, and does not own the design system token or theme definition unless bootstrapping from a baseline spec.

## Required Inputs and Assumptions

Required inputs:
- The component name and the UI pattern or interaction it must support
- A design artifact: Figma frame, annotated spec, or screenshot with interaction notes
- `project-ds-spec.md` when it exists — this defines the primitives layer, token conventions, and whether shadcn/ui initialization is required
- The existing component library or primitives currently in use (shadcn/ui, Radix UI, Ark UI, Mantine, none)
- The target framework and styling approach (React + Tailwind CSS, Vue + CSS Modules, etc.)

If any required input is missing, infer a provisional value and prefix it with `Assumed context:`. Lower confidence on any API or structural decision that depends on an inferred input.

Known vs unknown: the design artifact is often available but may lack interaction states, loading states, or error conditions. The existing primitives layer may be undeclared. Both must be resolved before the API surface model is built.

Assumptions to make explicit when undeclared:
- If no primitives layer is declared, assume the project targets vanilla React + Tailwind CSS.
- If no token naming convention is found in `project-ds-spec.md`, use the shadcn/ui CSS variable convention as the default.
- If no existing component inventory is accessible, treat the component as new rather than an extension.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live/real interaction** — Inspect the running application in a browser. Read existing component source in the repository. Highest fidelity for understanding current conventions and deviations.
2. **Structured system access** — Read `project-ds-spec.md`, the existing component directory, design token files, and Storybook stories. Best source for declared conventions and system boundaries.
3. **Design artifacts/documentation** — Figma frames, Code Connect annotations, design system docs. Use to extract the visual spec, prop surface, and variant matrix.
4. **Screenshots/static input** — Manual screenshots or images shared by the team. Useful for visible states; no interaction context.
5. **Inference** — Extrapolate API surface, variant set, or token usage from code patterns, sibling components, or established category norms. Must be labeled explicitly.

Declare which path was used. State its limitations in the deliverable. Prefer combining paths 1–3 when all are available. If only path 4 or 5 is available, label the output as `fallback` or `inferred` and flag which decisions require validation.

## Tool Stack

**Repository (runtime, primary):** Direct read and write access to the project codebase. Used to inspect existing components, read `project-ds-spec.md`, understand folder conventions, and commit the implementation. This is the ground truth for what the system already contains and what conventions must be followed.

**Figma (runtime, primary):** Read the visual spec, extract variant matrices, inspect tokens and spacing, and view Code Connect annotations when configured. Use `get_design_context` and `get_variable_defs` to pull tokens and component properties directly. When Code Connect is set up, Figma's Dev Mode surfaces the actual component code snippet alongside the design, reducing spec-to-code translation errors.

**Storybook (runtime, secondary):** Component workshop for isolated development, documentation, and interaction testing. Write stories that cover every variant and interactive state. Use the a11y addon (built on axe-core) to catch WCAG violations during development. Use the Vitest integration (Storybook 8+/v9) to run interaction tests and accessibility tests as part of the test suite. The ecosystem advantage — 200+ addons, Chromatic integration, Figma plugin — makes it the default documentation and testing layer for production component systems.

**Chromatic (visual testing, primary):** Cloud visual regression platform built by the Storybook team. On every commit, Chromatic captures pixel-accurate screenshots of all stories across browsers and compares them to the accepted baseline. Visual diffs surface in a shared UI review workspace where design, product, and engineering can accept or reject changes. Integrates with GitHub, GitLab, and Bitbucket PRs via status checks. Use Chromatic for any component entering the shared system or replacing an existing one.

**shadcn/ui (component primitives, primary):** A collection of copy-paste components built on Radix UI primitives and Tailwind CSS. Components are installed directly into the project (not as a locked npm dependency), giving full ownership of the source. Use when `project-ds-spec.md` specifies a shadcn/ui baseline or when the project needs fast, accessible, Tailwind-compatible components without design lock-in. Initialize via `npx shadcn@latest init` before building custom components on top.

**Radix UI (component primitives, primary):** Unstyled, accessible primitives — Dialog, Dropdown, Tooltip, Select, Popover, and more — with full ARIA compliance and keyboard navigation baked in. Radix handles the behavioral and accessibility layer; you bring the styles. Use Radix directly when the design system requires a fully custom visual layer built on proven accessible foundations. shadcn/ui is built on Radix, so they are complementary: use shadcn/ui for rapid setup and Radix directly for lower-level control.

**Ark UI (component primitives, secondary):** Headless UI components built on Zag.js state machines, with framework parity across React, Vue, Solid, and Svelte. Best choice when the project spans multiple frameworks and requires consistent behavior across all of them, or when precise state-machine-driven interaction semantics are needed (e.g., complex combobox, date picker, or multi-select behavior).

**Ladle (visual testing, secondary):** A Vite-native Storybook alternative with 10–50x faster cold-start times. Supports the same CSF (Component Story Format) as Storybook. Use Ladle when the project is React-only, the team has found Storybook startup time prohibitive in a large monorepo, and the advanced addon ecosystem is not required.

**Histoire (visual testing, secondary):** Vite-native component workshop for Vue 3 (and Svelte). The functional equivalent of Storybook for the Vue ecosystem. Use Histoire on Vue-primary projects where Storybook's overhead outweighs its benefits and Ladle's React-only focus is a limitation.

**Bit.dev (component distribution, primary):** AI-powered component workspace for sharing, versioning, and distributing components across multiple applications or teams. Components published to Bit are independently versioned and can be consumed as packages without a monorepo setup. Use Bit.dev when the component must be consumed by more than one application, when the team manages a multi-repo design system, or when component ownership needs to be tracked across projects.

**Fallback — reference/reuse + Chrome DevTools:** When repository and Figma access are unavailable. Inspect running UI in the browser via DevTools to extract current implementation patterns. Reference existing component source through code search. Label all output as `fallback`.

## Tool Routing

- Design spec is available in Figma and Code Connect is configured → use Figma (with `get_design_context`, `get_variable_defs`, Code Connect snippets) alongside repository read access to cross-reference the existing component directory.
- Component must be documented and reviewed before merge → write Storybook stories covering all variants and states; push to Chromatic for visual regression baseline and UI review.
- Project specifies shadcn/ui in `project-ds-spec.md` and the frontend is blank or near-blank → initialize the shadcn/ui baseline first (`npx shadcn@latest init`), then build the component on that foundation rather than improvising local primitives.
- Project targets React only and Storybook startup time is a known pain point → use Ladle as the component workshop; maintain CSF format so stories are portable to Storybook if the project grows.
- Project targets Vue 3 → use Histoire as the component workshop.
- Component must be shared across more than one application or team → publish to Bit.dev after implementation; document the scope and component name.
- Project needs framework-parity behavior across React, Vue, Solid, or Svelte → use Ark UI primitives as the behavioral foundation.
- Primary tools unavailable → use reference/reuse and Chrome DevTools; label output as `fallback`.
- Do not rely on a single tool. The expected full-stack combination for a production component is: Figma (spec) + repository (existing conventions) + shadcn/ui or Radix (primitives) + Storybook (workshop + a11y) + Chromatic (visual regression).

## Environment and Reproducibility

Record the following in the deliverable when known:
- Framework and version (e.g., React 18.3, Next.js 15, Vue 3.5)
- Styling approach and version (e.g., Tailwind CSS 3.4, CSS Modules, styled-components 6)
- Primitives layer and version (e.g., shadcn/ui CLI v2.x, Radix UI 1.x, Ark UI 3.x)
- Storybook version and active addons (e.g., Storybook 8.5 with a11y, Vitest, and Chromatic addons)
- Chromatic project key and baseline build number when visual tests are captured
- Node.js and package manager version (e.g., Node 22, pnpm 9)
- Design artifact source (Figma file URL and last-modified date)
- Whether Code Connect mappings exist for the component

If any of the above is unknown, state it explicitly. Do not assume version-specific APIs or behaviors without confirming the installed versions.

## Model Building

Before writing any implementation code, the agent MUST construct the component API surface model. This is the structural blueprint that all implementation decisions derive from.

The model must answer four questions:

1. **Props surface**: What is the minimal, explicit public API? List every prop with its type, default value, and whether it is required. Distinguish controlled vs. uncontrolled variants of stateful props. Do not add props that have no declared use case.

2. **Variant matrix**: What are the supported visual variants, sizes, and semantic intents (e.g., primary/secondary/destructive; sm/md/lg)? Map each variant to a design token or Tailwind class set. Note which combinations are unsupported or explicitly excluded.

3. **Interactive state inventory**: What states must the component render? Cover: default, hover, focus-visible, active/pressed, disabled, loading, error, empty, and any domain-specific states (e.g., selected, indeterminate for a checkbox). Note which states are driven by props, which by internal state, and which by CSS pseudo-classes.

4. **Composition boundaries**: What does the component own vs. what must stay outside it? Define slot points (children, renderProp, or named slots). Identify whether parent layout, data fetching, or event orchestration belongs to a wrapper — not to this component.

No code may be written before this model is documented in `### Component API surface model` within the deliverable section.

## Core Method Execution

Follow this sequence exactly. Do not skip steps. Do not write code before completing steps 1–3.

**Step 1 — Resolve the design system foundation.** Read `project-ds-spec.md` if it exists. Identify: the primitives layer in use, token naming convention, and any existing component that covers or partially covers the target pattern. If `project-ds-spec.md` recommends shadcn/ui and the frontend has no component foundation yet, initialize shadcn/ui first (`npx shadcn@latest init`) using the latest official CLI, then build the component on that baseline. Do not improvise local primitives when a spec-approved foundation exists.

**Step 2 — Extract the visual spec from Figma.** Use `get_design_context` and `get_variable_defs` to pull the component frame, token bindings, and variant properties. If Code Connect mappings exist for the component in Figma, read the code snippet to identify the intended component surface. Cross-reference the Figma variant matrix with the declared design token set. Flag any discrepancy between design tokens in Figma and tokens defined in the codebase.

**Step 3 — Build the API surface model.** Using the outputs of steps 1 and 2, construct the component model (props, variants, states, composition boundaries). Write this into `### Component API surface model` before proceeding. Label any element marked `Assumed context:` that is not directly evidenced by the spec.

**Step 4 — Check for reuse or extension opportunities.** Search the existing component directory. If a sibling component covers 70%+ of the needed behavior, extend it rather than creating a new one. If a Radix or Ark primitive already handles the behavioral layer (keyboard, ARIA, state machine), build on it directly. Do not reimplement behavior that a vetted primitive already provides correctly.

**Step 5 — Implement the component.** Write the component file following existing project conventions (file naming, export style, co-located types). Apply the token or Tailwind class set from the variant matrix. Implement all interactive states identified in the model. Ensure the component accepts and forwards `className` (or equivalent) for consumer-side overrides without breaking the internal style contract. Add data attributes for variant and state (e.g., `data-variant`, `data-state`) to enable external targeting.

**Step 6 — Write Storybook stories.** Create a story file (CSF3 format) with:
- A `Default` story showing the base variant
- A story per named variant
- A story per meaningful interactive state (loading, disabled, error)
- An `AllVariants` story for snapshot comparison
- ArgTypes declared for all props so the Controls panel is fully usable

Run the a11y addon during development. Resolve any axe-core violations before committing.

**Step 7 — Capture Chromatic baseline.** Push the Storybook build to Chromatic. Accept the visual baseline for all new stories. Record the Chromatic build number in the deliverable. Flag any story where the rendered output deviates from the Figma spec and document it as a finding.

**Step 8 — Document adoption guidance.** Write `### Adoption notes` in the deliverable covering: how to import the component, which props are required, which variants are not yet supported, known gotchas, and any migration notes if the component replaces an existing one.

## Structured Findings

Every design system misalignment, API design issue, or reusability gap discovered during implementation must use this exact schema. No free-form output. Separate observation from interpretation. Every finding must be traceable to a source.

```
#### Finding <id>
Observation: [What was found — without interpretation]
Evidence: [Source: Figma frame / repository path / Storybook story / Chromatic diff]
Cause: [Why this gap or issue exists — label as inferred if not confirmed]
Impact: [What breaks or degrades if this is not addressed]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — directly observed in the running application, design spec, or codebase; confirmed by at least two sources.
- **Medium** — observed in one source; not yet cross-validated across spec and implementation.
- **Low** — inferred from indirect evidence; requires validation against the actual design intent or user behavior.

## Prioritization Logic

Prioritize findings and implementation decisions by impact on reusability and system alignment:

1. **Critical** — Issues that break ARIA compliance, prevent the component from being used across the intended surfaces, or cause token/style desyncs with the design system spec. Must be resolved before the component is merged.
2. **Significant** — API surface decisions that will require a breaking change if corrected later (e.g., prop naming, controlled vs. uncontrolled pattern, composition boundary). Must be documented and reviewed before merge even if not blocking.
3. **Minor** — Style deviations, missing edge-case states, or documentation gaps that do not break existing consumers. Group these into a single `### Minor gaps` block.

Do not list more than six standalone findings. Observations that do not affect reusability, accessibility, or system alignment belong in the coverage map, not in findings.

## Pattern Detection

After the component model and implementation are complete, the agent must identify:

- **Reuse patterns**: Where does this component's behavior or structure duplicate a sibling component? Flag opportunities to extract a shared primitive.
- **API anti-patterns**: Props that accept arbitrary strings where a union type would be safer; callback props that leak internal state; components that require consumers to manage state that could be internalized.
- **Design system drift**: Where does the implemented component deviate from tokens, spacing scales, or naming conventions defined in `project-ds-spec.md`? Drift compounds over time — surface it immediately.
- **Composition over-reach**: Where has the component taken on responsibilities (layout, data fetching, routing logic) that belong outside it? These reduce reusability by coupling the component to a specific context.

Distinguish intentional customization (explicitly approved in the spec) from unintentional drift (undeclared deviation from the system). They require different responses.

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- Be directional — state what to address, not the full implementation solution
- Acknowledge evidence limits where confidence is Medium or Low
- Avoid recommending new primitives or design system changes without noting the downstream impact on existing consumers

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly in the deliverable:

- **Fully implemented**: Variants, states, and composition patterns that are complete and covered by Storybook stories.
- **Partially implemented**: States or edge conditions that exist in the design spec but are not yet in the component (e.g., loading state scaffolded but not wired to a real data fetch).
- **Not implemented**: Variants or states deliberately deferred, with the rationale noted.
- **Not analyzed**: Design system surfaces the component touches that were not reviewed (e.g., dark mode token mapping, responsive breakpoint behavior, right-to-left layout).

## Limits and Unknowns

Mandatory section. State:

- What design states could not be sourced from the Figma spec (no frame, gated by access, or not annotated)
- Where token bindings between Figma variables and codebase CSS variables could not be confirmed
- Where accessibility behavior was validated only by axe-core static analysis (not by keyboard or screen-reader testing)
- Where the props API was designed based on the current use case only and may not generalize to future consumers without modification
- Where Chromatic visual baselines were not captured (e.g., no Chromatic project configured for this repo)
- Any framework or version constraints that limit the component's portability

Do not collapse this section to a single line. Unconfirmed decisions carry compounding risk in shared design systems.

## Workflow Rules

- Build the API surface model before writing any implementation code. No exceptions.
- Read `project-ds-spec.md` first when it exists. If it recommends shadcn/ui and the frontend is blank or near-blank, initialize the shadcn/ui baseline before building the component.
- Distinguish fact (confirmed in spec, code, or running app) from inference (extrapolated from patterns). Label every inference.
- Do not reimplement behavior that Radix UI or Ark UI provides correctly. Build on vetted primitives.
- Every story must cover the variant it is named for. Do not leave stories as empty shells.
- Record which tool path was used and why in the deliverable.
- Extend over rebuild: if a sibling component covers 70%+ of the needed behavior, extend it. Document the extension boundary.
- Avoid adding props that have no declared use case in the current scope. API surface grows; it rarely shrinks cleanly.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### component-implementation` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: component-implementation`, include:

- `### Component API surface model`: The full model — props with types and defaults, variant matrix, interactive state inventory, composition boundaries. Written before implementation begins.
- `### System foundation alignment`: State whether the component builds on an existing foundation, extends a sibling component, or first bootstraps a foundation from `project-ds-spec.md`. Confirm whether a shadcn/ui initialization was required.
- `### Props and API`: The finalized public API as implemented — props, types, defaults, controlled/uncontrolled pattern, forwarded attributes.
- `### Variants and states`: The complete list of supported variants, interactive states, and edge conditions as implemented, with the corresponding Storybook story name for each.
- `### Composition and reuse constraints`: Composition boundaries, slot points, dependencies, and what must remain outside the component. Include guidance on when to extend vs. wrap vs. compose.
- `### Findings`: Structured findings (design system misalignments, API issues, reusability gaps) using the required schema.
- `### Recommendations`: Directional recommendations linked to findings.
- `### Code touchpoints`: Files created or modified, component family location, and Storybook story file path.
- `### Adoption notes`: Import path, required props, unsupported patterns, migration guidance for consumers replacing a previous implementation.
- `### Coverage map`: What is fully implemented, partially implemented, not implemented, and not analyzed.
- `### Gaps in evidence`: What could not be sourced, confirmed, or validated.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: component-implementation`.
- Record which tool path was used and why.
- Label each deliverable section as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
- Ensure the section meets this done-when bar: The component is reusable, aligned to the design system spec, all variants and states are implemented and documented in Storybook stories, and downstream consumers can adopt it without inferring unsupported patterns.
