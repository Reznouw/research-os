# 28 Sistema de Metricas de Investigacion - Puntaje 0-100 (0-20)

> **Como saber con precision si la investigacion avanza bien, la IA trabaja bien y los recursos se usan correctamente.**
> **Escala:** 0-100 (granular) = 0-20 (nota curso, dividir entre 5)
> **Fecha:** 2026-08-28 (v2 - con puntaje detallado por rubrica y 115 reglas)
> **Ubicacion:** `curso_proyecto_investigacion/auditoria/28_sistema_metricas.md`
> **Integracion:** `metricas/dashboard.md` + `metricas/scorecard_semana_XX.md` + `ESTADO.md`

---

## Escala de calidad

| Puntaje 0-100 | Nota 0-20 | Nivel | Semaforo | Significado |
|---|---|---|---|---|
| 90-100 | 18-20 | Excelente | 🟢 | Listo para entregar, sin riesgo |
| 80-89 | 16-17.9 | Bueno | 🟢 | Bien, pulir detalles menores |
| 70-79 | 14-15.9 | Aceptable | 🟡 | Aprobado pero con observaciones |
| 60-69 | 12-13.9 | En riesgo | 🟠 | Requiere accion esta semana |
| 0-59 | 0-11.9 | Critico | 🔴 | No entregar, corregir urgente |

**Nota curso PF = 0.10*EX1 + 0.10*EX2 + 0.15*TP1 + 0.15*EX3 + 0.10*DD + 0.40*TF** — cada entregable vale distinto, pero este puntaje mide la **calidad interna semanal**.

---

## 4 Pilares (100 puntos totales)

| Pilar | Peso | Que mide | Fuente |
|---|---|---|---|
| **1. Calidad de investigacion** | **40 pts** | Reglas + Rubricas + Estado del arte | Reglamento 6 titulos (115 reglas) + Fig 3-10 |
| **2. IA y herramientas** | **20 pts** | Transcripcion, agentes, verificacion, cross-links | `21_herramientas_instaladas.md` + `26_protocolo_transcripcion_audio.md` |
| **3. Recursos y tiempo** | **20 pts** | Gantt, actas, asistencia, costo | `04_plan_viabilidad_12_meses.md` + `10_ficha_acta_asesoria.md` |
| **4. Avance y entregables** | **20 pts** | Entregables, formato, plazo, vestimenta | `06_reglamento_tituloIV_entregables.md` + `07_reglamento_tituloV_evaluacion.md` |
| **TOTAL** | **100 pts** |  |  |

---

## Pilar 1: Calidad de investigacion (40 pts) - 10 sub-metricas

### 1.1 Reglas criticas (10 pts) - Las que causan 0 o sancion

| # | Regla | Peso | Como se puntua |
|---|---|---|---|
| R30 | No copiar del internet | -5 si viola | 0 o 10 |
| R62-63 | Inasistencia = 0, no recuperable | -5 si viola |  |
| R66 | Modo impersonal obligatorio | -2 si viola |  |
| R68 | Impuntualidad/sobrepasar tiempo -3p | -2 si viola |  |
| R81-83 | Grabar audio y subir a tiempo | -2 si viola |  |
| R88-90 | Reclamo max 5 lineas, antes de registro | -1 si viola |  |

**Calculo:** 10 - (suma de penalizaciones). Min 0.

### 1.2 Reglas de entregables (10 pts) - Formato y nombres

| # | Regla | Como se puntua |
|---|---|---|
| R51 | Nombre exacto `XX-Tipo-PI-...` | 2 pts si 100% correcto, 1 si 80-99%, 0 si <80% |
| R45-R50 | Entregables completos (5-6 por evaluacion) | 2 pts si 100%, 1 si falta 1, 0 si faltan 2+ |
| R65 | Informe: 11 items (formato, redaccion, numeracion, IEEE, etc.) | 3 pts (3 si cumple 9-11, 2 si 6-8, 1 si 3-5, 0 si <3) |
| R67 | Exposicion: 7 items (formato, diapositivas, claridad, etc.) | 3 pts (misma escala) |

### 1.3 Rubrica EX1 preparacion (10 pts) - Fig 3 detallada

