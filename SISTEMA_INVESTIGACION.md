# Sistema de investigacion inteligente en OpenCode

## Que se esta construyendo

Un entorno dentro de esta carpeta para que OpenCode actue como asesor de investigacion, auditor metodologico, lector de papers, gestor de evidencia y constructor de articulos en LaTeX.

No es una aplicacion aparte. Es una configuracion de trabajo sobre OpenCode usando:

- Contexto permanente: `AGENTS.md`.
- Comandos: `opencode.json`.
- Agentes: `.opencode/agent/*.md`.
- Skill local: `.opencode/skills/research-intelligence/SKILL.md`.
- Memoria cientifica: `auditoria_investigacion/*.md`.
- Investigacion externa: `auditoria_investigacion/investigacion_externa/*.md`.
- Perspectivas practicas: `perspectivas_investigadores/*.txt` y `auditoria_investigacion/20_perspectivas_practicas_de_investigadores.md`.
- Curso Proyecto de Investigacion: `curso_proyecto_investigacion/` con syllabus, ejemplos referenciales, extracciones, auditoria y V3 WBAN.
- Produccion futura: `paper_wban/`.

## Capacidades esperadas

| Capacidad | Como se cubre |
| --- | --- |
| Entender el proyecto | Lee `AGENTS.md`, indice maestro, base de conocimiento y registro de afirmaciones |
| Leer articulos con metodo | Usa fichas por paper: problema, metodo, datos, variables, metricas, resultados, limitaciones |
| Razonar como asesor | Usa semaforo verde/amarillo/rojo y checklist anti-exageracion |
| Preguntar bien | Pregunta solo cuando falta una decision que cambia metodologia o alcance |
| Investigar internet | Registra fuentes externas con URL, fecha, utilidad y limitaciones |
| Construir paper | Pasa por plan, matriz de evidencia, borrador, auditoria y LaTeX |
| Usar LaTeX Live | Comando `latex-build` y agente `latex-paper-builder` |
| Mejorar memoria | Nuevas fuentes se agregan a Markdown, no solo al chat |
| Auditar claims | Usa `/paper-audit` para clasificar SUPPORTED/PARTIAL/OVERSTATED/UNSUPPORTED/UNVERIFIED |
| Verificar citas | Usa `/paper-audit` para revisar existencia y alineacion claim-cita |
| Orquestar pipeline | Usa `/research-plan` para etapa actual, gates y readiness |
| Investigar profundo | Usa `/research-plan` o `/ingest-source` con outline, items, fields y reporte |
| Aprender de perspectivas practicas | Usa `perspectivas_investigadores/` como corpus de workflow y `20_perspectivas_practicas_de_investigadores.md` como reglas consolidadas |
| Ingesta multimodal | Usa texto automatico + imagen/OCR selectivo para PDF, PPT/PPTX, imagenes, tablas, figuras y formulas |
| Alinear con curso de investigacion | Usa syllabus y ejemplos EX1/EX2/EX3/TP/TF para convertir ideas tecnicas en proyecto academico evaluable |

## Arquitectura operativa

### 1. Modo asesor

Usar cuando hay que decidir tema, pregunta, alcance, contribucion o metodologia.

Comando recomendado:

`/research-plan <tema o pregunta>`

Salida esperada:

- Pregunta de investigacion delimitada.
- Hipotesis o contribucion tentativa.
- Variables.
- Metricas.
- Fuentes necesarias.
- Riesgos.
- Preguntas reales para el usuario.

### 2. Modo lectura de fuente

Usar cuando entra un paper, blog, GitHub, transcripcion de YouTube, fuente web, PDF, PPT/PPTX, imagen, scan, tabla, figura o formula.

Comando recomendado:

`/ingest-source <ruta o URL + objetivo>`

Salida esperada:

- Ficha de fuente.
- Claims reutilizables.
- Limitaciones.
- Citas o datos relevantes.
- Decision: usar, usar con cuidado, descartar.
- Etiquetas de confianza cuando la fuente sea multimodal: `AUTO_TEXT`, `VISUAL_READ`, `TABLE_VERIFIED`, `FORMULA_VERIFIED`, `FIGURE_INTERPRETED`, `CLAIM_READY` o `PENDING`.

