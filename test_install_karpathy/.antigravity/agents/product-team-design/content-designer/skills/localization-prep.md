---
name: localization-prep
description: Applies W3C i18n guidelines, Unicode CLDR standards, ICU Message Format, and pseudo-localization testing to audit user-facing strings, surface expansion and structural risks, and produce a handoff-ready localization package that translators and engineers can act on without guesswork.
trigger: When user-facing text must survive translation and locale-sensitive adaptation cleanly — at string freeze, before a new locale is added, when a feature with new strings ships, or when existing copy is flagged for localization issues.
required_inputs:
  - the set of user-facing strings, string keys, or Figma screens in scope
  - the target locales or locale set (e.g., de-DE, ja-JP, ar-SA, pt-BR)
  - the surface type (UI labels, help text, error messages, marketing copy, legal text)
  - the engineering i18n framework in use when known (e.g., i18next, react-intl, Android strings.xml, iOS Localizable.strings)
recommended_passes:
  - Pass 1 — String inventory: categorize all strings by surface type and collect into structured inventory
  - Pass 2 — Risk audit: identify hardcoded strings, concatenation issues, plural failures, layout expansion risks, locale-sensitive data patterns
  - Pass 3 — ICU/framework alignment: validate or recommend ICU Message Format usage for variables, plurals, and genders
  - Pass 4 — Pseudo-localization: simulate 30–40% string expansion and flag layout breakage risks
  - Pass 5 — Translator notes: write context notes, character limits, and screenshot references for every ambiguous string
tool_stack:
  runtime:
    primary: [lokalise, figma]
    secondary: [phrase, crowdin]
  extraction:
    primary: [i18next-parser, react-intl-cli]
  pseudo_localization:
    primary: [pseudolocalization-tool, chromium-pseudo-locale]
  artifacts:
    primary: [notion]
  fallback:
    primary: [search_query, reference/verify]
tool_routing:
  - if: team uses a TMS already (Lokalise, Phrase, or Crowdin)
    use: connect to TMS for string import, in-context review, and translator note authoring
  - if: strings live in Figma designs before engineering handoff
    use: figma with a localization plugin (e.g., Localization by Aplazame or Content Reel) to extract text layers and check for expansion constraints
  - if: engineering framework is i18next or react-intl
    use: i18next-parser or formatjs CLI to extract string keys and validate ICU format compliance
  - if: layout expansion risk is the primary concern
    use: pseudo-localization simulation — apply 30–40% string expansion and check for truncation, overflow, or broken layouts
  - if: team uses Crowdin with open-source project
    use: crowdin for free-tier TMS with GitHub integration and automated string sync
  - if: primary tools are unavailable or no TMS is configured
    use: search_query + reference/verify; produce best-guess output labeled as inferred
best_guess_output: A localization-ready content package including a categorized string inventory, string risk table with severity ratings, ICU format recommendations, pseudo-localization expansion estimates, locale-sensitive data rules, terminology lockdown list, and translator notes — labeled as inferred where no primary tool access exists.
output_artifacts:
  - knowledge/content-designer-localization-prep.md
  - knowledge/assets/ (for visual artifacts)
done_when: Every string in scope is inventoried by surface type, every high and critical risk has a recommended fix, ICU format is validated or flagged, expansion estimates are documented for all strings, translator notes are written for all ambiguous strings, and the package is actionable for both the localization team and engineering without further clarification.
---

# Localization Prep

## Purpose

This skill audits user-facing strings and prepares a complete localization handoff package that translators, engineers, and designers can act on without guesswork.

Reasoning type: systematic audit — moving from string inventory through structural risk detection to actionable recommendations grounded in i18n standards.

Methods anchored to: W3C Internationalization (i18n) Activity guidelines, Unicode CLDR (Common Locale Data Repository) for locale-sensitive data patterns, ICU Message Format for plurals, genders, and variables, pseudo-localization testing (30–40% string expansion), string freeze process timing, and translator notes standards (context, character limits, screenshots).

This skill does NOT perform translation, manage TMS workflows end-to-end, write locale-specific copy, or make engineering decisions about i18n architecture. It produces the content audit and handoff package; implementation is done by engineers and translators.

