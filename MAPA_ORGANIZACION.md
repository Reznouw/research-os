# Mapa de organizacion del proyecto

> **Donde va cada cosa.** Este archivo es la referencia definitiva.
> Si no sabes donde guardar un archivo, mira aqui.
> Si algo esta en el lugar equivocado, moverlo aqui.

---

## Estructura general

```
INVESTIGACION/
├── curso_proyecto_investigacion/     ← Todo lo oficial del curso
│   ├── fuentes_originales/          ← Documentos DEL PROFESOR / DEL CURSO
│   ├── estado_del_arte/             ← Papers compartidos entre propuestas
│   └── auditoria/                   ← Protocolos y reglas del sistema (21-27)
│
├── propuestas/                      ← 5 carpetas autocontenidas
│   ├── propuesta_01_.../            ← Cada una tiene su propio mundo
│   └── ...
│
├── fuentes_investigacion/           ← Fuentes encontradas en internet
│
├── herramientas/                    ← Scripts Python
├── latex/                           ← Sistema LaTeX
├── perspectivas_investigadores/     ← 28 perfiles de investigadores
├── research_memory/                 ← Aprendizajes globales
└── .opencode/                       ← Agentes y configuracion
```

---

## Donde va cada tipo de archivo

### DOCUMENTOS OFICIALES DEL CURSO

**Donde:** `curso_proyecto_investigacion/fuentes_originales/`

| Tipo de archivo | Ejemplo | Donde va |
|---|---|---|
| Syllabus | `01_silabus_1AEL0260_2026.md` | `fuentes_originales/` |
| Reglamento | `reglamento_curso.pdf` | `fuentes_originales/` |
| Programa anual | `programa_2026.pdf` | `fuentes_originales/` |
| Audio de clase | `audio_clase_semana1.mp3` | `fuentes_originales/` |
| Material del profesor | `guia_formulacion.pdf` | `fuentes_originales/` |
| Rubricas | `rubrica_EX1.docx` | `fuentes_originales/` |
| Grupos de investigacion | `02_grupos_investigacion_1AEL0260.md` | `fuentes_originales/` |
| Reglamento - Titulo I | `03_reglamento_tituloI_caracteristicas.md` | `fuentes_originales/` |
| Reglamento - Titulo II | `04_reglamento_tituloII_desarrollo.md` | `fuentes_originales/` |
| Reglamento - Titulo III | `05_reglamento_tituloIII_profesores.md` | `fuentes_originales/` |
| Reglamento - Titulo IV | `06_reglamento_tituloIV_entregables.md` | `fuentes_originales/` |
| Reglamento - Titulo V | `07_reglamento_tituloV_evaluacion.md` | `fuentes_originales/` |
| Reglamento - Titulo VI | `08_reglamento_tituloVI_penalizaciones.md` | `fuentes_originales/` |
| PNCTI 2006-2021 | `09_PNCTI_2006_2021.md` | `fuentes_originales/` |
| Ficha de acta de asesoria | `10_ficha_acta_asesoria.md` | `fuentes_originales/` |
| Transcripcion audio Dia 1 | `transcripciones/Grabadora - 20260825-1414.m4a_transcripcion.md` | `fuentes_originales/transcripciones/` |
| Ficha de clase Dia 1 | `transcripciones/FICHA_CLASE_DIA1_2026-08-25.md` | `fuentes_originales/transcripciones/` |
| Plantilla PPT EX1 | `11_plantilla_PPT_EX1.md` | `fuentes_originales/` |
| Plantilla Informe EX1 | `12_plantilla_informe_EX1.md` | `fuentes_originales/` |
| Ejemplo referencial PPT EX1 | `13_ejemplo_referencial_PPT_EX1.md` | `fuentes_originales/` |
| Ejemplo referencial Informe EX1 | `14_ejemplo_referencial_informe_EX1.md` | `fuentes_originales/` |
| Unidad 1 - Indice | `unidad1/00_indice.md` | `fuentes_originales/unidad1/` |
| Unidad 1 - Introduccion | `unidad1/01_introduccion_fundamentos.md` | `fuentes_originales/unidad1/` |
| Unidad 1 - Normas IEEE | `unidad1/02_normas_IEEE.md` | `fuentes_originales/unidad1/` |
| Unidad 1 - SCOPUS/WOS/ZOTERO/Patentes | `unidad1/03_SCOPUS_WOS_ZOTERO_patentes.md` | `fuentes_originales/unidad1/` |
| Unidad 1 - Situacion Problematica | `unidad1/05_situacion_problematica.md` | `fuentes_originales/unidad1/` |
| Reglamento | **COMPLETO** - 6 titulos, 36 articulos, 93 reglas | `fuentes_originales/` |

