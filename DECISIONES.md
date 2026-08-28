# DECISIONES del proyecto

> **Este archivo es append-only. Nunca se borra ni se edita una decision anterior.**
> Cada decision nueva se agrega al final con fecha, contexto, razon y impacto.
> Esto es como el sistema "nunca olvida" por que se tomo cada decision.

---

## D001 - 2026-08-25 - Usar Research OS de WBAN como base

**Contexto:** El usuario tiene un Research OS probado en WBAN con 8 skills, 7 agentes, pipeline de 10 etapas y quality gates. Quiere reusarlo para una tesis nueva.

**Decision:** Copiar el nucleo dominio-agnostico de WBAN a INVESTIGACION. No copiar la memoria especifica de WBAN (corpus, paper, auditoria).

**Razon:** RESEARCH_OS.md dice literalmente que WBAN es benchmark, no limite. El nucleo (skills, agentes, pipeline, gates) es dominio-agnostico.

**Impacto:** INVESTIGACION hereda toda la capacidad de research sin el peso del corpus WBAN.

---

## D002 - 2026-08-25 - Renzosky en nivel CURSOS, no en INVESTIGACION

**Contexto:** El metodo Renzosky de estudio aplica a multiples cursos (AWS, CISCO, INVESTIGACION, tema de tesis).

**Decision:** Instalar la skill renzosky-study-method y opencode.json en CURSOS/ (nivel superior), no dentro de cada curso.

**Razon:** Renzosky es un metodo de estudio transversal, no especifico de investigacion. Si vive en CURSOS/, todos los cursos lo heredan.

**Impacto:** /renzosky-generar y /renzosky-ensenar funcionan en cualquier subcarpeta de CURSOS/.

---

## D003 - 2026-08-25 - Copiar perspectivas_investigadores a INVESTIGACION

**Contexto:** Las 28 transcripciones de investigadores estaban en WBAN. El usuario pidio copiarlas a INVESTIGACION.

**Decision:** Copiar toda la carpeta perspectivas_investigadores/ a INVESTIGACION/. Actualizar AGENTS.md para referenciarlas como memoria local, no externa.

**Razon:** Son workflow de investigacion aplicable a cualquier tesis, no especificas de WBAN. Tenerlas locales evita dependencia cruzada.

**Impacto:** Las perspectivas son ahora capa 5 de memoria en AGENTS.md.

---

## D004 - 2026-08-26 - Separar propuestas de tema_tesis

**Contexto:** El scoping inicial estaba dentro de tema_tesis/. Pero las propuestas son previas a tener un tema elegido.

**Decision:** Crear carpeta propuestas/ separada de tema_tesis/. Mover SCOPING_INICIAL.md a propuestas/. tema_tesis/ queda para el desarrollo del tema ya elegido.

**Razon:** Fases distintas: primero se generan y comparan propuestas (propuestas/), despues se desarrolla la elegida (tema_tesis/). Mezclarlas confunde el estado.

**Impacto:** Estructura mas clara: propuestas/ = antes de elegir, tema_tesis/ = despues de elegir.

---

## D005 - 2026-08-26 - Crear ESTADO.md como single source of truth

**Contexto:** El sistema necesita "nunca olvidar nada" entre sesiones. Sin un archivo de estado, cada sesion arranca de cero.

**Decision:** Crear ESTADO.md que se lee primero en cada sesion y se actualiza al final. Contiene: fase actual, que esta hecho, que falta, proximo paso, memoria rapida, riesgos.

**Razon:** Un solo archivo que refleja el estado completo del proyecto es mas confiable que reconstruir desde multiples archivos cada vez.

**Impacto:** Cada sesion arranca leyendo ESTADO.md. Cualquier agente nuevo entiende el proyecto en 1 lectura.

---

## D006 - 2026-08-26 - Crear DECISIONES.md como log append-only

**Contexto:** Las decisiones se pierden entre sesiones si no se registran. El usuario puede no recordar por que se eligio algo.

**Decision:** Crear DECISIONES.md append-only. Cada decision tiene fecha, contexto, decision, razon, impacto. Nunca se editan entradas pasadas.

**Razon:** El racional de las decisiones es tan importante como las decisiones mismas. Si algo se cuestiona despues, se puede revisar por que se tomo.

**Impacto:** Trazabilidad completa de decisiones. El sistema puede explicar cualquier eleccion.

---

## D007 - 2026-08-26 - Crear FLUJO_SESION.md como protocolo obligatorio

**Contexto:** El usuario quiere un flujo claro cada vez que escribe. Que el sistema lea contexto de forma consistente.

**Decision:** Crear FLUJO_SESION.md que define exactamente que se lee al inicio, durante y al final de cada sesion.

**Razon:** Sin protocolo, cada sesion puede leer contexto distinto y producir resultados inconsistentes.

**Impacto:** Toda sesion sigue el mismo protocolo. El sistema es predecible.

---

## D008 - 2026-08-26 - Propuestas autocontenidas (eliminar tema_tesis/)

**Contexto:** La estructura original tenia `tema_tesis/` separado de `propuestas/`. El usuario considero que esto desordenaba: cada propuesta deberia tener toda su estructura de desarrollo dentro.

**Decision:** Eliminar `tema_tesis/`. Crear 5 carpetas de propuestas autocontenidas dentro de `propuestas/`. Cada una con: `propuesta_NN.md` + `00_RAW/` + `renzosky/` + `estado_del_arte/` + `fichas_papers/` + `matriz_evidencia/` + `entregables/(EX1-EX2-TP1-EX3-DD1-TF1)`.

**Razon:** Cada propuesta es un proyecto potencial completo. Al tener toda la estructura dentro, cuando se elija una propuesta, esa carpeta ya tiene todo listo para desarrollarse sin mover archivos. Es mas ordenado y menos propenso a errores.

**Impacto:** Estructura mas clara. Cada propuesta es autocontenida. Al elegir una, se trabaja dentro de su carpeta. Actualizado ESTADO.md, AGENTS.md, FLUJO_SESION.md y README de propuestas.

---

## D009 - 2026-08-26 - Crear 28 agentes investigadores con pipeline de revision

**Contexto:** El usuario pidio que cada uno de los 28 investigadores de las transcripciones sea un agente con su perfil, capacidad de leer cualquier archivo del proyecto, y que al terminar un entregable se seleccione solo 5 (los mas afines) para revisar y corregir.

**Decision:**
1. Crear 28 agentes en `.opencode/agent/investigadores/` (inv_01 a inv_28), cada uno con su perfil, acceso a cualquier archivo, y formato de revision estructurado.
2. Crear `PERFILES_INVESTIGADORES.md` como archivo maestro con los 28 perfiles completos.
3. Crear `SELECCION_INVESTIGADORES.md` con mapa de seleccion de 5 agentes por tipo de entregable/seccion.
4. Crear `FLUJO_REVISION.md` con el pipeline: entregable → 5 agentes en paralelo → consolidacion → correccion → REVISION_REPORTE.md.
5. Crear comando `/revision-investigadores` en opencode.json.
6. No se crea otro documento del entregable. Se mejora el existente.

