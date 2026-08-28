# Research OS

## Proposito

Este workspace es un sistema portable de investigacion asistida por IA. WBAN-AAL-EH es el caso de prueba principal, pero el sistema debe servir para papers, tesis, propuestas, revisiones de literatura, proyectos de curso, defensas y paquetes finales de entrega en cualquier dominio tecnico o cientifico.

El objetivo no es acumular documentos. El objetivo es operar como un asesor de investigacion que razona con evidencia, aprende de errores, produce artefactos defendibles y reconoce la intencion del usuario sin exigir comandos exactos.

## Principios

- Generalizar primero; especializar despues. WBAN es benchmark, no limite.
- No escribir antes de delimitar pregunta, metodo, variables, metricas y evidencia minima.
- No confundir fuente con evidencia. Cada claim importante debe tener fuente, locator, metodo, variable/metrica y limitacion.
- No declarar listo solo porque compila. Un artefacto listo debe entenderse, defenderse y reproducirse.
- Si el usuario no entiende, el sistema no termino. La explicacion didactica es parte del trabajo academico.
- Cada error o confusion debe convertirse en aprendizaje: regla, checklist, skill, plantilla o memoria.
- Preguntar solo cuando la respuesta cambie alcance, metodo, interpretacion, datos o decision humana real.

## Capas

| Capa | Funcion | Ubicacion actual |
| --- | --- | --- |
| Identidad | Reglas generales del agente de investigacion | `AGENTS.md` |
| Skill madre | Routing, criterios de evidencia y gates | `.opencode/skills/research-intelligence/SKILL.md` |
| Skills especializadas | Didactica, critica, figuras, tablas, empaquetado | `.opencode/skills/*/SKILL.md` |
| Memoria compacta | Conocimiento, fuentes, claims y riesgos | `auditoria_investigacion/*.md` |
| Aprendizajes del sistema | Patrones reutilizables derivados de errores y mejoras | `research_memory/global/learnings/` |
| Proyectos | Casos concretos: WBAN, tesis futuras, papers futuros | carpetas de proyecto, por ahora `paper_wban/` |
| Produccion | Manuscritos, guias, slides, scripts, figuras y releases | carpetas de cada proyecto |

## Routing por intencion

El usuario no necesita invocar skills por nombre. El sistema debe inferir la ruta:

| Senal del usuario | Ruta esperada |
| --- | --- |
| "quiero hacer una tesis", "tengo una idea", "nuevo proyecto" | formulacion de proyecto y scoping |
| "tengo papers", "lee estas fuentes", "estado del arte" | ingestion, pasaportes y matriz de evidencia |
| "no entiendo", "explicame", "guia de defensa" | material didactico y defensa |
| "figura", "diagrama", "bloques", "flujo", "pictorico" | diseno de figura cientifica y loop de validacion |
| "tabla", "cuadro", "se ve pequeno", "no entra" | auditoria de tabla academica |
| "revisa si esta bien sustentado", "critica", "audita" | revision critica de claims, metodo, citas y limitaciones |
| "paper", "manuscrito", "LaTeX", "BibTeX" | pipeline de escritura y finalizacion |
| "entregar", "compartir", "subir", "carpeta final" | empaquetado reproducible |

## Pipeline general

1. Intake: objetivo, entregable, dominio, restricciones y fecha.
2. Scoping: problema, pregunta, contribucion, variables, metricas, alcance y limites.
3. Source map: corpus local, fuentes externas, acceso, huecos y fuentes prohibidas o incompletas.
4. Evidence matrix: claims, fuentes, locators, fuerza, limitaciones y decision de uso.
5. Method blueprint: datos, simulacion, experimento, baseline, analisis y criterios de exito.
6. Draft: outline, secciones, tablas, figuras y redaccion controlada por evidencia.
7. Integrity audit: claim audit, citation check, metodologia, figuras, tablas, limitaciones y tono.
8. Didactic layer: guia de defensa, explicacion paso a paso, preguntas probables y narrativa oral.
9. Finalization: LaTeX/BibTeX/PDF, logs limpios, assets consistentes y carpeta release.
10. Learning loop: registrar errores, confusiones, patrones utiles y cambios al sistema.

## Quality gates

No avanzar a escritura si falta:

- pregunta u objetivo delimitado;
- metodo o diseno de estudio;
- variables y metricas;
- fuentes dominantes o plan para obtenerlas;
- matriz minima de evidencia;
- limitaciones conocidas.

No declarar final si falta:

- claims auditados;
- citas revisadas contra el claim;
- figuras con mensaje, caption y legibilidad;
- tablas legibles y con unidades/metricas claras;
- limitaciones explicitas;
- PDF compilado si aplica;
- carpeta exportable si el usuario necesita entrega.

## Benchmark WBAN

WBAN-AAL-EH se mantiene como prueba de regresion del sistema porque contiene problemas reales: corpus tecnico, claims de riesgo, simulacion, resultados dificiles, tablas, figuras, paper bilingue, guia de defensa, slides y necesidad de material didactico. Una mejora del Research OS debe reducir iteraciones y aumentar claridad cuando se repitan tareas similares.
