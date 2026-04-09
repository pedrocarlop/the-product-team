---
name: framework-patterns
description: Reference guiding framework-specific technical implementations (e.g. Next.js, React, Shadcn) ensuring best practice usage imported from established industry patterns.
trigger: When building or modifying UI using a specific framework, before starting implementation to anchor assumptions.
primary_mcp: repository
fallback_tools: reference/ground
best_guess_output: A set of framework-specific rules to adhere to in the resulting implementation deliverable.
output_artifacts: knowledge/framework-spec.md
done_when: Framework-specific constraints have been reviewed and applied to the implementation plan.
---

# Framework Patterns (ECC Derived)

## Purpose
Brings deep domain expertise from ECC's specific library of framework guidelines (React, Next.js, etc.) into the Product Team's engineering roles. This skill defines explicit constraints the `frontend-engineer` must follow when writing code.

## Required Workflow

**Follow these steps in order.**

### Step 1: Initialize Header
Produce standard YAML:
```yaml
---
role: frontend-engineer
project: <slug>
deliverable: framework-spec.md
```

### Step 2: Identify Active Frameworks
Scan `package.json` or context to determine the tech stack.
- Next.js? (App Router or Pages Router?)
- React?
- Tailwind/Shadcn?

### Step 3: Apply Mandatory Rules (Next.js App Router Example)
If using Next.js App Router, adhere strictly to these imported ECC rules:
1. **Server Components by Default**: Use Server Components for all data fetching. Only use `"use client"` when state (`useState`), effect (`useEffect`), or browser APIs are required.
2. **Route Handlers**: Avoid creating API routes under `pages/api`. Use `app/api/route.ts` instead.
3. **Data Mutation**: Use Server Actions (`"use server"`) for form mutations instead of generic API endpoints where possible.
4. **Shadcn Integration**: When building UI, prioritize reusing installed `components/ui` components before building bespoke ones. 

### Step 4: Output The Constraints
Draft the `framework-spec.md` with a bulleted list of constraints based on the framework identified. If the codebase uses another stack, state the generic React rules (Hooks over Classes, controlled vs uncontrolled inputs, etc.).

### Step 5: Reflection
Self-critique:
- **What worked**: Were the identified frameworks obvious?
- **What didn't**: Conflicts between design specs and framework constraints.
- **Next steps**: Apply these during the `executor` pass.