**Razon:** Cada investigador tiene una perspectiva unica. Al tenerlos como agentes individuales con acceso libre al proyecto, evitan sesgarse. El agente principal no se satura porque delega la revision a 5 agentes en paralelo via task tool. Solo recibe las revisiones consolidadas y aplica correcciones.

**Impacto:** Pipeline de revision completo. 28 agentes disponibles, 5 seleccionados por afinidad. Comando `/revision-investigadores` activa el flujo. REVISION_REPORTE.md queda como trazabilidad de cada revision.

---

## D010 - 2026-08-26 - Crear agente 29 Dr. Ernesto Ibarra

**Contexto:** El Dr. Ernesto Ibarra fue el investigador principal del proyecto WBAN. Su metodologia (PEH-QoS, PHAM, DQAC, PASS) estructuro todo el sistema. El usuario pidio un agente 29 que represente fielmente su forma de trabajar, con detalle profundo extraido de toda la carpeta WBAN.

**Decision:**
1. Crear `PERFIL_IBARRA_COMPLETO.md` en perspectivas_investigadores/ con perfil completo: identidad, trayectoria, 4 lineas, metodologia detallada (PEH-QoS, HEH-BMAC, simulacion, prototipado low-cost, validacion, FEA, etc.), filosofia, 15 papers con DOI y resultados, claims verdes/amarillos/rojos, 19 patrones, como influencia el pipeline, como presentarle propuestas, afinidad Edge AI/FPGA.
2. Crear agente `inv_29_ernesto_ibarra.md` en .opencode/agent/investigadores/ que referencia el perfil completo.
3. Actualizar SELECCION_INVESTIGADORES.md: Ibarra entra en propuesta de tesis, TP1, EX3, DD1, TF1, y en todas las secciones especificas (introduccion, estado del arte, metodologia, resultados, figuras, conclusiones, LaTeX). Reemplaza a agentes menos especificos en cada seleccion (mantiene 5 por seleccion).
4. No resumir ni sesgar: el perfil preserva la profundidad extraida de 3 exploraciones paralelas de WBAN.

**Razon:** Ibarra es el investigador mas valioso porque tenemos muchisima documentacion suya y literalmente todo lo que se hizo para los papers WBAN fue por su perspectiva. Su metodologia de baseline obligatorio, no sobreclaiming, metricas concretas, limitaciones honestas, costo como variable, modularidad, y ruta incremental aplica directamente a Edge AI/FPGA.

**Impacto:** 29 agentes investigadores total. Ibarra aparece en casi todas las selecciones de 5. Es el agente con afinidad Edge AI/FPGA mas alta. Su perfil completo preserva 15 papers, definiciones operativas de PHAM/DQAC/PASS, claims auditados, y patrones extraidos.

---

## D011 - 2026-08-26 - Copiar protocolos de ingesta de WBAN

**Contexto:** Los protocolos 21 (herramientas instaladas), 22 (pipeline ingesta multimodal) y 23 (PDF/PPT/imagenes) son dominio-agnosticos pero estaban solo en WBAN. Se necesitan locales en INVESTIGACION.

**Decision:** Copiar los 3 protocolos a `INVESTIGACION/curso_proyecto_investigacion/auditoria/`. Crear `24_flujo_ingesta_a_markdown.md` que explica el flujo completo: PPT/PDF → extraccion automatica → slides criticas a imagen → lectura visual → ficha .md → ESTADO.md actualizado → ficha usada en entregables → reglas a research_memory.

**Razon:** El sistema de INVESTIGACION necesita los protocolos locales para no depender de WBAN externamente. El flujo 24 explica como la informacion extraida via imagenes vuelve a los markdowns y actualiza el contexto: es hibrido (automatico para texto/imagen, manual para interpretacion/ficha/estado), y la conexion entre sesiones es via ESTADO.md.

**Impacto:** INVESTIGACION tiene ahora sus propios protocolos de ingesta (21-24). El flujo queda claro: extraccion automatica + lectura visual selectiva → ficha .md → ESTADO.md → entregables.

---

## D012 - 2026-08-26 - Copiar scripts Python de WBAN a INVESTIGACION

**Contexto:** Los protocolos 21-23 estaban copiados pero los scripts Python que los implementaban no. Hay 3 scripts dominio-agnosticos en WBAN.

**Decision:** Copiar a `INVESTIGACION/herramientas/`:
1. `render_pdf_pages.py` — renderiza paginas PDF a PNG con PyMuPDF.
2. `extract_pdf_text_manifest.py` — extrae texto de PDFs recursivamente + manifest CSV.
3. `extract_pdfs_ibarra.py` (renombrado de extract_pdfs.py) — extrae texto + markdown con PyMuPDF + pymupdf4llm + MANIFEST_EXTRACCIONES.md.
4. No copiar scripts de simulacion WBAN (simulador_energia_qos.py, etc.) — son especificos de WBAN.
5. Actualizar protocolo 21 con los scripts locales y sus comandos de uso.

**Razon:** Los scripts son la implementacion de los protocolos 22-23. Sin ellos, los protocolos son teoria sin ejecucion. Los 3 son dominio-agnosticos: trabajan con cualquier PDF/PPT.

**Impacto:** INVESTIGACION tiene ahora sus scripts locales de extraccion. Protocolo 21 actualizado con comandos concretos.

---

## D013 - 2026-08-26 - Crear sistema LaTeX para PDF y Word

**Contexto:** El curso 1AEL0260 requiere entregables en PDF (formato formal) o Word. Ya teniamos LaTeX Live y Pandoc verificados pero no habia plantillas ni protocolo de uso en INVESTIGACION.

**Decision:**
1. Crear `latex/PROTOCOLO_LATEX.md` con 3 flujos: markdown→PDF via LaTeX, markdown→Word via Pandoc, markdown→PDF directo.
2. Crear 3 plantillas en `latex/plantillas/`:
   - `entregable_upc.tex` — generica para cualquier entregable.
   - `tesis_upc.tex` — completa para TF1 (40%) con todas las secciones del syllabus.
   - `slides_defensa.tex` — Beamer para diapositivas de defensa oral (DD1 y exposiciones).
3. Crear `latex/proyecto/` y `latex/proyecto/figuras/` para los .tex activos.
4. Mapear cada entregable a formato: EX1/EX2 → Word, TP1/TF1 → PDF (LaTeX), DD1 → PDF + slides.
5. Usar `/latex-build` ya configurado en opencode.json para compilar.