**Regla:** Si viene del profesor o del curso, va aqui. Estos archivos son "verdad oficial".

---

### ESTADO DEL ARTE (papers compartidos)

**Donde:** `curso_proyecto_investigacion/estado_del_arte/`

| Tipo de archivo | Ejemplo | Donde va |
|---|---|---|
| Paper revisado | `ibarra_2024_edge_fpga.pdf` | `estado_del_arte/papers/` |
| Tesis previa | `tesis_upc_fpga_2023.pdf` | `estado_del_arte/tesis/` |
| Conferencia | `conf_icassp_2024.pdf` | `estado_del_arte/conferencias/` |

**Regla:** Papers que sustentan el estado del arte general del tema. Son compartidos entre las 5 propuestas. Solo van aqui los que ya fueron leidos y fichados.

---

### FUENTES DE INVESTIGACION (encontradas en internet)

**Donde:** `fuentes_investigacion/`

| Tipo de archivo | Ejemplo | Donde va |
|---|---|---|
| Paper encontrado | `wang_2023_quantization.pdf` | `fuentes_investigacion/papers/` |
| Video de YouTube | `conferencia_fpga_edge_ai.mp4` | `fuentes_investigacion/videos/` |
| Blog tecnico | `tutorial_quintuplets_fpga.html` | `fuentes_investigacion/blogs/` |
| Articulo de revista | `ieee_spectrum_fpga_2024.pdf` | `fuentes_investigacion/revistas/` |
| Producto similar | `DE25-Nano_datasheet.pdf` | `fuentes_investigacion/productos_similares/` |
| Antecedente | `tesis_upc_2023_fpga.pdf` | `fuentes_investigacion/antecedentes/` |

**Regla:** Todo lo que encuentres en internet va aqui primero. Despues de leerlo y evaluarlo, decides si va a `estado_del_arte/` (compartido) o a `propuestas/XX/fichas_papers/` (especifico).

**Manifest:** `fuentes_investigacion/manifest_fuentes.md` es la lista maestra de TODAS las fuentes.

---

### PROPSUESTAS (carpetas autocontenidas)

**Donde:** `propuestas/propuesta_XX_NOMBRE/`

| Subcarpeta | Que tiene | Cuando se usa |
|---|---|---|
| `00_RAW/` | Material bruto original (PDFs, PPT, textos sin procesar) | Al inicio, cuando se ingesta material |
| `renzosky/` | Fichas Renzosky generadas desde material bruto | Despues de procesar con /renzosky-generar |
| `estado_del_arte/` | Fichas de papers ESPECIFICOS de esta propuesta | Cuando un paper solo aplica a esta propuesta |
| `fichas_papers/` | Fichas de lectura de papers | Despues de leer un paper y crear su ficha |
| `matriz_evidencia/` | Tabla de evidencia de la propuesta | Cuando se evalua la propuesta |
| `entregables/` | Carpetas EX1, EX2, TP1, EX3, DD1, TF1 | Donde se escriben los entregables finales |

**Regla:** Cada propuesta es un mundo propio. Los papers especificos de una propuesta van en su `fichas_papers/` o `estado_del_arte/`. Los compartidos van en `curso_proyecto_investigacion/estado_del_arte/`.

