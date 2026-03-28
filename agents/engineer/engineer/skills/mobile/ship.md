---
name: ship
description: Validate, harden, and release a mobile feature safely with device testing, app store submission checks, OTA update coordination, and mobile-specific rollback planning.
---

# Ship

## Purpose

Use this skill to turn an implemented mobile feature into a safe production release by verifying device behavior, coordinating app store submission, managing binary and OTA update boundaries, and planning for the unique rollback constraints of mobile.

## When to Use

- When mobile code is complete and the remaining work is validation and release
- When an app store submission, OTA update, or phased rollout needs coordination
- When device-specific testing, app lifecycle verification, or mobile rollback planning must be completed before release

## When Not to Use

- When the feature design or spec is still changing
- When the work is only about composing screens or translating design to code
- When the feature is entirely server-side and does not touch the mobile binary or client behavior

## Required Inputs

- The implemented UI, native modules, and any bridged API changes
- Test results across unit, integration, UI automation, and manual device testing
- Build variant and signing configuration for the target release channel
- Feature flag configuration and remote config dependencies
- App store submission requirements: screenshots, metadata, review guidelines compliance
- OTA update boundaries: what can be updated without a binary release vs what requires a store submission

## Workflow

1. Verify the implemented behavior on target devices: real hardware for critical paths, simulators for breadth.
2. Confirm test coverage: unit tests for logic, UI automation for critical flows, and manual testing for device-specific behavior (gestures, orientations, lifecycle events).
3. Check app lifecycle behavior: does the feature survive backgrounding, low memory, orientation changes, and interrupted network?
4. Validate feature flags and remote config: can the feature be disabled remotely without a new binary?
5. Prepare the app store submission: review guideline compliance, updated screenshots, metadata, and any required privacy declarations.
6. Plan the rollout: phased percentage rollout where available, TestFlight or internal testing track first, then staged public release.
7. Document the rollback plan: for binary releases, what is the minimum time to push a hotfix through app review? For OTA-updatable code, what is the remote disable path?

## Design Principles / Evaluation Criteria

- Mobile releases have higher rollback cost than server deploys; verification must be proportionally thorough
- App store review timelines are external constraints that must be planned around, not wished away
- Device diversity means "works on one device" is not release readiness
- Feature flags and remote config are the primary rollback mechanism for binary releases
- Cleanup of feature flags, deprecated API fallbacks, and minimum version bumps should be planned at ship time

## Output Contract

- A release-readiness summary covering device testing, app lifecycle, and store compliance status
- Test evidence: automated results, manual device test log, and any known device-specific issues
- App store submission checklist: metadata, screenshots, privacy declarations, and review guideline compliance
- Rollout plan: internal testing track, phased rollout percentage, and go/no-go criteria
- Rollback plan: remote disable path for flagged features, hotfix timeline estimate for binary issues
- Cleanup backlog: flags to remove, deprecated fallbacks to delete, minimum OS version bumps to schedule

## Guardrails

- Do not treat simulator-only testing as sufficient for release
- Do not ship without confirming app lifecycle behavior (backgrounding, memory pressure, network loss)
- Do not submit to the app store without verifying review guideline compliance
- Do not rely solely on app store rollback (version revert); prefer remote feature flags for fast disable
- Do not leave OTA vs binary update boundaries ambiguous

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Sentry MCP, Figma MCP
- Websites: [Apple Developer Documentation](https://developer.apple.com/documentation/), [Android Developers](https://developer.android.com/), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines), [Material Design](https://m3.material.io/), [Flutter Docs](https://docs.flutter.dev/)
- CI build output and test reports
- Device lab or cloud testing service
- App Store Connect and Google Play Console
- Crash reporting and mobile APM dashboards
- Feature flag and remote config management
