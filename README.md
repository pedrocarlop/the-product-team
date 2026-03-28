# Product Team

Product Team is a package for Codex that turns a normal repository into a workspace where multiple agents can operate like a small product team.

Product Team es un paquete para Codex que convierte un repositorio normal en un espacio donde varios agentes pueden trabajar como un pequeño equipo de producto.

In simple terms, this project adds a coordinator, a set of specialists, and a shared work log so Codex can decide how to organize work instead of just reacting task by task.

En términos simples, este proyecto añade un coordinador, un conjunto de especialistas y un registro compartido del trabajo para que Codex pueda decidir cómo organizarlo en vez de limitarse a reaccionar tarea por tarea.

## Core Idea

The main rule is simple: start with the lightest possible process.

La regla principal es simple: empezar con el proceso más ligero posible.

That means Product Team does not create a group of agents for every request. It first checks whether one agent can handle the job well. Only if coordination would clearly improve the result does it bring in more roles.

Eso significa que Product Team no crea un grupo de agentes para cada petición. Primero comprueba si un solo agente puede resolver el trabajo bien. Solo si la coordinación mejora claramente el resultado incorpora más roles.

In practice, the flow is:

En la práctica, el flujo es:

1. A request comes in.
2. The coordinator decides whether the work is simple or cross-functional.
3. If it is simple, the work is done directly.
4. If it is more complex, the coordinator chooses the smallest team that makes sense.
5. The important decisions and status are written to `logs/`.

1. Llega una petición.
2. El coordinador decide si el trabajo es simple o si cruza varias áreas.
3. Si es simple, se hace directamente.
4. Si es más complejo, el coordinador elige el equipo más pequeño que tenga sentido.
5. Las decisiones importantes y el estado se escriben en `logs/`.

## What This Project Really Is

Think of Product Team as an operating system for agent collaboration inside Codex.

Piensa en Product Team como un sistema de funcionamiento para la colaboración entre agentes dentro de Codex.

It is not an end-user product by itself. It is a reusable way of working that you can install inside another repository so Codex has:

No es un producto final para usuarios por sí mismo. Es una forma reutilizable de trabajar que puedes instalar dentro de otro repositorio para que Codex tenga:

- one coordinator that controls the process
- specialist roles for different kinds of work
- a written memory of what happened
- clear rules for when to work directly and when to coordinate

- un coordinador que controla el proceso
- roles especialistas para distintos tipos de trabajo
- una memoria escrita de lo que ha pasado
- reglas claras para decidir cuándo trabajar de forma directa y cuándo coordinar

## The Main Parts

## Las partes principales

### 1. The Coordinator: `orchestrator`

### 1. El coordinador: `orchestrator`

The orchestrator is the role that decides how work should happen.

El orquestador es el rol que decide cómo debe hacerse el trabajo.

It is responsible for understanding the request, deciding whether to stay direct or start a coordinated workflow, choosing roles, ordering the work, and asking for approval before major multi-role execution.

Se encarga de entender la petición, decidir si conviene seguir por vía directa o iniciar un flujo coordinado, elegir roles, ordenar el trabajo y pedir aprobación antes de una ejecución grande con varios roles.

Its philosophy is:

Su filosofía es:

- do not overcomplicate simple work
- do not create a team unless the team adds value
- keep the process written down

- no complicar trabajos simples
- no crear un equipo si ese equipo no aporta valor
- dejar el proceso por escrito

### 2. The Specialists

### 2. Los especialistas

The package includes a set of roles that represent broad areas of work.

El paquete incluye un conjunto de roles que representan grandes áreas de trabajo.

Business:

Negocio:

- `product-lead`: decides what should be built and why
- `analyst`: works with metrics, forecasts, and numbers
- `go-to-market`: focuses on growth, marketing, sales, and launch
- `business-ops`: improves processes and operational structure

- `product-lead`: decide qué debería construirse y por qué
- `analyst`: trabaja con métricas, previsiones y números
- `go-to-market`: se centra en crecimiento, marketing, ventas y lanzamiento
- `business-ops`: mejora procesos y estructura operativa

Design:

Diseño:

- `designer`: covers research, UX, UI, content, accessibility, and more
- `design-systems`: owns reusable components, tokens, and visual consistency

- `designer`: cubre investigación, UX, UI, contenido, accesibilidad y más
- `design-systems`: se encarga de componentes reutilizables, tokens y coherencia visual