---

## Required Inputs and Assumptions

**Required:**
- The strings, string keys, or Figma screens in scope for this pass
- The target locale set (at minimum: one high-expansion locale such as de-DE, and one bidirectional locale such as ar-SA if RTL is relevant)
- The surface type category (UI labels, help text, error messages, marketing copy, legal text)
- The engineering i18n framework when known

**Known vs unknown at prep time:**
- Known: the source language (typically en-US), the feature or flow the strings belong to
- Often unknown: character limits per string, confirmed engineering string keys, whether pluralization logic is already implemented, which locales are actively maintained
- Often ambiguous: whether a string is translatable (e.g., product names, trademarks, URLs — these require explicit classification)

**Assumption rule:** If target locales are not specified, default to a representative expansion set: de-DE (text expansion ~35%), ja-JP (multi-byte, compact), ar-SA (RTL, number formatting), pt-BR (expansion ~20%), and zh-CN (compact, logographic). Label this assumption as `Assumed locale set:` in the deliverable and note that the actual locale set must be confirmed before handoff.

---

## Input Mode and Evidence Path

Declare the path before starting the audit:

1. **Live / connected system** — direct access to TMS (Lokalise, Phrase, Crowdin) or the codebase string files. Highest fidelity; full key inventory, existing translations, and comment history are accessible.
2. **Figma designs** — strings extracted from Figma frames using a localization plugin or manual text-layer audit. Covers design-time strings; may not reflect engineering implementation.
3. **Exported string files** — .json, .po, .xliff, Android strings.xml, iOS Localizable.strings provided as artifacts. Good coverage; requires cross-referencing with designs to catch hardcoded UI strings.
4. **Screenshots / static input** — strings read from screenshots or design files. Limited: no key names, no variable structure, no existing translation history.
5. **Inference** — no direct access to strings; audit is from feature descriptions or tickets. All output labeled as `inferred`. Flag for engineering verification before handoff.

**Declare the path in `### String inventory` in the deliverable.**

---

## Tool Stack

**Runtime primary — Lokalise**
Cloud-based translation management system. Supports key-based string imports (.json, .po, .xliff, YAML), in-context editor for visual string review, translator notes with character limit fields, screenshot attachments, and ICU Message Format validation. Best for teams that need a centralized TMS with strong API and CI/CD integration. Use for: string import, translator note authoring, in-context review setup, and localization order management.

**Runtime primary — Figma (with localization plugins)**
Use Figma's text layer extraction to audit design-time strings. Plugins such as Localization by Aplazame or Content Reel surface text layers with expansion simulation. Best for pre-engineering audits where strings live in designs before being coded. Use for: text layer inventory, visual expansion checking, and design-time character limit flagging.

**Runtime secondary — Phrase (formerly Memsource / Phrase.com)**
Enterprise-grade TMS with translation memory, machine translation integration, and CAT tool built-in. Strong for large-scale localization programs with professional translation vendors. Use when team has a managed vendor relationship or requires CAT tool compatibility. Supports ICU Message Format and XLIFF natively.

**Runtime secondary — Crowdin**
Cloud TMS with GitHub/GitLab integration and a free tier for open-source projects. Supports over-the-air localization updates for mobile apps. Best for teams that want automated string sync from the codebase without a dedicated localization engineer. Use when the team's primary integration need is source control sync and translator community collaboration.

**String extraction — i18next-parser / formatjs CLI**
i18next-parser scans JavaScript/TypeScript/React source files and extracts i18next translation keys into JSON files. formatjs CLI (part of react-intl) validates ICU Message Format syntax, extracts messages, and compiles them for distribution. Use these for auditing what strings are actually in the codebase versus what is hardcoded or missing a key.

**Pseudo-localization testing — pseudolocalization-tool / Chromium pseudo-locale**
pseudolocalization-tool (npm package) applies pseudo-localized transforms to string files: expands strings by 30–40%, adds diacritical marks, and wraps strings in markers to detect untranslated strings at runtime. Chromium's built-in pseudo-locale (en-XA for expansion, ar-XB for RTL mirroring) can be activated in web apps without a real translation. Use for: layout expansion testing, untranslated string detection, RTL mirroring checks, and identifying hardcoded strings that don't appear in the pseudo-localized UI.

