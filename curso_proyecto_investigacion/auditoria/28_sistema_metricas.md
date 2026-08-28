# 28 Sistema de Metricas de Investigacion

> **Como saber si la investigacion avanza bien, la IA trabaja bien y los recursos se usan correctamente.**
> **Fecha de registro:** 2026-08-28
> **Ubicacion:** `curso_proyecto_investigacion/auditoria/28_sistema_metricas.md`
> **Integracion:** `metricas/` (dashboard + scorecards) + `ESTADO.md` (resumen semanal)

---

## Proposito

Responder 3 preguntas cada semana:

1. ¿La investigacion va bien? (calidad, cumplimiento, evidencia)
2. ¿La IA trabaja bien? (transcripcion, agentes, herramientas)
3. ¿Los recursos se usan bien? (tiempo, costo, avance)

Si alguna metrica esta en rojo, se actua antes de que afecte la nota.

---

## 4 Pilares de metricas

### Pilar 1: Calidad de investigacion (¿vamos bien academicamente?)

| Metrica | Como se mide | Verde | Amarillo | Rojo | Fuente |
|---|---|---|---|---|---|
| Cumplimiento reglamento | % de las 115 reglas (R1-R115) cumplidas | 95-100% | 80-94% | <80% | `auditoria/01_silabus_como_regla.md` + Ficha Clase Dia 1 |
| Completitud estado del arte | # papers SCOPUS/WOS fichados vs. minimo (5 por EX1) | >=5 | 3-4 | <3 | `fichas_papers/` + `manifest_fuentes.md` |
| Calidad de propuesta | Score 0-20 segun rubrica EX1 Fig 3 | 16-20 | 12-15 | <12 | Ficha evaluacion EX1 |
| Validacion de problema | ¿Problema general + causas + arbol definidos? | Si, con sustento | Parcial | No | `unidad1/05_situacion_problematica.md` |
| Patentes encontradas | # patentes Espacenet/Patentscope | >=2 | 1 | 0 | `fuentes_investigacion/` |

### Pilar 2: IA y herramientas (¿la IA trabaja bien?)

| Metrica | Como se mide | Verde | Amarillo | Rojo | Fuente |
|---|---|---|---|---|---|
| Precision transcripcion | WER estimado / prob_idioma faster-whisper | prob >=0.95 | 0.85-0.94 | <0.85 | `*_metadata.json` (prob_idioma) |
| Uso de agentes | # revisiones con /revision-investigadores por entregable | 5 agentes | 3-4 | <3 | `FLUJO_REVISION.md` |
| Herramientas verificadas | % herramientas OK (PyMuPDF, Pandoc, LaTeX, Zotero, ffmpeg, faster-whisper) | 100% | 80-99% | <80% | `auditoria/21_herramientas_instaladas.md` |
| Tiempo transcripcion | min de audio / min de proceso | <5x | 5-10x | >10x | `transcripciones/` |

### Pilar 3: Recursos y tiempo (¿usamos bien el tiempo?)

| Metrica | Como se mide | Verde | Amarillo | Rojo | Fuente |
|---|---|---|---|---|---|
| Avance vs. Gantt | % avance real vs. planificado (12 meses prop 01) | ±10% | ±20% | >20% retraso | `propuesta_01/documentacion_inicial/04_plan_viabilidad_12_meses.md` |
| Actas acumuladas | # actas vs. minimo por evaluacion | Cumple | -1 | -2 o mas | `10_ficha_acta_asesoria.md` |
| Asistencia | % clases asistidas (max 4 faltas = 25%) | 90-100% | 75-89% | <75% | Reglamento Art. 9 |
| Costo vs. presupuesto | S/ real vs. S/ 1250 DE25-Nano | Dentro | +20% | +50% | `01_propuesta_preliminar_DE25_Nano.md` |

### Pilar 4: Avance y entregables (¿entregamos a tiempo?)

| Metrica | Como se mide | Verde | Amarillo | Rojo | Fuente |
|---|---|---|---|---|---|
| Entregables a tiempo | % entregados antes de martes 1 PM | 100% | 80-99% | <80% | Reglamento Art. 32 |
| Formato correcto | % archivos con nombre exacto `XX-Tipo-PI-...` | 100% | 80-99% | <80% | `06_reglamento_tituloIV_entregables.md` |
| Estado TF1 (40%) | % completitud TF1 a semana 12 | >60% | 40-60% | <40% | `ESTADO.md` |

---

## Scorecard semanal (plantilla)

Copiar esta tabla cada semana en `metricas/scorecard_semana_XX.md`:

```markdown
# Scorecard Semana XX (YYYY-MM-DD)

| Pilar | Metrica | Valor | Estado | Accion |
|---|---|---|---|---|
| Calidad | Cumplimiento reglamento | 98% | Verde | - |
| Calidad | Estado del arte | 2/5 papers | Rojo | Buscar 3 mas en SCOPUS |
| IA | Precision transcripcion | 0.97 | Verde | - |
| Recursos | Actas | 1/1 | Verde | - |
| Avance | Entregable | A tiempo | Verde | - |

**Semaforo general:** Verde / Amarillo / Rojo
**Prioridad semanal:** [que hacer para pasar a verde]
```

---

## Dashboard (resumen visual)

Ubicacion: `metricas/dashboard.md` - se actualiza cada semana con los 4 pilares en formato semaforo:

```
Pilar 1 Calidad:       [ Verde  ] 98% reglas
Pilar 2 IA:            [ Verde  ] 0.97 prob, 5 agentes
Pilar 3 Recursos:      [ Amarillo] Actas 2/3 (falta 1)
Pilar 4 Avance:        [ Verde  ] EX1 entregado a tiempo
------------------------------------------------------------
GENERAL: AMARILLO -> Accion: generar acta con evaluador esta semana
```

---

## Automatizacion minima (sin codigo complejo)

Cada sesion, al leer `ESTADO.md`, verificar:

1. ¿Cuantas reglas incumplidas? (revisar `02_grupos` no aplica, solo academicas)
2. ¿Cuantos papers fichados esta semana?
3. ¿Cuantas actas tenemos vs. minimo?
4. ¿Entregable de esta semana esta a tiempo y con formato correcto?

Si 2+ metricas en rojo -> **alerta**: priorizar esas 2 antes de avanzar con lo nuevo.

---

## Cross-links

| Documento | Relacion |
|---|---|
| `ESTADO.md` | Resumen semanal del avance (donde se refleja el dashboard) |
| `DECISIONES.md` | Log de decisiones cuando una metrica pasa a rojo |
| `metricas/dashboard.md` | Dashboard visual con los 4 pilares |
| `metricas/scorecard_semana_XX.md` | Scorecard detallado por semana |
| `auditoria/00_indice_maestro_auditoria.md` | Indice que conecta este protocolo con los otros 27 |
| `propuesta_01/documentacion_inicial/04_plan_viabilidad_12_meses.md` | Gantt de 12 meses (Pilar 3) |
| `10_ficha_acta_asesoria.md` | Actas minimas (Pilar 3) |
| `06_reglamento_tituloIV_entregables.md` | Nombres exactos (Pilar 4) |
| `07_reglamento_tituloV_evaluacion.md` | Rubricas EX1 (Pilar 1) |