Engineering:

Ingeniería:

- `engineer`: builds product features across frontend, backend, mobile, and full stack work
- `platform-engineer`: handles APIs, databases, performance, security, and technical architecture

- `engineer`: construye funcionalidades de producto en frontend, backend, móvil y trabajo full stack
- `platform-engineer`: se ocupa de APIs, bases de datos, rendimiento, seguridad y arquitectura técnica

Review:

Revisión:

- `reviewer`: checks whether the result is solid, useful, and high enough quality

- `reviewer`: comprueba si el resultado es sólido, útil y con suficiente calidad

### 3. Shared Memory: `logs/`

### 3. Memoria compartida: `logs/`

`logs/` is where the workflow writes down what happened.

`logs/` es donde el flujo de trabajo deja escrito lo que ha pasado.

This matters because the system does not want to depend on chat memory alone. It wants a durable record of the request, the plan, the current status, the deliverables, and the important decisions.

Esto importa porque el sistema no quiere depender solo de la memoria del chat. Quiere un registro duradero de la petición, del plan, del estado actual, de los entregables y de las decisiones importantes.

In plain language, `logs/` is the project notebook.

En lenguaje sencillo, `logs/` es el cuaderno del proyecto.

## How It Works Step by Step

## Cómo funciona paso a paso

### Step 1. A request arrives

### Paso 1. Llega una petición

Examples:

Ejemplos:

> "Fix the typo on the login page"

> "Corrige el typo de la página de login"

> "Redesign the checkout flow to reduce drop-off"

> "Rediseña el flujo de checkout para reducir el abandono"

The orchestrator starts by understanding the real goal behind the request.

El orquestador empieza entendiendo el objetivo real que hay detrás de la petición.

### Step 2. It chooses direct work or coordinated work

### Paso 2. Elige trabajo directo o trabajo coordinado

This is the most important decision in the whole system.

Esta es la decisión más importante de todo el sistema.

Direct work is used when the request is mostly in one domain, clear enough, and unlikely to improve much by involving many roles.

El trabajo directo se usa cuando la petición pertenece sobre todo a una sola área, está lo bastante clara y es poco probable que mejore mucho involucrando a muchos roles.

Coordinated work is used when the request mixes several disciplines, needs sequencing, contains important tradeoffs, or benefits from formal review.

El trabajo coordinado se usa cuando la petición mezcla varias disciplinas, necesita una secuencia clara, contiene decisiones importantes o se beneficia de una revisión formal.

### Step 3. If the work is direct, it stays simple

### Paso 3. Si el trabajo es directo, se mantiene simple

In the direct path, the orchestrator logs the request, clarifies what it understood, keeps status up to date, and proceeds without unnecessary ceremony.

En la vía directa, el orquestador registra la petición, aclara qué ha entendido, mantiene el estado actualizado y sigue adelante sin ceremonias innecesarias.

### Step 4. If the work is coordinated, it staffs the smallest useful team

### Paso 4. Si el trabajo es coordinado, elige el equipo útil más pequeño

The system avoids large teams by default. If two roles are enough, it uses two. If one role is enough, it uses one. The point is not to simulate a giant company. The point is to add just enough structure to improve the outcome.

El sistema evita por defecto los equipos grandes. Si dos roles bastan, usa dos. Si un rol basta, usa uno. La idea no es simular una empresa enorme. La idea es añadir la estructura justa para mejorar el resultado.

### Step 5. The orchestrator writes one shared plan

### Paso 5. El orquestador redacta un único plan compartido

When several roles are involved, Product Team does not want each role inventing its own process. The orchestrator creates one plan that says what will happen, in what order, who owns each part, and where review will happen.

Cuando intervienen varios roles, Product Team no quiere que cada uno invente su propio proceso. El orquestador crea un plan que dice qué va a pasar, en qué orden, quién se encarga de cada parte y dónde habrá revisión.

### Step 6. It asks for approval before major multi-role execution

### Paso 6. Pide aprobación antes de una ejecución grande con varios roles

For bigger coordinated work, the system pauses before the main execution starts. That way the user can confirm the direction first.

En los trabajos coordinados más grandes, el sistema se detiene antes de empezar la ejecución principal. Así la persona usuaria puede confirmar antes la dirección.

### Step 7. It coordinates execution and keeps the record current

### Paso 7. Coordina la ejecución y mantiene el registro al día

