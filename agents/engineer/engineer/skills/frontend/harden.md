---
name: harden
description: Strengthen frontend code for browser resilience, rendering safety, client-side security, accessibility compliance, and perceived performance before release.
---

# Harden

## Purpose

Use this skill to make frontend code safe to ship to real browsers on real networks — handling rendering edge cases, client-side security risks, accessibility regressions, and performance degradation that only appear outside development environments.

## When to Use

- Before releasing UI that handles user input, authentication tokens, or sensitive data in the browser
- When a feature depends on network requests that can fail, hang, or return unexpected shapes
- When the component tree has states (loading, error, empty, partial data) that need explicit handling
- When Lighthouse, axe, or manual testing reveals accessibility or performance regressions

## When Not to Use

- When the implementation is still changing shape
- When the work is server-side logic with no browser surface
- When the only remaining task is feature completion, not production readiness

## Required Inputs

- The component tree or page being hardened
- The risk surface: client-side auth, XSS vectors, third-party scripts, local storage usage, or PII in the DOM
- Network dependencies: API calls, WebSocket connections, third-party SDKs
- The target browsers, viewport ranges, and assistive technologies
- Team standards for CSP, CORS, error boundaries, and logging

## Workflow

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

1. Audit the component tree for unhandled states: loading, error, empty, stale data, and race conditions.
2. Check client-side security: XSS via innerHTML or dangerouslySetInnerHTML, token storage, CSP headers, third-party script sandboxing.
3. Add error boundaries, fallback UI, and retry logic for failed network requests.
4. Validate accessibility: focus management, ARIA attributes, keyboard navigation, screen reader announcements, and color contrast.
5. Profile rendering performance: bundle size impact, layout shifts (CLS), largest contentful paint (LCP), and unnecessary re-renders.
6. Confirm feature flags, graceful degradation for older browsers, and a rollback path.
7. Verify that hardening changes do not break existing visual or behavioral contracts.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Every user-visible state must have an explicit, designed UI — no blank screens or frozen spinners
- Client-side code must assume the network is unreliable and the DOM is untrusted
- Accessibility is a shipping requirement, not a follow-up task
- Performance budgets apply to real devices on real networks, not dev machines
- Rollback should be possible without a full redeployment

## Output Contract

- A hardening review covering state coverage, security, accessibility, and performance
- Specific fixes applied or recommended, with severity and rationale
- Residual risks that require follow-up or monitoring
- Confirmation of rollback path and feature-flag coverage

## Examples

### Example 1

Input:
- Page: User profile editor with avatar upload and form validation
- Risk: Upload can fail silently, form state can desync if the API returns partial errors

Expected output:
- Add explicit error UI for upload failure with retry action
- Add optimistic state management with rollback on API error
- Confirm focus returns to the error source for screen reader users
- Verify CLS stays within budget when error messages appear

## Guardrails

- Do not treat hardening as cosmetic polish — it addresses production failure modes
- Do not ship client-side forms without input sanitization and CSRF protection
- Do not suppress errors in the console without logging them to an observability service
- Do not assume all users have fast connections, modern browsers, or no assistive technology

## Optional Tools / Resources

- Lighthouse, axe-core, and browser accessibility inspectors
- Bundle analyzers and performance profilers
- Error-tracking services (Sentry, Datadog RUM)
- Feature flag systems and deployment tooling
