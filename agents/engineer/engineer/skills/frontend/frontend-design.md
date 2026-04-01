---
name: frontend-design
description: "Set design quality standards for frontend interfaces — composition, typography, color, motion, imagery, and copy. Use when the task involves building any user-facing frontend surface to ensure output feels intentional, bold, and premium, not generic. Applies to landing pages, product UI, dashboards, and app surfaces."
---

# Frontend Design Quality

## Overview

This skill gives you design-taste guardrails so frontend output feels deliberate, premium, and current. It covers composition, typography, color, motion, imagery, copy, and litmus checks. The goal is award-level interfaces — not generic SaaS card grids.

## When to Use

- When building any new frontend surface (landing page, dashboard, app screen, settings page).
- When refactoring or redesigning an existing UI.
- When reviewing frontend output for design quality.
- When translating a design spec into code and visual decisions are needed.

## When Not to Use

- When working within an established design system with explicit patterns — follow the system instead.
- When the task is purely backend, API, or data work with no UI component.
- When the user explicitly requests a minimal/wireframe aesthetic.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: Write the Working Model

Before any code, write three things:

1. **Visual thesis** — one sentence describing mood, material, and energy.
   - Good: "Dark, dense, editorial energy with a single warm accent and monospace typography."
   - Good: "Light, airy, photographic hero with restrained sans-serif and generous whitespace."
   - Bad: "Clean modern design." (too vague to guide decisions)

2. **Content plan** — what goes in each section:
   - Hero: what's the brand/product, what's the promise, what's the CTA, what's the dominant visual?
   - Support: what's the proof point, feature, or social validation?
   - Detail: what adds depth, atmosphere, or workflow context?
   - Final CTA: what's the conversion action?

3. **Interaction thesis** — 2-3 motion ideas that change the feel:
   - "Staged entrance on hero elements with opacity + translate"
   - "Scroll-linked parallax on the feature section image"
   - "Hover-reveal expanding detail on capability cards"

### Step 3: Build from Composition, Not Components

Start with the overall layout and composition for each section, then fill in components:

- **Prefer full-bleed heroes** or full-canvas visual anchors over constrained containers.
- **One composition per section** — do not stack multiple ideas in one viewport.
- **Default to cardless layouts.** Use sections, columns, dividers, lists, and media blocks instead of cards. Cards are justified only when they serve a clear interaction need (selection, comparison, expansion).
- **Let spacing do the work.** Use whitespace, alignment, scale, cropping, and contrast before adding chrome, borders, or decorative elements.
- **Canonical full-bleed rule**: on branded landing pages, the hero must run edge-to-edge with no inherited page gutters, framed container, or shared max-width. Constrain only the inner text/action column.

### Step 4: Set Typography

- Use expressive, purposeful font families — avoid system defaults and generic stacks (Inter, Roboto, Arial, system-ui). These read as "AI generated."
- **Two typefaces maximum**: one display, one body. Add a third only with clear justification.
- Make the **brand name or product name** the loudest text on the page.
- Use font size, weight, and letterspacing to create visual hierarchy, not color alone.
- Keep headlines to roughly 2-3 lines on desktop and readable in one glance on mobile.

### Step 5: Set Color and Visual Direction

- Define a clear visual direction before picking colors.
- Use **CSS custom properties** (`--var`) for all color values — no hardcoded hex in component styles.
- Do not default to purple-on-white or blue-on-white. These are the signature of generic AI output.
- Choose **one accent color** and build a palette from it. Add a second only with reason.
- **Background treatment**: no flat, single-color backgrounds. Use gradients, subtle textures, photographic backgrounds, tinted sections, or depth layers.

### Step 6: Handle Imagery

Imagery must do narrative work, not decoration:

- Use at least one **strong, real-looking image** for brands, venues, editorial pages, and lifestyle products.
- Prefer in-situ photography over abstract gradients or fake 3D objects.
- Choose or crop images with a stable tonal area for text overlay.
- Do not use images with embedded signage, logos, or typographic clutter fighting the UI.
- Do not generate images with built-in UI frames, splits, cards, or panels.
- If multiple moments are needed, use multiple images, not one collage.
- The first viewport needs a **real visual anchor**. Decorative texture is not enough.

### Step 7: Apply Motion

Motion is for presence and hierarchy, not noise. Ship 2-3 intentional motions per page:

| Motion Type | Purpose | Example |
|------------|---------|---------|
| **Entrance sequence** | Draw attention to hero content | Staged fade + translate on logo, headline, CTA |
| **Scroll-linked effect** | Create depth and engagement | Parallax on feature image, progressive reveal |
| **Hover/reveal transition** | Sharpen affordance and reward interaction | Expanding detail on cards, color shift on buttons |

**Motion rules:**
- Noticeable in a quick recording.
- Smooth on mobile.
- Fast and restrained — not slow or lingering.
- Consistent across the page.
- Removed if ornamental only.
- Use `prefers-reduced-motion` to disable non-essential animations.

### Step 8: Write Copy

**For landing pages and marketing surfaces:**
- Write in product language, not design commentary.
- Let headlines carry meaning — no vague "Unlock the power of..." language.
- Supporting copy should be one short sentence.
- Cut repetition between sections — each section gets one responsibility.
- If deleting 30% of the copy improves the page, keep deleting.

**For product UI (dashboards, settings, admin tools):**
- Use **utility copy**: orientation, status, and action — not promise, mood, or brand voice.
- Start with the working surface itself: KPIs, charts, filters, tables, status.
- Section headings should say what the area is or what the user can do there.
  - Good: "Selected KPIs", "Plan status", "Last sync"
  - Bad: "Unlock Your Data Potential", "Your Journey Starts Here"
