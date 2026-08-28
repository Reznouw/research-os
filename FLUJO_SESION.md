# FLUJO DE SESION - Protocolo obligatorio

> **Este protocolo se sigue en cada sesion, sin excepcion.**
> Es como el sistema "nunca olvida nada": lee el estado, trabaja, actualiza el estado.

---

## INICIO de cada sesion (lectura de contexto)

### Paso 1: Leer siempre (orden estricto)

1. **ESTADO.md** — El primer archivo. Dice en que fase esta el proyecto, que esta hecho, que falta, y cual es el proximo paso. Si algo changed desde la ultima sesion, este archivo lo refleja.
2. **DECISIONES.md** — Solo las entradas recientes (ultimas 5-10). Para recordar por que se tomaron decisiones clave.
3. **AGENTS.md** — Reglas de comportamiento del agente.

### Paso 2: Leer segun la fase indicada en ESTADO.md

| Fase en ESTADO.md | Archivos a leer ademas |
|---|---|
| PREPARACION DE PROPUESTAS | `propuestas/README.md`, `propuestas/propuesta_*/propuesta_*.md` (las que existan), `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md` |
| PROPUESTAS EN REVISION | `propuestas/propuesta_*/propuesta_*.md` (todas), `propuestas/COMPARATIVA.md` si existe, `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md` |
| TEMA ELEGIDO - ESTADO DEL ARTE | `propuestas/[propuesta_elegida]/propuesta_*.md`, `propuestas/[propuesta_elegida]/estado_del_arte/*.md`, `propuestas/[propuesta_elegida]/fichas_papers/*.md` |
| TEMA ELEGIDO - DRAFT | `propuestas/[propuesta_elegida]/matriz_evidencia/*.md`, `propuestas/[propuesta_elegida]/entregables/*.md` |
| AUDITORIA | `propuestas/[propuesta_elegida]/entregables/*` (el entregable a auditar) |
| DEFENSA / DIDACTICA | `propuestas/[propuesta_elegida]/renzosky/*.md`, `propuestas/[propuesta_elegida]/entregables/*` |
| ENTREGA FINAL | `propuestas/[propuesta_elegida]/entregables/TF1/*`, `research_memory/global/learnings/*` |

### Paso 3: Confirmar al usuario

Al inicio de la primera respuesta de la sesion, declarar brevemente:

```
Sesion iniciada.
Fase actual: [fase de ESTADO.md]
Proximo paso: [proximo paso de ESTADO.md]
```

No mas de 3 lineas. El usuario ya sabe; es solo confirmacion de que el contexto se cargo.

---

## DURANTE la sesion (trabajo)

### Regla de decisions

Cada vez que se tome una decision que afecte el proyecto (cambiar tema, cambiar metodologia, descartar propuesta, cambiar formato, aceptar regla nueva del curso):

1. Append a `DECISIONES.md` con formato D00X, fecha, contexto, decision, razon, impacto.
2. Actualizar `ESTADO.md` si la decision cambia la fase o el proximo paso.

### Regla de ingesta

Cada vez que el usuario pase informacion nueva (documento, reglamento, audio, paper, datos):

1. Guardar el original en la carpeta correspondiente (`curso_proyecto_investigacion/fuentes_originales/`, `tema_tesis/00_RAW/`, etc.).
2. Procesar con source-ingestor (extraer reglas, claims, citas).
3. Guardar el resultado en la carpeta de auditoria o fichas.
4. Actualizar ESTADO.md con lo que se ingesto.

### Regla de propuestas

Cuando se generen o modifiquen propuestas:

1. Cada propuesta es una carpeta autocontenida: `propuestas/propuesta_NN_[tema_corto]/`.
2. Dentro de cada carpeta: `propuesta_NN.md` (documento principal) + `00_RAW/` + `renzosky/` + `estado_del_arte/` + `fichas_papers/` + `matriz_evidencia/` + `entregables/(EX1-EX2-TP1-EX3-DD1-TF1)`.
3. Mantener `propuestas/COMPARATIVA.md` actualizado con la comparacion entre todas.
4. Actualizar ESTADO.md con el numero de propuestas activas y sus estados.
5. Cuando se elija una propuesta, marcarla como "Elegida" en su `propuesta_NN.md` y en ESTADO.md. Esa carpeta se convierte en el proyecto activo.

### Regla de entregables

Cuando se trabaje en un entregable (EX1, EX2, TP1, EX3, DD1, TF1):

1. Crear carpeta `tema_tesis/entregables/[ENTREGABLE]/`.
2. Seguir la estructura esperada definida en `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md`.
3. Antes de declarar listo, pasar gate de auditoria (paper-audit).
4. Actualizar ESTADO.md: cambiar estado del entregable a "En progreso" o "Completado".

### Regla de aprendizajes

Cada vez que ocurra un error, confusion, correccion del profesor o patron reutilizable:

1. Append a `research_memory/global/learnings/` con un archivo nuevo o actualizando uno existente.
2. Si es un error que puede repetirse, convertir en regla en AGENTS.md o en la skill correspondiente.

### Regla de perspectivas

Antes de escribir una seccion del paper o entregable, revisar `perspectivas_investigadores/` buscando el consejo aplicable:

| Seccion a escribir | Perspectivas relevantes |
|---|---|
| Estado del arte / related work | "How to read papers", "Reading a Paper", "Speed Read Research Papers" |
| Introduccion | "How to Write a Great Research Paper" (Microsoft Research, TAUVOD) |
| Figuras | "Principles of Beautiful Figures", Vizuara |
| LaTeX | "Data Professor LaTeX", "Vuk Rosic Write & Publish AI Research Paper" |
| Peer review / respuesta | "Belal Al Droubi Publication & Peer-Review", TAUVOD |
| Metodologia | "Vizuara MIT PhD", "Prof. Rahul Pandya IIT" |

Estas son fuente de workflow, no de evidencia cientifica.

### Regla de revision por investigadores

Cuando un entregable este listo para revision:

1. Identificar el tipo de entregable o seccion.
2. Consultar `perspectivas_investigadores/SELECCION_INVESTIGADORES.md` para elegir los 5 agentes mas afines.
3. Lanzar los 5 agentes en paralelo (task tool). Cada agente lee su perfil, las reglas del curso, y el entregable.
4. Consolida las 5 revisiones (HIGH/MEDIUM/LOW, consenso, conflictos).
5. Aplica correcciones al entregable existente (no crear otro archivo).
6. Guarda `REVISION_REPORTE.md` en la carpeta del entregable.
7. Actualiza ESTADO.md.
8. Ver `FLUJO_REVISION.md` para detalle completo.

Comando: `/revision-investigadores <entregable>`

---

## FIN de cada sesion (actualizacion de estado)

### Siempre, antes de terminar:

1. **Actualizar ESTADO.md:**
   - `Ultima actualizacion`: fecha y sesion.
   - `Fase actual`: cambiar si cambio.
   - `Que esta hecho`: marcar nuevos completados.
   - `Que falta`: actualizar.
   - `Proximo paso accionable`: el proximo paso real.
   - `Memoria rapida para la siguiente sesion`: 3-7 bullets de lo mas importante de esta sesion.
   - `Riesgos activos`: actualizar.

2. **Si hubo decisions:** Confirmar que DECISIONES.md esta actualizado.

3. **Si hubo ingesta:** Confirmar que los archivos se guardaron en sus carpetas.

4. **Si hubo aprendizajes:** Confirmar que research_memory/global/learnings/ esta actualizado.

### Mensaje final al usuario

Al terminar la sesion, declarar:

```
Sesion finalizada.
Estado actualizado: [fase]
Proximo paso: [proximo paso]
Pendientes: [lista breve de pendientes si los hay]
```

---

## Estructura de carpetas definitiva

```
INVESTIGACION/
│
├── ESTADO.md                          ← PRIMER archivo que se lee
├── DECISIONES.md                      ← Log append-only de decisions
├── FLUJO_SESION.md                    ← Este archivo (protocolo)
├── AGENTS.md                          ← Reglas del agente
├── RESEARCH_OS.md                     ← Pipeline general
├── SISTEMA_INVESTIGACION.md           ← Capacidades operativas
├── opencode.json                      ← Comandos y permisos
│
├── .opencode/                         ← Skills + agentes
│   ├── agent/                         (7 agentes)
│   └── skills/                        (8 skills)
│
├── research_memory/
│   └── global/
│       └── learnings/                 ← Aprendizajes reutilizables
│
├── curso_proyecto_investigacion/      ← Reglas del curso
│   ├── fuentes_originales/            ← Syllabus, reglamento, documentos crudos
│   └── auditoria/                     ← Reglas extraidas de las fuentes
│
├── perspectivas_investigadores/       ← 28 transcripciones (workflow, no evidencia)
│
└── propuestas/                        ← 5 propuestas autocontenidas
    ├── README.md                      ← Guia de propuestas
    ├── COMPARATIVA.md                 ← (Se crea cuando haya 2+ formales)
    │
    ├── propuesta_01_edge_ai_fpga_reconfigurable/
    │   ├── propuesta_01.md            ← Documento principal
    │   ├── 00_RAW/                    ← Material bruto
    │   ├── renzosky/                  ← 4 documentos de estudio
    │   ├── estado_del_arte/           ← Papers y matriz de referentes
    │   ├── fichas_papers/             ← Ficha de cada paper
    │   ├── matriz_evidencia/          ← Claims, fuentes, locators
    │   └── entregables/
    │       ├── EX1/
    │       ├── EX2/
    │       ├── TP1/
    │       ├── EX3/
    │       ├── DD1/
    │       └── TF1/
    │
    ├── propuesta_02_hls_fpga_de10nano/
    │   └── (misma estructura)
    │
    ├── propuesta_03_finn_hls4ml_tinyml/
    │   └── (misma estructura)
    │
    ├── propuesta_04_quantization_pruning_fpga/
    │   └── (misma estructura)
    │
    └── propuesta_05_pendiente/
        └── (misma estructura, pendiente de tema)
```

## Regla de oro: nunca olvidar

El sistema "nunca olvida nada" porque:

1. **ESTADO.md** se lee primero en cada sesion y refleja el estado completo.
2. **DECISIONES.md** registra cada decision con su razon (append-only).
3. **research_memory/global/learnings/** registra cada error o patron.
4. Cada sesion termina actualizando ESTADO.md.
5. La estructura de carpetas es predecible: cada tipo de contenido tiene su lugar.
6. Las reglas del curso estan en `curso_proyecto_investigacion/auditoria/`.
7. Las perspectivas de investigadores estan en `perspectivas_investigadores/`.
8. Las propuestas estan en `propuestas/`.
9. El desarrollo del tema esta en `tema_tesis/`.

Si alguna de estas carpetas no existe cuando se necesita, se crea. Si algun archivo falta, se identifica como gap en ESTADO.md.
