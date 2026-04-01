---
name: frontend-design
description: Set the overall visual direction for new UI work — composition, typography, color, motion, and quality standards — so surfaces feel intentional, distinctive, and premium, not generic AI slop.
---

# Frontend Design Quality

Use this skill when the task involves UI or visual design for frontend interfaces. It provides design quality standards to ensure your deliverables feel premium, intentional, and implementable.

## When to Use

- When a new surface needs a clear aesthetic direction before detailed UI specification
- When the current direction feels generic, inconsistent, or visually underdeveloped
- When a feature needs a stronger point of view across typography, color, spacing, hierarchy, and motion
- When reviewing or critiquing frontend design work

## Before You Design

Write these three things before producing any artifacts:
1. **Visual thesis** — one sentence describing mood, material, and energy (e.g. "warm, editorial, generous whitespace with kinetic type")
2. **Content plan** — map the information architecture: hero, support, detail, final CTA
3. **Interaction thesis** — 2-3 motion ideas that will change how the page feels

Start from product context, not visual taste alone. Confirm the audience, core job-to-be-done, tone, and quality bar. Audit the existing design system, product patterns, and approved components before introducing new visual moves.

## Composition First

- Start with composition, not components or wireframe grids.
- Prefer full-bleed heroes or full-canvas visual anchors over constrained card layouts.
- One composition per section — don't stack multiple ideas in one viewport.
- Default to cardless layouts. Use cards only when they serve interaction (selection, comparison, expansion).
- Let whitespace, alignment, scale, cropping, and contrast create hierarchy before adding chrome.

## Typography Direction

- Specify expressive, purposeful font families — avoid generic stacks (Inter, Roboto, Arial, system-ui).
- Limit to two typefaces: one display, one body.
- Make the brand/product name the loudest text.
- Use font size, weight, letterspacing, and case to build hierarchy. Do not rely on color alone.

## Color Direction

- Define a visual direction before picking colors.
- Specify CSS custom properties for all color values in your handoff specs.
- Avoid purple-on-white or blue-on-white defaults — they read as "AI generated".
- One accent color. Add a second only with reason.
- Backgrounds: specify gradients, tinted sections, textures, or photographic backgrounds. No flat white or flat black without visual break.

## Motion Design

- Motion is for presence and hierarchy, not decoration.
- Specify 2-3 intentional motions per page:
  - **Entrance**: staged reveal (fade + translate, stagger)
  - **Scroll-linked**: parallax, progressive reveal, sticky transitions
  - **Hover/reveal**: interactive detail on engagement
- Note `prefers-reduced-motion` behavior in your specs.

## Landing Page Pattern

1. **Hero**: brand, promise, CTA, dominant visual. Full-bleed. One composition. No hero cards.
2. **Support**: feature highlights or proof. Max three.
3. **Detail**: atmosphere, workflow depth, credibility.
4. **Final CTA**: convert — simple, direct, visually distinct.

### Hero Rules
- One composition, full-bleed visual, brand first, text narrow and anchored.
- No card grids, stat strips, or feature lists in the hero area.

## Product UI Guidelines

- For dashboards and functional UI: utility copy (orientation, status, action), not marketing.
- No aspirational hero lines on dashboards.
- Preserve existing design system conventions.
- Focus: information density, scannability, task completion.

## Copy Direction

- Write in product language, not design commentary.
- Headlines carry meaning — no vague "Unlock the power..." language.
- One idea per section, one responsibility per paragraph.
- Short enough to scan.

## Hard Rules

- No cards by default
- No more than one idea per section
- No filler copy
- No more than two typefaces without reason
- No more than one accent color without reason
- No flat backgrounds without texture, gradient, or visual break

## What to Produce

- A concise visual direction statement (the visual thesis)
- The primary hierarchy decisions: focal points, typography, color emphasis, spacing rhythm, and motion posture
- The component and token choices that carry the direction consistently
- Any explicit anti-patterns to avoid while refining the UI spec
- Breakpoint and state behavior: how the direction holds across loading, error, empty, and mobile views

## Litmus Checks

Before delivering design work:
- [ ] Is the brand unmistakable?
- [ ] Is there one strong visual anchor per section?
- [ ] Can the page be understood by scanning headlines only?
- [ ] Does each section have one job?
- [ ] Are cards justified or a crutch?
- [ ] Does motion improve hierarchy or add noise?
- [ ] Is typography intentional (not system defaults)?
- [ ] Is there a defined color direction?
- [ ] Is the design specified with enough detail for implementation (tokens, spacing, states)?
- [ ] Does the direction hold at real breakpoints and across loading, error, and empty states?

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, and Paper MCP for visual references and design QA
- [Material Design](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [Storybook Docs](https://storybook.js.org/docs)
- [Mobbin](https://mobbin.com/)
- [Laws of UX](https://lawsofux.com/)