**Razon:** El curso exige Word/PowerPoint en PDF. LaTeX es estandar para tesis formales. Pandoc cubre Word. Las plantillas evitan empezar de cero cada vez.

**Impacto:** INVESTIGACION tiene sistema LaTeX completo. 3 plantillas listas. Protocolo define cuando PDF vs Word. Comando `/latex-build` compila.

---

## D014 - 2026-08-26 - Crear indice maestro de auditoria

**Contexto:** Cada vez que se agrega un protocolo, script o herramienta nueva, debe quedar documentada y conectada para que cualquier sesion sepa que existe y donde esta.

**Decision:** Crear `auditoria/00_indice_maestro_auditoria.md` que indexa:
- Los 6 protocolos (01, 21, 22, 23, 24, 25) con que define cada uno y que scripts/plantillas lo implementan.
- Los 3 scripts Python disponibles con su ruta, comango de uso y protocolo que lo define.
- Las 3 plantillas LaTeX con su ruta y protocolo.
- Las 5 herramientas externas con version y protocolo.
- Regla de actualizacion: cada nuevo avance se appenda al indice + ESTADO.md + DECISIONES.md.

**Razon:** Sin un indice maestro, los protocolos se acumulan sin que las sesions futuras sepan que existen. El indice es el puente entre `auditoria/` y `ESTADO.md`/`DECISIONES.md`.

**Impacto:** Cualquier sesion que lee `auditoria/00_indice_maestro_auditoria.md` sabe exactamente que hay, donde esta, y que protocolo/script/plantilla lo conecta. Todo queda trazable.

---

## D015 - 2026-08-26 - Protocolo de transcripcion de audio

**Contexto:** El usuario tiene un audio de la clase del curso que necesita transcribir para usar como material bruto. Ya teniamos `faster-whisper 1.2.1` y `ffmpeg 9.0` instalados pero sin script ni protocolo en INVESTIGACION.

**Decision:**
1. Crear `herramientas/transcribir_audio.py` que genera 3 archivos desde audio: .md (con timestamps y metadata), .json (datos estructurados), .txt (texto plano para Renzosky).
2. Crear `auditoria/26_protocolo_transcripcion_audio.md` con pipeline, comandos, modelos, y limitaciones.
3. Agregar al indice maestro (script + herramienta + protocolo).

**Razon:** Sin un protocolo de transcripcion, el usuario tendria que improvisar cada vez que quiera pasar audio a texto. El script genera 3 formatos: .md para academico, .json para programatico, .txt para Renzosky.

**Impacto:** La pipeline completa queda: audio → transcribir_audio.py → .md/.json/.txt → ficha Renzosky → ESTADO.md → entregables. Todo documentado en auditoria/26.

---

## D016 - 2026-08-26 - Protocolo de gestion bibliografica con Zotero

**Contexto:** Zotero esta instalado pero no tiene protocolo dedicado. Better BibTeX no esta instalado. Sin un protocolo de bibliografia, las referencias se gestionan manualmente sin trazabilidad.

**Decision:**
1. Crear `auditoria/27_protocolo_zotero.md` con pipeline: paper → Zotero → Better BibTeX → references.bib → LaTeX.
2. Incluir comandos de uso, estructura de colecciones, tags, y flujo completo con el sistema.
3. Documentar Better BibTeX como pendiente de instalar.
4. Cross-links con todos los demas protocolos.

**Razon:** Zotero es la herramienta de referencia para bibliografia. Sin protocolo, el usuario no sabe como conectar Zotero con LaTeX. El .bib es el puente entre Zotero y \bibliography{references}.

**Impacto:** Pipeline de bibliografia completa. Cuando se instale Better BibTeX, el flujo será: paper → Zotero → .bib → LaTeX → PDF con referencias.

---

## D017 - 2026-08-26 - Cross-links entre protocolos

**Contexto:** Los protocolos 21-27 existen pero no se referencian entre si. Un protocolo nuevo no sabe que los otros existen ni como se conectan.

**Decision:** Agregar seccion "Cross-links" al final de cada protocolo (21-27) con tabla que muestra la relacion con los demas protocolos, scripts, y herramientas.

**Razon:** Sin cross-links, cada protocolo es una isla. Con cross-links, el sistema es una red: si necesito extraer texto de un PDF de Zotero, se que debo usar 21 (herramientas) + 23 (PDF/PPT) + 27 (Zotero) + 24 (ingesta a markdown).

**Impacto:** Los 7 protocolos ahora son una red conectada. Cada uno sabe que los otros existen y como se relacionan. La navigation entre protocolos es fluida.

---

## D018 - 2026-08-26 - Estructura de carpetas para documentos

**Contexto:** El usuario pregunta donde poner documentos oficiales del curso, documentos del estado del arte, y fuentes de internet (papers, videos, blogs, etc.).

**Decision:** Crear 3 niveles de carpetas:

1. **Documentos oficiales del curso** → `curso_proyecto_investigacion/fuentes_originales/`
   - Ya tiene el syllabus. Aqui van: reglamento, programa anual, audio de clases, material del profesor.

2. **Estado del arte (compartido entre propuestas)** → `curso_proyecto_investigacion/estado_del_arte/`
   - Subcarpetas: `papers/`, `tesis/`, `conferencias/`
   - Aqui van los papers y documentos que se usan para construir el estado del arte.
   - Las propuestas individuales tienen su propio `fichas_papers/` para fichas de lectura.

3. **Fuentes de investigacion (general)** → `fuentes_investigacion/`
   - Subcarpetas: `papers/`, `videos/`, `blogs/`, `revistas/`, `productos_similares/`, `antecedentes/`
   - Aqui van todas las fuentes encontradas en internet durante la investigacion.
   - `manifest_fuentes.md` es la lista maestra de todas las fuentes.
   - Las fuentes compartidas entre propuestas van aqui. Las especificas van en `propuestas/XX/fichas_papers/`.

**Razon:** Sin esta estructura, los documentos se mezclan y no se sabe que es oficial del curso, que es estado del arte, y que es fuente de internet. La separacion permite: (1) saber que es confiable (oficial del curso), (2) saber que ya se reviso (estado del arte), (3) saber que fuentes hay disponibles (manifest).

**Impacto:** Estructura clara de 3 niveles. Cada tipo de documento tiene su lugar. El manifest conecta todas las fuentes.

---

## D019 - 2026-08-26 - Mapa de organizacion y revision general

**Contexto:** El usuario pide una revision general para verificar que no hay repeticiones y que quede claro donde va cada archivo.

