# Scorecard Semana 01 - 2026-08-28 - 83/100 (16.6/20) 🟢 BUENO

> **Protocolo:** `curso_proyecto_investigacion/auditoria/28_sistema_metricas.md`
> **Dashboard:** `metricas/dashboard.md`

| Pilar | Sub-metrica | Pts | Max | % | Detalle | Fuente |
|---|---|---|---|---|---|---|
| 1.1 | Reglas criticas (R30,62,63,66,68,81,88-90) | 10 | 10 | 100% | Sin violaciones, 115 reglas OK | Reglamento 6 titulos |
| 1.2 | Reglas entregables (R45-54, R51, R65, R67) | 8 | 10 | 80% | Nombre 100% (2 pts), Entregables 100% (2 pts), Informe 6/11 items (2/3), Exposicion 6/7 items (2/3) | Art. 20-21,27,28 |
| 1.3 | Rubrica EX1 (Fig 3: 3.1-3.6) | 6 | 10 | 60% | 3.1=2 (tema definido), 3.2=1 (parcial), 3.3=1 (parcial), 3.4=1 (parcial), 3.5=0.5, 3.6=0.5 | Fig 3 |
| 1.4 | Estado del arte (papers + productos) | 1 | 5 | 20% | 0 papers SCOPUS/WOS (0/3), 1 producto (1/2) | `fichas_papers/` |
| 1.5 | Patentes (Espacenet/Patentscope) | 0 | 5 | 0% | 0 patentes | `fuentes_investigacion/` |
| **P1** | **Calidad** | **25** | **40** | **62%** | **Aceptable** |  |
| 2.1 | Precision transcripcion (prob_idioma) | 5 | 5 | 100% | prob 1.0 (clase Dia 1), 4 audios transcritos | `*_metadata.json` |
| 2.2 | Agentes usados | 5 | 5 | 100% | 33 agentes (29+4) | `FLUJO_REVISION.md` |
| 2.3 | Herramientas verificadas | 5 | 5 | 100% | 6/6 OK (PyMuPDF, pandoc, LaTeX, Zotero, ffmpeg, faster-whisper) | `21_herramientas_instaladas.md` |
| 2.4 | Cross-links completos | 5 | 5 | 100% | 7/7 protocolos con cross-links, indice 00 | `00_indice_maestro_auditoria.md` |
| **P2** | **IA** | **20** | **20** | **100%** | **Excelente** |  |
| 3.1 | Avance vs Gantt (12 meses) | 5 | 5 | 100% | Mes 1 (definicion) - en plan | `04_plan_viabilidad_12_meses.md` |
| 3.2 | Actas (vs minimo) | 5 | 5 | 100% | 0/0 (EX1 no requiere), plan 10 actas listo | `10_ficha_acta_asesoria.md` |
| 3.3 | Asistencia | 5 | 5 | 100% | 0/4 faltas (100%) | Art. 9 |
| 3.4 | Costo (S/1250 vs presupuesto) | 3 | 5 | 60% | S/1250 cotizado, falta justificar vs Jetson Orin Nano | `01_propuesta_preliminar_DE25_Nano.md` |
| **P3** | **Recursos** | **18** | **20** | **90%** | **Bueno** |  |
| 4.1 | Entregables a tiempo | 5 | 5 | 100% | 0/0, proximo EX1 Sem 3 (martes 1 PM) | Art. 32 |
| 4.2 | Formato nombre correcto | 5 | 5 | 100% | Plantillas `Apellido1-Apellido2` anonimizadas | Art. 20-21 |
| 4.3 | Audio/video subido | 5 | 5 | 100% | Enlace TXT (no archivo), no YouTube | Art. 31 |
| 4.4 | Vestimenta | 5 | 5 | 100% | Ropa de vestir (EX1), terno TF1 | Art. 28 |
| **P4** | **Avance** | **20** | **20** | **100%** | **Excelente** |  |
| **TOTAL** |  | **83** | **100** | **83%** | **16.6/20 - BUENO** |  |

## Analisis

**Punto fuerte:** P2 y P4 en 100% - la infraestructura esta solida.
**Punto debil:** P1 en 62% por falta de estado del arte (0 papers, 0 patentes) - es esperado en Semana 01.
**Riesgo:** Si P1 no sube a 35+ antes de EX1 (Semana 3), la nota de EX1 sera baja (Fig 3 3.5 y 3.6 valen 2 puntos cada una).

## Accion prioritaria Semana 02

Para subir de 83 a 96/100 (19.2/20):

| Accion | Sube | Esfuerzo |
|---|---|---|
| Buscar 5 papers SCOPUS/WOS (FPGA Edge AI, quantization, HLS) | P1.4 de 1 a 5 (+4) | 4 horas |
| Buscar 2 patentes Espacenet (FPGA accelerator) | P1.5 de 0 a 5 (+5) | 2 horas |
| Completar borrador EX1 3.5 y 3.6 | P1.3 de 6 a 8 (+2) | 2 horas |
| Justificar S/1250 vs Jetson con tabla | P3.4 de 3 a 5 (+2) | 1 hora |
| **Total** | **+13 pts -> 96/100** | **9 horas** |
