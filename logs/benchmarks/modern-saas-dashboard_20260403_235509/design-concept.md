# Skill: ui-concept-direction

## Visual artifacts
- [Placeholder: Glassmorphic SaaS Dashboard Concept]

## New design check
Confirmed: Greenfield project management SaaS.

## Reference selection
1. Linear - For minimalist bento-grid layouts.
2. Vercel - For high-contrast typography and geometric precision.
3. Apple - For glassmorphic depth and soft shadows.

## Direction 1: Glassmorphic Precision
- **Visual thesis**: A translucent, layered interface focused on depth and focus.
- **Style pillars**: Glassmorphism, blurred backdrops, vibrant accents.
- **Token direction**: Primary: hsl(220, 100%, 50%). Background: hsl(0, 0%, 100%, 0.7).
- **Typography**: Outfit, sans-serif.
- **Aesthetic Layer**: High-fidelity glassmorphism with `backdrop-filter: blur(10px)`.
- **Component Breakdown**:
  1. Task Card: Glassy background, 12px rounded corners, subtle border.
  2. Sidebar: Translucent sidebar with active state in hsl(220, 100%, 50%).
  3. Header: Floating blur header.
- **Reference cues**: Apple / Vercel.
- **Divergence axes**: Depth vs Flatness.

## Direction 2: High-Contrast Bento
- **Visual thesis**: A structured, grid-based layout inspired by bento-box designs.
- **Style pillars**: Rigid grid, high contrast, bold typography.
- **Token direction**: Neutral: hsl(210, 20%, 98%). Accent: hsl(280, 100%, 60%).
- **Typography**: Inter, sans-serif.
- **Aesthetic Layer**: Bento grids with subtle gradients and crisp edges.
- **Component Breakdown**:
  1. Grid Cell: Bordered container with 16px padding.
  2. Stat Widget: Large typography with gradient background.
  3. Navigation: Minimalist vertical bar.
- **Reference cues**: Linear.

## ### Component Breakdown
1. **Glassmorphic Card**: A card component with a 1px solid border (hsl(0, 0%, 100%, 0.2)), a blurred background, and a 12px border-radius.
2. **Gradient Action Button**: Primary action button with a linear-gradient from hsl(220, 100%, 60%) to hsl(220, 100%, 40%).
3. **Bento Info Box**: A 2x2 grid component for summary statistics, using high-density layouts.

## Project ds-spec seed
- **Typography direction**: Primary: Outfit. Secondary: Inter.
- **Color and token direction (HSL only)**:
  - Primary: hsl(220, 100%, 50%)
  - Base: hsl(0, 0%, 100%)
  - Surface/Glass: hsl(0, 0%, 100%, 0.5)
- **Implementation foundation**: shadcn/ui is highly recommended for its Radix components and easy styling with Tailwind HSL tokens.

## Recommended direction
Direction 1: Glassmorphic Precision. It offers the most premium feel for a 2026 SaaS product.

## Reflection
The transition to HSL and specific aesthetic mandates significantly improved the visual articulation of the concept.
