---
name: implement-from-design
description: Build an implementation map from an approved design — inventory surfaces, map components and tokens, verify state coverage — then write production code that faithfully reproduces the design intent, including all required states and interactions.
trigger: When approved design work is ready for implementation and the implementation target (component, route, surface) has been clearly scoped.
required_inputs:
  - approved design artifact (Figma file URL, frame link, or exported spec)
  - implementation target: the specific surface, component, or route being built in this pass
  - framework and component-library context (e.g., Next.js + shadcn/ui, plain React + Tailwind CSS)
  - project-ds-spec.md path when a design system spec exists for this project
recommended_passes:
  - design surface inventory (enumerate all frames, variants, and states in scope)
  - component mapping (match design components to code components or primitives)
  - token mapping (map design tokens / Figma variables to code-side CSS variables or Tailwind tokens)
  - shadcn/ui baseline initialization (conditional — only when spec recommends it and repo is blank/near-blank)
  - feature implementation pass (write production code aligned to the design)
  - fidelity review pass (compare implementation against design; record gaps)
tool_stack:
  runtime:
    primary: [figma, repository]
    secondary: [storybook, chromatic]
  artifacts:
    primary: [figma_dev_mode, figma_code_connect, tokens_studio, style_dictionary]
  generation:
    primary: [shadcn_ui, tailwind_css]
    secondary: [locofy, builder_io]
  fallback:
    primary: [chrome_devtools, reference_trace]
tool_routing:
  - if: Figma file is accessible and the project has Code Connect mappings configured
    use: [figma_code_connect, figma_dev_mode]
    note: Code Connect surfaces production component snippets directly in Dev Mode — prefer this path; it avoids stale handoff specs
  - if: Figma file is accessible but Code Connect is not configured
    use: [figma_dev_mode, tokens_studio]
    note: Use Dev Mode for measurements, spacing, and token inspection; use Tokens Studio to export variable sets to Style Dictionary format
  - if: design system tokens need to flow from Figma Variables into CSS / Tailwind
    use: [tokens_studio, style_dictionary]
    note: Tokens Studio exports W3C-compliant token JSON; Style Dictionary transforms to CSS custom properties, Tailwind config, or JS constants
  - if: project-ds-spec.md recommends shadcn/ui and the repo is blank or near-blank
    use: [shadcn_ui]
    note: Run the CLI init path described in the Workflow Notes; align components.json and theme variables to the spec before writing feature code
  - if: implementing atomic or primitive components that map directly to shadcn/ui registry components
    use: [shadcn_ui, tailwind_css]
  - if: need to verify visual fidelity after implementation
    use: [storybook, chromatic]
    note: Write stories for all required states; run Chromatic to produce a side-by-side baseline for design review
  - if: converting a dense, multi-screen Figma file with many reusable layout patterns
    use: [locofy]
    note: Locofy can scaffold component structure and layout from Figma; treat output as a starting skeleton, not production code
  - if: managing a visual CMS page alongside component code
    use: [builder_io]
    note: Builder.io connects visual editing to a live codebase; use when the design surface is marketing or content-heavy
  - if: primary tools are unavailable, blocked, or out of credits
    use: [chrome_devtools, reference_trace]
    note: Label output section as `fallback`; lower confidence of any measurement or token value obtained this way
best_guess_output: A working UI implementation that faithfully reproduces the approved design, covers all required states and interactions, and is aligned to the project design system spec.
output_artifacts: knowledge/frontend-engineer-implement-from-design.md
done_when: The implemented surface matches the approved design's structure, spacing, typography, color, and behavioral states; all required states are covered in code; the fidelity gaps section explicitly accounts for any deviations; and the code touchpoints are identified so downstream review can verify the right surface.
mesh:
  inputs:
    - ui-designer:screen-production-design
    - product-designer:handoff-spec
  next:
    - frontend-engineer:stateful-ui-build
    - frontend-engineer:component-implementation
    - frontend-engineer:browser-debug
  context: "Implementation translates high-fidelity designs and handoff specs into structural frontend code."
---

# Implement From Design

## Purpose

