---
name: naming-and-taxonomy
description: Applies card sorting, tree testing, semantic analysis, and Dan Klyn's ontology–taxonomy–choreography model to design coherent, durable naming systems and information architecture labels for product surfaces, navigation, and settings.
trigger: When terminology or IA wording needs deliberate design — new feature naming, navigation restructuring, settings taxonomy, global term standardization, or when synonym proliferation or user confusion is detected in existing labels.
required_inputs:
  - the product surface, feature area, or navigation structure being named
  - the decision or design question the naming work should resolve
  - existing terms in use (even if inconsistent) and known conflicting or ambiguous labels
  - user mental model evidence when available (research notes, card sort results, search analytics)
recommended_passes:
  - Pass 1 — Concept model: inventory entities, map relationships, identify user mental models before any naming begins
  - Pass 2 — Semantic analysis: audit existing labels, scan competitor terminology, surface patterns and anomalies
  - Pass 3 — Candidate generation: produce naming candidates against rubric (clarity, distinctiveness, durability, localizability, brand fit)
  - Pass 4 — Validation design: structure card sorting or tree testing protocol when research is available
  - Pass 5 — Recommendation: score candidates, select winners, document rationale and terms to retire
tool_stack:
  runtime:
    primary: notion
    secondary: airtable
  card_sorting:
    primary: optimal_workshop
    secondary: uxtweak, maze
  tree_testing:
    primary: optimal_workshop
    secondary: uxtweak
  term_management:
    primary: frontify
    secondary: notion
  semantic_analysis:
    primary: search_query
    secondary: semrush, ahrefs
  fallback:
    primary: search_query, reference/reuse
tool_routing:
  - if: card sorting study is needed to discover user mental models
    use: optimal_workshop (OptimalSort) for moderated or unmoderated open/closed card sorts; uxtweak or maze as alternatives with lower cost
  - if: navigation label validation is needed via tree testing
    use: optimal_workshop (Treejack) for tree testing; uxtweak as alternative
  - if: a permanent, versioned term register is needed
    use: airtable for structured glossary database with term history and status fields; notion for lighter-weight term documentation
  - if: brand glossary or cross-team terminology governance is needed
    use: frontify to publish an approved term library accessible to design, content, and engineering
  - if: competitor terminology and industry search language must be analyzed
    use: semrush or ahrefs for keyword research and industry term frequency; supplement with search_query for direct competitor scanning
  - if: all primary tools are unavailable, blocked, or out of credits
    use: search_query and reference/reuse; label all output as fallback or inferred
best_guess_output: A naming and taxonomy proposal with a concept model, naming criteria, scored candidate table, recommended naming system with rationale, and a list of terms to retire — labeled as inferred where no primary tool access was used.
output_artifacts:
  - knowledge/content-designer-naming-and-taxonomy.md
  - knowledge/assets/ (for visual artifacts)
done_when: Every label in scope has a recommended name with rationale, naming candidates are scored against the rubric, terms to retire are documented, the naming system is internally consistent, and at least one validation path (card sort, tree test, or expert review) has been applied or explicitly deferred with justification.
---

# Naming and Taxonomy

## Purpose

This skill designs coherent, durable naming systems and information architecture labels for product surfaces, navigation, settings, and feature concepts.

Reasoning type: ontological before linguistic — the agent must first establish what entities exist and how they relate before generating any label. Naming decisions are downstream of concept model decisions.

Methods anchored to: Dan Klyn's distinction between ontology (what things are), taxonomy (how they are categorized), and choreography (how they behave over time); Peter Morville's information architecture facets (findable, accessible, usable, credible, desirable); card sorting methodology (open and closed) for discovering and validating user mental models; tree testing for navigation label validation; semantic analysis of competitor and industry terminology; and a naming criteria rubric (clarity, distinctiveness, durability, localizability, brand fit).

This skill does NOT write full UX copy, design full navigation structures without existing IA artifacts, conduct original user research sessions, or make brand positioning decisions. It translates concept models and evidence into specific, justified label recommendations.

---

## Required Inputs and Assumptions

**Required:**
- The product surface, feature area, or navigation structure being named
- The specific decision the naming work must resolve (e.g., "what do we call this new workflow type?", "how should we label the three tiers of access?")
- Existing terms already in use — even if inconsistent, duplicated, or internally contested
- Known conflicting, ambiguous, or retiring labels