| Item Fig 3 | Max | Como se puntua (Si=2, Parcial=1, No=0) |
|---|---|---|
| 3.1 Tema (max 3 propuestas) | 2 | Si=2, Parcial=1, No=0 |
| 3.2 Importancia del problema | 2 | Si=2, Parcial=1, No=0 |
| 3.3 Descripcion solucion | 2 | Si=2, Parcial=1, No=0 |
| 3.4 Viabilidad | 2 | Si=2, Parcial=1, No=0 |
| 3.5 Soluciones comerciales | 1 | Si=1, Parcial=0.5, No=0 |
| 3.6 Articulos investigacion | 1 | Si=1, Parcial=0.5, No=0 |
| **Total** | **10** |  |

> Para EX3/TF1 usar Fig 5 (13 items, 13p) -> escalar a 10. Para EX2/TP1 usar Fig 4/6 (10p) directo.

### 1.4 Estado del arte (5 pts)

| Metrica | 5 pts | 3 pts | 1 pt | 0 pts |
|---|---|---|---|---|
| Papers SCOPUS/WOS fichados | >=5 | 3-4 | 1-2 | 0 |
| Productos comerciales | >=3 | 2 | 1 | 0 |

**Calculo:** Papers (0-3) + Productos (0-2) = 5.

### 1.5 Patentes (5 pts)

| # patentes Espacenet/Patentscope | Puntos |
|---|---|
| >=2 | 5 |
| 1 | 3 |
| 0 | 0 |

**Total Pilar 1:** 1.1 (10) + 1.2 (10) + 1.3 (10) + 1.4 (5) + 1.5 (5) = **40 pts**

---

## Pilar 2: IA y herramientas (20 pts) - 4 sub-metricas