Translate an approved design artifact into production-quality frontend code by following a structured implementation method: build an implementation map first, then write code that faithfully reproduces the design intent including all required states and interactions.

This skill applies structured design-to-code reasoning: surface inventory, component and token mapping, state coverage analysis, and fidelity verification. It produces code that is traceable to a design decision — not code that approximates a screenshot.

This skill does NOT:
- Make design decisions or propose unsolicited design changes
- Run shadcn/ui initialization over an already-established system
- Accept AI-generated code scaffolds (e.g., from Locofy) as production output without engineering review
- Produce generic UI that is not grounded in the specific design artifact provided

---

## Required Inputs and Assumptions

Required inputs:
- Approved design artifact: a Figma file URL, frame link, or exported design spec pointing to the specific surface in scope
- Implementation target: the exact surface, component, route, or feature being built in this pass (must be bounded — one surface per pass)
- Framework and component-library context: e.g., Next.js 14 + shadcn/ui + Tailwind CSS v4, or React 18 + plain CSS modules
- `project-ds-spec.md` path when a project-level design system spec exists

If inputs are missing, infer provisional values and label each `Assumed context:`. Lower confidence on any finding that depends on an inferred input.

Known vs unknown: the design target is usually a Figma link but the right frame within that file may not be obvious. The component-library baseline is often implied rather than stated. The state coverage expected (hover, focus, disabled, error, empty, loading) must be derived from the design or product spec — it is not always enumerated in the Figma file. These must all be resolved before code is written.

---

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live / real interaction** — Direct Figma access via the MCP server or Dev Mode with Code Connect mappings. Highest fidelity; surfaces production component snippets, exact token names, spacing values, and variant properties directly in the IDE.
2. **Structured system access** — Figma Dev Mode (inspect panel), Tokens Studio export, Style Dictionary config. Best balance of coverage and precision for token-to-code translation.
3. **Design artifacts or documentation** — `project-ds-spec.md`, exported specs, annotated redlines, Zeplin screens. Useful when live Figma access is unavailable; may not reflect the latest design state.
4. **Screenshots / static input** — Exported frames or stakeholder-shared images. Limited to visible states; no variant or token context; requires significant inference.
5. **Inference** — Spacing, token, or behavior inferred from visual inspection alone. Last resort. Must be labeled explicitly as `inferred`.

Declare which path was used for each surface or artifact in the deliverable. Prefer path 1 or 2. When falling back, state the specific gap this creates and what would be needed to close it.

---

## Tool Stack

**Runtime — primary:**

**Figma + Dev Mode** (figma.com): The authoritative design source. Dev Mode provides an inspection panel with exact spacing, typography, color, radius, and shadow values. When Figma Variables are used and exposed via Tokens Studio, token names (not raw values) are visible in the inspect panel, enabling semantic token mapping. Figma's MCP server (introduced 2025) allows AI agents to query design context directly — including which specific token is bound to a property — without manual inspection.

**Figma Code Connect** (github.com/figma/code-connect): A CLI and in-app tool that links design system components in Figma to their counterpart components in the codebase. When configured, Dev Mode shows real production component snippets (including props) instead of generated CSS. Best used when the project has a mature design system with a 1:1 component mapping. Reduces the gap between what designers see and what engineers implement.

**Repository** (repository MCP): Read and write access to the codebase. Required for reading existing component structure, understanding the tech stack, and writing implementation files. Always read the existing codebase before writing new components — do not duplicate what already exists.

**Artifacts — primary:**

**Tokens Studio for Figma** (tokens.studio): A Figma plugin and platform that manages design tokens as structured JSON within Figma Variables. Exports tokens in W3C Design Token Community Group format. Acts as the bridge between Figma's design decisions (color, spacing, typography scales, radius, shadow) and the codebase token pipeline. The standard path for teams that maintain a living design token system. Syncs to GitHub, GitLab, or direct file export.

**Style Dictionary** (styledictionary.com): A build system that transforms token JSON (from Tokens Studio or raw W3C token files) into platform-ready outputs: CSS custom properties, Tailwind CSS config, SCSS variables, JS/TS constants, and more. Configured via `config.json` or `config.js`. Use when the project needs tokens to flow automatically from design into code without manual copy-paste. Supports custom transforms for project-specific naming conventions.

