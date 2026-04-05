# Product Team

[Read this in English](./README.md)

## Instalacion

### Codex (por defecto)

Desde un checkout local:

```bash
./install.sh --target "$PWD"
```

Desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

### Claude Code

Desde un checkout local:

```bash
./install.sh --platform claude --target "$PWD"
```

O con el wrapper:

```bash
./install-claude.sh --target "$PWD"
```

Desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install-claude.sh | bash -s -- --target "$PWD"
```

### Antigravity

Desde un checkout local:

```bash
./install.sh --platform antigravity --target "$PWD"
```

O con el wrapper:

```bash
./install-antigravity.sh --target "$PWD"
```

Desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install-antigravity.sh | bash -s -- --target "$PWD"
```

### Con Python directamente

```bash
python3 scripts/install.py --target "$PWD"
python3 scripts/install.py --platform claude --target "$PWD"
python3 scripts/install.py --platform antigravity --target "$PWD"
```

### Validar y actualizar

Los scripts auto-detectan la plataforma desde el manifest instalado:

```bash
python3 .codex/product-team/scripts/validate-install.py   # Codex
python3 .claude/product-team/scripts/validate-install.py   # Claude Code
python3 .antigravity/product-team/scripts/validate-install.py  # Antigravity
```

```bash
python3 .codex/product-team/scripts/update-install.py      # Codex
python3 .claude/product-team/scripts/update-install.py      # Claude Code
python3 .antigravity/product-team/scripts/update-install.py # Antigravity
```

## Que Hace

Product Team es un flujo instalable para repositorios que quieren que el trabajo con agentes se parezca mas a un equipo real de producto.

Instala:

- un orquestador que enruta cada peticion
- un conjunto de roles especialistas en negocio, diseno, ingenieria y revision
- tres superficies de salida: `/logs` (traza de ejecucion), `/knowledge` (entregables), `/app` (codigo)
- un bloque gestionado en `AGENTS.md` (Codex), `CLAUDE.md` (Claude Code), o `ANTIGRAVITY.md` (Antigravity) que convierte Product Team en la entrada por defecto

La regla principal de funcionamiento es: **usar el proceso mas ligero que todavia haga bien el trabajo.**

Product Team no crea un equipo para cada peticion. Primero el orquestador decide si el trabajo debe quedarse en via directa o pasar a coordinacion. Cuando coordinar ayuda, elige el conjunto minimo de roles que aporta valor.

## Como Funcionan Los Roles

El repositorio esta organizado alrededor de activos locales por rol en `agents/<disciplina>/<rol>/`. Cada rol sigue el mismo patron:

- un `.toml` con el prompt del sistema y la politica de ejecucion
- una tarjeta `capabilities.md`
- un `skill-catalog.md` que siempre se lee primero
- un conjunto de flujos `skills/*.md`

La topologia actual de roles (16 especialistas + 1 orquestador + 1 referencia = 18 en total):

| Disciplina | Roles |
|---|---|
| Negocio | `product-lead`, `analyst`, `business-ops`, `go-to-market` |
| Diseno | `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer` |
| Ingenieria | `frontend-engineer`, `backend-engineer`, `platform-engineer` |
| Revision | `design-reviewer`, `qa-reviewer` |
| Soporte | `orchestrator`, `reference` |

Lo que es consistente en los roles especialistas:

- trabajan solo a partir de asignaciones emitidas por el orquestador
- leen primero `skill-catalog.md` y despues los `skill_paths` asignados
- ejecutan un flujo de skill concreto, no un resumen generico del rol
- siguen la misma regla de fallback: `primary MCP -> alternative tool/MCP -> best guess inferred output`
- etiquetan la evidencia como `sourced`, `fallback` o `inferred`
- escriben entregables en `knowledge/` y registros de ejecucion en `logs/active/<project-slug>/`

El limite entre disciplinas es intencional:

- Los roles de **negocio y diseno** son propietarios de artefactos de asesoria. En flujos coordinados no son duenos de la implementacion del repo.
- Los roles de **ingenieria** solo pueden editar archivos versionados cuando el orquestador les da propiedad explicita de implementacion y un `repo_write_scope` acotado.
- **Reference** es un rol de apoyo en solo lectura para grounding, trazabilidad, reutilizacion y verificacion.

## Contrato De Asignacion

Cuando el orquestador staffea especialistas, cada asignacion incluye:

| Campo | Proposito |
|---|---|
| `run_id` | Identificador unico de la etapa de ejecucion |
| `assignment_mode` | `primary_executor`, `lean_input`, o `peer_reviewer` |
| `owned_outputs` | Rutas en `knowledge/` que el agente escribira |
| `reads_from` | Rutas en `knowledge/` que el agente debe leer (incluyendo proyectos previos) |
| `repo_write_owner` | Rol que es dueno de escritura en el repo, o null |
| `repo_write_scope` | Ruta en `app/` para codigo, o null |
| `return_expected` | Descripcion breve del entregable esperado |
| `skill_paths` | Flujos de skill exactos a ejecutar |
| `primary_tools` | Servidores/herramientas MCP requeridos |
| `fallback_policy` | Herramienta alternativa o `best guess inferred output` |
| `evidence_mode` | `sourced`, `fallback`, o `inferred` |

La regla global de fallback es: `primary MCP -> alternative tool/MCP -> best guess inferred output`.

## Como Fluyen Las Peticiones

1. Una peticion entra por `product-team-orchestrator`.
2. El orquestador lee su propio catalogo de skills y decide entre ejecucion directa o coordinada.
3. Si el trabajo es simple y claramente de un solo rol, puede quedarse en via directa.
4. Si el trabajo es transversal o tiene mas riesgo, el orquestador staffea el conjunto minimo de roles util.
5. Los roles reciben un contrato explicito de asignacion.
6. Cada especialista lee `skill-catalog.md`, abre los `skill_paths` asignados, y ejecuta ese flujo.
7. Los entregables van a `knowledge/` (canonico + snapshot en `knowledge/runs/<run-id>/`). El codigo va a `app/`. Los registros de ejecucion van a `logs/`.

Para trabajo de diseno nuevo, el flujo no debe ir en linea recta. La parte de diseno debe **divergir antes de converger**: explorar direcciones materialmente distintas, compararlas, y solo entonces pasar a diseno de produccion e implementacion.

## Sistema De Conocimiento

`knowledge/README.md` es el contrato para la inteligencia de negocio persistente. El conocimiento se organiza como una **wiki persistente y acumulativa** — compilada una vez y mantenida al dia, no redescubierta en cada consulta.

Reglas clave:

- **Organizacion plana**: Sin anidamiento por slug de proyecto para que los agentes encuentren conocimiento relevante entre todos los proyectos.
- **Indice wiki** (`knowledge/index.md`): Catalogo orientado por tema de todos los entregables, organizado por dominio. El orquestador lo lee primero para encontrar conocimiento relevante sin escanear cada archivo.
- **Registro de cambios** (`knowledge/changelog.md`): Log append-only de cada mutacion de conocimiento (`created`, `updated`, `superseded`, `archived`). Permite al orquestador ver que cambio desde el ultimo proyecto.
- **Cabeceras de entregable**: Cada archivo empieza con frontmatter YAML (`role`, `project`, `run_id`, `confidence`, `inputs_used`, `evidence_mode`, `related`). El campo `related` crea enlaces cruzados entre entregables.
- **TL;DR obligatorio**: Cada entregable incluye una seccion `## TL;DR` (1-3 frases) inmediatamente despues de la cabecera, permitiendo escaneo rapido sin leer archivos completos.
- **Paginas de entidad** (`knowledge/entities/`): Conceptos transversales (competidores, personas, patrones, decisiones) tienen paginas dedicadas que agregan hallazgos de multiples entregables.
- **Historial sin perdida**: Al actualizar un entregable, los agentes escriben primero en `knowledge/runs/<run-id>/`, luego pueden actualizar el archivo canonico. Las versiones previas nunca se sobrescriben. Cada mutacion se registra en `changelog.md`.
- **Orden progresivo de escaneo**: (1) `index.md` para categorias de dominio, (2) cola de `changelog.md` para cambios recientes, (3) secciones TL;DR de archivos relevantes, (4) archivos completos solo cuando es directamente necesario, (5) enlaces `related` para contexto.
- **Continuidad de conocimiento**: Antes de cada asignacion, el orquestador sigue el orden progresivo de escaneo e incluye archivos relevantes en `reads_from`. Las decisiones se acumulan entre proyectos.
- **Lint** (skill `lint-knowledge`): Chequeo de salud periodico que detecta archivos obsoletos, contradicciones, huerfanos, referencias cruzadas faltantes, lagunas de conocimiento y deriva de entidades. Resultados en `knowledge/orchestrator-lint.md`.
- **Reflexion obligatoria**: Cada entregable termina con una seccion `## Reflection` (Que funciono, Que no, Siguientes pasos).

## Flujo De Sistema De Diseno

Para diseno de producto greenfield:

1. `ui-designer` explora direcciones visuales y elige una.
2. `ui-designer` siembra `project-ds-spec.md` a partir de hasta 3 referencias solo-inspiracionales de la libreria incluida de design-system kits (40+ sistemas de diseno de companias como Airbnb, Stripe, Notion, Figma, y otros).
3. Si el frontend esta en blanco y la spec lo justifica, la spec compartida puede recomendar una base de shadcn/ui.
4. `design-systems-designer` operacionaliza la spec compartida en tokens, primitivas, familias de componentes, reglas de layouts/widgets, gobernanza y QA.
5. El trabajo posterior de pantallas y componentes hereda de `project-ds-spec.md`, no directamente de referencias de companias.
6. La ingenieria solo puede materializar la recomendacion de shadcn cuando tiene propiedad explicita de escritura en el repo.

La plantilla para `project-ds-spec.md` esta en `references/project-ds-spec-template.md`.

## Layout Instalado

El instalador mantiene Product Team con namespace propio e idempotencia. El directorio base depende de la plataforma:

| Plataforma | Dir base | Archivo gestionado |
|---|---|---|
| Codex | `.codex/` | `AGENTS.md` |
| Claude Code | `.claude/` | `CLAUDE.md` |
| Antigravity | `.antigravity/` | `ANTIGRAVITY.md` |

```
target-repo/
  AGENTS.md | CLAUDE.md | ANTIGRAVITY.md   # Bloque gestionado (segun plataforma)
  logs/
    README.md                               # Contrato de traza de ejecucion
    TIMELINE.md                             # Indice cronologico de proyectos
    active/                                 # Registros de proyectos activos
    archive/                                # Proyectos completados
  knowledge/                                # (Solo Codex)
    README.md                               # Contrato de conocimiento
    assets/                                 # Artefactos visuales
    reviews/                                # Entregables de revision
    runs/                                   # Historial sin perdida
  app/                                      # (Solo Codex) Salidas de codigo
  <base-dir>/                               # .codex/ | .claude/ | .antigravity/
    product-team/
      README.md                             # Documentacion del paquete
      manifest.json                         # Metadatos de instalacion
      references/                           # Catalogo de roles, plantillas, design systems
      scripts/                              # Validador, actualizador, utilidades
      auto-improve/                         # Sistema de auto-mejora
    agents/
      product-team-business/<rol>/          # Definiciones de roles de negocio
      product-team-design/<rol>/            # Definiciones de roles de diseno
      product-team-engineer/<rol>/          # Definiciones de roles de ingenieria
      product-team-review/<rol>/            # Definiciones de roles de revision
```

Las instalaciones de Claude y Antigravity omiten los directorios `knowledge/` y `app/`.

## Logs Y Memoria

`logs/README.md` es el contrato de la memoria persistente del proyecto.

Cada proyecto vive en `logs/active/<project-slug>/` (formato: `YYYYMMDD-kebab-case-objetivo`):

- **`context.md`** — Cabecera YAML (`slug`, `objective`, `confidence_score`, `status`, `current_run_id`) mas objetivo, restricciones, criterios de finalizacion, roles staffeados, skill_paths, estado y decisiones clave.
- **`runs/<run-id>-<YYYYMMDD-HHMM>/`** — Un directorio por etapa de ejecucion:
  - `prompt.md` — La asignacion exacta dada al agente.
  - `trace.md` — Razonamiento del agente, uso de herramientas, decisiones clave, rutas de entregables.
  - `feedback.md` — Retroalimentacion del usuario o notas de revision.
- **`TIMELINE.md`** — Indice cronologico de todos los proyectos con fecha, slug, objetivo, roles y estado.

Los proyectos completados se mueven de `active/` a `archive/`. Ver `logs/archive/sample-20260101-onboarding-flow/` para un ejemplo completo.

## Sistema De Plantillas De Fragmentos

El bloque gestionado que se inyecta en los repositorios de destino se genera desde una plantilla compartida:

- **Plantilla**: `assets/product-team.fragment.template.md` (usa placeholder `{{PLATFORM}}`)
- **Generador**: `scripts/generate-fragments.sh`
- **Salidas**: `assets/AGENTS.fragment.md`, `assets/CLAUDE.fragment.md`, `assets/ANTIGRAVITY.fragment.md`

Edita la plantilla, luego ejecuta `scripts/generate-fragments.sh` para regenerar los tres fragmentos.

## Validacion

Validacion de la estructura fuente:

```bash
scripts/validate-orchestrator-contract.sh
```

Esto ejecuta todas las verificaciones:

- Validacion de estructura TOML para cada rol
- Frescura del catalogo de roles (`scripts/render_role_catalog.py --check`)
- Frescura de catalogos de skills (`scripts/render_skill_catalogs.py --check`)
- Frescura de prompts de roles (`scripts/render_role_prompts.py --check`)
- Frescura del roster de agentes (`scripts/render_agents_md.py --check`)
- Validacion de escenarios del orquestador (`scripts/check-orchestrator-scenarios.py`)

