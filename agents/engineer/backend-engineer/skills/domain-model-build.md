---
name: domain-model-build
description: Model backend entities, invariants, state transitions, persistence boundaries, and transformation rules before implementing or changing domain behavior.
trigger: When business rules, lifecycle changes, authorization relationships, or backend data transformations must be encoded.
primary_mcp: repository
fallback_tools:
  - reference/ground
  - reference/trace
required_inputs:
  - the feature or domain slice being changed
  - the current source of truth for domain rules, schema, or state transitions
  - the persistence layer or data store in use when known
  - any authorization, lifecycle, or workflow constraints that affect the model
  - known ambiguity, edge cases, or downstream consumers of the model
recommended_passes:
  - domain vocabulary and entity inventory
  - rule and invariant extraction
  - state transition mapping
  - data transformation and persistence review
  - ambiguity and risk synthesis
tool_stack:
  runtime:
    primary: [repository]
    secondary: [logs]
  modeling:
    primary: [atlas, openfga]
    secondary: [dbml, schemaspy]
  artifacts:
    primary: [reference, trace]
  fallback:
    primary: [reference/ground, reference/trace]
tool_routing:
  - if: the codebase contains the domain implementation or schema
    use: [repository]
  - if: current runtime behavior, migrations, or incidents are needed to ground the model
    use: [logs]
  - if: the work is schema-first or migration-sensitive
    use: [atlas]
  - if: the work includes permissions, ownership, or relationship-based authorization
    use: [openfga]
  - if: the domain is easiest to review as a relational diagram or DSL
    use: [dbml]
  - if: the current database shape needs reverse-engineered documentation
    use: [schemaspy]
  - if: the primary path is unavailable, blocked, or incomplete
    use: [reference/ground, reference/trace]
best_guess_output: A backend domain model implementation or design with explicit entities, rules, transitions, transformations, and open risks.
output_artifacts: logs/active/<project-slug>/deliverables/backend-engineer-domain-model-build.md
done_when: Core rules are explicit, mapped to a clear source of truth, and any unresolved ambiguities, edge cases, or data-shape risks are documented.
---

# Domain Model Build

## Purpose

Model the backend domain before changing behavior.

This skill builds the conceptual and structural model for entities, rules, state transitions, and data transformations so implementation work has a stable source of truth. It is focused on domain logic and persistence boundaries, not transport, routing, or API surface design.

This skill does not own endpoint design, frontend behavior, or generic implementation guidance detached from the domain model.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/backend-engineer-domain-model-build.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: domain-model-build`, include:
- `### Domain entities or concepts`: Define the key entities, concepts, aggregates, and relationships involved.
- `### Core rules`: State the domain rules, invariants, or business logic that must hold.
- `### State transitions`: Describe lifecycle changes, guarded mutations, or allowed and disallowed transitions.
- `### Data transformations`: Explain derived data, normalization, denormalization, or mapping logic.
- `### Code touchpoints`: Identify the modules, tables, services, model files, or persistence boundaries that own the source of truth.
- `### Open risks`: Call out ambiguity, edge cases, or domain gaps that remain.

## Required Inputs and Assumptions

Required inputs:
- The feature, workflow, or domain slice being changed
- The current source of truth for domain rules, schema, or lifecycle behavior
- The persistence layer, data store, or aggregate boundary when known
- Any permissions, ownership, or relationship constraints that affect the model
- Known ambiguity, edge cases, or downstream consumers that depend on the model

If inputs are missing, infer a provisional frame and prefix it with `Assumed context:`. Lower confidence for any conclusion that depends on an inferred input.

Known vs unknown:
- The domain vocabulary may be named in product docs but not in code.
- The state model may be implicit in migrations, handlers, or tests.
- Authorization rules may live outside the core domain model and need to be surfaced explicitly.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live / current implementation evidence** - Read the repository, schema, tests, migrations, and any runtime logs that show present behavior.
2. **Structured system access** - Use schema review, model docs, migration history, and permission modeling tools when available.
3. **Design artifacts or documentation** - Read domain notes, decision records, RFCs, or explicit modeling docs.
4. **Screenshots / static input** - Use only when the model is documented visually or in review material.
5. **Inference** - Derive the model from code patterns or surrounding context as a last resort.