After approval, the orchestrator activates the roles in sequence, passes outputs from one role to the next, updates status, and records reviews and decisions.

Después de la aprobación, el orquestador activa los roles en secuencia, pasa los resultados de un rol al siguiente, actualiza el estado y registra revisiones y decisiones.

## Why One Role Can Cover Several Subtasks

## Por qué un rol puede cubrir varias subtareas

A role in this project is intentionally broad.

Un rol en este proyecto es intencionadamente amplio.

For example, a `designer` can cover research, UX, UI, and content without handing off to a new agent for every small step. An `engineer` can cover frontend and backend work in the same role.

Por ejemplo, un `designer` puede cubrir investigación, UX, UI y contenido sin pasar el trabajo a un nuevo agente en cada pequeño paso. Un `engineer` puede cubrir frontend y backend dentro del mismo rol.

This reduces handoffs, duplication, and confusion.

Esto reduce traspasos, duplicación y confusión.

## What Gets Written in `logs/`

## Qué se escribe en `logs/`

Inside `logs/active/<project-slug>/`, you will usually find files like these:

Dentro de `logs/active/<project-slug>/`, normalmente encontrarás archivos como estos:

- `00_routing.md`: why the system chose direct work or coordinated work
- `01_intake.md`: what the request means, plus limits, risks, and dependencies
- `02_staffing.md`: which roles were selected, only for coordinated work
- `03_unified-plan.md`: the main plan, only for coordinated work
- `04_approval.md`: the approval record, only for coordinated work
- `status.md`: the current state of execution
- `context.md`: the live summary needed to resume later
- `plans/`: optional specialist advice
- `deliverables/`: outputs from the roles
- `reviews/`: review notes and validation
- `decisions/`: important decisions and conflict resolution

- `00_routing.md`: por qué el sistema eligió trabajo directo o coordinado
- `01_intake.md`: qué significa la petición, además de límites, riesgos y dependencias
- `02_staffing.md`: qué roles se eligieron, solo en trabajo coordinado
- `03_unified-plan.md`: el plan principal, solo en trabajo coordinado
- `04_approval.md`: el registro de aprobación, solo en trabajo coordinado
- `status.md`: el estado actual de la ejecución
- `context.md`: el resumen vivo para poder retomar más adelante
- `plans/`: consejo opcional de especialistas
- `deliverables/`: resultados producidos por los roles
- `reviews/`: notas de revisión y validación
- `decisions/`: decisiones importantes y resolución de conflictos

There is also `logs/archive/` for completed or inactive work.

También existe `logs/archive/` para trabajos terminados o inactivos.

## What This Package Installs

## Qué instala este paquete

When you run the installer, it copies the Product Team workflow into the target repository.

Cuando ejecutas el instalador, copia el flujo de trabajo de Product Team dentro del repositorio de destino.

The main things it installs are:

Las cosas principales que instala son:

- the agent definitions
- their local skills and guides
- the shared package documentation
- the `logs/` structure
- a managed block inside `AGENTS.md`

- las definiciones de agentes
- sus habilidades y guías locales
- la documentación compartida del paquete
- la estructura de `logs/`
- un bloque gestionado dentro de `AGENTS.md`

The main paths it creates are:

Las rutas principales que crea son:

- `.codex/agents/product-team-...`
- `.codex/product-team/`
- `logs/active/`
- `logs/archive/`

The installer is designed to update its own files without overwriting unrelated files in the target project.

El instalador está pensado para actualizar sus propios archivos sin sobrescribir archivos no relacionados del proyecto de destino.

## How To Start

## Cómo empezar

### 1. Install it into your project

### 1. Instálalo en tu proyecto

If you are inside the repository where you want to install it:

Si estás dentro del repositorio donde quieres instalarlo:

```bash
./install.sh --target "$PWD"
```

Or directly from GitHub:

O directamente desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

Or with Python:

O con Python:

```bash
python3 scripts/install.py --target "$PWD"
```

### 2. Validate the install

### 2. Valida la instalación

From the root of the project where you installed it:

Desde la raíz del proyecto donde lo instalaste:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

### 3. Ask the coordinator to do work

### 3. Pídele trabajo al coordinador

Once installed, use `product-team-orchestrator` in Codex.

Una vez instalado, usa `product-team-orchestrator` en Codex.

Examples:

Ejemplos:

> "Fix this onboarding flow"

> "Arregla este flujo de onboarding"

> "Create a new pricing page"

