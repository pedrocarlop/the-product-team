---
name: bridge
description: Map mobile design specs to native and cross-platform code by resolving JS-to-native boundaries, platform API requirements, and mobile-specific implementation constraints.
---

# Bridge

## Purpose

Use this skill to translate mobile design intent into implementation decisions that account for the unique constraints of mobile development: JS-to-native bridge boundaries, platform-specific APIs, device capabilities, app lifecycle behavior, and performance budgets that do not exist on web.

## When to Use

- When a mobile design needs to be mapped to native components, platform APIs, or cross-platform framework primitives
- When deciding what runs in JS versus what requires a native module or platform bridge
- When platform-specific behavior (iOS vs Android) needs explicit resolution before implementation
- When mobile performance constraints (animation frame budget, memory limits, startup time) affect how a design should be implemented

## When Not to Use

- When the task is to verify an already-implemented mobile screen against the design
- When the main need is a prototype or motion study rather than implementation planning
- When the design translation is entirely within the JS layer and does not touch native boundaries

## Required Inputs

- The design source: Figma file, spec, or annotated screenshot for the mobile surface
- The target mobile stack: React Native, Flutter, SwiftUI, Jetpack Compose, or native
- Platform API requirements: camera, biometrics, push notifications, file system, or sensors
- Known platform differences between iOS and Android for the feature
- Performance budget: animation frame rate, cold start impact, memory ceiling
- Existing native modules, platform bridges, and shared components available in the codebase

## Workflow

1. Read the design and identify which elements can be implemented in the cross-platform layer and which require native code.
2. Map each component to the appropriate implementation surface: shared UI framework, platform-specific component, or native module.
3. Identify JS-to-native bridge boundaries and specify the data shape, threading model, and error handling for each crossing.
4. Resolve platform divergences: where iOS and Android need different implementations, document both paths and the reason for divergence.
5. Assess performance implications: will animations hit 60fps? Does the feature add to startup time? Are there memory-intensive operations that need native optimization?
6. Document open questions about platform API availability, minimum OS version requirements, and permission handling.

## Design Principles / Evaluation Criteria

- Bridge boundaries should be intentional, not accidental; every native crossing needs justification
- Platform-specific implementations should be contained and documented, not scattered
- Performance constraints are not optional on mobile; they shape implementation choices
- The implementation plan should account for both iOS and Android, not assume one platform and retrofit
- Prefer platform conventions (native navigation, gesture handling, haptics) over custom implementations that fight the OS

## Output Contract

- A component mapping showing what lives in shared code versus native code for each platform
- Bridge boundary specifications: data contracts, threading notes, and error handling for JS-to-native crossings
- Platform divergence documentation: what differs between iOS and Android and why
- Performance assessment: animation feasibility, memory impact, and startup time considerations
- Permission and capability requirements: what the app must request and when
- Open questions about platform API availability, minimum OS version support, and native module needs

## Examples

### Example 1

Input:
- Source: A camera-based document scanning feature designed in Figma
- Target: React Native app with some existing native modules

Expected output:
- Bridge boundary: Camera capture and image processing must run natively; the review and annotation UI can be React Native
- iOS: Use VisionKit for document detection; Android: Use ML Kit document scanner
- Data contract: Native module returns `{ imageUri: string, corners: Point[], confidence: number }` to JS
- Threading: Image processing runs on background thread; UI updates on main thread
- Performance: Camera preview must maintain 30fps minimum; processing should show progress indicator if >500ms
- Permission: Camera permission required; request at feature entry, not app launch
- Gap: No existing native module for document edge detection; needs to be built or sourced

## Guardrails

- Do not assume a web-style implementation will work on mobile without checking platform constraints
- Do not cross the JS-to-native bridge without documenting the data contract and error handling
- Do not ignore platform differences; "works on iOS" does not mean "works on Android"
- Do not accept animation designs without confirming they can run within the mobile frame budget
- Do not bury platform API requirements; they affect app store review, permissions, and minimum OS version

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Sentry MCP, Figma MCP
- Websites: [Apple Developer Documentation](https://developer.apple.com/documentation/), [Android Developers](https://developer.android.com/), [React Native Docs](https://reactnative.dev/), [Flutter Docs](https://docs.flutter.dev/)
- Existing native module inventory in the codebase
- Platform API compatibility tables for minimum OS version support
- Performance profiling tools: Xcode Instruments, Android Studio Profiler
