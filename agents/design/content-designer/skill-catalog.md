# Content Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `content-review`

- Description: Applies heuristic evaluation, readability scoring, and voice/tone rubric analysis to audit an existing content surface — surfaces, components, and copy taxonomy — and produces traceable findings, severity-scored issues, and directional rewrite recommendations.
- Trigger: When product copy exists on a surface, flow, or component set and the team needs to know what to rewrite, in what order, and why. Run after shipping, before a content audit, ahead of a brand refresh, or when copy quality is flagged as a risk.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A content review with a surface inventory, heuristic findings in structured schema, readability scores, voice/tone ratings, severity-prioritized issues, and directional rewrite recommendations — labeled as inferred where no direct source access exists.
- Output: knowledge/runs/<run-id>/content-designer-content-review.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every string in scope has been evaluated against the content heuristics, every finding has a location reference and severity score, and the team can prioritize rewrites without reading the raw copy themselves.

## `conversation-and-guidance-design`

- Description: Applies intent taxonomy, Grice's cooperative principle, progressive disclosure, and Google PAIR conversation design guidelines to design in-product guidance, assistant flows, and conversational interfaces that support task completion without over-explaining.
- Trigger: When the product needs embedded guidance, assistant copy, onboarding flows, chatbot dialogue, tooltips with logic, or any conversational surface where the system speaks to the user to help them complete a task.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A guidance and conversation design pack including a user intent map, guidance model, structured message library per flow state, escalation and fallback copy, and a pattern audit — labeled sourced, fallback, or inferred to match the evidence path used.
- Output: knowledge/runs/<run-id>/content-designer-conversation-and-guidance-design.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every user intent in scope has guidance copy for each flow state (entry, in-progress, reassurance, escalation, fallback); all copy passes Grice's relevance and quantity maxims; no guidance gap or missing escalation path remains undocumented.

## `error-empty-success-states`

- Description: Applies state machine modeling, Nielsen's error heuristics, and the NNG empty-state framework to enumerate all non-default UI states and write recovery-first, severity-tiered messaging for each one.
- Trigger: When a feature needs state-specific messaging beyond the happy path — including error, empty, loading, timeout, partial-success, and success states.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A state inventory covering all system states, with a headline, body, CTA, recovery action, voice constraint, and confidence level per state — labeled as inferred where no live product access exists.
- Output: knowledge/runs/<run-id>/content-designer-error-empty-success-states.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every critical state has explicit user-facing messaging with a recovery action, no state exposes raw technical codes to users, severity voice is consistent across the message set, and the coverage map confirms all enumerated states are addressed or explicitly deferred.

## `localization-prep`

- Description: Applies W3C i18n guidelines, Unicode CLDR standards, ICU Message Format, and pseudo-localization testing to audit user-facing strings, surface expansion and structural risks, and produce a handoff-ready localization package that translators and engineers can act on without guesswork.
- Trigger: When user-facing text must survive translation and locale-sensitive adaptation cleanly — at string freeze, before a new locale is added, when a feature with new strings ships, or when existing copy is flagged for localization issues.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A localization-ready content package including a categorized string inventory, string risk table with severity ratings, ICU format recommendations, pseudo-localization expansion estimates, locale-sensitive data rules, terminology lockdown list, and translator notes — labeled as inferred where no primary tool access exists.
- Output: knowledge/runs/<run-id>/content-designer-localization-prep.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every string in scope is inventoried by surface type, every high and critical risk has a recommended fix, ICU format is validated or flagged, expansion estimates are documented for all strings, translator notes are written for all ambiguous strings, and the package is actionable for both the localization team and engineering without further clarification.

## `microcopy-flow-design`

- Description: Applies Torrey Podmajersky's Strategic UX Writing method, the STEM framework (Situation, Task, Expectation, Message), and Jobs-to-be-Done copy framing to produce a flow-level microcopy set — covering every screen, state, and decision point in a user flow with consistent voice, vocabulary, and sequencing logic.
- Trigger: When a feature or flow needs coherent UX writing — including new flows, redesigned flows with stale copy, flows with inconsistent nomenclature, or any surface where copy ambiguity is causing user drop-off or support volume.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A flow-level microcopy set organized as a step-by-step copy table — with screen name, copy element type, proposed copy, STEM rationale, and voice rule applied — covering all reachable states in the flow. Labeled as inferred where no primary tool access exists.
- Output: knowledge/runs/<run-id>/content-designer-microcopy-flow-design.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every step in the flow has copy for all reachable states (default, loading, error, empty, success), copy is internally consistent in terminology and voice, all decision points have clear action labels, and the flow can be navigated without ambiguity by a first-time user.

## `naming-and-taxonomy`

- Description: Applies card sorting, tree testing, semantic analysis, and Dan Klyn's ontology–taxonomy–choreography model to design coherent, durable naming systems and information architecture labels for product surfaces, navigation, and settings.
- Trigger: When terminology or IA wording needs deliberate design — new feature naming, navigation restructuring, settings taxonomy, global term standardization, or when synonym proliferation or user confusion is detected in existing labels.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A naming and taxonomy proposal with a concept model, naming criteria, scored candidate table, recommended naming system with rationale, and a list of terms to retire — labeled as inferred where no primary tool access was used.
- Output: knowledge/runs/<run-id>/content-designer-naming-and-taxonomy.md, knowledge/runs/<run-id>/assets/ (for visual artifacts)
- Done when: Every label in scope has a recommended name with rationale, naming candidates are scored against the rubric, terms to retire are documented, the naming system is internally consistent, and at least one validation path (card sort, tree test, or expert review) has been applied or explicitly deferred with justification.