> "Crea una nueva página de precios"

> "Redesign checkout to improve conversion"

> "Rediseña el checkout para mejorar la conversión"

The orchestrator will decide whether this should stay direct or become a coordinated workflow.

El orquestador decidirá si conviene mantenerlo como trabajo directo o convertirlo en un flujo coordinado.

### 4. Check `logs/` if you want to understand what happened

### 4. Mira `logs/` si quieres entender qué ha pasado

If you want to see why the system made a decision, what the plan was, or where the work stopped, `logs/` is the place to look.

Si quieres ver por qué el sistema tomó una decisión, cuál era el plan o en qué punto se quedó el trabajo, `logs/` es el lugar al que mirar.

## Simple Examples

## Ejemplos simples

Small request:

Petición pequeña:

> "Change the signup button text"

> "Cambia el texto del botón de registro"

This will usually stay direct.

Esto normalmente seguirá por vía directa.

Medium request in one main domain:

Petición mediana dentro de una sola área principal:

> "Build a markdown editor"

> "Construye un editor markdown"

This may still stay direct if it is mostly implementation work.

Esto puede seguir siendo trabajo directo si es sobre todo trabajo de implementación.

Complex request:

Petición compleja:

> "Redesign checkout to reduce abandonment"

> "Rediseña el checkout para reducir el abandono"

This will usually trigger planning, staffing, approval, execution, and review.

Esto normalmente activará planificación, elección de roles, aprobación, ejecución y revisión.

## What Problem This Solves

## Qué problema resuelve

Without a system like this, multi-agent work gets messy very quickly:

Sin un sistema así, el trabajo con varios agentes se vuelve confuso muy rápido:

- it is not clear who is deciding
- work gets duplicated
- context gets lost
- resuming later becomes hard
- multiple competing plans appear

- no queda claro quién decide
- el trabajo se duplica
- se pierde el contexto
- cuesta retomar el trabajo más tarde
- aparecen varios planes compitiendo entre sí

Product Team tries to solve that with three ideas:

Product Team intenta resolverlo con tres ideas:

- one coordinator owns the process
- the team should be as small as possible
- the workflow should leave a written memory

- un coordinador se encarga del proceso
- el equipo debe ser lo más pequeño posible
- el flujo de trabajo debe dejar una memoria escrita

## For Non-Technical Readers

## Para personas no técnicas

The shortest possible explanation is:

La explicación más corta posible es:

- this project does not build a product by itself
- this project installs a way of working inside Codex
- that way of working decides whether one agent or several agents should handle the task
- when several agents are needed, there is a plan, approval, coordination, and written follow-up

- este proyecto no construye un producto por sí mismo
- este proyecto instala una forma de trabajar dentro de Codex
- esa forma de trabajar decide si una tarea debe hacerla un agente o varios
- cuando hacen falta varios agentes, hay plan, aprobación, coordinación y seguimiento por escrito

## If You Maintain This Repository

## Si mantienes este repositorio

The main source-of-truth locations are:

Los principales lugares que actúan como fuente de verdad son:

- `agents/`: role definitions and local skills
- `logs/README.md`: the rules for the project memory system
- `install.sh` and `scripts/install.py`: installation entrypoints
- `assets/AGENTS.fragment.md`: the managed block injected into `AGENTS.md`
- `assets/package-README.md`: the README copied into installed projects

- `agents/`: definiciones de roles y habilidades locales
- `logs/README.md`: las reglas del sistema de memoria del proyecto
- `install.sh` y `scripts/install.py`: puntos de entrada de la instalación
- `assets/AGENTS.fragment.md`: el bloque gestionado que se inserta en `AGENTS.md`
- `assets/package-README.md`: el README que se copia a los proyectos instalados

If you change roles, structure, or orchestrator behavior, validate with:

Si cambias roles, estructura o el comportamiento del orquestador, valida con:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Then test a real install in a temporary folder and run:

Después prueba una instalación real en una carpeta temporal y ejecuta:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Short Summary

## Resumen corto

Product Team adds organization to Codex. If the task is simple, it keeps things simple. If the task is complex, it builds the smallest useful team, creates a plan, asks for approval, and records the work so it can be understood later.

Product Team añade organización a Codex. Si la tarea es simple, mantiene el proceso simple. Si la tarea es compleja, crea el equipo útil más pequeño, redacta un plan, pide aprobación y deja el trabajo registrado para poder entenderlo después.
