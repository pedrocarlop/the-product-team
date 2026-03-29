# Product Team

[Read this in Spanish](./README.es.md)

Product Team is a Codex package that turns a normal repository into a workspace where agents can operate like a small product team.

It adds a coordinator, a set of specialists, and a shared work log so Codex can choose how to organize work instead of reacting task by task.

After installation, requests in that repository go through the Product Team coordinator by default. Simple work may still stay direct, but that choice is made inside the workflow unless the user explicitly opts out for that request.

## Core Idea

The main rule is simple: start with the lightest process that will work.

Product Team does not create a group of agents for every request. It first checks whether one agent can handle the job well. Only when coordination would clearly help does it bring in more roles.

In practice, the flow is:

1. A request comes in.
2. The coordinator decides whether the work is simple or cross-functional.
3. If it is simple, the work is done directly.
4. If it is more complex, the coordinator chooses the smallest team that makes sense.
5. The important decisions and status are written to `logs/`.

## What This Project Really Is

Think of Product Team as an operating system for agent collaboration inside Codex.

It is not an end-user product by itself. It is a reusable workflow you install inside another repository so Codex has:

- one coordinator that controls the process
- specialist roles for different kinds of work
- a written memory of what happened
- clear rules for when to work directly and when to coordinate

## The Main Parts

### 1. The Coordinator: `orchestrator`

The orchestrator is the role that decides how work should happen.

It is responsible for understanding the request, deciding whether to stay direct or start a coordinated workflow, choosing roles, ordering the work, and asking for approval before major multi-role execution.

Its philosophy is:

- do not overcomplicate simple work
- do not create a team unless the team adds value
- keep the process written down

### 2. The Specialists

The package includes a set of roles that represent broad areas of work.

Business:

- `product-lead`: decides what should be built and why
- `analyst`: works with metrics, forecasts, and numbers
- `go-to-market`: focuses on growth, marketing, sales, and launch
- `business-ops`: improves processes and operational structure

Design:

- `designer`: covers research, UX, UI, content, accessibility, and more
- `design-systems`: owns reusable components, tokens, and visual consistency

Engineering:

- `engineer`: builds product features across frontend, backend, mobile, and full stack work
- `platform-engineer`: handles APIs, databases, performance, security, and technical architecture

Review:

- `reviewer`: checks whether the result is solid, useful, and high enough quality

### 3. Shared Memory: `logs/`

`logs/` is where the workflow records what happened.

It exists so the system does not depend on chat memory alone. It keeps a durable record of the request, status, deliverables, and important decisions.

In plain language, `logs/` is the project notebook.

## How It Works Step by Step

### Step 1. A request arrives

Examples:

> "Fix the typo on the login page"
>
> "Redesign the checkout flow to reduce drop-off"

The orchestrator starts by understanding the real goal behind the request.

### Step 2. It chooses direct work or coordinated work

This is the key decision in the system.

Direct work is used when the request is mostly in one domain, clear enough, and unlikely to benefit much from involving many roles.

Coordinated work is used when the request mixes disciplines, needs sequencing, contains important tradeoffs, or benefits from formal review.

### Step 3. If the work is direct, it stays simple

In the direct path, the orchestrator logs the request, clarifies what it understood, keeps status up to date, and proceeds without unnecessary ceremony.

### Step 4. If the work is coordinated, it staffs the smallest useful team

The system avoids large teams by default. If two roles are enough, it uses two. If one role is enough, it uses one. The goal is to add just enough structure to improve the outcome.

### Step 5. The orchestrator writes one shared plan

When several roles are involved, the orchestrator creates one shared plan: what will happen, in what order, who owns each part, and where review will happen.

### Step 6. It asks for approval before major multi-role execution

For bigger coordinated work, the system pauses before main execution starts so the user can confirm the direction. The orchestrator should summarize the plan and ask "Do you want to proceed?"

### Step 7. It coordinates execution and keeps the record current