**Figma Dev Mode annotation / Zeplin** (zeplin.io): When a dedicated handoff layer exists outside Figma, Zeplin provides a locked, versioned view of finalized screens — distinct from the active design canvas. Zeplin's 2025 MCP server allows AI agents to query screen specs directly. Use Zeplin when the team has intentionally separated in-progress and ready-to-build surfaces, or when the Figma file is too noisy for direct dev inspection.

**Generation — primary:**

**shadcn/ui** (ui.shadcn.com): A component collection built on Radix UI primitives and styled with Tailwind CSS. Components are copy-owned — added to the project repository via CLI (`pnpm dlx shadcn@latest add <component>`), not imported from a package. This makes them fully customizable. When `project-ds-spec.md` recommends shadcn/ui and the repo is blank or near-blank, initialize the full foundation first (see Workflow Notes). The `components.json` file governs aliases, base color, CSS variable usage, and icon library — align this to the spec before adding any components.

**Tailwind CSS** (tailwindcss.com): Utility-first CSS framework. In Tailwind v4 (2025), configuration is driven by CSS `@theme` blocks rather than `tailwind.config.js`, enabling direct CSS custom property mapping from Style Dictionary output. Use Tailwind utility classes for layout, spacing, and typography implementation. Avoid overriding Tailwind base styles with arbitrary values unless the design explicitly deviates from the token scale.

**Generation — secondary:**

**Locofy** (locofy.ai): An AI-powered Figma plugin that converts multi-screen Figma designs into React, Next.js, Vue, or HTML/CSS scaffolds. Useful for generating initial component structure and layout from dense design files, particularly for dashboard or SaaS surfaces. Treat Locofy output as a structural skeleton — review and refactor for production quality before committing.

**Builder.io** (builder.io): A visual development platform that connects a visual editing canvas to a live codebase via registered components. Best suited when the design surface is content-heavy or marketing-oriented and requires non-engineer editing workflows. Generates React components that integrate with Builder's content API.

**Review — primary:**

**Storybook** (storybook.js.org): A component development environment for isolating and rendering UI components with all their required states. Write stories for each state in scope (default, hover, focus, disabled, error, empty, loading, responsive breakpoints). Storybook stories serve as the living documentation of what was implemented and provide the baseline for visual regression testing.

**Chromatic** (chromatic.com): A cloud visual testing service built by the Storybook team. Captures pixel-accurate snapshots of every Storybook story and compares them against a baseline on every build. Enables side-by-side visual review by designers and stakeholders without requiring local setup. Post-implementation, run Chromatic to produce a reviewable baseline — designers can approve or reject visual changes directly in the Chromatic UI.

**Fallback:**

**Chrome DevTools + reference/trace**: When primary tools are unavailable, use browser inspection to measure spacing and infer token values from a reference implementation or the design artifact. Label all values obtained this way as `fallback` and flag them for verification.

---

## Tool Routing

- Figma is accessible and Code Connect mappings are configured → use Figma Code Connect + Dev Mode as the primary inspection path; production component snippets surface in the IDE automatically.
- Figma is accessible but Code Connect is not configured → use Figma Dev Mode for inspection; use Tokens Studio export + Style Dictionary for token-to-code translation.
- Design tokens need to flow from Figma Variables into Tailwind or CSS → use Tokens Studio (export) → Style Dictionary (transform) → Tailwind `@theme` or CSS custom properties.
- `project-ds-spec.md` recommends shadcn/ui and the repo is blank or near-blank → initialize the shadcn/ui foundation before any feature code (see Workflow Notes).
- Implementing atomic components that match shadcn/ui's component registry → use `pnpm dlx shadcn@latest add <component>` and customize from the spec; do not hand-write primitives that shadcn/ui already provides.
- Verifying visual fidelity after implementation → write Storybook stories for all required states; run Chromatic to produce a reviewable snapshot baseline.
- Design surface is a dense multi-screen Figma file with many layout patterns → consider using Locofy to scaffold structure; treat output as skeleton, not production code.
- Primary tools are unavailable → use Chrome DevTools + reference/trace; label output as `fallback`.
- Avoid single-tool bias. The strongest implementation path combines: Figma Dev Mode (source of truth for measurements and tokens) + shadcn/ui (component primitives) + Tailwind CSS (styling) + Storybook (state coverage and review baseline).