State which path was used and note its limits in the deliverable. Prefer paths 1 and 2 together when the model affects durable data or authorization decisions.

## Tool Stack

**Runtime - primary:**

**Repository**: Source code, schema files, tests, migrations, and model definitions. This is the primary source of truth for what exists now.

**Runtime - secondary:**

**Logs**: Runtime evidence, incident notes, and execution traces that show how the current model behaves in practice.

**Modeling - primary:**

**Atlas**: Schema-as-code tooling for database planning, migration safety, linting, and drift-aware schema review. Use it when the domain model depends on relational changes that must stay safe over time.

**OpenFGA**: Relationship-based authorization modeling. Use it when ownership, access, or permission state is part of the domain model and should be expressed as a first-class relationship graph.

**Modeling - secondary:**

**DBML**: A concise database modeling language for readable ERDs and schema review. Use it to make entity relationships explicit before implementation or migration work.

**SchemaSpy**: Reverse-engineers database metadata into browsable documentation and ER diagrams. Use it to inspect the current schema shape and expose hidden coupling or naming drift.

**Fallback - reference/ground + reference/trace**: Use when repository or structured model access is incomplete. Label all output as fallback when the model is inferred from secondary sources.

## Tool Routing

- The current domain code, schema, or tests are available -> start with `repository`.
- Runtime behavior, migration impact, or operational drift matters -> add `logs`.
- The task is schema-first or migration-sensitive -> use `atlas` to review or validate the desired structure before changing it.
- Permissions, ownership, or relationship-based access is part of the model -> use `openfga`.
- The domain is easier to reason about as a relational diagram or DSL -> use `dbml`.
- The existing database shape needs reverse-engineered documentation -> use `schemaspy`.
- The primary evidence path is unavailable or incomplete -> use `reference/ground, reference/trace`.
- Do not depend on a single source when the domain boundary affects persistence, lifecycle, or authorization semantics.

## Tool Selection Rationale

- Use `repository` first because it shows the live source of truth for entities, schema, tests, and model code.
- Use `logs` when behavior exists in production or staging but is not obvious from code alone.
- Use `atlas` when schema change safety, drift detection, or migration planning is part of the domain risk.
- Use `openfga` when the model includes ownership, permission, or relationship edges that should stay explicit.
- Use `dbml` when a concise relational sketch will expose missing entities or broken boundaries faster than raw code.
- Use `schemaspy` when the current database structure needs reverse-engineered documentation before changes are made.
- Use `reference/ground` and `reference/trace` only when the primary evidence path is missing or incomplete.

## Tool Path

