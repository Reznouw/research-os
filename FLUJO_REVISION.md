# Pipeline de revision por investigadores

> **Cuando un entregable esta listo para revision, este pipeline lo pasa por 5 investigadores afines, consolida sus correcciones y mejora el entregable.**
> No se crea otro documento. Se mejora el entregable existente.

## Flujo del pipeline

```
Entregable listo para revision
    ↓
1. Identificar tipo de entregable (EX1, EX2, TP1, EX3, DD1, TF1, o seccion especifica)
    ↓
2. Consultar SELECCION_INVESTIGADORES.md para elegir los 5 agentes afines
    ↓
3. Lanzar los 5 agentes en paralelo (task tool)
    Cada agente:
    - Lee su perfil en PERFILES_INVESTIGADORES.md
    - Lee las reglas del curso (01_silabus_como_regla.md)
    - Lee el entregable a revisar
    - Lee cualquier otro archivo relevante (propuesta, estado del arte, etc.)
    - Devuelve su revision en formato estructurado
    ↓
4. Consolidar las 5 revisiones en un REVISION_REPORTE.md temporal
    - Agrupar hallazgos por severidad (HIGH, MEDIUM, LOW)
    - Identificar conflictos entre investigadores
    - Identificar consenso (2+ investigadores con mismo hallazgo)
    ↓
5. Aplicar correcciones al entregable existente
    - Empezar por HIGH (consenso primero)
    - Luego MEDIUM
    - Luego LOW si hay tiempo
    - NO crear otro archivo. Editar el entregable existente.
    ↓
6. Verificar que las correcciones no rompen otros investigadores
    - Si un cambio afecta algo que otro investigador approbo, verificar
    ↓
7. Guardar REVISION_REPORTE.md en la carpeta del entregable
    propuestas/[propuesta]/entregables/[ENTREGABLE]/REVISION_REPORTE.md
    ↓
8. Actualizar ESTADO.md
    - Marcar entregable como "Revisado y corregido"
    - Registrar learning si hubo patron reutilizable
```

## Formato del REVISION_REPORTE.md

```markdown
# Revision de [ENTREGABLE] - [fecha]

## Investigadores que revisaron
1. [Nombre] (agente XX)
2. [Nombre] (agente XX)
3. [Nombre] (agente XX)
4. [Nombre] (agente XX)
5. [Nombre] (agente XX)

## Hallazgos consolidados

### HIGH (critico, debe corregirse)
- [Hallazgo] - Reportado por: [investigador(es)]
- [Hallazgo] - Reportado por: [investigador(es)]

### MEDIUM (importante, deberia corregirse)
- [Hallazgo] - Reportado por: [investigador(es)]

### LOW (sugerencia, puede corregirse si hay tiempo)
- [Hallazgo] - Reportado por: [investigador(es)]

### Consenso (2+ investigadores coinciden)
- [Hallazgo] - Reportado por: [X] investigadores

### Conflictos (investigadores discrepan)
- [Topic]: [Investigador A] dice X, [Investigador B] dice Y

## Correcciones aplicadas
- [Correccion 1] (HIGH, consenso)
- [Correccion 2] (HIGH)
- [Correccion 3] (MEDIUM)
- ...

## Lo que esta bien (no se cambio)
- [Aspecto approbado por mayoria]

## Frases clave de cada investigador
- [Investigador 1]: "[frase]"
- [Investigador 2]: "[frase]"
- ...

## Estado final
Entregable: [Revisado y corregido / Pendiente de correccion]
Proximo paso: [que hacer ahora]
```

## Reglas del pipeline

1. **No se crean documentos nuevos del entregable.** Se edita el entregable existente.
2. El unico archivo nuevo es REVISION_REPORTE.md, que se guarda en la carpeta del entregable.
3. Los 5 agentes trabajan en paralelo (task tool) para no saturar el contexto del agente principal.
4. El agente principal NO lee todo lo que leen los agentes. Solo recibe sus revisiones consolidadas.
5. Si hay conflicto entre investigadores, el agente principal decide basandose en las reglas del curso.
6. Las correcciones se aplican en orden: HIGH consenso > HIGH individual > MEDIUM > LOW.
7. Si una correccion requiere informacion que no se tiene, se marca como pendiente en ESTADO.md.
8. Despues de corregir, el agente principal puede lanzar una segunda ronda de revision si los cambios fueron significativos.