**Strongly helpful:**
- User mental model evidence: card sort results, tree test results, support ticket language, search query logs
- Competitor term inventory from adjacent products
- Localization constraints: languages the product ships in, known translation risk terms
- Brand voice guidelines: tone, formality level, any established naming conventions

**Known vs unknown at naming time:**
- Known: the entities that need names, the surfaces where labels appear
- Often unknown: which mental model users actually hold, whether synonyms reflect genuine conceptual differences or historical drift, localization feasibility of candidate terms

**Assumption rule:** If user mental model evidence is absent, infer a provisional model from observable product structure, support language, and competitor terminology. Label the inferred model as `Assumed context:` and flag it as requiring validation before final naming decisions are committed to production.

---

## Input Mode and Evidence Path

Declare the path used before beginning any naming work. Options:

1. **Card sort results available** — Mental model evidence is sourced from a completed open or closed card sort. Highest confidence for taxonomy structure. Use results to anchor the concept model directly.
2. **Tree test results available** — Navigation label validation data exists. Use to score existing or candidate labels against findability before recommending.
3. **Search analytics available** — Internal site search logs or external keyword data (Semrush, Ahrefs) reveal the language users actually use when seeking concepts. Use to assess naturalness of candidate terms.
4. **Competitor and industry term audit** — Semantic analysis of how the competitive landscape names equivalent concepts. Moderate confidence; indicates industry convention without proving user preference.
5. **Design artifacts and documentation** — Existing navigation, settings screens, design system token names, developer API terminology. Useful for mapping what already exists; limited for understanding user intent.
6. **Inference** — No primary evidence; naming is based on product knowledge, linguistic analysis, and domain expertise. Label all output as `inferred`. Flag for validation before production use.

**Declare the evidence path in the `### Concept model` section of the deliverable.**

---

## Tool Stack

**Runtime primary — Notion**
Naming system documentation: term definitions, candidate comparison tables, decision rationale, terms to retire. Central deliverable home. Use for structured naming proposals and version-tracked term registers.

**Runtime secondary — Airtable**
Structured glossary database with columns for term, status (active / candidate / retiring), surface, definition, localization note, and last-reviewed date. Preferred when the naming system spans many terms and requires ongoing governance by multiple roles. Supports filtered views by surface or status.

**Card sorting — Optimal Workshop (OptimalSort)**
Moderated and unmoderated open and closed card sorts. Open sorts reveal how users naturally group and name concepts without constraint. Closed sorts test whether a proposed taxonomy matches user expectations. Industry standard for IA research. Use when a new taxonomy structure needs validation before committing.

**Card sorting alternative — UXTweak / Maze**
UXTweak offers card sorting and tree testing in a single platform at lower cost than Optimal Workshop. Maze card sort is well-integrated into existing design workflows via Figma. Use either when Optimal Workshop is unavailable or budget is constrained.

**Tree testing — Optimal Workshop (Treejack)**
Tests whether users can find items using proposed navigation labels and hierarchy — without visual design cues. Measures findability per label, directness rate, and first-click accuracy. Use for validating navigation label changes before shipping.

**Term management — Frontify**
Publishes an approved, searchable glossary accessible to design, content, engineering, and marketing. Supports term status (approved / deprecated / under review), usage examples, and cross-team visibility. Use when the naming system must be governed across multiple teams or when a design system already lives in Frontify.

**Semantic analysis — Semrush / Ahrefs**
Keyword research and competitive term frequency analysis. Use to understand what language users search for when seeking the concept in question, how competitors name equivalent features, and which terms carry high search intent vs. low. Particularly valuable for named features that will appear in marketing, documentation, or public surfaces.

**Fallback — search_query, reference/reuse**
Manual competitor surface scanning and industry reference review when primary tools are unavailable. Label all output as `fallback`. Cross-reference at least three competitor or industry sources before drawing semantic conclusions from fallback research.

---

## Tool Routing