**Revision realizada:**
1. Revisar todas las carpetas de INVESTIGACION/ (13 directorios, 8 protocolos, 4 scripts, 3 plantillas LaTeX, 29 agentes).
2. Detectar duplicacion en ESTADO.md (lineas 75-76 y 92-93 eran identicas) → eliminada.
3. Clarificar distinciones:
   - `fuentes_originales/` = documentos oficiales del curso (del profesor).
   - `fuentes_investigacion/` = fuentes encontradas en internet (por leer).
   - `estado_del_arte/` = papers leidos y fichados (compartidos entre propuestas).
   - `propuestas/XX/fichas_papers/` = papers especificos de una propuesta.
   - `propuestas/XX/codigo/` = codigo futuro de cada propuesta (no creado aun).
4. No se encontraron repeticiones de archivos reales (carpetas vacias verificadas).
5. Crear `MAPA_ORGANIZACION.md` como documento maestro de referencia.

**Decision:** Crear `MAPA_ORGANIZACION.md` en el raiz de INVESTIGACION/ con:
- Estructura general del proyecto.
- Donde va cada tipo de archivo (oficial, estado del arte, fuentes, codigo, etc.).
- Estructura futura de carpetas con codigo.
- Donde busco yo cuando el usuario escribe.
- Repeticiones detectadas y resueltas.
- Regla de oro para guardar archivos.

**Razon:** Sin un mapa claro, los archivos se mezclan. El mapa es la referencia definitiva: si no sabes donde guardar algo, mira aqui.

**Impacto:** Organizacion validada, sin repeticiones, con mapa maestro. El sistema esta listo para recibir documentos reales.

---

## D020 - 2026-08-26 - Informacion oficial de grupos del curso

**Contexto:** El usuario pasa la lista oficial de los 18 grupos de investigacion del curso 1AEL0260 (NRC 6140). El usuario esta en el Grupo 15.

**Decision:**
1. Guardar en `fuentes_originales/02_grupos_investigacion_1AEL0260.md` — es informacion oficial del curso.
2. Actualizar ESTADO.md con datos del grupo (Grupo 15, miembros, carrera).
3. El archivo incluye: todos los 18 grupos, distribucion por carrera, y notas importantes.

**Razon:** La informacion de grupos es oficial del curso (viene del profesor). Va en `fuentes_originales/`. Conecta con ESTADO.md para que cualquier sesion sepa en que grupo estamos y con quien trabajamos.

**Impacto:** ESTADO.md ahora dice "Grupo 15, Lozano Durand + Reymundo Ramos, Ing. Electronica". Cualquier sesion futura sabe esto al leer ESTADO.md.

---

## D021 - 2026-08-26 - Ingesta reglamento Titulo I (caracteristicas)

**Contexto:** El usuario pasa el reglamento general del curso (26 paginas). Se decide dividir por TITULOS para evitar markdowns gigantes. El usuario enfatiza: NO RESUMIR, cada falta es menos nota.

**Decision:**
1. Dividir el reglamento por TITULOS, un archivo .md por titulo.
2. Numeracion: `03_reglamento_tituloI_caracteristicas.md`, `04_reglamento_tituloII_...md`, etc.
3. Preservar texto literal de cada articulo.
4. Extraer reglas criticas al final de cada titulo (tabla R1, R2, ... con articulo e impacto).
5. Mapear areas relevantes para nuestro proyecto al final.

**Razon:** 26 paginas en un solo markdown es inmanejable. Dividir por titulos permite buscar reglas especificas rapidamente. Preservar texto literal es obligatorio porque es documento oficial.

**Impacto:** Titulo I ingestado con 9 reglas criticas extraidas (R1-R9). Areas relevantes para FPGA Edge AI identificadas: Sistemas Embebidos, Circuitos Digitales, PDS/Imagenes. Pendiente: Titulo II en adelante.

---

## D022 - 2026-08-26 - Ingesta reglamento Titulo II (desarrollo del proyecto)

**Contexto:** El usuario pasa el Titulo II del reglamento (Art. 7-15). Incluye reglas criticas sobre trabajo en equipo, asistencia, actas de asesoria, portafolio digital, carta de patrocinador, y prohibicion de copia.

**Decision:**
1. Guardar en `fuentes_originales/04_reglamento_tituloII_desarrollo.md` - texto literal sin resumir.
2. Preservar formato de acta de reunion (Figura 1) y modelo de carta de patrocinador (Figura 2).
3. Extraer 27 reglas criticas (R10-R36) con articulo e impacto.
4. Crear tabla operativa de actas requeridas por entregable.
5. Crear plan de actas para el Grupo 15.
6. Actualizar ESTADO.md con columna "Actas min" en tabla de entregables.

**Reglas mas criticas del Titulo II:**
- R23: TF1 requiere 8 actas (7 con evaluador + 2 con otros). Si no se tienen, penalizacion.
- R30: Copiar del internet = sancion muy severa.
- R18: El profesor solo firma el acta el mismo dia. No despues.
- R19: Asesoria virtual debe enviarse por email el mismo dia.
- R36: Si el proyecto es poco ingenieril, priorizar aporte al estado del arte.

**Razon:** El Titulo II contiene las reglas operativas del curso. Las actas de asesoria son obligatorias y acumulativas. Sin ellas, hay penalizacion directa en cada evaluacion. La tabla de actas por entregable es la guia operativa mas importante del semestre.

**Impacto:** ESTADO.md ahora muestra actas minimas por entregable. Plan de actas creado para Grupo 15. 27 reglas criticas adicionales (R10-R36). Pendiente: Titulo III en adelante.

---

## D023 - 2026-08-26 - Ingesta reglamento Titulo III (funciones de los profesores)

**Contexto:** El usuario pasa el Titulo III del reglamento (Art. 16-19). Define el rol del profesor, duracion maxima de asesorias (15 min), autoridad para aceptar proyectos, y que el evaluador revisa items + exposicion + diapositivas + informes.

**Decision:**
1. Guardar en `fuentes_originales/05_reglamento_tituloIII_profesores.md` - texto literal sin resumir.
2. Extraer 8 reglas criticas (R37-R44).
3. Crear estrategia de asesoria para Grupo 15: antes, durante, despues.
4. Destacar que el criterio del profesor es final (no apelar a externos).

**Reglas mas criticas del Titulo III:**
- R39: Asesoria maximo 15 minutos. Hay que preparar preguntas antes.
- R44: El evaluador revisa items + exposicion + diapositivas + informes. Nada es opcional.
- R43: Los profesores resuelven lo no contemplado en el reglamento. Su criterio es final.

**Razon:** El Titulo III define quien tiene autoridad y cuanto tiempo tenemos. 15 minutos por asesoria significa que hay que ir preparado con preguntas concretas y avance tangible.

**Impacto:** Estrategia de asesoria creada. 8 reglas criticas adicionales (R37-R44). Total acumulado: 44 reglas. Pendiente: Titulo IV en adelante.