Validacion de skills:

```bash
python3 scripts/check_skill_validation_scenarios.py
```

Validacion de proyecto instalado:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Sistema De Auto-Mejora

Ubicado en `assets/auto-improve/`, es un bucle de hill-climbing para el refinamiento continuo de skills:

1. **Benchmark** (`benchmark.py`) — Prepara un escenario con una skill bajo prueba y captura el artefacto esperado.
2. **Judge** (`judge.py`) — Puntua el artefacto producido usando rubricas estructurales (deterministico) o LLM-as-judge (para evaluacion matizada).
3. **Meta-Optimizer** (`meta_optimizer.py`) — Analiza fallos y genera prompts de optimizacion. Con `--apply`, modifica la skill directamente.
4. **Cron Trigger** (`scripts/cron-trigger.sh`) — Orquesta el ciclo completo. Auto-commitea mejoras cuando las puntuaciones aumentan.

Escenarios disponibles (en `assets/auto-improve/scenarios/`):

- `modern-saas-dashboard` — Diseno: concepto visual para un dashboard SaaS
- `engineering-frontend-component` — Ingenieria: implementacion de componente React
- `business-product-prd` — Negocio: documento de requisitos de producto
- `ux-research-plan` — Investigacion: plan de investigacion de usuarios
- `content-microcopy-flow` — Contenido: microcopy de flujo de checkout
- `design-system-audit` — Sistemas de diseno: auditoria de sistema
- `go-to-market-launch` — Go-to-market: plan de lanzamiento
- `backend-api-implementation` — Backend: diseno de API REST
- `platform-schema-migration` — Plataforma: plan de migracion de esquema
- `design-usability-review` — Revision: evaluacion de usabilidad
- `qa-release-gate` — QA: evaluacion de preparacion de release

Una plantilla CI para GitHub Actions esta en `assets/auto-improve/templates/self-improvement-ci.yml`.

## Autoria De Skills

`skill-authoring-guide.md` define el estandar de produccion para crear skills. Principios fundamentales:

- **Metodo sobre prompt** — Las skills codifican flujos de trabajo expertos reales, no instrucciones genericas.
- **Evidencia sobre opinion** — Salidas fundamentadas en input observable o suposiciones explicitamente declaradas.
- **Estructura sobre prosa** — Las salidas son estructuradas, escaneables y reutilizables.
- **Reproducibilidad** — Otro agente deberia poder seguir el mismo proceso y llegar a conclusiones similares.

Cada skill incluye: frontmatter (contrato de ejecucion), proposito, inputs requeridos, ruta de evidencia, stack de herramientas, paso de construccion de modelo, ejecucion del metodo principal, hallazgos estructurados, logica de priorizacion, deteccion de patrones, recomendaciones, mapa de cobertura, limites, y logging sin perdida.

## Mantener Este Paquete

Fuentes de verdad:

- `agents/`: definiciones de roles y skills locales
- `logs/README.md`: contrato de `/logs` en tiempo de ejecucion
- `knowledge/README.md`: contrato de conocimiento
- `install.sh` y `scripts/install.py`: puntos de entrada del instalador
- `assets/product-team.fragment.template.md`: plantilla del bloque gestionado
- `assets/package-README.md`: README copiado a los proyectos instalados
- `references/specialist-baseline.md`: plantilla de prompt compartida para todos los especialistas
- `references/role-catalog.md`: referencia canonica de staffing
- `skill-authoring-guide.md`: estandares de produccion de skills

Despues de cambiar la estructura de roles, prompts, o routing:

```bash
# Regenerar archivos gestionados
python3 scripts/render_role_catalog.py --write
python3 scripts/render_skill_catalogs.py --write
python3 scripts/render_role_prompts.py --write
python3 scripts/render_agents_md.py --write
scripts/generate-fragments.sh

# Validar
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Luego probar una instalacion real:

```bash
python3 scripts/install.py --target /tmp/test-install
python3 /tmp/test-install/.codex/product-team/scripts/validate-install.py

# O para otras plataformas:
python3 scripts/install.py --platform claude --target /tmp/test-claude
python3 /tmp/test-claude/.claude/product-team/scripts/validate-install.py
```

## Version Corta

Product Team instala un flujo coordinado dentro de otro repositorio. Mantiene simple el trabajo simple, anade coordinacion solo cuando ayuda, enruta a traves de roles reales de negocio/diseno/ingenieria, usa flujos de skills MCP-first con fallback, preserva conocimiento sin perdida entre proyectos, y deja un registro operativo escrito en `/logs`.