- Discovering how users mentally group product concepts → use Optimal Workshop (OptimalSort) for open card sort; UXTweak or Maze as alternatives.
- Validating that users can find items under proposed navigation labels → use Optimal Workshop (Treejack) for tree testing; UXTweak as alternative.
- Building a versioned, governed term register for multi-team use → use Airtable for database structure; Frontify for publication and governance.
- Analyzing industry and competitor terminology patterns → use Semrush or Ahrefs for search frequency signals; supplement with search_query for direct product scanning.
- Documenting and storing naming proposals and decisions → use Notion as primary deliverable home.
- Primary tools unavailable → use search_query and reference/reuse; label output explicitly as `fallback` or `inferred`.
- Do not rely on a single method. Combining semantic analysis (what industry uses) with card sort evidence (what users expect) and tree testing (what users can find) produces durable naming decisions. Any single method alone risks over-indexing on language the team or market prefers rather than language users understand.

---

## Environment and Reproducibility

- **Platform:** browser-based tools (Optimal Workshop, UXTweak, Maze, Airtable, Notion, Frontify, Semrush, Ahrefs) — no local install required
- **Card sort state:** record participant count, sort type (open/closed), sort date, and completion rate. Card sort results are point-in-time and tied to the product structure shown; re-test when product structure changes significantly.
- **Tree test state:** record participant count, test date, the tree structure tested, and the tasks given. Tree test validity depends on task wording — document tasks verbatim.
- **Semantic analysis state:** Semrush and Ahrefs data reflects search volume at a specific point in time; industry terminology evolves. Record data pull date.
- **Version:** name the version of the product IA or navigation structure that was the input to this naming pass. If the structure changes, the naming recommendation may need revision.

---

## Model Building

The agent must build a concept model before generating any candidate names. Naming words before understanding what the words refer to produces labels that feel right locally but break down at system scale.

### Concept model components

**1. Entity inventory**
List every concept, object, action, state, or role that needs a name or label in this scope. Include:

```
| Entity ID | What it is (description)              | Current name(s) in use     | Surface(s) where it appears   |
|-----------|---------------------------------------|----------------------------|-------------------------------|
| E01       | [description]                         | [existing terms]           | [nav / settings / UI / docs]  |
| E02       | ...                                   | ...                        | ...                           |
```

Flag entities with multiple names in use as synonym proliferation candidates.

**2. Relationship map**
Document how entities relate to each other: parent–child hierarchies, sibling groupings, action–object relationships, states and transitions. Use Dan Klyn's three-layer frame:

- **Ontology** — What is this thing? What makes it distinct from adjacent things? Where are the conceptual boundaries?
- **Taxonomy** — How does it fit into a hierarchy or classification with related things?
- **Choreography** — How does it behave over time, in sequence, or in relation to user actions?

Ontology must be resolved before taxonomy is imposed. Taxonomy must be resolved before choreography labels (e.g., button labels, action names) are designed.

**3. User mental model map**
Record what mental model users appear to hold for this concept, based on available evidence. If card sort results exist, map the user-generated groupings here. If evidence is absent, infer from support ticket language, internal search queries, or onboarding friction points. Label inferred mental models explicitly.

Note where the user mental model diverges from the current product model — this divergence is usually the source of confusing labels.

**4. Hierarchy and facet check**
Apply Morville's IA facets to the concept inventory. For each entity or label, ask:
- **Findable**: Can a user searching for this concept encounter the right label?
- **Accessible**: Does the label communicate clearly to users with different levels of domain expertise?
- **Usable**: Does the label predict the behavior or content behind it accurately enough that users can act?

No naming candidates are generated until the concept model is complete and reviewed.

---

## Core Method Execution

Follow this sequence for every naming and taxonomy engagement.

**Step 1 — Clarify the scope and decision frame**
Define which concepts, surfaces, or navigation layers are in scope for this pass. Identify the specific naming question(s) to answer. If the scope is vague, write a provisional scope statement, label it `Assumed context:`, and proceed.

**Step 2 — Build the concept model**
Complete the entity inventory, relationship map, user mental model map, and facet check per the Model Building section above. Document in `### Concept model`. Do not proceed until this is done.

**Step 3 — Audit existing terminology**
For every entity in scope, list all current names and labels in use across surfaces (UI, docs, API, support, marketing). Identify:
- Synonym proliferation: the same concept named differently across surfaces
- Ambiguous labels: terms that could refer to more than one concept
- Over-technical terms: terms that map to internal or engineering constructs rather than user tasks
- Collisions: terms that are used for one concept in the product but mean something different in the industry or to the user

Document findings in `### Terminology audit`.