---

## D024 - 2026-08-26 - Ingesta reglamento Titulo IV (entregables)

**Contexto:** El usuario pasa el Titulo IV del reglamento (Art. 20-21). Define los entregables exactos de cada evaluacion (EX1, EX2, EX3, TP1, TF1) y el formato EXACTO de nombres de archivo.

**Decision:**
1. Guardar en `fuentes_originales/06_reglamento_tituloIV_entregables.md` - texto literal sin resumir.
2. Preservar Tabla 1 (EX1, EX2, EX3) y Tabla 2 (TP1, TF1) completas.
3. Extraer 10 reglas criticas (R45-R54).
4. Generar plantilla de nombres para Grupo 15: `EX1-PPT-PI-6140-2026-2-Lozano-Reymundo.{ppt,pdf}` etc.
5. Crear checklist de produccion por entregable conectando con protocolo LaTeX 25.
6. Notar que DD1 no aparece en las tablas del reglamento - verificar con syllabus o profesor.

**Reglas mas criticas del Titulo IV:**
- R51: El nombre del archivo debe seguir el formato EXACTO. Nombre incorrecto = menos nota.
- R46-R50: Cada evaluacion tiene entre 5 y 6 entregables. Cualquiera faltante = menos nota.
- R52: EX1 usa video; EX2/EX3/TP1/TF1 usan audio + exposicion. No mezclar.
- R53: El audio se graba DESPUES de la exposicion, no antes.

**Razon:** Los nombres de archivo son lo mas facil de sacar mal y lo mas facil de penalizar. Tener la plantilla con los nombres exactos para Grupo 15 evita errores tontos.

**Impacto:** Plantilla de nombres lista para Grupo 15. Checklist de produccion conecta con LaTeX. 10 reglas criticas adicionales (R45-R54). Total acumulado: 54 reglas. Pendiente: Titulo V en adelante.

---

## D025 - 2026-08-26 - Ingesta reglamento Titulo V (evaluacion del curso)

**Contexto:** El usuario pasa el Titulo V del reglamento (Art. 22-32). Es el titulo mas critico: define la formula de nota, las rubricas de evaluacion (Fig 3-10), el cronograma, los tiempos, el codigo de vestimenta, y las penalizaciones.

**Decision:**
1. Guardar en `fuentes_originales/07_reglamento_tituloV_evaluacion.md` - texto literal sin resumir.
2. Preservar las 7 fichas de evaluacion (Fig 3-9) y la ficha de informe (Fig 10) completas.
3. Extraer 30 reglas criticas (R55-R84).
4. Crear resumen operativo: criterios por entregable, estructura de computo, codigo de vestimenta, tiempos.
5. Detectar discrepancia: syllabus decia EX2=sem 6, EX3=sem 13; reglamento dice EX2=sem 5-6, EX3=sem 12-13. Usar reglamento como autoridad.
6. Actualizar ESTADO.md con semanas corregidas, tiempos y vestimenta.

**Reglas mas criticas del Titulo V:**
- R55: TF1 vale 40% - es lo mas importante del semestre.
- R62: Inasistencia = nota cero. No recuperable.
- R63: Todas las evaluaciones son NO recuperables.
- R66: Escritura en modo impersonal obligatorio.
- R68: Impuntualidad o sobrepasar tiempo = hasta -3 puntos.
- R70: TF1 requiere terno (varones) / cocktail (damas).
- R81: Todas las exposiciones deben grabarse en audio.
- R84: Entregables deben subirse dentro del plazo.

**Criterios clave para cada entregable:**
- EX1: proponer tema (max 3), importancia, solucion, viabilidad, antecedentes.
- EX2: titulo definido, problema, causas/consecuencias, solucion, antecedentes.
- TP1: conceptos teoricos, arbol de problema, sector/area/usuarios, estado del arte Scopus/WOS, 3 articulos con limitaciones.
- EX3: arbol de objetivos, solucion/diagrama, metodos/algoritmos, variables/metricas/validacion, estado del arte Scopus/WOS.
- TF1: todo lo de EX3 + objetivos/alcances/limitaciones + Gantt + viabilidad.

**Razon:** El Titulo V es la guia definitiva de como se evalua todo. Sin esto, no se puede priorizar el trabajo. TF1 vale 40% y requiere terno - no se puede improvisar.

**Impacto:** ESTADO.md actualizado con semanas, tiempos, vestimenta. 30 reglas criticas adicionales (R55-R84). Total acumulado: 84 reglas. Pendiente: Titulo VI en adelante.

---

## D026 - 2026-08-26 - Ingesta reglamento Titulo VI (penalizaciones) - REGLAMENTO COMPLETO

**Contexto:** El usuario pasa el Titulo VI del reglamento (Art. 33-36), el ultimo titulo. Define penalizaciones, amonestacion institucional, y el protocolo de reclamos.

**Decision:**
1. Guardar en `fuentes_originales/08_reglamento_tituloVI_penalizaciones.md` - texto literal sin resumir.
2. Extraer 9 reglas criticas (R85-R93).
3. Crear protocolo de reclamo (email, max 5 lineas, antes del registro de notas).
4. Consolidar lista completa de motivos de penalizacion de TODO el reglamento en una tabla.
5. Marcar el reglamento como COMPLETO en ESTADO.md.

**Reglas mas criticas del Titulo VI:**
- R88: Reclamos SOLO por escrito y via email. Verbales = no validos.
- R89: Reclamo debe hacerse ANTES del registro de notas. Despues = no valido.
- R90: Reclamo maximo 5 lineas. Mas largo = rechazado.
- R87: Faltas muy graves = amonestacion institucional.
- R93: Resultados se entregan antes del registro (ventana para reclamar).

**REGLAMENTO COMPLETO:**
- 6 titulos (I-VI)
- 36 articulos (1-36)
- 93 reglas criticas (R1-R93)
- 10 figuras (1-10)
- 4 tablas (1-4)

**Razon:** El reglamento esta completo. Ahora cualquier sesion puede consultar las 93 reglas para verificar que no se incumpla ninguna. El protocolo de reclamo asegura que si algun dia hay que reclamar una nota, se haga correctamente.

**Impacto:** Reglamento 100% ingestado. 93 reglas criticas extraidas. Protocolo de reclamo creado. Lista consolidada de penalizaciones disponible. El sistema tiene ahora la verdad oficial completa del curso.

---

## D027 - 2026-08-26 - Ingesta PNCTI 2006-2021

**Contexto:** El usuario pasa el Plan Nacional Estrategico de Ciencia, Tecnologia e Innovacion para la Competitividad y el Desarrollo Humano 2006-2021 (PNCTI), referenciado en el Art. 5 del reglamento. Documento de CONCYTEC, 2278 lineas, decreto supremo 001-2006-ED.