**Artifacts — Notion**
Localization package documentation: string inventory tables, risk tables, translator notes, terminology lockdown lists. Use for structured deliverable writing and for sharing the package with the localization team.

**Fallback — search_query, reference/verify**
Use to look up ICU Message Format syntax, CLDR locale data, W3C i18n technique articles, or framework-specific i18n documentation when direct tool access is unavailable. Label output as `fallback`.

---

## Tool Routing

- Team has a configured TMS → import strings into Lokalise or Phrase, author translator notes directly in the TMS, set character limits per key, attach screenshots. Do not duplicate this work in Notion; link to TMS project instead.
- Strings are in Figma designs pre-engineering → use Figma localization plugin for text layer extraction; run visual expansion check in Figma; export text inventory to Notion for risk audit.
- Engineering framework is i18next or react-intl → run i18next-parser or formatjs CLI to extract keys, then cross-reference with design inventory to catch hardcoded strings not yet in the i18n system.
- Layout expansion risk is the primary concern → apply pseudolocalization-tool to string files; activate Chromium pseudo-locale in the app; document truncation and overflow findings with screenshots.
- Team uses Crowdin with GitHub integration → audit via Crowdin's string list; add translator notes in-context; set up branch-based string sync so new strings are automatically queued for translation.
- No TMS configured → produce the full string inventory, risk table, and translator notes in Notion; recommend TMS setup as part of the output; label all output as `sourced` (if strings are directly readable) or `inferred` (if from descriptions only).
- All primary tools unavailable → use search_query + reference/verify; produce best-guess output; label as `fallback`.

---

## Environment and Reproducibility

- **String freeze date:** record when strings were frozen (i.e., when engineering committed to no further source string changes). Localization prep is only reliable if done after string freeze or with explicit acknowledgment that strings may change.
- **Source locale:** always en-US unless stated otherwise. Note if any strings are already locale-adapted (e.g., en-GB variants).
- **Framework version:** note the i18n library version (e.g., i18next 23.x, react-intl 6.x) because ICU support and plural rule handling vary by version.
- **String file format:** .json, .po, .xliff, strings.xml, Localizable.strings — note which format was audited.
- **TMS project ID:** if a TMS is in use, record the project identifier so the deliverable can be traced back to the source.
- **Reproducibility note:** localization prep output is point-in-time. If strings change after prep, re-run the risk audit on changed strings before handoff.

---

## Model Building

The agent must construct a string inventory model before performing any risk assessment.

### String inventory model

Categorize every string in scope into one of the following surface types. Surface type determines risk profile and translator guidance requirements.

**1. UI labels and navigation**
Button text, menu items, tab labels, section headers, field labels, tooltips. Typically short (1–5 words). High sensitivity to character limit and expansion. Must remain functionally clear in all locales.

**2. Help text and instructional copy**
Inline guidance, placeholder text, hint text, onboarding instructions. Medium length (10–50 words). High risk for sentence structure changes that break the English-language assumption of subject-verb-object order.

**3. Error messages**
Validation errors, system errors, network failures. Often contain variables (field names, counts, URLs). High risk for concatenation issues and variable position changes across languages.

**4. Marketing and promotional copy**
CTAs, feature callouts, value propositions, email subject lines. Variable length. Often contains idioms, wordplay, or culturally specific references that require transcreation rather than direct translation.

**5. Legal and compliance text**
Terms of service, privacy notices, consent language, regulatory disclosures. Requires certified or legal-review translation in many locales. Do not mark as low-risk based on length alone.

**6. Metadata and system strings**
Page titles, alt text, aria-labels, email subjects, notification titles. Often overlooked; frequently hardcoded; high impact on accessibility and SEO in localized builds.

**Inventory table format:**