**Step 4 — Run semantic analysis**
Scan competitor and adjacent products for how they name equivalent concepts. Use Semrush or Ahrefs to identify search language users apply when seeking these concepts. Look for:
- Industry convergence: terms used consistently across 3+ competitors (suggests a settled convention users may already hold)
- Differentiators: terms a competitor has coined that are now associated with their brand and should be avoided
- Search language: how users phrase the concept in search queries vs. how the product currently labels it

Document in `### Semantic analysis`.

**Step 5 — Generate naming candidates**
For each entity or label in scope, generate 3–5 naming candidates. Candidates must be generated against the naming rubric, not by brainstorm alone. Each candidate must be:
- Distinct from other entities in the concept model
- Grounded in either user language (from evidence) or clear domain convention (from semantic analysis)
- Tested mentally against localization: does it translate without distortion, does it carry gender or formality implications in target languages?

**Step 6 — Score candidates against the naming rubric**
Apply the structured candidate scoring schema (see Structured Findings section).

**Step 7 — Design validation when research is available**
If card sorting or tree testing is in scope:
- **Open card sort**: present entity names or brief descriptions (not current labels) to participants; ask them to group and name the groups; reveal the user-generated taxonomy
- **Closed card sort**: present proposed category labels; ask participants to place entities into them; reveal fit between proposed taxonomy and user expectations
- **Tree testing**: build the proposed navigation tree in Treejack; give participants task-based scenarios; measure findability rate, directness, and first-click accuracy per label

If research is not available in this pass, note the validation gap explicitly and recommend the appropriate study type.

**Step 8 — Recommend the naming system**
Select winning names based on rubric scores and validation evidence. Document the recommended naming system as a complete set — not individual names in isolation. The system must be internally consistent: naming conventions (noun vs. verb, singular vs. plural, compound vs. separate words) must be uniform across the entity set. Document rationale for each selection.

**Step 9 — Document terms to retire**
List every current term that the recommended naming system replaces. For each retiring term, note: what it is being replaced with, where it currently appears, and the migration priority.

---

## Structured Findings

Every naming candidate must be scored using this schema. No free-form candidate assessment.

```
### Candidate: [term]
Entity:          [Entity ID from concept model]
Definition:      [One sentence — what this name would refer to]
Clarity score:   [1–5 — how unambiguous is this label for target users]
Distinctiveness: [1–5 — how well does it avoid collision with sibling concepts or competitor terms]
Durability:      [1–5 — how well will it hold as the product evolves; is it feature-specific or concept-level]
Localizability:  [1–5 — how cleanly does it translate; note specific language risks]
Brand fit:       [1–5 — alignment with established naming conventions and tone]
Total score:     [sum / 25]
Evidence path:   [sourced / fallback / inferred]
Recommendation:  [Preferred / Acceptable / Reject — with one-line rationale]
```

**Scoring guide:**
- 5: No issues — strong fit on this dimension
- 4: Minor concern, addressable
- 3: Moderate concern; requires trade-off acknowledgment
- 2: Significant weakness; only use if alternatives score worse
- 1: Disqualifying on this dimension

**Separation rule:** The candidate description (what it would mean) must be written before scoring. Never collapse definition and evaluation into the same step.

---

## Prioritization Logic

After all candidates are scored, apply the following prioritization logic to determine which naming decisions require the most attention and rigor.

**1. Prioritize by user confusion risk**
Entities where current terminology has generated measurable confusion (support tickets, search failure, usability session breakdowns) take highest priority. Naming changes here have the highest impact on user success.

**2. Prioritize by surface visibility**
Labels on primary navigation, global headers, onboarding flows, and empty states are seen by every user on every session. Name these before labels in secondary settings or power-user flows.

**3. Prioritize by system breadth**
Entities that appear across multiple surfaces, roles, or product areas generate the most downstream inconsistency when poorly named. Resolve these first to prevent synonym proliferation from spreading.

**4. Defer low-visibility, low-confusion candidates**
Labels that appear only in advanced settings, APIs, or documentation with low user confusion evidence can be recommended with lower validation confidence. Flag them as `lower priority` and note the validation that would increase confidence.

---

## Pattern Detection

After the terminology audit and semantic analysis are complete, the agent must explicitly identify and document:

- **Synonym proliferation**: the same concept labeled differently across UI, docs, API, support copy, and marketing. Most common source of taxonomy debt. Document every instance per entity.
- **Ambiguous labels**: a single term that refers to more than one distinct concept. High user confusion risk. These must be resolved before any dependent naming decisions are finalized.
- **Over-technical terms**: labels derived from implementation or engineering constructs rather than user tasks or mental models. Common in settings and API-facing surfaces. Flag for translation into user-task language.
- **Collisions with existing concepts**: terms the product uses that carry a different meaning in the industry, in the user's prior experience, or in adjacent product surfaces. These undermine learnability.
- **Premature specificity**: names tied to a feature's current implementation that will become inaccurate or misleading as the product evolves (e.g., "Import CSV" when the feature will eventually support multiple formats).
- **False relationships**: names that imply a conceptual grouping or hierarchy that does not exist in the product model (e.g., calling two independent actions "Basic" and "Advanced" implies a progression the UX does not actually enforce).

---

## Coverage Map

Document in the deliverable which entities and surfaces were addressed in this naming pass.

```
| Entity ID | Entity name          | Surfaces covered            | Naming status       | Validation status          |
|-----------|----------------------|-----------------------------|---------------------|----------------------------|
| E01       | [name]               | [list surfaces]             | Recommended         | Tree tested                |
| E02       | [name]               | [list surfaces]             | Recommended         | Not validated — card sort deferred |
| E03       | [name]               | [list surfaces]             | Candidates scored   | Awaiting stakeholder review|
| E04       | [name]               | [list surfaces]             | Out of scope        | —                          |
```

State the overall coverage: what proportion of in-scope entities received a full naming recommendation vs. a scored candidate set vs. a deferred decision. If fewer than 70% of in-scope entities have a final recommendation, flag the output as a first pass and specify what is needed to complete it.

---

## Limits and Unknowns

Document honestly:

- Where user mental model evidence is absent and the concept model is inferred
- Which naming candidates could not be validated by card sort or tree test
- Where localization assessment was not done by a native speaker or localization specialist
- Terms that may conflict with legal, trademark, or brand constraints not reviewed in this pass
- Competitor terms that may be protected or strongly associated with a competitor brand
- Where synonym proliferation exists in surfaces outside the naming system's scope (e.g., in third-party integrations, partner documentation) that cannot be addressed without broader coordination
- Where the naming recommendation depends on a product model or IA decision that is still in flux

Do not omit this section. Naming decisions made on inferred evidence can propagate into design system tokens, API contracts, and localization files — the downstream cost of a wrong name is high.

---

## Workflow Rules

1. Build the concept model before generating any naming candidates. Naming without ontological clarity produces labels that are locally plausible but systemically incoherent.
2. Complete the terminology audit before semantic analysis. Know what the product already says before analyzing what the industry says.
3. Apply the naming rubric to every candidate. No winner may be selected by preference alone.
4. Do not finalize a naming system that contains unresolved ambiguities — two entities with names that could be confused must be distinguished before the recommendation is complete.
5. Distinguish the naming recommendation (what to use) from the migration recommendation (how to get there) — both must be documented, but they are separate deliverables.
6. Label every output section as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
7. If a card sort or tree test is in scope but cannot be run in this pass, state so explicitly in the recommendation and note the validation risk of proceeding without it.
8. Do not recommend retiring a term without documenting where it appears and what replaces it. Orphaned retirements create content debt.

---

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/content-designer-naming-and-taxonomy.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

---

## Required Deliverable Sections

Within `## Skill: naming-and-taxonomy`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Concept model` — entity inventory, relationship map (ontology / taxonomy / choreography layers), user mental model map, facet check; evidence path declared
- `### Terminology audit` — all current terms in use per entity, synonym proliferation findings, ambiguous labels, over-technical terms, collisions
- `### Semantic analysis` — competitor naming patterns, industry conventions, search language signals, differentiators to avoid
- `### Naming candidates` — all candidates in structured scoring schema, grouped by entity
- `### Recommended naming system` — winning names with rationale, naming convention rules, internal consistency statement
- `### Terms to retire` — retiring terms with replacements, surfaces affected, migration priority
- `### Coverage map` — entities and surfaces addressed, naming and validation status per entity
- `### Limits and unknowns` — inferred inputs, unvalidated decisions, localization gaps, out-of-scope surfaces

---