**Decision:**
1. Guardar en `fuentes_originales/09_PNCTI_2006_2021.md` - es documento oficial referenciado por el reglamento.
2. Preservar texto literal de las secciones clave: principios rectores, criterios, sectores productivos, sectores sociales, areas del conocimiento, vision, objetivos, metas, programas.
3. Identificar sectores y areas relevantes para nuestro proyecto FPGA Edge AI:
   - Sector productivo #6: Telecomunicaciones (ALTA relevancia)
   - Area de conocimiento #3: TIC (ALTA relevancia)
   - Area de conocimiento #2: Ciencia y Tecnologia de Materiales (MEDIA)
   - Area de conocimiento #5: Ciencias Basicas (MEDIA)
4. Extraer 3 citas clave del PNCTI para usar en los entregables (EX1, EX2, TP1, EX3, TF1).
5. Crear guia de como usar el PNCTI en cada entregable.

**Razon:** El Art. 5 del reglamento establece que los proyectos deben alinearse con los sectores prioritarios del PNCTI. Las rubricas de EX3 y TF1 (puntos 3.2) piden explicitamente "identificar correctamente el sector productivo, area de conocimiento y usuarios potenciales." Sin el PNCTI ingestado, no se puede justificar esta alineacion.

**Impacto:** El proyecto puede ahora justificar su alineacion con:
- Sector productivo prioritario: Telecomunicaciones
- Area de conocimiento: TIC
- Cita del Gartner Group sobre tecnologias estrategicas (infraestructura en tiempo real, dispositivos moviles de bajo costo)
- Cita sobre el doble rol de las TIC (soporte transversal + capacidad tecnologica propia)
3 citas listas para usar en entregables.

---

## D028 - 2026-08-26 - Ficha de acta de asesoria creada

**Contexto:** El usuario pide crear un documento con la ficha de acta de reunion en fuentes_originales. El formato esta en el Art. 10 del reglamento (Figura 1).

**Decision:**
1. Guardar en `fuentes_originales/10_ficha_acta_asesoria.md`.
2. Incluir plantilla oficial (Figura 1) en formato rellenable.
3. Prellenar datos del Grupo 15 (Lozano Durand + Reymundo Ramos).
4. Incluir reglas de valides del acta (R16-R25).
5. Crear plan de actas estimado para todo el semestre (10 actas).
6. Crear checklist antes y despues de cada asesoria.
7. Incluir formato para asesoria virtual (email).

**Razon:** El acta es el documento mas frecuente del semestre. Sin una plantilla lista y un plan de actas, el grupo puede perder puntos por no acumular las actas minimas en cada evaluacion. Tener el checklist asegura que no se olvide escanear, nombrar y subir el acta el mismo dia.

**Impacto:** Plantilla de acta lista para usar. Plan de 10 actas para el semestre. Checklist operativo antes/despues de cada asesoria. Formato de nombre de archivo con ejemplos concretos para Grupo 15.

---

## D029 - 2026-08-26 - Transcripcion y analisis de clase Dia 1 (2h20m)

**Contexto:** El usuario pasa el audio de la primera clase (Prof. Del Carpio, 25 de agosto, 2h20m). Es el documento mas rico en informacion practica porque contiene aclaraciones que no estan en el reglamento escrito.

**Decision:**
1. Transcribir con faster-whisper medium (es, 3513 segmentos, prob 1.0, ~96k chars).
2. Guardar en `fuentes_originales/transcripciones/` con 3 archivos: .md (con tabla de timestamps), .json (3513 segmentos estructurados), .txt (texto plano para Renzosky).
3. Crear `FICHA_CLASE_DIA1_2026-08-25.md` con 7 secciones tematicas + 22 reglas nuevas (R94-R115).
4. Corregir cronograma con info del audio: TF1 en semana 16, Practica 3 en 12-13, Practica 2 en 5-6, EX1 en 3.
5. Registrar detalles operativos: deadline martes 1 PM, portafolio OneDrive, licencias MTC para drones, permisos para leche materna.

**Reglas nuevas mas criticas (R94-R115):**
- R98: Video EX1 como enlace en TXT, no archivo .mp4 (penalidad).
- R99: No usar YouTube (confidencialidad para patente).
- R100: 20 min a 1x, no 2x (penalidad por 1 segundo).
- R107: Si no apruebas en Practica 3, jalas (no hay siguiente oportunidad).
- R111: DPEI 25% faltas = no rindes TF1 = max 12.
- R112: Lista al inicio + verificacion en asesoria (no te puedes ir).

**Razon:** El audio contiene matices que el reglamento escrito no tiene. Sin esta ficha, el grupo perderia informacion operativa critica (deadlines, formato de video, licencias, etc.).

**Impacto:** 22 reglas nuevas (R94-R115). Total acumulado: 115 reglas (R1-R115). Ficha de 7 secciones tematicas disponible para consultar antes de cada evaluacion. Texto plano disponible como material bruto para Renzosky si aplica.

---

## D030 - 2026-08-26 - Plantillas PPT e Informe EX1 documentadas

**Contexto:** El usuario pasa las 2 plantillas oficiales de EX1: PPT (11 slides) e Informe (6 secciones + Referencias). Son oficiales del aula virtual 6140. Solo en EX1 se permiten maximo 2 propuestas.

**Decision:**
1. Guardar `11_plantilla_PPT_EX1.md` con los 11 slides completos, texto literal, notas marginales, y reglas operativas.
2. Guardar `12_plantilla_informe_EX1.md` con las 6 secciones completas + Referencias, formato IEEE.
3. Documentar que todo lo azul se borra, que si no hay segunda propuesta se elimina Slide 3, y que las tablas/figuras deben estar enumeradas.
4. Generar nombres exactos para Grupo 15 para cada entregable.
5. Conectar con: Ficha de clase Dia 1 (donde se explico la plantilla), Reglamento Titulo IV (nombres de archivos), Reglamento Titulo V (rubricas), y silabo.

**Reglas criticas de las plantillas:**
- Todo lo azul = instrucciones, se borra.
- Si no hay segunda propuesta, eliminar Slide 3 (no dejarla vacia).
- PPT: 11 slides fijos; Informe: 6 secciones fijas.
- Productos: minimo 3; Publicaciones: 5.
- Tablas/figuras enumeradas con referencia si no son propias.
- No respetar la plantilla = penalidad.
- Informe: descripcion en el parrafo antes de cada tabla ("En la Tabla X, ...").

**Razon:** Sin estas plantillas documentadas, el grupo no sabe que estructura seguir para EX1. Son el contrato de evaluacion de la primera nota (10%).

**Impacto:** Plantillas EX1 documentadas completas. Estructura de 11 slides y 6 secciones lista para usar. Reglas operativas conectadas con el audio de la clase y el reglamento.