- Start with `repository`.
- Use `logs` when current runtime behavior, migrations, or incidents are needed to ground the model.
- Use `atlas` when schema drift, migration safety, or declarative schema planning materially affects the domain.
- Use `openfga` when permissions, ownership, or relationship rules are part of the model.
- Use `dbml` or `schemaspy` when a relational view will expose model gaps faster than raw code.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, reference/trace`.
- If both paths fail, produce the best-guess output described as: A backend domain model implementation or design with explicit entities, rules, transitions, transformations, and open risks.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Environment and Reproducibility

Record the following in the deliverable when known:

- Service or module name
- Repository path or schema file path reviewed
- Commit hash or build identifier
- Database engine and schema version when relevant
- Migration state or release window when relevant
- Auth or data-state assumptions that affect the model
- Runtime environment or logs consulted, if any

If any item is unknown, state it explicitly. Do not present inferred data-shape behavior as confirmed behavior.

## Model Building

Before evaluating implementation details, construct the domain model.

The model should answer:

1. What are the core entities, concepts, aggregates, or relationships?
2. What invariants must always hold?
3. What state transitions are allowed, forbidden, or conditional?
4. What data is derived, normalized, denormalized, or transformed?
5. What persistence boundaries or ownership boundaries matter?
6. What permissions or relationship edges are part of the domain if applicable?

No conclusions should be written before the model is built and named.

## Core Method Execution

Follow this sequence:

1. Clarify scope. Identify the exact domain slice, any known constraints, and the source of truth that matters most.
2. Inventory entities and relationships. List the core nouns, aggregates, ownership boundaries, and any authorization relationships.
3. Extract invariants. Separate hard rules from implementation preferences or accidental behavior.
4. Map transitions. Identify lifecycle changes, guarded mutations, and any illegal state moves.
5. Review transformations. Note normalization, derived fields, denormalization, or mapping logic that changes meaning or shape.
6. Check persistence and schema fit. Verify whether the current schema, migrations, or model files support the rules without hidden coupling.
7. Surface ambiguity. Mark edge cases, missing constraints, or places where the model is implied rather than explicit.
8. Synthesize findings. Group repeated problems into system-level patterns and keep the output traceable.

When helpful, validate the model with one of these aids:
- `atlas` for schema drift or migration safety
- `openfga` for permission and relationship modeling
- `dbml` for readable schema review
- `schemaspy` for reverse-engineered schema documentation

## Workflow Notes

- Keep core rules explicit enough that later changes do not splinter the domain model.
- Separate foundational domain logic from transport, UI, or API concerns.
- Preserve stable entity, relationship, and model names when downstream roles need a durable source of truth.
- Prefer one clear source of truth for each invariant, even when multiple layers reference it.
- Surface ambiguity instead of encoding accidental behavior as a rule.

## Structured Findings

Every finding must use this exact schema. Keep observations separate from interpretation and tie each finding to evidence.

```
#### Finding <id>
Observation: [What was found, without interpretation]
Evidence: [Source: repository path / schema / log / doc / diagram]
Cause: [Why this issue likely exists - label as inferred if not confirmed]
Impact: [What breaks, drifts, or becomes harder to maintain]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** - directly observed in the repository, schema, logs, or current docs, and confirmed by at least two sources when available.
- **Medium** - observed in one source or tool path; not yet cross-validated.
- **Low** - inferred from indirect evidence; needs validation against the real model or runtime behavior.

## Prioritization Logic

Prioritize findings by model risk and downstream blast radius:

1. **Critical** - Broken invariants, incorrect ownership boundaries, invalid transitions, or schema changes that can corrupt data or expose unauthorized access.
2. **Significant** - Rule ambiguity, weak boundaries, transformation drift, or schema decisions that will likely require a breaking change later.
3. **Minor** - Naming, documentation, or low-risk alignment gaps that do not materially change behavior.

Do not exceed six standalone findings unless the domain slice is unusually large. Group repeated issues into patterns rather than listing duplicates.

## Pattern Detection

Look for recurring or system-level issues:

- **Rule duplication** - The same business rule is encoded in multiple places.
- **Boundary drift** - Ownership between domain, persistence, and transport layers is unclear.
- **Transition gaps** - A state can be entered but not exited, or a required guard is missing.
- **Transformation drift** - Derived data or normalization logic differs across call sites.
- **Authorization leakage** - Access rules are implicit, duplicated, or mixed into unrelated logic.
- **Schema mismatch** - The code model and stored model have diverged.

Distinguish intentional design choices from unintentional drift. They require different follow-up actions.

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- State a direction, not a full implementation plan
- Note evidence limits when confidence is Medium or Low
- Avoid recommending new abstractions unless the model risk justifies the downstream change

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly in the deliverable:

- **Fully analyzed**: Entities, rules, transitions, or transformations that were grounded in a clear source of truth.
- **Partially analyzed**: Areas where the model exists but important edges or ownership details are still unclear.
- **Not analyzed**: Related surfaces that were out of scope or had no usable evidence.
- **Not implemented**: Model gaps that are known but intentionally deferred, with rationale.

## Limits and Unknowns

Mandatory section. State:

- What could not be validated from the available model sources
- What requires real runtime, schema, or migration validation
- Where confidence is low because the source of truth is incomplete
- Where authorization or data ownership assumptions remain unverified
- Where a tool path such as Atlas, OpenFGA, DBML, or SchemaSpy was unavailable

Do not collapse this section into a single sentence. Unverified model decisions create compounding risk.

## Workflow Rules

The agent must:
- Build the model before analysis
- Separate fact from inference
- Keep the domain logic distinct from transport or UI concerns
- Merge duplicates and avoid redundant findings
- Preserve stable names for entities, relationships, and model files when downstream work depends on them
- Treat missing inputs as assumptions, not as confirmed facts