| Sub-metrica | 5 pts | 3 pts | 0 pts | Fuente |
|---|---|---|---|---|
| **2.1 Precision transcripcion** (prob_idioma) | >=0.95 | 0.85-0.94 | <0.85 | `*_metadata.json` |
| **2.2 Agentes usados** (# revisiones /revision-investigadores) | 5 agentes | 3-4 | <3 | `FLUJO_REVISION.md` |
| **2.3 Herramientas verificadas** (% OK) | 100% (6/6) | 80-99% | <80% | `21_herramientas_instaladas.md` |
| **2.4 Cross-links completos** (% protocolos con cross-links) | 100% (7/7) | 70-99% | <70% | `00_indice_maestro_auditoria.md` |

**Total Pilar 2:** 4 x 5 = **20 pts**

---

## Pilar 3: Recursos y tiempo (20 pts) - 4 sub-metricas

| Sub-metrica | 7 pts | 4 pts | 0 pts | Fuente |
|---|---|---|---|---|
| **3.1 Avance vs Gantt** (12 meses) | ±10% | ±20% | >20% retraso | `04_plan_viabilidad_12_meses.md` |
| **3.2 Actas** (vs minimo) | Cumple | -1 | -2 o mas | `10_ficha_acta_asesoria.md` |

| Sub-metrica | 6 pts | 3 pts | 0 pts | Fuente |
|---|---|---|---|---|
| **3.3 Asistencia** (% clases) | 90-100% (0-1 falta) | 75-89% (2-3 faltas) | <75% (4+ faltas = DPEI) | Art. 9, R111 |
| **3.4 Costo** (S/ vs 1250) | Dentro | +20% | +50% (S/1875+) | `01_propuesta_preliminar_DE25_Nano.md` |

**Total Pilar 3:** 7+7+6+? = **20 pts** (3.1=6, 3.2=6, 3.3=4, 3.4=4 -> ajustar a 20: 5+5+5+5 = 20). **Correccion:** Cada una 5 pts para simplificar.

| Sub-metrica | 5 pts | 3 pts | 0 pts |
|---|---|---|---|
| **3.1 Gantt** | ±10% | ±20% | >20% |
| **3.2 Actas** | Cumple | -1 | -2+ |
| **3.3 Asistencia** | 0-1 falta | 2-3 faltas | 4+ faltas |
| **3.4 Costo** | Dentro S/1250 | +20% | +50% |

**Total Pilar 3:** 4 x 5 = **20 pts**

---

## Pilar 4: Avance y entregables (20 pts) - 4 sub-metricas

| Sub-metrica | 5 pts | 3 pts | 0 pts | Fuente |
|---|---|---|---|---|
| **4.1 Entregables a tiempo** (% antes de martes 1 PM) | 100% | 80-99% | <80% | Art. 32, R84 |
| **4.2 Formato nombre correcto** (% `XX-Tipo-PI-...`) | 100% | 80-99% | <80% | Art. 20-21, R51 |
| **4.3 Audio/video subido** (enlace TXT, no archivo) | 100% | 50% | 0% | Art. 31, R98-99 |
| **4.4 Vestimenta** (ropa de vestir / terno TF1) | 100% | - | 0% (penalizacion) | Art. 28, R69-70 |

**Total Pilar 4:** 4 x 5 = **20 pts**

---

## Calculo del puntaje total

```
TOTAL 0-100 = Pilar1 (40) + Pilar2 (20) + Pilar3 (20) + Pilar4 (20)

NOTA 0-20 = TOTAL / 5

Ejemplo Semana 01:
  P1: 1.1=10 + 1.2=8 + 1.3=6 + 1.4=1 + 1.5=0 = 25/40
  P2: 5+5+5+5 = 20/20
  P3: 5+5+5+3 = 18/20  (costo +20% por S/1250 aun no justificado)
  P4: 5+5+5+5 = 20/20  (todo a tiempo, formato listo)
  TOTAL = 25+20+18+20 = 83/100 = 16.6/20 = BUENO (verde)
```

---

## Scorecard semanal (plantilla con puntaje)

Copiar en `metricas/scorecard_semana_XX.md`:

```markdown
# Scorecard Semana XX (YYYY-MM-DD) - Puntaje 0-100

| Pilar | Sub-metrica | Pts | Max | Detalle |
|---|---|---|---|---|
| 1.1 | Reglas criticas | 10 | 10 | Sin violaciones |
| 1.2 | Reglas entregables | 8 | 10 | Nombre 100%, informe 6/11 items |
| 1.3 | Rubrica EX1 (Fig 3) | 6 | 10 | 3.1=2, 3.2=1, 3.3=1, 3.4=1, 3.5=0.5, 3.6=0.5 |
| 1.4 | Estado del arte | 1 | 5 | 0 papers, 1 producto |
| 1.5 | Patentes | 0 | 5 | 0 patentes |
| **P1** | **Calidad** | **25** | **40** |  |
| 2.1 | Transcripcion | 5 | 5 | prob 1.0 |
| 2.2 | Agentes | 5 | 5 | 5 agentes |
| 2.3 | Herramientas | 5 | 5 | 6/6 OK |
| 2.4 | Cross-links | 5 | 5 | 7/7 |
| **P2** | **IA** | **20** | **20** |  |
| 3.1 | Gantt | 5 | 5 | En plan |
| 3.2 | Actas | 5 | 5 | 0/0 |
| 3.3 | Asistencia | 5 | 5 | 0 faltas |
| 3.4 | Costo | 3 | 5 | +20% |
| **P3** | **Recursos** | **18** | **20** |  |
| 4.1 | A tiempo | 5 | 5 | 100% |
| 4.2 | Formato nombre | 5 | 5 | 100% |
| 4.3 | Audio/video | 5 | 5 | Enlace TXT |
| 4.4 | Vestimenta | 5 | 5 | OK |
| **P4** | **Avance** | **20** | **20** |  |
| **TOTAL** |  | **83** | **100** | **16.6/20 - BUENO** |

**Prioridad:** Buscar 5 papers SCOPUS + 2 patentes para subir P1 de 25 a 35
```

---

## Dashboard (resumen)

`metricas/dashboard.md` muestra:

```
TOTAL: 83/100 (16.6/20) - BUENO 🟢
P1 Calidad:    25/40 (62%) 🟡 -> falta estado del arte
P2 IA:         20/20 (100%) 🟢
P3 Recursos:   18/20 (90%) 🟢
P4 Avance:     20/20 (100%) 🟢
```

---

## Regla de accion

- **Si P1 < 25/40 o TOTAL < 60:** No avanzar con nuevo entregable; corregir calidad primero.
- **Si P3 actas < 3/5 o asistencia < 3/5:** Generar acta esta semana, no faltar.
- **Si 2+ pilares < 70%:** Alerta roja, priorizar esas 2.

---

## Cross-links

| Documento | Relacion |
|---|---|
| `ESTADO.md` | Resumen semanal (refleja TOTAL 0-100) |
| `07_reglamento_tituloV_evaluacion.md` | Fig 3-10 con puntajes max (20, 180) que alimentan P1 |
| `01_silabus_como_regla.md` + `03-08_reglamento_*.md` | 115 reglas (R1-R115) que alimentan P1.1 y P1.2 |
| `04_plan_viabilidad_12_meses.md` | Gantt (P3.1) |
| `10_ficha_acta_asesoria.md` | Actas (P3.2) |
| `06_reglamento_tituloIV_entregables.md` | Nombres (P4.2), entregables (P4.1) |