```
| Key ID          | Surface type      | Source string (en-US)               | Character count | Variables | Plural logic | Priority |
|-----------------|-------------------|--------------------------------------|-----------------|-----------|--------------|----------|
| btn.save        | UI label          | Save changes                         | 12              | none      | no           | High     |
| err.required    | Error message     | {field} is required                  | 15 + variable   | {field}   | no           | High     |
| onboard.step2   | Help text         | Connect your account to get started  | 37              | none      | no           | Medium   |
| notif.items     | Metadata          | You have {count} new items           | 21 + variable   | {count}   | yes          | High     |
```

Build the full inventory before proceeding to the risk audit. Do not skip strings from the scope because they seem simple. Hardcoded strings and missing keys are found during inventory, not during risk assessment.

---

## Core Method Execution

Follow this sequence. Do not skip steps or reorder them.

**Step 1 — String extraction and inventory**
Extract all user-facing strings from scope (TMS, string files, Figma designs, or codebase scan). Categorize each string by surface type. Record key ID, source string, character count, variables, and whether plural logic is needed. Flag strings that have no key (hardcoded in UI or design). Complete the inventory table before proceeding.

**Step 2 — ICU Message Format validation**
For each string containing variables, plurals, or gendered forms, check whether it is written in valid ICU Message Format. ICU is the international standard for expressing these patterns in a way that works across locales.

ICU plural example (correct):
```
{count, plural, one {You have # new message} other {You have # new messages}}
```

ICU select example for gender (correct):
```
{gender, select, male {He accepted} female {She accepted} other {They accepted}}
```

Flag strings where:
- Variables are concatenated as string fragments (e.g., `"You have " + count + " items"`) — this breaks word order in many languages
- Plural logic uses a simple if/else rather than ICU plural categories (zero, one, two, few, many, other — per CLDR rules)
- Gendered noun agreement is needed for the target locale but not handled in the source
- Date, time, currency, or number formatting is hardcoded (e.g., `"$9.99"`, `"12/31/2024"`) rather than using locale-aware formatters

**Step 3 — Expansion risk assessment**
Apply Unicode CLDR expansion heuristics per target locale. Standard expansion estimates:
- German (de-DE): +20–35% character expansion
- French (fr-FR): +15–25%
- Portuguese Brazil (pt-BR): +15–25%
- Russian (ru-RU): +15–20%
- Japanese (ja-JP): typically shorter or equal
- Chinese Simplified (zh-CN): typically shorter or equal
- Arabic (ar-SA): typically equal length but requires RTL layout and different numeral system

For every string shorter than 20 characters, apply a minimum 100% expansion buffer — short strings expand proportionally more than long strings. Flag strings in constrained UI containers (button labels, table headers, tab labels, icon+label combinations) as High expansion risk.

**Step 4 — Pseudo-localization simulation**
Apply pseudo-localization to the string set:
- Use pseudolocalization-tool to generate a pseudo-locale string file: expand all strings by 35%, add diacritical marks to ASCII characters, wrap strings in `[!! ... !!]` markers.
- Load the pseudo-locale in the application or prototype.
- Document every layout breakage: truncation, overflow, wrapping, misalignment, clipped text.
- Run ar-XB (RTL mirror) simulation to identify bidirectional layout issues.
- Record all failures in the risk table with surface reference.

**Step 5 — Locale-sensitive data audit**
Identify all strings that contain or reference locale-sensitive data. Per W3C i18n and CLDR standards:
- **Dates and times:** check format (MM/DD/YYYY is US-only; use ISO 8601 or locale-aware formatters)
- **Numbers and decimals:** period vs. comma as decimal separator varies by locale
- **Currency:** do not hardcode currency symbols; use locale-aware currency formatters
- **Phone numbers:** format varies by country; do not hardcode format assumptions
- **Addresses:** field order and format vary significantly; do not hardcode address structure
- **Name order:** family name / given name order differs by locale (e.g., East Asian locales)
- **Units of measurement:** imperial vs. metric is not just US vs. rest of world; be explicit
- **Collation/sorting:** alphabetical sort order differs by locale; do not hardcode sort assumptions

**Step 6 — Terminology lockdown**
Identify product-specific terms, brand names, feature names, and trademarked terms that must not be translated. Document these in a Do Not Translate (DNT) list with rationale. Also identify terms that should be translated consistently (approved translations exist or must be created) and terms with multiple plausible translations that require a decision.

