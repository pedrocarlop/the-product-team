# Product Team

[Read this in English](./README.md)

Product Team es un paquete para Codex que convierte un repositorio normal en un espacio donde varios agentes pueden trabajar como un pequeño equipo de producto.

En términos simples, este proyecto añade un coordinador, un conjunto de especialistas y un registro compartido del trabajo para que Codex pueda decidir cómo organizarlo en vez de limitarse a reaccionar tarea por tarea.

## Idea principal

La regla principal es simple: empezar con el proceso más ligero posible.

Eso significa que Product Team no crea un grupo de agentes para cada petición. Primero comprueba si un solo agente puede resolver el trabajo bien. Solo si la coordinación mejora claramente el resultado incorpora más roles.

En la práctica, el flujo es:

1. Llega una petición.
2. El coordinador decide si el trabajo es simple o si cruza varias áreas.
3. Si es simple, se hace directamente.
4. Si es más complejo, el coordinador elige el equipo más pequeño que tenga sentido.
5. Las decisiones importantes y el estado se escriben en `logs/`.

## Qué es realmente este proyecto

Piensa en Product Team como un sistema de funcionamiento para la colaboración entre agentes dentro de Codex.

No es un producto final para usuarios por sí mismo. Es una forma reutilizable de trabajar que puedes instalar dentro de otro repositorio para que Codex tenga:

- un coordinador que controla el proceso
- roles especialistas para distintos tipos de trabajo
- una memoria escrita de lo que ha pasado
- reglas claras para decidir cuándo trabajar de forma directa y cuándo coordinar

## Las partes principales

### 1. El coordinador: `orchestrator`

El orquestador es el rol que decide cómo debe hacerse el trabajo.

Se encarga de entender la petición, decidir si conviene seguir por vía directa o iniciar un flujo coordinado, elegir roles, ordenar el trabajo y pedir aprobación antes de una ejecución grande con varios roles.

Su filosofía es:

- no complicar trabajos simples
- no crear un equipo si ese equipo no aporta valor
- dejar el proceso por escrito

### 2. Los especialistas

El paquete incluye un conjunto de roles que representan grandes áreas de trabajo.

Negocio:

- `product-lead`: decide qué debería construirse y por qué
- `analyst`: trabaja con métricas, previsiones y números
- `go-to-market`: se centra en crecimiento, marketing, ventas y lanzamiento
- `business-ops`: mejora procesos y estructura operativa

Diseño:

- `designer`: cubre investigación, UX, UI, contenido, accesibilidad y más
- `design-systems`: se encarga de componentes reutilizables, tokens y coherencia visual

Ingeniería:

- `engineer`: construye funcionalidades de producto en frontend, backend, móvil y trabajo full stack
- `platform-engineer`: se ocupa de APIs, bases de datos, rendimiento, seguridad y arquitectura técnica

Revisión:

- `reviewer`: comprueba si el resultado es sólido, útil y con suficiente calidad

### 3. Memoria compartida: `logs/`

`logs/` es donde el flujo de trabajo deja escrito lo que ha pasado.

Esto importa porque el sistema no quiere depender solo de la memoria del chat. Quiere un registro duradero de la petición, del plan, del estado actual, de los entregables y de las decisiones importantes.

En lenguaje sencillo, `logs/` es el cuaderno del proyecto.

## Cómo funciona paso a paso

### Paso 1. Llega una petición

Ejemplos:

> "Corrige el typo de la página de login"
>
> "Rediseña el flujo de checkout para reducir el abandono"

El orquestador empieza entendiendo el objetivo real que hay detrás de la petición.

### Paso 2. Elige trabajo directo o trabajo coordinado

Esta es la decisión más importante de todo el sistema.

El trabajo directo se usa cuando la petición pertenece sobre todo a una sola área, está lo bastante clara y es poco probable que mejore mucho involucrando a muchos roles.

El trabajo coordinado se usa cuando la petición mezcla varias disciplinas, necesita una secuencia clara, contiene decisiones importantes o se beneficia de una revisión formal.

### Paso 3. Si el trabajo es directo, se mantiene simple

En la vía directa, el orquestador registra la petición, aclara qué ha entendido, mantiene el estado actualizado y sigue adelante sin ceremonias innecesarias.

### Paso 4. Si el trabajo es coordinado, elige el equipo útil más pequeño

El sistema evita por defecto los equipos grandes. Si dos roles bastan, usa dos. Si un rol basta, usa uno. La idea no es simular una empresa enorme. La idea es añadir la estructura justa para mejorar el resultado.

### Paso 5. El orquestador redacta un único plan compartido

Cuando intervienen varios roles, Product Team no quiere que cada uno invente su propio proceso. El orquestador crea un plan que dice qué va a pasar, en qué orden, quién se encarga de cada parte y dónde habrá revisión.