- If a section does not help someone operate, monitor, or decide, remove it.
- **Litmus**: if an operator scans only headings, labels, and numbers, can they understand the page?

### Step 9: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Viewport Budget

- If the first screen includes a sticky/fixed header, that header counts against the hero. The combined header + hero content must fit within the initial viewport at common desktop and mobile sizes.
- When using `100vh`/`100svh` heroes, subtract persistent UI chrome: `calc(100svh - var(--header-height))`, or overlay the header instead of stacking.
- If the first viewport still works after removing the image, the image is too weak.
- If the brand disappears after hiding the nav, the hierarchy is too weak.

## Landing Page Default Sequence

1. **Hero**: brand or product, promise, CTA, one dominant visual. Full-bleed. One composition.
2. **Support**: one concrete feature, offer, or proof point. Max three ideas per section.
3. **Detail**: atmosphere, workflow depth, product credibility, or story.
4. **Final CTA**: convert, start, visit, or contact. Simple, direct, visually distinct from hero.

**Hero rules:**
- One composition only.
- Full-bleed image or dominant visual plane.
- Brand first, headline second, body third, CTA fourth.
- No hero cards, stat strips, logo clouds, pill soup, or floating dashboards by default.
- Keep the text column narrow and anchored to a calm area of the image.
- All text over imagery must maintain strong contrast and clear tap targets.

## App UI Default

Default to Linear-style restraint:
- Calm surface hierarchy.
- Strong typography and spacing.
- Few colors.
- Dense but readable information.
- Minimal chrome.
- Cards only when the card is the interaction.

Avoid:
- Dashboard-card mosaics.
- Thick borders on every region.
- Decorative gradients behind routine product UI.
- Multiple competing accent colors.
- Ornamental icons that do not improve scanning.

## Hard Rules

These are non-negotiable:
- No cards by default.
- No hero cards by default.
- No boxed or center-column hero when the brief calls for full bleed.
- No more than one dominant idea per section.
- No section should need many tiny UI devices to explain itself.
- No headline should overpower the brand on branded pages.
- No filler copy.
- No split-screen hero unless text sits on a calm, unified side.
- No more than two typefaces without a clear reason.
- No more than one accent color unless the product has a strong existing system.
- No flat white or flat black backgrounds without texture, gradient, or visual break.

## Reject These Failures

If the output matches any of these, it has failed:
- Generic SaaS card grid as the first impression.
- Beautiful image with weak brand presence.
- Strong headline with no clear action.
- Busy imagery behind text that kills readability.
- Sections that repeat the same mood statement.
- Carousel with no narrative purpose.
- App UI made of stacked cards instead of layout.
- Purple-on-white or blue-on-white color scheme with no personality.
- System-default font stack (Inter, Roboto, Arial).

## Litmus Checks

Before submitting frontend work, verify every item:
- [ ] Is the brand or product unmistakable in the first screen?
- [ ] Is there one strong visual anchor (not just text)?
- [ ] Can the page be understood by scanning headlines only?
- [ ] Does each section have one job?
- [ ] Are cards actually necessary, or are they a crutch?
- [ ] Does motion improve hierarchy or atmosphere?
- [ ] Would the design still feel premium if all decorative shadows were removed?
- [ ] Is typography intentional and distinctive (not system defaults)?
- [ ] Is there a defined color direction (CSS variables, not ad-hoc hex)?
- [ ] Does the page load and function on both desktop and mobile?
- [ ] If an existing design system is present, are its conventions preserved?

## Worked Examples

### Example 1: Landing Page
**Task:** Build a landing page for a developer productivity tool.

**Working model:**
- Visual thesis: "Dark, code-editor-inspired with monospace accents and a single electric blue highlight."
- Content plan: Hero (product name + tagline + CLI screenshot + CTA) → Support (3 capability statements with inline code examples) → Detail (integration logos + workflow animation) → CTA (get started free).
- Interaction thesis: Staggered entrance on hero text, scroll-linked code typing animation, hover-expand on feature items.

**Result:** Dark background with subtle grid texture. Product name in 72px monospace. CLI screenshot as full-bleed hero visual. Electric blue CTA button. No cards anywhere. Each section one full viewport height.

### Example 2: Dashboard
**Task:** Build an analytics dashboard for a SaaS product.

**Working model:**
- Visual thesis: "Clean, data-first, muted palette with one metric-highlight color."
- Content plan: Header (product + navigation) → KPI strip (4 headline metrics) → Chart area (primary chart + filters) → Detail table (drilldown data).
- Interaction thesis: Metric counters animate on load, chart crosshairs on hover, table rows highlight on hover.

**Key decision:** Use utility copy throughout. No marketing hero. Heading says "Revenue Overview", not "Unlock Your Revenue Potential." Every element helps someone monitor, compare, or decide.

## Troubleshooting

### Issue: Output looks "AI generated"
**Cause:** System-default fonts, purple/blue accent, flat white background, equal-weight card grid.
**Solution:** Apply the working model. Choose a distinctive font. Pick a non-default accent color. Add background texture or gradient. Break the grid with asymmetric composition.

### Issue: Hero lacks visual impact
**Cause:** No strong image, or text is not anchored to a calm area.
**Solution:** Add a full-bleed image or dominant visual plane. Ensure the brand name is the loudest element. Use scale contrast — make one thing big and everything else smaller.

### Issue: Too many competing elements
**Cause:** Multiple ideas per section, excessive UI chrome.
**Solution:** Apply the one-idea-per-section rule. Remove the weakest elements until each section has clear focus. Let whitespace separate ideas instead of borders.