**Step 7 — Translator notes authoring**
For every string that is ambiguous, contains a variable, has a character limit, or is likely to be misread without context, write a translator note. Use the standard:
- **Context:** where does this string appear? What is the user doing at this moment?
- **Character limit:** maximum characters allowed in this surface
- **Variables:** what values can {variable} take? Is it a number, a name, a product name?
- **Screenshot reference:** attach or reference a screenshot showing the string in context
- **DNT note:** if the string contains a term that must not be translated, call it out explicitly

**Step 8 — String freeze alignment**
Confirm or recommend the string freeze date relative to the localization timeline. Standard guidance per W3C i18n best practices: string freeze should occur at least 2–3 weeks before the localized launch date for professional translation, accounting for translation time, review cycles, and engineering integration. If strings are not frozen, flag the risk explicitly and note which strings are at risk of changing.

---

## Structured Findings

Every string risk must conform to this schema. No free-form narrative in the risk table.

```
| String ID     | Surface           | Risk type             | Risk severity | Recommended fix                          | Translator note needed |
|---------------|-------------------|-----------------------|---------------|------------------------------------------|------------------------|
| btn.save      | UI label          | Expansion risk        | Medium        | Increase button min-width by 40%         | No                     |
| err.required  | Error message     | Concatenation risk    | Critical      | Rewrite as ICU: {field} is required.     | Yes — {field} values   |
| notif.items   | Metadata          | Plural handling risk  | High          | Implement ICU plural with CLDR categories| Yes — numeric range    |
| date.display  | Help text         | Locale-sensitive data | High          | Use locale-aware date formatter          | No                     |
```

**Risk severity definitions:**
- **Critical:** will break in translation without a code or content change (e.g., concatenation that makes grammatical sentences impossible in the target language; hardcoded untranslatable string)
- **High:** likely to produce poor UX in the target locale without a fix (e.g., truncation under expansion, plural logic that uses only singular/plural without CLDR categories)
- **Medium:** risk to quality or layout that should be addressed before launch but does not block translation (e.g., expansion risk in a non-critical container, missing context for an ambiguous string)
- **Low:** minor quality risk; acceptable to ship with a note (e.g., a string where an alternative phrasing would localize more naturally but the current form is translatable)

---

## Prioritization Logic

After the full risk table is assembled:

1. **Critical risks first:** any string with a Critical severity risk must have a recommended fix confirmed before the localization handoff is sent. Do not hand off Critical-risk strings without engineering or content resolution.
2. **High-risk strings second:** group by risk type (concatenation, plural, expansion, locale-sensitive data). Address concatenation and plural issues before expansion risks — structural issues are harder to fix post-translation.
3. **Surface frequency multiplier:** strings that appear on multiple screens or at high-traffic surfaces (login, onboarding, error recovery) carry higher effective priority than their individual risk rating suggests. Flag these.
4. **Medium and Low risks:** document and include in the handoff package with clear notes; do not block handoff on Medium/Low risks unless the locale or surface is specifically high-stakes (e.g., legal text, payment flows).
5. **String count threshold:** if more than 20% of strings in scope are Critical or High risk, recommend a pre-handoff engineering review session before sending to translation. Flag this explicitly.

---

## Pattern Detection

After the risk table is complete, the agent must identify and name cross-string patterns:

- **Concatenation pattern:** multiple error messages or dynamic strings built by joining translated fragments — flag as a systemic pattern, not individual string issues. Recommend a single architectural fix (move to ICU templates) rather than per-string patches.
- **Hardcoded string pattern:** strings appearing in the UI that are not present in any string file — these will not be translated. Document every hardcoded string found and the surface it appears in.
- **Plural handling failure pattern:** multiple strings using simple if/else plural logic that does not account for CLDR plural categories (zero, one, two, few, many, other). Flag as a pattern and recommend ICU plural adoption across the category.
- **Layout expansion failure cluster:** strings in the same UI component (e.g., all tab labels, all table column headers) that collectively fail under expansion. Address as a component-level design fix, not string-by-string.
- **Locale-sensitive data pattern:** multiple strings referencing dates, currencies, or numbers in locale-specific formats. Flag as a systemic data formatting issue; recommend a locale-aware utility function or formatter rather than per-string workarounds.
- **Missing translator context cluster:** a group of strings — often from the same feature area — where none have translator notes. Flag the whole feature as under-documented for localization.