---

## Environment and Reproducibility

Record the following in the deliverable when known:

- Figma file URL and the specific frame(s) or section(s) used as the design source
- Date of the Figma inspection session (designs change; evidence ages)
- Framework version: Next.js version, React version, Tailwind CSS version, shadcn/ui version (via `package.json`)
- `components.json` base color, CSS variable mode, and icon library (if shadcn/ui is used)
- Node.js and package manager version if initialization is run
- Whether Code Connect mappings exist and which components are connected
- Tokens Studio version and export format used (if token pipeline is involved)
- Style Dictionary version and config path (if token transformation is run)

If any of the above is unknown, state it explicitly. Do not present inferred measurements as authoritative spec values.

---

## Model Building

Before writing any code, the agent MUST construct an implementation map. No code may be written before the implementation map is complete.

**Step 1 — Design surface inventory.** Identify every distinct frame, variant, and state in scope for this pass. For each, record:
- Frame or component name in Figma
- Surface type (page, modal, drawer, card, form, navigation, empty state, etc.)
- Variants declared in Figma (e.g., size: sm/md/lg; state: default/hover/active/disabled/error)
- Any states that are NOT in the Figma file but are required by the product spec or standard interaction patterns (hover, focus-visible, loading, skeleton, error boundary)

**Step 2 — Component mapping.** For each design component in the inventory, map it to one of:
- An existing code component in the repository (include file path)
- A shadcn/ui registry component to be added (include CLI command)
- A new custom component to be authored (note: this adds scope)
- A Tailwind utility composition requiring no dedicated component file

Document the mapping table: `Design component → Code component → Status (exists / to-add / to-create)`.

**Step 3 — Token mapping.** For each design decision that uses a Figma Variable or named style (color, spacing, typography, radius, shadow), map it to its code-side equivalent:
- CSS custom property name (e.g., `--color-primary`)
- Tailwind token name (e.g., `bg-primary`)
- Raw value if the token is not yet configured in code (flag as `gap: token not in codebase`)

**Step 4 — State coverage matrix.** Build a matrix of: `component × state × coverage`.
- Column headers: default, hover, focus-visible, active, disabled, error, loading/skeleton, empty, responsive (mobile/tablet/desktop)
- Row values: `in-design` (state is in Figma), `inferred` (state is not in Figma but required), `out-of-scope` (explicitly excluded from this pass)

No conclusions about implementation complexity or approach before this matrix is built.

---

## Core Method Execution

Follow this sequence strictly.

**Step 1 — Read the design system spec.** Before inspecting Figma, read `knowledge/project-ds-spec.md` if it exists. Identify: recommended component library, token structure, CSS framework, existing initialization state, and any explicit implementation decisions. This governs the entire foundation setup.

**Step 2 — Inspect the design artifact.** Use the tool routing logic to inspect the Figma file. Retrieve: frame structure, component names, spacing values, typography styles, color tokens, radius values, shadow styles, and any interactive states or variants declared. Record which tool path was used.

**Step 3 — Construct the implementation map.** Execute the four model-building steps above. Do not proceed until the design surface inventory, component mapping, token mapping, and state coverage matrix are all documented.

**Step 4 — Initialize the foundation (conditional).** If `project-ds-spec.md` recommends shadcn/ui AND the assignment owns repository writes AND the frontend is blank or near-blank:
- Run `pnpm dlx shadcn@latest init -t <framework>` (add `--monorepo` if the repo shape requires it).
- After init, align `components.json` to the spec: set `baseColor`, confirm `cssVariables: true`, set the correct `aliases` for components/hooks/lib/utils, and configure the icon library.
- Translate spec token decisions into the generated `globals.css` theme variables — do not accept CLI defaults blindly.
- Record the exact init command, the framework flag used, and every file created or modified.
- Do NOT re-initialize shadcn/ui over an established system. If the project is no longer blank enough, keep the existing foundation and record the mismatch or incremental-adoption plan as an open implementation risk.