---

## D031 - 2026-08-26 - Ejemplos referenciales EX1 documentados (PPT e Informe)

**Contexto:** El usuario pasa los 2 ejemplos referenciales del ciclo pasado para EX1: PPT (20 slides) e Informe (Word), ambos del mismo proyecto (maquina automatica PET, Ing. Mecatronica, Arias+Cristobal, abril 2026, evaluado por Del Carpio).

**Advertencia del profesor:** "No es el mejor mejor trabajo pero es uno de los mas buenos que me toco asesorar. Pero no que sea siempre al pie de la letra porque tuvo sus errores tambn"

**Decision:**
1. Guardar `13_ejemplo_referencial_PPT_EX1.md` con los 20 slides completos, texto literal, observaciones y errores detectados.
2. Guardar `14_ejemplo_referencial_informe_EX1.md` con las secciones disponibles del informe (4.3-6 + Referencias), observaciones y lecciones para Grupo 15.
3. Documentar diferencias entre PPT e Informe: PPT repite tabla por producto/articulo; Informe tiene tabla unica con todas las filas.
4. Detectar y documentar errores del ejemplo: viabilidad tecnica/operativa intercambiadas, 18 meses en vez de 8, y formato IEEE con pequenos descuidos.

**Lecciones para Grupo 15 (FPGA Edge AI):**
- Productos: buscar 4 con foto, fabricante, costo, funcion, ventajas, desventajas (ej. aceleradores FPGA, DE10-Nano, Jetson Nano, Coral Edge TPU).
- Publicaciones: 5 articulos con fortalezas, debilidades, y contribucion del proyecto (ej. papers sobre FPGA + Edge AI, quantization, HLS).
- Tablas enumeradas y descritas en el texto.
- Apuntar a superar este nivel corrigiendo los errores.

**Razon:** El ejemplo muestra la brecha entre la plantilla (que es el contrato) y el informe real (que es la ejecucion). Sin ver un ejemplo, el grupo no sabe que tan detallado debe ser cada seccion ni que errores evitar.

**Impacto:** Ejemplos EX1 documentados completos. 5 errores detectados y documentados. Diferencias PPT vs Informe aclaradas. Lecciones para Grupo 15 listas para aplicar en EX1 (semana 3).

---

## D032 - 2026-08-27 - Unidad 1 completa documentada (4 archivos)

**Contexto:** El usuario pasa todos los documentos de la Unidad 1: introduccion, fundamentos de investigacion cientifica, normas IEEE, busqueda SCOPUS, busqueda WOS, ZOTERO, situacion problematica, y patentes. Son 7 documentos oficiales que definen el estado del arte y la formulacion de la tesis.

**Decision:**
1. Crear carpeta `fuentes_originales/unidad1/` con 4 archivos organizados:
   - `01_introduccion_fundamentos.md` - Intro + tipos de investigacion + flujo del proyecto
   - `02_normas_IEEE.md` - Norma IEEE completa (cita en texto + formatos por tipo de fuente)
   - `03_SCOPUS_WOS_ZOTERO_patentes.md` - Las 4 herramientas para estado del arte (SCOPUS + WOS + ZOTERO + patentes)
   - `05_situacion_problematica.md` - Titulo de tesis (formula 1+2+3+4) + situacion problematica + arbol del problema + requerimientos + problemas de ingenieria
   - `00_indice.md` - Indice de la unidad
2. El archivo `05_situacion_problematica.md` es el mas critico: define la formula del titulo (Aporte+Problema+Tecnica+Escenario) y la estructura completa de la situacion problematica con 6 sub-secciones.

**Puntos mas criticos de la Unidad 1:**
- EX1 necesita: 3 productos + 5 publicaciones (SCOPUS/WOS) + patentes + formato IEEE.
- Titulo de tesis: APORTE (obligatorio) + PROBLEMA (obligatorio) + TECNICA (opcional) + ESCENARIO (opcional).
- Situacion problematica: 6 partes (conceptos introductorios, descripcion + problema general, causas, consecuencias, enunciado + arbol, requerimientos, problemas de ingenieria).
- ZOTERO: 1 click para guardar referencias desde Scopus/WOS.

**Razon:** La Unidad 1 es la base metodologica del curso. Sin estos documentos, el grupo no sabe como buscar informacion ni como formular el titulo y la situacion problematica de la tesis.

**Impacto:** Unidad 1 documentada completa. Formula del titulo lista para aplicar a las 5 propuestas. Estructura de situacion problematica con 6 sub-secciones disponible. Flujo de estado del arte (SCOPUS/WOS -> ZOTERO -> IEEE) documentado.

---

## D033 - 2026-08-27 - Research OS subido a GitHub (sin descartar nada)

**Contexto:** El usuario pide subir todo el sistema Research OS a https://github.com/Reznouw/research-os actualizado y sin descartar nada, para que sirva a otros companeros.

**Decision:**
1. Inicializar git en INVESTIGACION/ (134 archivos, 74,559 lineas).
2. Crear .gitignore que solo excluye node_modules (3667 archivos) y temporales LaTeX.
3. Todo lo demas se sube: 14 documentos en fuentes_originales/, 4 en unidad1/, transcripciones con ficha, 7 protocolos, 29 agentes, 5 propuestas, herramientas, latex, etc.
4. Remote: origin = https://github.com/Reznouw/research-os.git
5. Push inicial a master (134 archivos), luego merge con main (scaffold inicial 325c085) usando --allow-unrelated-histories, resolviendo conflictos tomando la version completa.
6. Push final a main: 140 archivos totales, rama principal actualizada.

**Razon:** El usuario quiere que el sistema este disponible para companeros. No se descarta nada: cada documento oficial, cada plantilla, cada ejemplo y cada protocolo queda versionado.

**Impacto:** Repo actualizado en https://github.com/Reznouw/research-os (branch main, historial limpio sin datos personales).

---

## D034 - 2026-08-27 - Remover propuestas privadas y datos personales del repo publico

**Contexto (parte 1 - propuestas):** El usuario revisa GitHub y ve que las 5 carpetas de propuestas estan publicas. Teme que le roben las ideas.

**Contexto (parte 2 - datos personales):** El usuario pide quitar quien es su equipo y los demas equipos (nombres personales, correos, codigos UPC) del repo publico. El archivo `02_grupos_investigacion_1AEL0260.md` contiene 38 nombres + 38 emails de los 18 equipos. Ademas, `ESTADO.md` y plantillas contienen nombres del Grupo 15.

**Contexto:** El usuario revisa GitHub y ve que las 5 carpetas de propuestas (propuesta_01 a 05) estan publicas. Teme que le roben las ideas de investigacion.

