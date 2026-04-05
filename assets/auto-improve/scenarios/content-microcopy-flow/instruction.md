# Scenario: Content Microcopy Flow

## Task
Write the complete microcopy system for an e-commerce checkout flow spanning four stages: cart review, shipping information, payment details, and order confirmation. The product sells physical goods to consumers and supports guest checkout.

## Requirements
1. **Button Labels**: Primary and secondary action labels for each stage (e.g., "Continue to Shipping", "Edit Cart"). Labels must be specific and action-oriented, not generic ("Submit", "Next").
2. **Error Messages**: At least 3 field-level validation errors per form stage (e.g., invalid email, missing zip code, expired card). Each error must be specific about what went wrong and how to fix it.
3. **Empty States**: Copy for empty cart, no saved addresses, and payment method not accepted scenarios.
4. **Help Text**: Inline helper text for ambiguous fields (e.g., "We'll only use this for delivery updates", CVV explanation).
5. **Confirmation Copy**: Order confirmation page copy including order summary header, next-steps messaging, and email confirmation notice.

## Output Contract
Produce a `microcopy-system.md` artifact organized by checkout stage, with each stage containing subsections for buttons, errors, empty states, and help text. Use tables or definition lists for clarity.