---

### CODIGOS Y SCRIPTS DE PROPSUESTAS (futuro)

**Donde:** `propuestas/propuesta_XX_NOMBRE/codigo/`

| Tipo de codigo | Ejemplo | Donde va |
|---|---|---|
| Codigo HLS (C++) | `alu_fixedpoint.cpp` | `propuesta_XX/codigo/hls/` |
| Scripts Python (simulacion) | `simulacion_latencia.py` | `propuesta_XX/codigo/simulacion/` |
| Scripts Python (evaluacion) | `eval_modelo.py` | `propuesta_XX/codigo/evaluacion/` |
| Makefiles | `Makefile` | `propuesta_XX/codigo/` |
| Archivos de configuracion | `synthesis.tcl` | `propuesta_XX/codigo/` |
| Resultados de simulacion | `resultados_latencia.csv` | `propuesta_XX/codigo/resultados/` |
| Documentacion del codigo | `README.md` | `propuesta_XX/codigo/` |

**Regla:** El codigo de cada propuesta va dentro de su carpeta. Nunca en el raiz de INVESTIGACION. Si el codigo es compartido entre propuestas, va en `herramientas/` o se crea una carpeta comun.

**Estructura futura de una propuesta con codigo:**
```
propuestas/propuesta_01_edge_ai_fpga_reconfigurable/
├── 00_RAW/
├── renzosky/
├── estado_del_arte/
├── fichas_papers/
├── matriz_evidencia/
├── codigo/                         ← NUEVO: codigo de esta propuesta
│   ├── hls/                        ← Codigo HLS (C++)
│   ├── simulacion/                 ← Scripts de simulacion (Python)
│   ├── evaluacion/                  ← Scripts de evaluacion (Python)
│   ├── resultados/                  ← CSV, logs, graficos de simulacion
│   ├── synthesis.tcl               ← Scripts de sintesis FPGA
│   ├── Makefile                     ← Build system
│   └── README.md                    ← Documentacion del codigo
└── entregables/
    ├── EX1/
    ├── EX2/
    ├── TP1/
    ├── EX3/
    ├── DD1/
    └── TF1/
```

---

### HERRAMIENTAS COMPARTIDAS

**Donde:** `herramientas/`

| Script | Que hace | Protocolo |
|---|---|---|
| `extract_pdfs_ibarra.py` | Extrae texto + markdown de PDFs | 21, 23 |
| `extract_pdf_text_manifest.py` | Extrae texto recursivo + manifest | 21, 22 |
| `render_pdf_pages.py` | Renderiza paginas PDF a PNG | 21, 22, 23 |
| `transcribir_audio.py` | Transcribe audio a texto | 26 |

**Regla:** Scripts compartidos entre multiples carpetas van aqui. Scripts especificos de una propuesta van en `propuestas/XX/codigo/`.

---

### PROTOCOLOS Y REGLAS

**Donde:** `curso_proyecto_investigacion/auditoria/`

| Protocolo | Que define |
|---|---|
| `00_indice_maestro_auditoria.md` | Indice que conecta todo |
| `01_silabus_como_regla.md` | Reglas del curso extraidas del syllabus |
| `21_herramientas_instaladas.md` | Herramientas instaladas y scripts |
| `22_pipeline_ingesta_multimodal.md` | Pipeline de ingesta textual vs visual |
| `23_protocolo_pdf_ppt_imagenes.md` | Flujos para PDF, PPT, imagenes |
| `24_flujo_ingesta_a_markdown.md` | Como llega info a los markdowns |
| `25_protocolo_latex.md` | Produccion PDF/Word |
| `26_protocolo_transcripcion_audio.md` | Transcripcion de audio |
| `27_protocolo_zotero.md` | Gestion bibliografica |

---

### AGENTES INVESTIGADORES

**Donde:** `.opencode/agent/investigadores/`