### Paso 6. Pide aprobación antes de una ejecución grande con varios roles

En los trabajos coordinados más grandes, el sistema se detiene antes de empezar la ejecución principal. Así la persona usuaria puede confirmar antes la dirección.

### Paso 7. Coordina la ejecución y mantiene el registro al día

Después de la aprobación, el orquestador activa los roles en secuencia, pasa los resultados de un rol al siguiente, actualiza el estado y registra revisiones y decisiones.

## Por qué un rol puede cubrir varias subtareas

Un rol en este proyecto es intencionadamente amplio.

Por ejemplo, un `designer` puede cubrir investigación, UX, UI y contenido sin pasar el trabajo a un nuevo agente en cada pequeño paso. Un `engineer` puede cubrir frontend y backend dentro del mismo rol.

Esto reduce traspasos, duplicación y confusión.

## Qué se escribe en `logs/`

Dentro de `logs/active/<project-slug>/`, normalmente encontrarás archivos como estos:

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

También existe `logs/archive/` para trabajos terminados o inactivos.

## Qué instala este paquete

Cuando ejecutas el instalador, copia el flujo de trabajo de Product Team dentro del repositorio de destino.

Las cosas principales que instala son:

- las definiciones de agentes
- sus habilidades y guías locales
- la documentación compartida del paquete
- la estructura de `logs/`
- un bloque gestionado dentro de `AGENTS.md`

Las rutas principales que crea son:

- `.codex/agents/product-team-...`
- `.codex/product-team/`
- `logs/active/`
- `logs/archive/`

El instalador está pensado para actualizar sus propios archivos sin sobrescribir archivos no relacionados del proyecto de destino.

## Cómo empezar

### 1. Instálalo en tu proyecto

Si estás dentro del repositorio donde quieres instalarlo:

```bash
./install.sh --target "$PWD"
```

O directamente desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

O con Python:

```bash
python3 scripts/install.py --target "$PWD"
```

### 2. Valida la instalación

Desde la raíz del proyecto donde lo instalaste:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

### 3. Pídele trabajo al coordinador

Una vez instalado, usa `product-team-orchestrator` en Codex.

Ejemplos:

> "Arregla este flujo de onboarding"
>
> "Crea una nueva página de precios"
>
> "Rediseña el checkout para mejorar la conversión"

El orquestador decidirá si conviene mantenerlo como trabajo directo o convertirlo en un flujo coordinado.

### 4. Mira `logs/` si quieres entender qué ha pasado

Si quieres ver por qué el sistema tomó una decisión, cuál era el plan o en qué punto se quedó el trabajo, `logs/` es el lugar al que mirar.

## Ejemplos simples

Petición pequeña:

> "Cambia el texto del botón de registro"

Esto normalmente seguirá por vía directa.

Petición mediana dentro de una sola área principal:

> "Construye un editor markdown"

Esto puede seguir siendo trabajo directo si es sobre todo trabajo de implementación.

Petición compleja:

> "Rediseña el checkout para reducir el abandono"

Esto normalmente activará planificación, elección de roles, aprobación, ejecución y revisión.

## Qué problema resuelve

Sin un sistema así, el trabajo con varios agentes se vuelve confuso muy rápido:

- no queda claro quién decide
- el trabajo se duplica
- se pierde el contexto
- cuesta retomar el trabajo más tarde
- aparecen varios planes compitiendo entre sí

Product Team intenta resolverlo con tres ideas:

- un coordinador se encarga del proceso
- el equipo debe ser lo más pequeño posible
- el flujo de trabajo debe dejar una memoria escrita

## Para personas no técnicas

La explicación más corta posible es:

- este proyecto no construye un producto por sí mismo
- este proyecto instala una forma de trabajar dentro de Codex
- esa forma de trabajar decide si una tarea debe hacerla un agente o varios
- cuando hacen falta varios agentes, hay plan, aprobación, coordinación y seguimiento por escrito

## Si mantienes este repositorio

Los principales lugares que actúan como fuente de verdad son:

- `agents/`: definiciones de roles y habilidades locales
- `logs/README.md`: las reglas del sistema de memoria del proyecto
- `install.sh` y `scripts/install.py`: puntos de entrada de la instalación
- `assets/AGENTS.fragment.md`: el bloque gestionado que se inserta en `AGENTS.md`
- `assets/package-README.md`: el README que se copia a los proyectos instalados

Si cambias roles, estructura o el comportamiento del orquestador, valida con:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Después prueba una instalación real en una carpeta temporal y ejecuta:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Resumen corto

Product Team añade organización a Codex. Si la tarea es simple, mantiene el proceso simple. Si la tarea es compleja, crea el equipo útil más pequeño, redacta un plan, pide aprobación y deja el trabajo registrado para poder entenderlo después.
