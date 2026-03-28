# Product Team

Product Team es un paquete para Codex que convierte un repositorio normal en un espacio donde varios agentes pueden trabajar como si fueran un pequeño equipo de producto.

Dicho de forma simple: este proyecto añade un "coordinador" y varios "especialistas" para que Codex no solo ejecute tareas sueltas, sino que también pueda decidir cómo organizar el trabajo, cuándo merece la pena pedir ayuda a otros agentes y cómo dejar todo documentado para no perder el hilo.

## La idea principal

Este sistema sigue una regla muy importante:

**primero intenta resolver las cosas de la forma más simple posible**.

Eso significa que no crea un equipo de agentes para todo. Antes de hacerlo, comprueba si una sola persona-agente puede resolver la tarea bien y más rápido.

En la práctica funciona así:

1. Llega una petición.
2. El coordinador decide si eso es algo simple o algo que necesita varias miradas.
3. Si es simple, se hace directamente.
4. Si es más complejo, el coordinador elige el equipo mínimo necesario.
5. Todo queda apuntado en una carpeta de `logs/` para que el trabajo tenga memoria.

## Cómo entender este proyecto sin tecnicismos

Piensa en Product Team como una oficina pequeña dentro de Codex:

- Hay una persona que reparte el trabajo: el **orchestrator**.
- Hay especialistas para producto, diseño, negocio, ingeniería y revisión.
- Hay una libreta compartida donde se apunta todo: la carpeta **`logs/`**.
- Hay un instalador que copia esta forma de trabajar dentro de cualquier proyecto tuyo.

No es una app final para usuarios. Es una forma de organizar cómo trabajan los agentes dentro de otro proyecto.

## Las piezas más importantes

### 1. El coordinador: `orchestrator`

Es el cerebro del sistema.

Su trabajo no es hacerlo todo, sino decidir:

- qué se ha pedido realmente
- si el trabajo es simple o complejo
- qué tipo de ayuda hace falta
- si compensa trabajar con un solo agente o con varios
- en qué orden deben trabajar
- cuándo hay que pedir aprobación antes de seguir

Su filosofía es clara:

- si una tarea se puede hacer bien sin montar un equipo, no monta un equipo
- si una tarea se puede hacer mejor con varias personas-agente, coordina ese proceso

### 2. Los especialistas

El proyecto trae varios roles ya preparados. Cada uno representa un tipo de trabajo.

#### Negocio

- `product-lead`: ayuda a definir qué se construye, por qué y con qué prioridad
- `analyst`: trabaja con números, métricas, previsiones e impacto
- `go-to-market`: piensa en crecimiento, marketing, ventas y salida al mercado
- `business-ops`: ordena procesos y operaciones

#### Diseño

- `designer`: cubre investigación, experiencia de usuario, interfaz, textos, accesibilidad y más
- `design-systems`: se centra en componentes, estilos comunes y coherencia visual

#### Ingeniería

- `engineer`: implementa producto, frontend, backend, móvil y trabajo full stack
- `platform-engineer`: se ocupa de APIs, bases de datos, rendimiento, seguridad, infraestructura y arquitectura técnica

#### Revisión

- `reviewer`: revisa si el resultado tiene sentido, si funciona bien y si la calidad es suficiente

### 3. La memoria del trabajo: `logs/`

Todo lo importante se guarda en `logs/`.

Esto es clave porque el sistema no quiere depender de la memoria de una conversación suelta. Quiere dejar rastro claro de:

- qué se pidió
- qué se entendió
- quién iba a participar
- cuál era el plan
- si hubo aprobación
- en qué punto está el trabajo
- qué decisiones se tomaron
- qué entregables se produjeron

En otras palabras: `logs/` es el historial vivo del proyecto.

## Cómo funciona paso a paso

### Paso 1. Entra una petición

Puede ser algo pequeño:

> "Corrige un typo en la página de login"

O algo más grande:

> "Rediseña el checkout para reducir el abandono"

El coordinador siempre empieza por entender qué se quiere conseguir de verdad.

### Paso 2. Decide si va por la vía rápida o por la vía coordinada

