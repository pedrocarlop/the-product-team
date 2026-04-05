# Scenario: QA Release Gate

## Task
Evaluate the release readiness of a payment processing feature that adds support for recurring subscriptions to an existing one-time payment system. The feature has been in development for 6 weeks and is targeted for production deployment. The assessment must be thorough enough to support a go/no-go decision.

## Requirements
1. **Test Coverage Assessment**: Evaluate coverage across unit tests, integration tests, and end-to-end tests. Identify coverage gaps in critical paths (subscription creation, billing cycle, payment failure handling, cancellation, refunds).
2. **Risk Matrix**: Create a risk matrix with at least 8 identified risks. Each risk must have likelihood (low/medium/high), impact (low/medium/high), mitigation status, and owner.
3. **Regression Checklist**: Provide a checklist of regression scenarios for existing payment functionality that must pass before release. Include at least 10 scenarios covering one-time payments, webhook handling, and reporting.
4. **Go/No-Go Recommendation**: Provide a clear recommendation with supporting evidence. If conditional, specify exactly what must be resolved before release. Include a rollback strategy.

## Output Contract
Produce a `release-gate.md` artifact with ## sections for each requirement. Include a risk matrix table, a regression checklist with pass/fail columns, and a clear verdict section at the top.
