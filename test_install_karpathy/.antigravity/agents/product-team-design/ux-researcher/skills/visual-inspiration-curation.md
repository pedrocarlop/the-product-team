---
name: visual-inspiration-curation
description: Systematically gather visual inspiration, aesthetic cues, and layout patterns from Pinterest and design-first sources to seed moodboards and concept directions.
trigger: When a new project needs visual grounding, a style direction needs validation, or the team requires a moodboard to align on aesthetic posture.
required_inputs:
  - the core product theme or aesthetic goal
  - target keywords for inspiration search (e.g., "minimalist fintech", "glassmorphism dashboard")
  - specific surface or interaction type being explored
recommended_passes:
  - initial inspiration search and board gathering
  - evidence capture and screenshotting
  - pattern curation and "moodboard" assembly
  - synthesis of visual pillars
tool_stack:
  runtime:
    primary: [browser_subagent, open, take_screenshot]
    secondary: [search_query]
  artifacts:
    primary: [figjam, notion, miro]
  inspiration: [pinterest, dribbble, behance, layers, refero, mobbin]
tool_routing:
  - if: searching for broad aesthetic themes, color palettes, or textural inspiration
    use: [pinterest]
  - if: capturing specific UI layouts or interaction patterns from live sites
    use: [browser_subagent, take_screenshot]
  - if: organizing inspiration into a collaborative moodboard or canvas with structured layouts
    use: [figjam, notion, miro]
  - if: checking established SaaS UI patterns
    use: [refero, mobbin]
best_guess_output: A visual inspiration report (moodboard) with curated evidence, aesthetic pillars, and a link to the canvas artifact.
output_artifacts:
  - knowledge/ux-researcher-visual-inspiration.md
  - knowledge/assets/ (for captured inspiration)
done_when: The inspiration board is assembled, visual pillars are defined from the curated set, and the artifact is linked for the design team.
---

# Visual Inspiration Curation

## Purpose

Systematically gather and curate visual inspiration to establish an aesthetic posture before production-grade design begins.

This skill focuses on "finding the vibe" — collecting color stories, typography cues, layout models, and interaction tones from Pinterest and other design citations. This is not about benchmarking competitor features (use `competitor-research` for that), but about building the visual DNA of a project.

## Required Inputs and Assumptions

- **Aesthetic Goal**: The general direction or "mood" (e.g., "warm and human", "industrial and precise").
- **Search Keywords**: Specific terms to use in Pinterest or browser searches.
- **Product Area**: The surface being inspired (e.g., "landing page", "mobile settings").

If inputs are missing, infer a provisional "vibe" based on the product description and prefix with `Assumed context:`.

## Core Method Execution

### Step 1 — Inspiration Search
Use `browser_subagent` to search Pinterest, Dribbble, or layers.is for the defined keywords. Browse for high-quality, relevant results that match the aesthetic goal. Look for:
- Color harmonies
- Typography treatments
- Grid and layout compositions
- Visual metaphors (shadows, gradients, textures)

### Step 2 — Evidence Capture
For setiap relevant pin or design:
1. Navigate to the high-resolution view.
2. Use `take_screenshot(fullPage=false)` to capture the specific design or interaction.
3. Save the image to `knowledge/assets/` with a descriptive name (e.g., `inspiration-glass-dashboard-01.png`).

### Step 3 — Canvas Assembly ("FigJam" / "Notion")
If a "FigJam" board or "Notion" gallery is requested:
1. Create or open the project board using the appropriate tool.
2. If using Notion, create a "Gallery" or "Gallery View" database to place images in an organized grid with metadata.
3. If using FigJam, cluster images by theme and use connectors to show relationships.
4. Note: If direct image upload via MCP is limited, use the markdown deliverable as the primary collector of these images, maintaining the same organizational structure as the canvas.

### Step 4 — Define Visual Pillars
Synthesize the collected evidence into 3-5 "Visual Pillars." Each pillar should describe a consistent theme found in the research (e.g., "Layered Depth", "Symmetric Tension", "Oversized Typography").

## Visual Documentation Standards

- **High Fidelity Only**: Avoid low-resolution thumbnails. Always capture the source at its native resolution.
- **Contextual Captions**: Every screenshot MUST have a caption explaining *why* it was saved (e.g., "Saved for its use of subtle borders and high-contrast text").
- **Organized Storage**: Use the standard assets folder.

## Deliverable Contract

Produce the deliverable at `knowledge/ux-researcher-visual-inspiration.md`.

### Required Deliverable Sections:
- `### Curated Inspiration`: Embed all captured screenshots with captions and source links.
- `### Visual Pillars`: List the 3-5 synthesized themes with evidence links.
- `### Canvas Link`: Link to the FigJam board, Notion page, or Miro board used for assembly.
- `### Reflection`: Professional reflection on the inspiration quality and next steps for the UI team.

---
*Read visual-inspiration-curation skills for this task.*