Aquí está la esencia del sistema.

#### Vía rápida: trabajo directo

Se usa cuando la tarea:

- pertenece claramente a un solo tipo de trabajo
- está bastante clara
- es más de ejecutar que de debatir
- no gana mucho añadiendo más agentes

Ejemplo:

> "Construye un editor markdown"

Aunque sea una tarea importante, puede seguir siendo bastante directa si no requiere negociación entre producto, diseño y revisión.

#### Vía coordinada: trabajo orquestado

Se usa cuando la tarea:

- mezcla varias disciplinas
- tiene decisiones que conviene pensar antes de construir
- necesita una secuencia clara entre varios especialistas
- puede mejorar de verdad con revisión o validación cruzada

Ejemplo:

> "Rediseña el checkout para reducir el abandono un 20%"

Aquí sí tiene sentido coordinar varias miradas: producto, diseño, implementación y revisión.

### Paso 3. Si el trabajo es directo, se ejecuta sin ceremonia innecesaria

En ese caso el coordinador:

- registra la petición
- deja claro qué entendió
- actualiza el estado del trabajo
- ejecuta

No crea un proceso largo solo por seguir un ritual.

### Paso 4. Si el trabajo es coordinado, monta el equipo mínimo

El sistema intenta evitar equipos grandes porque eso cuesta tiempo y complica el proceso.

Por eso, si bastan dos roles, usa dos. Si hace falta uno, usa uno. Si hacen falta cuatro, usa cuatro, pero no más.

Ejemplos:

- para una mejora visual sencilla pueden bastar `designer` + `engineer`
- para una funcionalidad completa pueden entrar `product-lead`, `designer`, `engineer` y `reviewer`
- para una tarea de datos puede bastar `platform-engineer`

### Paso 5. El coordinador redacta un plan único

Cuando hay varios agentes, este proyecto evita que cada uno tire por su lado.

Por eso el coordinador crea un plan común que dice:

- qué se va a hacer
- en qué orden
- quién se encarga de cada parte
- qué depende de qué
- dónde habrá revisión

Así todos trabajan con una misma hoja de ruta.

### Paso 6. Pide aprobación antes del trabajo importante

Si la tarea es grande o implica a varios especialistas, el sistema no asume que puede seguir sin más.

Primero deja el plan por escrito y luego espera aprobación antes de arrancar la ejecución principal.

### Paso 7. Coordina la ejecución

Una vez aprobado el plan:

- activa a los especialistas en orden
- pasa el resultado de uno al siguiente
- mantiene el estado actualizado
- registra decisiones y revisiones

Esto ayuda a que el proyecto no se convierta en una cadena caótica de mensajes.

## Qué significa que un rol "cubre varias cosas"

Una idea importante de este proyecto es que un rol no representa una microtarea, sino un área de trabajo bastante amplia.

Por ejemplo:

- un `designer` puede encargarse de investigación, estructura, interfaz y textos
- un `engineer` puede encargarse de frontend y backend

Eso evita pasar el trabajo de un agente a otro sin necesidad.

En vez de tener diez agentes minúsculos, el sistema usa pocos roles con suficiente amplitud para avanzar de verdad.

## Qué se guarda exactamente en `logs/`

Dentro de `logs/active/<nombre-del-proyecto>/` suelen aparecer archivos como estos:

- `00_routing.md`: por qué se decidió trabajo directo o coordinado
- `01_intake.md`: qué se entendió de la petición, límites, riesgos y dependencias
- `02_staffing.md`: qué roles se eligieron, solo si hubo coordinación
- `03_unified-plan.md`: el plan principal, solo si hubo coordinación
- `04_approval.md`: la aprobación del plan, solo si hubo coordinación
- `status.md`: estado actual del trabajo
- `context.md`: resumen vivo para retomar el proyecto sin perder contexto
- `plans/`: notas de apoyo de especialistas, si hacen falta
- `deliverables/`: entregables creados por los roles
- `reviews/`: revisiones y validaciones
- `decisions/`: decisiones importantes cuando hubo dudas o conflicto

