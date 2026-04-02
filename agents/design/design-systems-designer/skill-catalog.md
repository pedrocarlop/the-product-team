# Design Systems Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `atomic-library-build`

- Description: Build a component-library structure by modeling primitives, composition layers, promotion rules, and system boundaries before assigning atoms, molecules, organisms, and higher-level patterns.
- Trigger: When reusable components need a clearer system structure, a library reorganization, or a repeatable promotion path from one-off patterns into shared assets.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: An atomic component-library structure with explicit layers, promotion rules, missing pieces, and a pragmatic migration order.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: The team has a defensible library structure, knows what belongs in each layer, and can promote or reject new shared components without re-litigating the model.

## `component-governance`

- Description: Model component ownership, lifecycle states, decision rights, and contribution workflows before defining governance rules for change, variants, and deprecation.
- Trigger: When system growth needs operating rules, ownership clarity, or lifecycle control instead of relying on informal habits and tribal knowledge.
- Primary MCP/tool: notion, figma
- Fallback: repository, reference/reuse
- Best guess: A governance model covering ownership, contribution, variants, exceptions, deprecation, and the minimum process needed to keep the library healthy.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Teams can explain who decides, who reviews, which lifecycle state a component is in, and how components are introduced, changed, or removed without informal side channels.

## `design-code-mapping`

- Description: Build a canonical system model of components, tokens, states, and ownership anchors before tracing how design artifacts map to implementation reality.
- Trigger: When design and engineering need a reliable bridge between system primitives, or when drift makes handoff and maintenance ambiguous.
- Primary MCP/tool: figma, repository
- Fallback: reference/trace, reference/verify
- Best guess: A design-code mapping with concrete anchors, traceable gaps, explicit ownership notes, and the minimum follow-up actions needed to close parity risk.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md
- Done when: Design and engineering can identify the same primitives, states, and code anchors with enough precision to fix drift instead of debating what the system contains.

## `spacing-and-layout-scale`

- Description: Build a layout-system model across spacing primitives, composition roles, breakpoints, and density expectations before defining the scale and its usage rules.
- Trigger: When teams are inventing spacing ad hoc, layout rhythm is inconsistent, or the system needs a clear spatial foundation that can survive responsive implementation.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: A spacing and layout scale with explicit primitives, semantic usage rules, breakpoint behavior, migration guidance, and known exceptions.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Designers and engineers have a scale and semantic usage map they can apply to real layouts without reinventing spacing, breakpoint, or density rules.

## `system-audit`

- Description: Build a design-system health model from design, code, documentation, and adoption evidence before diagnosing drift, duplication, governance gaps, and next actions.
- Trigger: When the system needs a baseline before extension, migration, or cleanup and the team needs evidence-backed priorities instead of design-system opinions.
- Primary MCP/tool: figma, repository
- Fallback: paper, reference/ground
- Best guess: A design-system audit with explicit scope, findings, systemic patterns, confidence-tagged priorities, and the minimum next moves needed to stabilize the system.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: The team can point to the audited surfaces, understand the highest-risk drift and duplication patterns, and act on a prioritized remediation sequence without re-running discovery.

## `system-qa-and-adoption`

- Description: Build an operational model of verification surfaces, adoption audiences, and rollout dependencies before defining QA checks, blockers, and adoption guidance.
- Trigger: When the design system exists but consistency is untrusted, rollout is stalling, or the team needs a repeatable way to verify and adopt the system.
- Primary MCP/tool: repository, figma
- Fallback: chrome_devtools, reference/verify
- Best guess: A system QA and adoption plan with verification checks, blocker analysis, rollout guidance, exit criteria, and clear confidence limits.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Teams have a repeatable verification method, can see the highest adoption blockers, and know what must be true before the system rollout is considered operationally healthy.

## `token-architecture`

- Description: Construct a token-system model across primitives, semantics, themes, and code-delivery constraints before defining naming, aliasing, and migration rules.
- Trigger: When the system needs a durable token foundation, cross-platform alignment, or a cleaner bridge between design authoring and implementation.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: A token architecture proposal with explicit token layers, naming rules, semantic aliases, theme logic, code-delivery implications, and migration guidance.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Token layers, naming, aliasing, theme handling, and code-delivery constraints are explicit enough that new token work can scale without inventing a parallel system.