---

## Coverage Map

Document which string surfaces were covered in this pass.

| Surface type           | Coverage status      | String count | Notes                                    |
|------------------------|----------------------|--------------|------------------------------------------|
| UI labels              | Fully audited        | —            |                                          |
| Help text              | Fully audited        | —            |                                          |
| Error messages         | Partially audited    | —            | Engineering string files not yet provided|
| Marketing copy         | Not in scope         | —            | Handled separately by marketing team     |
| Legal text             | Not audited          | —            | Requires legal review; flag for separate pass |
| Metadata / aria-labels | Partially audited    | —            | Design-time strings only; codebase audit pending |

State the overall coverage confidence: if fewer than 80% of strings in scope are inventoried, label the prep package as preliminary and note what is missing before handoff can proceed.

---

## Limits and Unknowns

Document honestly:

- **Missing string keys:** strings visible in design but not present in engineering string files cannot be risk-assessed for ICU compliance
- **Unknown character limits:** where UI container character limits are not specified by design, expansion risk estimates are heuristic only
- **Unconfirmed locale set:** if the target locale set was assumed rather than confirmed, all locale-specific risk assessments carry lower confidence
- **Post-freeze changes:** any string modified after the prep pass was completed invalidates the risk assessment for that string; note the freeze date and flag any post-freeze changes
- **Transcreation gaps:** marketing copy and idiom-heavy strings are flagged but not resolved here; they require a separate transcreation brief
- **RTL layout validation:** bidirectional layout issues identified through pseudo-localization are flagged but require engineering validation in a running RTL environment

---

## Workflow Rules

1. Build the full string inventory before writing any risk assessments. Do not assess strings you have not yet inventoried.
2. Complete ICU validation and expansion risk assessment before writing translator notes — notes depend on knowing what the risk is.
3. Do not send a handoff package that contains Critical-risk strings without flagging them explicitly at the top of the package.
4. Distinguish structural issues (concatenation, plural logic, hardcoded strings) from presentation issues (expansion risk, character limits). Structural issues require engineering changes; presentation issues may be resolvable through design.
5. Label every string that is a product name, trademark, or DNT term explicitly. Do not leave it ambiguous for the translator.
6. Record which tool path was used for each major audit step (TMS extraction, Figma extraction, codebase scan, pseudo-localization). Label each as `sourced`, `fallback`, or `inferred`.
7. If string freeze has not occurred, state this at the top of the deliverable and note which sections of the audit may be invalidated by future string changes.
8. Do not hallucinate string content or key names. If a string's source content is unknown, label it `not accessed` and lower its risk confidence accordingly.

---

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/content-designer-localization-prep.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.

---

## Required Deliverable Sections

Within `## Skill: localization-prep`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### String inventory` — full inventory table categorized by surface type, with key ID, source string, character count, variables, plural logic flag, and priority
- `### ICU and framework audit` — ICU Message Format compliance findings; list of strings requiring structural changes; concatenation and plural handling failures
- `### Expansion risk table` — per-locale expansion estimates for flagged strings; pseudo-localization findings; layout breakage documentation
- `### Locale-sensitive data flags` — dates, currencies, numbers, addresses, names, and other locale-sensitive patterns found in the string set
- `### String risk table` — full risk table using the structured schema (String ID / Surface / Risk type / Risk severity / Recommended fix / Translator note needed)
- `### Terminology lockdown` — DNT list, consistency list, terms requiring translation decisions
- `### Translator notes` — context, character limits, variable definitions, and screenshot references per string requiring notes
- `### Coverage map` — which surfaces were fully, partially, and not audited
- `### Limits and unknowns` — gaps in the audit, assumptions made, conditions under which re-audit is needed

---