También existe `logs/archive/`, que sirve para mover proyectos ya terminados o inactivos.

## Qué instala este paquete en otro proyecto

Cuando ejecutas el instalador, este repositorio copia dentro del proyecto destino:

- los agentes
- sus habilidades y guías
- la documentación compartida del paquete
- la estructura de `logs/`
- un bloque gestionado dentro de `AGENTS.md`

Las rutas principales que crea son:

- `.codex/agents/product-team-...`
- `.codex/product-team/`
- `logs/active/`
- `logs/archive/`

Importante: el instalador intenta tocar solo sus propios archivos. No está pensado para sobrescribir archivos ajenos del proyecto.

## Cómo empezar a usarlo

### 1. Instálalo en tu proyecto

Si estás dentro del repositorio donde lo quieres instalar:

```bash
./install.sh --target "$PWD"
```

O desde GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

Si prefieres usar Python:

```bash
python3 scripts/install.py --target "$PWD"
```

### 2. Comprueba que la instalación quedó bien

Desde la raíz del proyecto donde lo instalaste:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

### 3. Pídele trabajo al coordinador

Una vez instalado, usa el `product-team-orchestrator` dentro de Codex.

Puedes pedirle cosas como:

> "Arregla este flujo de onboarding"

> "Crea una nueva página de precios"

> "Rediseña el checkout para mejorar la conversión"

Según la petición, el coordinador decidirá si trabaja directo o si monta un pequeño equipo.

### 4. Mira los `logs/` si quieres entender qué ha pasado

Si alguna vez quieres ver cómo se decidió el trabajo, cuál era el plan o en qué punto se quedó, ahí estará todo.

## Ejemplos sencillos

### Caso A: petición pequeña

Petición:

> "Cambia el texto del botón de registro"

Lo normal es que el coordinador lo trate como trabajo directo.

### Caso B: petición mediana pero de una sola área

Petición:

> "Construye un editor markdown"

Puede seguir siendo trabajo directo si es principalmente implementación y no necesita mucha coordinación entre áreas.

### Caso C: petición compleja

Petición:

> "Rediseña el checkout para reducir abandono"

Aquí lo habitual es:

1. entender bien el objetivo
2. elegir roles
3. proponer un plan
4. pedir aprobación
5. ejecutar por fases
6. revisar el resultado

## Qué problema resuelve este proyecto

Sin un sistema así, trabajar con varios agentes puede volverse confuso muy rápido:

- no queda claro quién decide
- varios agentes hacen trabajo duplicado
- se pierde el contexto
- cuesta retomar algo días después
- aparecen planes distintos compitiendo entre sí

Product Team intenta evitar eso con tres ideas:

- un coordinador que manda el proceso
- un equipo pequeño y suficiente, no enorme
- una memoria escrita y ordenada en `logs/`

## Para personas no técnicas: qué debes recordar

Si no eres experta o experto en código, la idea básica es esta:

- este proyecto no construye un producto por sí mismo
- este proyecto instala una manera de trabajar dentro de Codex
- esa manera de trabajar decide si una tarea la hace un solo agente o varios
- cuando participan varios, hay coordinación, plan, aprobación y seguimiento
- todo queda documentado para que el proceso no dependa de la memoria

## Si vas a mantener este repositorio

La fuente principal del proyecto está aquí:

- `agents/`: definición de roles y habilidades
- `logs/README.md`: reglas de la carpeta de memoria
- `scripts/install.py` e `install.sh`: instalación
- `assets/AGENTS.fragment.md`: bloque gestionado que se inserta en `AGENTS.md`
- `assets/package-README.md`: README que recibe el proyecto instalado

Si cambias roles, estructura o comportamiento del orquestador, conviene validar el paquete con:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Y después probar una instalación real en una carpeta temporal:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Resumen corto

Product Team es una capa de organización para Codex.

No añade solo agentes: añade una forma ordenada de decidir, ejecutar, coordinar y dejar memoria del trabajo. Si una tarea es simple, la resuelve sin ruido. Si una tarea es compleja, crea el equipo justo, propone un plan y lo deja todo registrado.