| Contenido | Donde |
|---|---|
| 29 agentes (inv_01 a inv_29) | `.opencode/agent/investigadores/` |
| Perfiles de los 28 | `perspectivas_investigadores/PERFILES_INVESTIGADORES.md` |
| Perfil de Ibarra | `perspectivas_investigadores/PERFIL_IBARRA_COMPLETO.md` |
| Mapa de seleccion | `perspectivas_investigadores/SELECCION_INVESTIGADORES.md` |
| Flujo de revision | `FLUJO_REVISION.md` |

---

### SISTEMA DE MEMORIA

**Donde:** `research_memory/`

| Contenido | Donde |
|---|---|
| Aprendizajes globales | `research_memory/global/learnings/` |

**Regla:** Aprendizajes que aplican a CUALQUIER proyecto. No a datos especificos de una propuesta.

---

## Flujo de documentos

```
DOCUMENTO NUEVO ENTRA
    ↓
¿De donde viene?
├── Del profesor/curso → fuentes_originales/
├── De internet → fuentes_investigacion/ + manifest_fuentes.md
└── Del usuario → 00_RAW/ de la propuesta
    ↓
¿Es general o especifico de una propuesta?
├── General → curso_proyecto_investigacion/estado_del_arte/
└── Especifico → propuestas/XX/estado_del_arte/ o fichas_papers/
    ↓
¿Hay codigo?
├── Si → propuestas/XX/codigo/
└── No → solo ficha .md
    ↓
Actualizar ESTADO.md + DECISIONES.md
```

---

## Donde busco yo cuando me escribes

| Que me dices | Donde miro primero |
|---|---|
| "el reglamento dice que..." | `curso_proyecto_investigacion/fuentes_originales/` |
| "el paper de Ibarra dice que..." | `propuestas/XX/fichas_papers/` o `curso_proyecto_investigacion/estado_del_arte/` |
| "en el audio de la clase..." | `curso_proyecto_investigacion/fuentes_originales/` (audio) + transcripcion en `herramientas/` |
| "en el PPT del profesor..." | `propuestas/XX/00_RAW/` (original) + `renzosky/` (fichas) |
| "necesito compilar a PDF" | `latex/` + protocolo 25 |
| "revisa el entregable" | `propuestas/XX/entregables/XX/` + protocolos de revision |
| "que herramientas tenemos" | `auditoria/21_herramientas_instaladas.md` |
| "que protocolo uso para..." | `auditoria/00_indice_maestro_auditoria.md` |
| "que fuentes tenemos" | `fuentes_investigacion/manifest_fuentes.md` |
| "agrega el codigo de..." | `propuestas/XX/codigo/` (futuro) |

---

## Repeticiones detectadas y resueltas

| Repeticion | Problema | Solucion |
|---|---|---|
| `estado_del_arte/` compartido vs propuesta | Podria confundir | Clarificado: compartido = general, propuesta = especifico |
| `fuentes_investigacion/papers/` vs `estado_del_arte/papers/` | Podria parecer duplicado | Clarificado: fuentes = por leer, estado_del_arte = leidos y fichados |
| ESTADO.md lineas Ibarra duplicadas | Dos entradas iguales | Eliminada la duplicacion |
| `research_memory/` vs `auditoria/` | Podria parecer solapado | Clarificado: research_memory = aprendizajes globales, auditoria = protocolos operativos |

---

## Regla de oro

**Si no sabes donde guardar algo, pregunta. Pero la guia rapida es:**

- ¿Viene del profesor? → `fuentes_originales/`
- ¿Lo encontraste en internet? → `fuentes_investigacion/`
- ¿Es un paper leido y fichado? → `estado_del_arte/` o `propuestas/XX/fichas_papers/`
- ¿Es codigo de una propuesta? → `propuestas/XX/codigo/`
- ¿Es un script que usan varias propuestas? → `herramientas/`
- ¿Es una regla o protocolo? → `auditoria/`
- ¿Es un aprendizaje general? → `research_memory/`