**Step 5 — Add required shadcn/ui components.** From the component mapping table, run `pnpm dlx shadcn@latest add <component>` for each shadcn/ui registry component required. Customize each added component to match the spec — do not treat CLI defaults as final.

**Step 6 — Implement the feature surface.** Write production code for the implementation target. Follow this order:
1. Implement the layout shell and structural markup (semantic HTML, ARIA roles)
2. Apply token-mapped Tailwind classes for spacing, typography, and color
3. Implement the default state to match the Figma frame exactly
4. Implement all additional states from the state coverage matrix (hover, focus, disabled, error, loading, empty)
5. Implement responsive behavior for all required breakpoints
6. Wire up any interactions, transitions, or animations specified in the design

At each step, reference the design artifact — do not rely on memory of the design.

**Step 7 — Write Storybook stories.** For each component implemented, write Storybook stories covering every state in the coverage matrix. Stories serve as the implementation record and the visual review baseline. Each state must be an independently rendered story (not a single story with manual toggling).

**Step 8 — Run the fidelity review.** Compare the rendered implementation against the Figma frames for each state. For each deviation, record a structured finding. If Chromatic is available, publish the Storybook to Chromatic and share the review link.

**Step 9 — Record open implementation risks.** Document any gaps, deviations, or unresolved questions that require designer or product owner input before the surface can be considered complete.

---

## Structured Findings

Every finding (fidelity mismatch, implementation gap, or open question) must use this exact schema. No free-form output. Separate observation from interpretation. Every finding must be traceable to the design artifact.

```
#### Finding <id>
Observation: [What was seen in the implementation vs. the design — without interpretation]
Evidence: [Design frame reference, Figma node name, or screenshot; code file and line range]
Repro steps: [How to see the deviation — which story, which state, which breakpoint]
Cause: [Why the deviation exists — labeled `inferred` if not confirmed]
Impact: [Effect on design fidelity, user experience, or downstream review]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — deviation is clearly visible, traceable to a specific design decision, and confirmed by direct inspection.
- **Medium** — deviation is likely but depends on an inferred token or spec value that was not directly observable.
- **Low** — deviation is suspected from a screenshot or fallback inspection; requires direct Figma access to confirm.

---

## Prioritization Logic

Prioritize findings by fidelity impact:

1. **Critical** — Deviations that break the design intent, misrepresent interactive behavior, violate accessibility (WCAG 2.1 AA), or are visible to users in the primary viewport and default state. Must be resolved before the surface ships.
2. **Significant** — Deviations in secondary states (hover, focus), minor spacing misalignments (>4px), or token mismatches that affect visual consistency but not core behavior. Should be resolved before designer sign-off.
3. **Minor** — Pixel-level differences within the design token grid (1-2px), inferred values that are not yet confirmed, or states that are out of scope for this pass. Group these into a single `### Minor gaps` block. Do not list as standalone findings.

Do not include more than eight standalone findings per pass. Issues that cannot be traced to a specific design decision belong in the limits and unknowns section, not in findings.

---

## Pattern Detection

After the fidelity review, identify:

- **Recurring gaps**: The same type of deviation appearing across multiple components or states (e.g., focus-visible ring missing everywhere, border-radius token not applied consistently). These indicate a system-level gap in the foundation setup, not individual implementation errors.
- **Token coverage gaps**: Design decisions that appear in the Figma file but have no corresponding token in the codebase — these indicate a token pipeline gap that will recur on every future implementation pass.
- **State blindspots**: Categories of states that are consistently absent from the Figma file (e.g., all error states are unspecified). Flag these as a design system debt item, not as implementation unknowns.
- **Scope drift**: Component mapping discoveries that revealed the implementation target was larger or smaller than initially scoped. Record the actual scope vs. the declared scope.

Distinguishing a system-level pattern (which requires a design system fix) from an instance-level deviation (which requires a local code fix) is the critical judgment call in this step.

