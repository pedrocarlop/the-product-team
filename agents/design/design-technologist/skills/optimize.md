---
name: optimize
description: Diagnose UI performance bottlenecks and define the highest-value changes needed to improve speed, smoothness, and perceived responsiveness.
---

# Optimize

Use this skill to improve a surface that feels slow, heavy, or visibly janky in loading or interaction.

## When to Use

- When performance complaints or metrics indicate a UI bottleneck
- When animation, rendering, images, or bundle weight are degrading the experience
- When the team needs a prioritized performance plan instead of vague optimization advice

## How to Use

Measure first. Identify whether the main issue is loading speed, interaction latency, layout instability, rendering cost, asset weight, or animation behavior. Separate blocking problems from minor cleanup so the plan targets the real bottlenecks instead of dispersing effort.

Tie each recommendation to an expected outcome such as improved LCP, INP, CLS, animation smoothness, or payload reduction. Performance work should be justified by impact, not by abstract best-practice purity.

## What to Produce

- A ranked list of performance issues with likely causes and expected impact
- Specific recommendations for assets, rendering, motion, network, or code behavior
- Any performance budgets or verification checks the team should adopt going forward

## Notes for Design Technologist

Optimize what is measured and what users can feel. Speculative micro-optimizations are noise unless they remove a demonstrated bottleneck.
