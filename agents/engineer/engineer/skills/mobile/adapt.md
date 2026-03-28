---
name: adapt
description: Adapt mobile implementations for platform-specific behavior, device constraints, OS version differences, and native accessibility APIs across iOS and Android.
---

# Adapt

## Purpose

Use this skill to modify a mobile implementation so it handles real-world device diversity — screen sizes, OS versions, platform conventions, hardware capabilities, and native accessibility services — without degrading the core experience.

## When to Use

- When a feature must work across iOS and Android with platform-appropriate behavior
- When older OS versions, low-memory devices, or unusual screen dimensions need explicit handling
- When native accessibility APIs (VoiceOver, TalkBack, Switch Control) require implementation-level changes
- When platform navigation patterns, gesture conventions, or system controls differ from what the design assumes

## When Not to Use

- When the issue is purely a design decision with no implementation constraint
- When the task is testing or auditing rather than changing the implementation
- When the work is about web responsive layout, not native mobile behavior

## Required Inputs

- The feature or screen that needs adaptation
- The platform matrix: iOS versions, Android API levels, and target device classes
- The specific constraint or mismatch driving the adaptation (OS behavior, hardware limitation, platform convention)
- Any design-system tokens or native component primitives available for reuse
- Known platform-specific bugs or OS quirks that affect the feature

## Workflow

1. Identify where the current implementation assumes a single platform or device class.
2. Map the differences in system behavior, gesture handling, navigation, and accessibility APIs across targets.
3. Choose platform-native patterns over cross-platform workarounds where the difference is meaningful to the user.
4. Handle graceful degradation for older OS versions or constrained hardware: feature gating, reduced animation, or fallback layouts.
5. Wire native accessibility services correctly — VoiceOver actions, TalkBack content descriptions, focus order, and live regions.
6. Test against the minimum supported OS version and the smallest supported screen to confirm nothing breaks.

## Design Principles / Evaluation Criteria

- Platform-native behavior should feel intentional, not accidental
- OS version support should degrade gracefully, not crash or silently break
- Accessibility implementation should use native APIs, not custom overlays
- Adaptations should be maintainable — avoid per-device hacks that do not generalize
- Performance on constrained devices matters as much as correctness

## Output Contract

- Platform-specific implementation changes or conditional logic
- Degradation strategy for unsupported OS versions or device classes
- Accessibility wiring for VoiceOver, TalkBack, and other native services
- Any platform-specific bugs or limitations that constrain the adaptation

## Examples

### Example 1

Input:
- Feature: Pull-to-refresh on a list screen
- Problem: Android and iOS handle refresh indicator positioning and haptic feedback differently

Expected output:
- iOS: Use UIRefreshControl with system haptics
- Android: Use SwipeRefreshLayout with Material positioning
- Both: Ensure screen readers announce the refresh state change

## Guardrails

- Do not use a single cross-platform implementation when the platforms behave meaningfully differently
- Do not drop accessibility support to simplify the adaptation
- Do not assume all users run the latest OS version
- Do not add platform-specific code paths without documenting which platforms they cover and why

## Optional Tools / Resources

- Xcode Accessibility Inspector and Android Accessibility Scanner
- Platform-specific Human Interface Guidelines and Material Design guidance
- Device labs or simulators for screen-size and OS-version testing
- Crash and ANR reports from production for adaptation priorities