Profundidad recomendada:

- Nivel 0: cribado por titulo, abstract, keywords y fit.
- Nivel 1: abstract, figuras/tablas, conclusion, limitaciones y resumen propio.
- Nivel 2: extraccion estructurada de metodo, datos, variables, metricas, baselines y resultados.
- Nivel 3: reconstruccion profunda para reproduccion, simulacion, comparacion o claim tecnico fuerte.

Para fuentes visuales o semivisuales, usar tambien:

- `auditoria_investigacion/22_pipeline_ingesta_multimodal.md`.
- `auditoria_investigacion/23_protocolo_pdf_ppt_imagenes.md`.

Regla: texto automatico da cobertura; imagen/OCR selectivo da confianza. No usar resultados numericos, formulas, tablas o graficas como claim final sin verificacion visual o locator fuerte.

### 3. Modo construccion de paper

Usar cuando ya hay tema y fuentes suficientes.

Comando recomendado:

`/paper-build <objetivo del paper>`

Salida esperada:

- Outline IEEE/academico.
- Matriz seccion-fuente-claim.
- Borrador progresivo.
- Archivos LaTeX cuando se cree `paper_wban/`.

### 4. Modo auditoria

Usar antes de confiar en el texto.

Comando recomendado:

`/paper-audit <archivo o resumen>`

Salida esperada:

- Frases exageradas.
- Claims sin evidencia.
- Citas faltantes.
- Problemas de metodo.
- Cambios concretos.

### 5. Modo compilacion LaTeX

Usar cuando exista un `.tex`.

Comando recomendado:

`/latex-build <ruta del .tex>`

Salida esperada:

- Comando sugerido o ejecutado.
- Errores de compilacion explicados.
- Fixes minimos.

### 6. Modos internos avanzados

Estos ya no son comandos visibles separados. Se ejecutan dentro de los cinco comandos principales cuando hacen falta.

| Modo interno | Comando que lo cubre |
| --- | --- |
| Readiness / etapa actual | `/research-plan` |
| Pipeline academico con gates | `/research-plan` y `/paper-build` |
| Deep research | `/research-plan` o `/ingest-source` |
| Claim audit | `/paper-audit` |
| Citation check | `/paper-audit` |
| Revision multi-lente tipo referee | `/paper-audit` |
| Alineacion con syllabus/curso | `/research-plan`, `/ingest-source` y `/paper-build` |

### 7. Modo proyecto de investigacion de carrera

Usar cuando el objetivo sea formular un proyecto para el curso EL260 o para una tesis/proyecto de investigacion en ingenieria electronica.

Fuentes base:

- `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md`.
- `curso_proyecto_investigacion/auditoria/02_patrones_ejemplos_referenciales.md`.
- `curso_proyecto_investigacion/v3_wban/WBAN_V3_preliminar_alineado_curso.md`.

Salida esperada:

- Situacion problematica de ingenieria.
- Problema general y pregunta de investigacion.
- Objetivos medibles.
- Estado del arte orientado a brecha.
- Solucion hipotetica y diagrama de bloques.
- Problemas de ingenieria derivados.
- Viabilidad tecnica, economica, social y operativa.
- Entregables por etapa EX1/EX2/EX3/TP/TF.

## Como saber si el sistema entendio

Debe poder producir un `READINESS_REPORT.md` con:

- Tema entendido.
- Fuentes dominantes.
- Fuentes debiles.
- Variables y metricas.
- Metodo recomendado.
- Afirmaciones permitidas.
- Afirmaciones prohibidas.
- Preguntas pendientes.
- Proximo paso accionable.

Si no puede llenar ese reporte, no esta listo.

## Primera prueba: paper WBAN

Ruta recomendada:

1. Crear `paper_wban/READINESS_REPORT.md`.
2. Crear `paper_wban/MATRIZ_EVIDENCIA.md`.
3. Crear `paper_wban/OUTLINE.md`.
4. Crear primer borrador en Markdown.
5. Auditar contra `10_registro_de_afirmaciones.md` y `17_mapa_de_verdad_y_riesgo.md`.
6. Convertir a LaTeX.
7. Compilar con LaTeX Live.

## Herramientas externas candidatas

No instalar sin decision explicita del usuario.

| Herramienta | Uso | Peso/riesgo | Prioridad |
| --- | --- | --- | --- |
| PyMuPDF/PyMuPDF4LLM | Extraccion local rapida de PDFs | Ligero, Python | Alta cuando entren PDFs nuevos |
| Pandoc | Markdown a LaTeX/PDF/Word | Medio, binario externo | Alta para conversion final |
| Zotero/Better BibTeX | Gestion de citas y BibTeX | Medio, app externa | Alta antes del paper final |
| Docling | PDF/PPTX/DOCX a Markdown/JSON con OCR/layout | Pesado, dependencias ML/OCR | Media si PyMuPDF no basta |
| Marker | PDF a Markdown/JSON con formulas/tablas | Pesado, dependencias ML | Media si hay formulas/tablas complejas |
| GROBID | Metadata, referencias y citas de papers | Pesado, Java/servicio local | Media-baja hasta tener muchas referencias |
| BM25 + embeddings | RAG local hibrido con abstencion y locators | Medio-pesado, indice/modelos | Futura, cuando corpus crezca |
| PubMed/arXiv/Semantic Scholar APIs | Busqueda academica verificable | Ligero, APIs/web | Alta sin instalacion fuerte |
| OpenAlex/Crossref | Verificacion legal de metadatos, DOI y referencias | Ligero, APIs/web | Alta sin instalacion fuerte |
| last30days | Investigacion reciente multi-fuente | Depende de instalacion/servicios | Baja para WBAN inmediato |
| LaTeX Live | Compilacion final | Ya instalado | Disponible |

Protocolo oficial de conversion/lectura multimodal: `auditoria_investigacion/22_pipeline_ingesta_multimodal.md` y `auditoria_investigacion/23_protocolo_pdf_ppt_imagenes.md`.

Estado instalado y verificado: `auditoria_investigacion/21_herramientas_instaladas.md`.

## Patrones externos incorporados

| Repo evaluado | Que se incorporo |
| --- | --- |
| Academic Research Skills | Pipeline por etapas, gates de integridad y claim audit |
| Deep-Research-skills | Outline -> items -> fields -> evidence -> report |
| AI-research-feedback | Revision multi-lente con defensor y esceptico |
| Research-Paper-Writing-Skills | Alineacion claim-evidencia en escritura por secciones |
| Medical Research Skills | Protocol design, evidence strength y checklists de rigor |
| ARIS | Plan/draft/adversarial review/iterate/persist |

## Perspectivas practicas incorporadas

| Grupo | Patron incorporado |
| --- | --- |
| Lectura de papers | Proposito de lectura, niveles 0-3, resumen propio de 5-7 frases, tablas/figuras como evidencia densa |
| Escritura de papers | Una idea central, contribuciones refutables, primera pagina clara, related work sin muro |
| Publicacion y peer review | Ficha de venue, anti-desk-reject, cover letter, respuesta punto por punto |
| Figuras y LaTeX | Pasaporte de figura, vectorialidad, legibilidad, paleta limitada, compilacion temprana |
| IA/RAG | IA como apoyo local, no sustituto; RAG con locators, abstencion, BM25 + embeddings |

Ver detalle en `auditoria_investigacion/20_perspectivas_practicas_de_investigadores.md`.

## Politica de fuentes

- Preferir open access, repositorios oficiales, arXiv, PubMed, IEEE cuando haya acceso institucional, GitHub, blogs tecnicos y transcripciones publicas.
- Si el usuario proporciona PDF local, se puede leer/procesar.
- No automatizar descargas no autorizadas.
- Toda cita usada en paper debe terminar en BibTeX o referencia equivalente.