After approval, the orchestrator activates the roles in sequence, passes outputs from one role to the next, updates status, and records reviews and decisions.

## Why One Role Can Cover Several Subtasks

A role in this project is intentionally broad.

For example, a `designer` can cover research, UX, UI, and content without handing off every small step. An `engineer` can cover frontend and backend work in the same role.

This reduces handoffs, duplication, and confusion.

## What Gets Written in `logs/`

Inside `logs/active/<project-slug>/`, you will usually find:

- `context.md`: project goal, state, decisions, roles, deliverables, and open questions
- `deliverables/`: outputs from the roles
- `decisions/`: important decisions and conflict resolution

Routing, staffing, planning, and approval happen in the context window — only project context and deliverables persist to disk.

There is also `logs/archive/` for completed or inactive work.

## What This Package Installs

When you run the installer, it copies the Product Team workflow into the target repository.

The main things it installs are:

- the agent definitions
- their local skills and guides
- the shared package documentation
- an updater that can pull the latest package later
- the `logs/` structure
- a managed block inside `AGENTS.md`

The main paths it creates are:

- `.codex/agents/product-team-...`
- `.codex/product-team/`
- `logs/active/`
- `logs/archive/`

The installer updates its own files without overwriting unrelated files in the target project.

## How To Start

### 1. Install it into your project

If you are inside the repository where you want to install it:

```bash
./install.sh --target "$PWD"
```

Or directly from GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

Or with Python:

```bash
python3 scripts/install.py --target "$PWD"
```

### 2. Validate the install

From the root of the project where you installed it:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

### 3. Update an installed project later

From the root of the installed project:

```bash
python3 .codex/product-team/scripts/update-install.py
```

The install manifest records where the package came from. If the original source checkout still exists, the updater uses that checkout so local agent-repo changes can be propagated into installed projects. If not, it falls back to the recorded remote archive.

### 4. Ask the coordinator to do work

Once installed, Product Team becomes the default entrypoint for requests in that repository unless the user explicitly opts out for a request. `product-team-orchestrator` still decides whether the work stays direct or becomes coordinated.

Examples:

> "Fix this onboarding flow"
>
> "Create a new pricing page"
>
> "Redesign checkout to improve conversion"

The orchestrator will decide whether this should stay direct or become a coordinated workflow.

### 5. Check `logs/` if you want to understand what happened

If you want to see why the system made a decision, what the plan was, or where the work stopped, `logs/` is the place to look.

## Simple Examples

Small request:

> "Change the signup button text"

This will usually stay direct.

Medium request in one main domain:

> "Build a markdown editor"

This may still stay direct if it is mostly implementation work.

Complex request:

> "Redesign checkout to reduce abandonment"

This will usually trigger planning, staffing, approval, execution, and review.

## What Problem This Solves

Without a system like this, multi-agent work gets messy very quickly:

- it is not clear who is deciding
- work gets duplicated
- context gets lost
- resuming later becomes hard
- multiple competing plans appear

Product Team tries to solve that with three ideas:

- one coordinator owns the process
- the team should be as small as possible
- the workflow should leave a written memory

## For Non-Technical Readers

The shortest possible explanation is:

- this project does not build a product by itself
- this project installs a way of working inside Codex
- that way of working decides whether one agent or several agents should handle the task
- when several agents are needed, there is a plan, approval, coordination, and written follow-up

## If You Maintain This Repository

The main source-of-truth locations are:

- `agents/`: role definitions and local skills
- `logs/README.md`: the rules for the project memory system
- `install.sh` and `scripts/install.py`: installation entrypoints
- `assets/AGENTS.fragment.md`: the managed block injected into `AGENTS.md`
- `assets/package-README.md`: the README copied into installed projects

If you change roles, structure, or orchestrator behavior, validate with:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Then test a real install in a temporary folder and run:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Short Summary

Product Team adds organization to Codex. If the task is simple, it keeps things simple. If the task is complex, it builds the smallest useful team, creates a plan, asks for approval, and records the work so it can be understood later.