---

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- Be directional, not prescriptive — state what to consider or investigate, not exactly what to build
- Acknowledge evidence limits where confidence is Medium or Low
- Avoid recommending architectural changes without evidence from the codebase

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

Example: `Rec 1 [links to Finding 3]: The focus-visible ring deviation appears across all interactive components — consider auditing the base Tailwind ring utility configuration against the design token spec rather than fixing each component individually.`

---

## Coverage Map

State explicitly:

- **Deeply implemented**: Components and states that were sourced from primary tools (Figma Dev Mode or Code Connect), mapped to tokens, and implemented with Storybook story coverage.
- **Partially implemented**: Components or states where evidence was incomplete, token values were inferred, or Storybook stories are missing.
- **Out of scope for this pass**: Components, states, or surfaces explicitly excluded. Include the reason.
- **Not implemented**: Design surfaces identified in the inventory but not yet touched. These are inputs for future passes.

The coverage map sets the boundary of what downstream review can verify vs. what needs further work.

---

## Limits and Unknowns

Mandatory section. State:

- Which Figma frames or states could not be accessed (wrong permissions, expired link, unpublished library)
- Which token values were inferred from visual inspection rather than read from the token source
- Where shadcn/ui component defaults were accepted because the spec did not specify the target value
- Where interaction behavior was inferred because the Figma file contains no prototyping or animation spec
- Which responsive breakpoints were not tested due to missing designs for those viewports
- Where Chromatic baseline has not been established yet (first pass has no regression comparison)
- What designer or product owner confirmation would increase confidence in the highest-impact deviations

Do not omit this section or collapse it to a single line. Gaps that are not named here will surface as bugs in review.

---

## Workflow Rules

- Build the implementation map before writing any code. No exceptions.
- Read `project-ds-spec.md` before inspecting the Figma file — the spec governs the foundation.
- Distinguish fact (directly read from Dev Mode, tokens, or code) from inference (estimated from visual inspection). Label every inference.
- Do not re-initialize shadcn/ui over an established system. Assess the repo state first.
- Do not accept AI-generated component output (from Locofy or similar) without reviewing it against the design and refactoring for production quality.
- Preserve fidelity-critical design details without turning the deliverable into line-by-line implementation prose.
- Call out where design intent is clear versus where engineering judgment filled a gap.
- Keep code touchpoints exact (file path + line range when available) so downstream review can verify the right surface.
- Merge duplicate findings before writing. One finding per distinct pattern, not one per occurrence.
- Avoid redundancy between the implementation map and findings. The map is the pre-work; findings are interpreted deviations.

---

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/frontend-engineer-implement-from-design.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

---

## Required Deliverable Sections

Within `## Skill: implement-from-design`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Design target`: Identify the design source (Figma file URL + frame), surface type, and approved direction being implemented. Record which tool path was used and label it `sourced`, `fallback`, or `inferred`.
- `### System foundation`: State whether this pass reuses an existing UI foundation or initializes one from `project-ds-spec.md`. If shadcn/ui was initialized in this pass, record the exact CLI command, framework flag, and every file created or modified. If initialization was skipped because the foundation is already established, record that decision.
- `### Implementation map`: The design surface inventory, component mapping table, token mapping table, and state coverage matrix built in the model-building step. This is the pre-code plan.
- `### Implementation scope`: Define exactly what was built in this pass. Reference the implementation map. Note any scope changes discovered during implementation.
- `### State coverage`: List every required state (default, hover, focus-visible, active, disabled, error, loading, empty, responsive breakpoints) and its implementation status (implemented / partially implemented / out of scope / not in design).
- `### Interaction notes`: Capture important interactions, transitions, or behavioral nuances that required engineering judgment. Note where design spec was silent and what judgment was applied.
- `### Code touchpoints`: The exact files, components, and routes involved. Include relative file paths and, where useful, line ranges for key implementations.
- `### Findings`: Structured findings using the required schema. No free-form deviation notes.
- `### Open implementation risks`: Remaining uncertainty, gaps, token mismatches, missing states, or blockers that require input from design or product before the surface ships.

---

