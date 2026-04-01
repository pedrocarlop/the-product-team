# Product Team

[Read this in English](./README.md)

## Instalación

Desde un checkout local:

```bash
./install.sh --target "$PWD"
```

Desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

Con Python:

```bash
python3 scripts/install.py --target "$PWD"
```

Validar un proyecto ya instalado:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

Actualizar después un proyecto instalado:

```bash
python3 .codex/product-team/scripts/update-install.py
```

## Qué Hace

Product Team es un flujo instalable de Codex para repositorios que quieren que el trabajo con agentes se parezca más al funcionamiento de un equipo real de producto.

Instala:

- un orquestador que enruta cada petición
- un conjunto dividido de roles especialistas en negocio, diseño, ingeniería y revisión
- una superficie compartida de memoria en `/logs` para contexto, entregables, decisiones y estado
- un bloque gestionado en `AGENTS.md` que convierte Product Team en la entrada por defecto del repo de destino

La regla principal de funcionamiento es: usar el proceso más ligero que todavía haga bien el trabajo.

Eso significa que Product Team no crea un equipo para cada petición. Primero el orquestador decide si el trabajo debe quedarse en vía directa o pasar a coordinación. Cuando coordinar ayuda, elige el conjunto mínimo de roles que aporta valor.

## Cómo Funcionan Los Roles

El repositorio está organizado alrededor de activos locales por rol en `agents/<disciplina>/<rol>/`. En negocio, diseño e ingeniería, los roles siguen el mismo patrón:

- un TOML de rol con el prompt del sistema y la política de ejecución
- una tarjeta `capabilities.md`
- un `skill-catalog.md` que siempre se lee primero
- un conjunto de flujos `skills/*.md` propios del rol

La topología actual de roles es:

- Negocio: `product-lead`, `analyst`, `business-ops`, `go-to-market`
- Diseño: `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer`
- Ingeniería: `frontend-engineer`, `backend-engineer`, `platform-engineer`
- Revisión: `design-reviewer`, `qa-reviewer`
- Soporte: `orchestrator`, `reference`

Lo que es consistente en los roles especialistas:

- trabajan solo a partir de asignaciones emitidas por el orquestador
- leen primero `skill-catalog.md` y después los `skill_paths` asignados
- ejecutan un flujo de skill concreto, no un resumen genérico del rol
- siguen la misma regla de fallback: `primary MCP -> alternative tool/MCP -> best guess inferred output`
- etiquetan la evidencia como `sourced`, `fallback` o `inferred`
- escriben en un artefacto propio dentro de `logs/active/<project-slug>/...`

El límite entre disciplinas es intencional:

- Los roles de negocio y diseño son propietarios de artefactos de asesoramiento. En flujos coordinados no son dueños de la implementación del repo.
- Los roles de ingeniería solo pueden editar archivos versionados cuando el orquestador les da propiedad explícita de implementación y un `repo_write_scope` acotado.
- `reference` es un rol de apoyo en solo lectura para grounding, trazabilidad, reutilización y verificación.

## Cómo Fluyen Las Peticiones

1. Una petición entra por `product-team-orchestrator`.
2. El orquestador lee su propio catálogo de skills y decide entre ejecución directa o coordinada.
3. Si el trabajo es simple y claramente de un solo rol, puede quedarse en vía directa.
4. Si el trabajo es transversal o tiene más riesgo, el orquestador staffea el conjunto mínimo de roles útil.
5. Los roles reciben un contrato explícito de asignación con campos como `skill_paths`, `owned_outputs`, `primary_tools`, `fallback_policy`, `repo_write_owner` y `evidence_mode`.
6. El trabajo se registra en `logs/active/<project-slug>/` para que el estado sobreviva más allá del contexto del chat.

Para trabajo de diseño nuevo, el flujo no debe ir en línea recta de idea a acabado. La parte de diseño debe divergir antes de converger: explorar direcciones materialmente distintas, compararlas y solo entonces pasar a diseño de producción e implementación.

## Layout Instalado

El instalador mantiene Product Team con namespace propio e idempotencia. Las rutas principales que instala son:

- `.codex/agents/product-team-<disciplina>/<rol>/`
- `.codex/product-team/`
- `logs/active/`
- `logs/archive/`

Puede actualizar archivos que pertenecen al flujo y el bloque gestionado de `AGENTS.md`, pero no debería sobrescribir archivos no relacionados del proyecto.

## Logs Y Memoria

`logs/README.md` es el contrato de la memoria persistente del proyecto.

En la práctica:

- `context.md` registra el objetivo, el estado, los roles staffeados, los `skill_paths` exactos y los criterios de finalización
- `deliverables/` guarda los entregables de los roles
- `decisions/` guarda decisiones duraderas
- `TIMELINE.md` indexa el trabajo del proyecto a lo largo del tiempo

El enrutado, la selección de roles y la aprobación ocurren en contexto, pero el registro duradero del proyecto vive en `/logs`.

## Mantener Este Paquete

Fuentes de verdad:

- `agents/`: definiciones de roles y skills locales
- `logs/README.md`: contrato de `/logs` en tiempo de ejecución
- `install.sh` y `scripts/install.py`: puntos de entrada del instalador
- `assets/AGENTS.fragment.md`: bloque gestionado que se inyecta en los repositorios de destino
- `assets/package-README.md`: README que se copia a los proyectos instalados

Si cambias la estructura de roles, prompts, routing o comportamiento del instalador, valida con:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Después haz una instalación real en una carpeta temporal y valídala:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Versión Corta

Product Team instala un flujo coordinado de Codex dentro de otro repositorio. Mantiene simple el trabajo simple, añade coordinación solo cuando ayuda, enruta a través de roles reales de negocio/diseño/ingeniería y deja un registro operativo escrito en `/logs`.