**Decision:**
1. Agregar `propuestas/` a `.gitignore` con comentario "Propuestas privadas - NO subir a GitHub".
2. `git rm -r --cached propuestas/` (elimina del tracking sin borrar local).
3. Commit y push normal a main (commit 63272c5).
4. Reescribir historial con `git filter-branch --index-filter` para borrar propostas de TODOS los commits anteriores.
5. `git gc --prune=now` para limpiar backups en refs/original.
6. Force push a main y master (commits reescritos 0ae3059, 8d520cb).
7. Verificar: `git log --all -- propuestas/` vacio y `git ls-tree origin/main` sin propostas.

**Razon:** Las propuestas son propiedad intelectual privada. No deben estar en un repo publico. El .gitignore previene futuros pushes accidentales. El filter-branch borra el historial para que nadie pueda recuperarlas via commits antiguos.

**Impacto (parte 1):** Propuestas 100% eliminadas de GitHub (historial y HEAD). Siguen intactas en local (6 archivos en propuestas/). Repo publico ahora solo tiene el sistema Research OS sin ideas privadas.

**Decision (parte 2 - datos personales):**
1. Agregar `02_grupos_investigacion_1AEL0260.md` a `.gitignore` (con `**/02_grupos*` para asegurar).
2. Anonimizar `ESTADO.md` (Grupo 15: Lozano/Reymundo -> [privado - ver copia local]).
3. Anonimizar `10_ficha_acta_asesoria.md` (nombres -> [Apellido, Nombre]).
4. Anonimizar `11_plantilla_PPT_EX1.md`, `12_plantilla_informe_EX1.md`, `06_reglamento_tituloIV_entregables.md` (Lozano-Reymundo -> Apellido1-Apellido2).
5. `git rm --cached` del archivo de grupos + `git add` de los anonimizados + commit.
6. Crear historial limpio con `git checkout --orphan clean-main` (133 archivos, sin grupos ni propuestas) y `git commit --amend` para quitar el grupos del commit.
7. Force push a main y master (0960637).

**Impacto (parte 2):** 38 nombres + 38 emails de los 18 equipos eliminados del historial de GitHub. Estado del grupo anonimizado en remoto. Local sigue intacto (grupos y propuestas solo ignorados en git).

---

## D035 - 2026-08-28 - Documentar propuesta 01 completa (5 docs de otra IA + asesoria Kalun)

**Contexto:** El usuario trae 5 documentos generados con otra IA sobre la propuesta 01 (Edge AI FPGA DE25-Nano): propuesta preliminar (17 secc), dossier estado del arte (17 secc, 9 refs), definicion del problema (4 caminos), plan de viabilidad 12 meses (30 secc), y 6 puntos de asesoria con Prof. Kalun (unico con DE25-Nano, experto PIC18).

**Decision:**
1. Crear `propuestas/propuesta_01_edge_ai_fpga_reconfigurable/documentacion_inicial/` con 5 archivos + README indice.
2. Ubicacion elegida: dentro de `propuesta_01/` porque es especifica de esa propuesta, en `documentacion_inicial/` para distinguir de `00_RAW` (material bruto) y `estado_del_arte` (fichas). Esta carpeta es PRIVADA (`.gitignore: propuestas/`).
3. No se sube a GitHub - queda solo local.
4. Orden de lectura: 01_propuesta -> 03_problema -> 02_dossier -> 04_viabilidad -> 05_Kalun.

**Puntos criticos de la asesoria Kalun:**
- Problematica es lo mas importante (80% vision computacional, 18% IoT, 2% FPGA en la universidad - seriamos los unicos en FPGA).
- DE25-Nano: nadie tiene estado del arte especifico, el profesor solo prendio un led, tiene Linux en HPS.
- Viabilidad economica: comparar contra Jetson Orin Nano y contra tesis/paper anterior.
- Necesita asesores externos y estar mas enamorado de la problematica.

**Razon:** El usuario dice "donde la colocaras" y "todavia hay que colocar lo que he investigado" - estos 5 docs son la base para que luego analicemos y definamos el camino A/B/C/D con el asesor.

**Impacto:** Propuesta 01 tiene ahora 5 docs preliminares (42 KB) + README. Pendiente: analizar con el asesor, elegir camino, definir contexto/modelos/metrica, e investigar estado del arte especifico de DE25-Nano.

---

## D036 - 2026-08-28 - Transcripcion de 3 conferencias y creacion de 3 agentes

**Contexto:** El usuario trae 3 audios de conferencias relevantes para la propuesta 01: Yongfu Li (LLM datasets, 29min), Victor Grimblatt (semiconductores LATAM, 48min), Melvin Acuna (arquitectura reconfigurable, 44min). Pide que sirvan como documentacion para la propuesta y como voces para nuevos agentes investigadores.

**Decision:**
1. Transcribir los 3 audios con faster-whisper medium (Yongfu Li en `en`, los otros 2 en `es`): 2390 segmentos totales (406+1178+806), guardados en `propuestas/propuesta_01/.../conferencias/transcripciones/` con .md/.json/.txt.
2. Crear 3 fichas en `conferencias/`: FICHA_Yongfu_Li_LLM.md, FICHA_Grimblatt_Semiconductores.md, FICHA_Acuna_Reconfigurable.md.
3. Ubicacion elegida: dentro de `propuesta_01/documentacion_inicial/conferencias/` porque son especificas de esa propuesta y son PRIVADAS (`.gitignore: propuestas/`). No se suben a GitHub.
4. Crear 3 agentes investigadores: inv_30_Yongfu_Li (green computing, low-power, SoC/NoC, EDA), inv_31_Victor_Grimblatt (semiconductores, LATAM, negocio, viabilidad economica), inv_32_Melvin_Acuna (arquitectura reconfigurable en microprocesadores). Total: 32 agentes (29+3).
5. Agentes en `.opencode/agent/investigadores/` (PUBLICO, si va a GitHub) porque son voces publicas de conferencistas, no ideas privadas de la propuesta. Enriquecen el sistema para todos los companeros.
6. Cada agente con su expertise y formato de revision especifico, referenciando su transcripcion y ficha.

**Razon:** Las 3 conferencias cubren los 3 pilares de la propuesta: Yongfu Li = eficiencia energetica y LLM (justifica no hacer LLM grande, foco en eficiencia), Grimblatt = contexto industrial LATAM (justificacion, sector, patrocinador), Acuna = arquitectura reconfigurable (nucleo tecnico). Como documentacion privada informan la propuesta; como agentes publicos mejoran el Research OS.

**Impacto:** 3 conferencias transcritas (2390 segmentos) y fichadas. 3 agentes creados (total 32). Transcripciones y fichas quedan locales (privadas). Agentes quedan publicos en GitHub para que todos los companeros los usen en revisiones.
