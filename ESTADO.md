# ESTADO del proyecto

> **Este archivo es el primer archivo que se lee en cada sesion y el ultimo que se actualiza.**
> Si este archivo dice algo, es la verdad del proyecto. Todo lo demas se lee segun indica aqui.

## Ultima actualizacion

Fecha: 2026-08-26
Sesion: Inicial (configuracion del sistema)

## Datos del curso

| Campo | Valor |
|---|---|
| Curso | Proyecto de Investigacion |
| Codigo | 1AEL0260 |
| Periodo | UG-2do Semestre 2026 Pregrado |
| Universidad | UPC |
| Carreras | Ingenieria Biomedica, Electronica, Mecatronica |
| Creditos | 3 |
| Semanas | 16 |
| NRC | 6140 |
| Cuerpo academico | Del Carpio Damian, Salvador Castaneda, Mayor Sanchez, Becerra Felipe |
| Formula evaluacion | NF = 0.1*EX1 + 0.1*EX2 + 0.15*TP1 + 0.15*EX3 + 0.1*DD1 + 0.4*TF1 |

## Datos del grupo

| Campo | Valor |
|---|---|
| Grupo | 15 |
| Miembro 1 | [privado - ver copia local] |
| Miembro 2 | [privado - ver copia local] |
| Carrera | Ing. Electronica |
| Proyectos | De a 2, cada uno hace su propio proyecto de tesis |
| Fuente | `fuentes_originales/02_grupos_investigacion_1AEL0260.md` (solo local, no en GitHub por privacidad) |

## Entregables y fechas

| Entregable | Semana | Peso | Estado | Carpeta | Actas min | Tiempo exposicion | Vestimenta |
|---|---|---|---|---|---|---|---|
| EX1 | 3 | 10% | No iniciado | propuestas/[propuesta_elegida]/entregables/EX1/ | - | 20 min | Ropa de vestir |
| EX2 | 5-6 | 10% | No iniciado | propuestas/[propuesta_elegida]/entregables/EX2/ | 1 acta | 20+10 min | Ropa de vestir |
| TP1 | 8 | 15% | No iniciado | propuestas/[propuesta_elegida]/entregables/TP1/ | 3 actas | 20 min | Ropa de vestir |
| EX3 | 12-13 | 15% | No iniciado | propuestas/[propuesta_elegida]/entregables/EX3/ | 6 actas (5+1) | 25+10 min | Ropa de vestir |
| DD1 | 14 | 10% | No iniciado | propuestas/[propuesta_elegida]/entregables/DD1/ | - | Individual | Ropa de vestir |
| TF1 | 16 | 40% | No iniciado | propuestas/[propuesta_elegida]/entregables/TF1/ | 8 actas (7+2) | 25 min | Terno/Cocktail |

## Fase actual

**Fase: PREPARACION DE PROPUESTAS**

El usuario tiene 1 semana para conseguir al menos 5 propuestas de tema de tesis (similares o diferentes). Hay 5 carpetas de propuestas creadas, cada una autocontenida con su estructura completa (00_RAW, renzosky, estado_del_arte, fichas_papers, matriz_evidencia, entregables). 4 propuestas tienen borrador, 1 esta pendiente.

## Propuestas actuales

| # | Carpeta | Tema | Estado |
|---|---|---|---|
| 01 | propuesta_01_edge_ai_fpga_reconfigurable | Arquitectura reconfigurable para inferencia Edge AI (FPGA DE25-Nano, co-diseno) | Borrador |
| 02 | propuesta_02_hls_fpga_de10nano | Aceleracion NN cuantizadas FPGA DE10-Nano con HLS | Borrador |
| 03 | propuesta_03_finn_hls4ml_tinyml | Frameworks FINN/hls4ml para TinyML sobre FPGA vs MCU | Borrador |
| 04 | propuesta_04_quantization_pruning_fpga | Pipeline quantization+pruning para Edge AI sobre FPGA | Borrador |
| 05 | propuesta_05_pendiente | Por definir | Pendiente |

## Que esta hecho

- [x] Research OS instalado (skills, agentes, opencode.json)
- [x] AGENTS.md adaptado (identidad Edge AI FPGA, no WBAN)
- [x] RESEARCH_OS.md copiado (pipeline dominio-agnostico)
- [x] SISTEMA_INVESTIGACION.md copiado
- [x] research_memory/global/learnings/ copiado
- [x] Syllabus 1AEL0260 ingestado en curso_proyecto_investigacion/
- [x] Reglas extraidas en auditoria/01_silabus_como_regla.md
- [x] Perspectivas de investigadores copiadas (28 transcripciones)
- [x] Scoping inicial dividido en 5 carpetas de propuestas autocontenidas
- [x] Cada propuesta con estructura: 00_RAW, renzosky, estado_del_arte, fichas_papers, matriz_evidencia, entregables (EX1-EX2-TP1-EX3-DD1-TF1)
- [x] Renzosky instalado en CURSOS/ (nivel superior, compartido)
- [x] AWS UNIDAD_01 y UNIDAD_02 procesadas con Renzosky
- [x] FLUJO_SESION.md creado (protocolo de sesion)
- [x] DECISIONES.md creado (log de decisiones)
- [x] Estructura de carpetas definida
- [x] 5 propuestas autocontenidas creadas (cada una con 00_RAW, renzosky, estado_del_arte, fichas_papers, matriz_evidencia, entregables EX1-EX2-TP1-EX3-DD1-TF1)
- [x] 28 agentes investigadores creados en .opencode/agent/investigadores/
- [x] PERFILES_INVESTIGADORES.md creado (perfiles completos de los 28)
- [x] SELECCION_INVESTIGADORES.md creado (mapa de seleccion de 5 por tipo de entregable)
- [x] FLUJO_REVISION.md creado (pipeline de revision)
- [x] Comando /revision-investigadores creado en opencode.json
- [x] Agente 29 Dr. Ernesto Ibarra creado (el mas valioso, perfil completo en PERFIL_IBARRA_COMPLETO.md)
- [x] SELECCION_INVESTIGADORES.md actualizado con Ibarra en propuestas, TP1, EX3, DD1, TF1 y secciones especificas
- [x] Protocolos 21 (herramientas), 22 (pipeline multimodal), 23 (PDF/PPT/imagenes) copiados de WBAN a INVESTIGACION/curso_proyecto_investigacion/auditoria/
- [x] Flujo de ingesta a markdown (24_flujo_ingesta_a_markdown.md) creado
- [x] 3 scripts Python copiados a INVESTIGACION/herramientas/ (render_pdf_pages.py, extract_pdf_text_manifest.py, extract_pdfs_ibarra.py)
- [x] Protocolo 21 actualizado con scripts locales y comandos de uso
- [x] Sistema LaTeX completo creado: latex/ con 3 plantillas (entregable, tesis TF1, slides Beamer) y carpeta proyecto/
- [x] Protocolo LaTeX movido a auditoria/ como 25_protocolo_latex.md
- [x] Protocolo 21 actualizado con referencia al protocolo 25
- [x] Indice maestro de auditoria creado (00_indice_maestro_auditoria.md) - conecta protocolos, scripts, plantillas y herramientas
- [x] Protocolo 26 creado: transcripcion de audio (faster-whisper 1.2.1 + ffmpeg 9.0)
- [x] Script transcribir_audio.py creado en herramientas/ - genera .md, .json y .txt desde audio
- [x] Protocolo 27 creado: gestion bibliografica con Zotero + Better BibTeX (pendiente instalar)
- [x] Cross-links agregados a todos los protocolos (21-27) - cada uno referencia a los demas
- [x] Carpetas de estado del arte compartido creadas: curso_proyecto_investigacion/estado_del_arte/{papers,tesis,conferencias}
- [x] Carpetas de fuentes de investigacion creadas: fuentes_investigacion/{papers,videos,blogs,revistas,productos_similares,antecedentes}
- [x] manifest_fuentes.md creado en fuentes_investigacion/ - lista maestra de todas las fuentes
- [x] Revision general completada - sin repeticiones, estructura validada
- [x] MAPA_ORGANIZACION.md creado - documento maestro de donde va cada cosa

## Que falta

- [ ] Ingestar reglamento completo del curso (usuario pasara documentos)
  - [x] Titulo I: Caracteristicas del proyecto (Art. 1-6) - guardado en fuentes_originales/03_reglamento_tituloI_caracteristicas.md
  - [x] Titulo II: Desarrollo del proyecto (Art. 7-15) - guardado en fuentes_originales/04_reglamento_tituloII_desarrollo.md
  - [x] Titulo III: Funciones de los profesores (Art. 16-19) - guardado en fuentes_originales/05_reglamento_tituloIII_profesores.md
  - [x] Titulo IV: Entregables en las evaluaciones (Art. 20-21) - guardado en fuentes_originales/06_reglamento_tituloIV_entregables.md
  - [x] Titulo V: Evaluacion del curso (Art. 22-32) - guardado en fuentes_originales/07_reglamento_tituloV_evaluacion.md
  - [x] Titulo VI: Penalizaciones, sanciones y reclamos (Art. 33-36) - guardado en fuentes_originales/08_reglamento_tituloVI_penalizaciones.md
  - REGLAMENTO COMPLETO: 6 titulos, 36 articulos, 93 reglas criticas (R1-R93), 10 figuras, 4 tablas
- [x] PNCTI 2006-2021 ingestado en fuentes_originales/09_PNCTI_2006_2021.md - referenciado por Art. 5 del reglamento, define sectores prioritarios (Telecomunicaciones + TIC relevantes para nuestro proyecto)
- [x] Ficha de acta de asesoria creada en fuentes_originales/10_ficha_acta_asesoria.md - plantilla + plan de actas + checklist
- [x] Audio de clase Dia 1 transcrito (2h20m, 3513 segmentos, faster-whisper medium) en fuentes_originales/transcripciones/
- [x] Ficha de clase Dia 1 creada (FICHA_CLASE_DIA1_2026-08-25.md) - 22 reglas nuevas extraidas (R94-R115), cronograma corregido, detalles operativos del portafolio (OneDrive, deadline martes 1 PM)
- [x] Plantilla PPT EX1 documentada (11_plantilla_PPT_EX1.md) - 11 slides, estructura completa, reglas operativas, nombres exactos para Grupo 15
- [x] Plantilla Informe EX1 documentada (12_plantilla_informe_EX1.md) - 6 secciones + Referencias, formato IEEE, 5 publicaciones, 3 productos
- [x] Ejemplo referencial PPT EX1 documentado (13_ejemplo_referencial_PPT_EX1.md) - 20 slides, maquina PET, 4 productos, 5 articulos, errores detectados
- [x] Ejemplo referencial Informe EX1 documentado (14_ejemplo_referencial_informe_EX1.md) - mismo proyecto en formato Word, diferencias PPT vs Informe
- [x] Unidad 1 completa documentada en fuentes_originales/unidad1/ - 4 archivos: introduccion+fundamentos, normas IEEE, SCOPUS/WOS/ZOTERO/patentes, situacion problematica (titulo, arbol, requerimientos)
- [x] Research OS subido a GitHub https://github.com/Reznouw/research-os - branch main limpio (133 archivos, sin datos personales ni propuestas), historial reescrito, force push
- [x] Propuesta 01 documentada en documentacion_inicial/ - 5 docs: propuesta preliminar (17 secc), dossier estado del arte (17 secc, 9 refs), definicion problema (4 caminos), plan viabilidad 12 meses, asesoria Kalun (6 puntos)
- [ ] Transcribir audio de la clase grabada
- [ ] Analizar documentacion_inicial de propuesta 01 con asesor (elegir camino A/B/C/D, definir contexto, modelos, metrica principal)
- [ ] Completar propuesta_05 (pendiente de tema)
- [ ] Refinar propuestas 01-04 con info nueva del curso
- [ ] Comparativa de propuestas (COMPARATIVA.md) cuando esten las 5
- [ ] Confirmar acceso a hardware (DE25-Nano, DE10-Nano, Quartus, FPGA Xilinx)
- [ ] Seleccionar modelo Edge AI especifico
- [ ] Estado del arte en SCOPUS/Web of Science
- [ ] Material bruto para Renzosky del tema elegido

## Proximo paso accionable

Esperar a que el usuario pase:
1. Mas informacion del curso (reglamento, documentos, audio)
2. Indicacion de empezar a generar las 5 propuestas
3. Confirmacion de acceso a hardware y herramientas

## Memoria rapida para la siguiente sesion

- El tema preferido del usuario es "Arquitectura reconfigurable para inferencia Edge AI basada en FPGA DE25-Nano mediante co-diseno hardware-modelo" (propuesta_01).
- Hay 5 carpetas de propuestas autocontenidas, cada una con estructura completa de desarrollo dentro.
- 4 propuestas tienen borrador (01-04), 1 esta pendiente (05).
- Cada propuesta tiene: propuesta_NN.md + 00_RAW/ + renzosky/ + estado_del_arte/ + fichas_papers/ + matriz_evidencia/ + entregables/(EX1-EX2-TP1-EX3-DD1-TF1).
- Hay 28 agentes investigadores en .opencode/agent/investigadores/. Cada uno tiene su perfil y acceso a cualquier archivo.
- Al terminar un entregable, se seleccionan 5 investigadores afines (via SELECCION_INVESTIGADORES.md) y revisan en paralelo. Comando: /revision-investigadores.
- El pipeline de revision (FLUJO_REVISION.md) no crea otro documento: mejora el entregable existente y guarda REVISION_REPORTE.md como trazabilidad.
- Las perspectivas_investigadores/ (28 txt + PERFILES + SELECCION) son workflow, no evidencia.
- Renzosky esta en CURSOS/ (nivel superior) y funciona para cualquier curso.
- El reglamento del curso NO esta en archivos locales todavia; el usuario lo pasara.
- Hay un audio de clase grabado que el usuario pasara despues.

## Riesgos activos

1. **Reglamento desconocido:** El reglamento completo del curso no se ha ingestado. Puede cambiar reglas de formato, entregables o evaluacion.
2. **Hardware no confirmado:** No sabemos si el usuario tiene acceso al DE25-Nano o que FPGAs tiene disponibles.
3. **Modelo Edge AI no seleccionado:** Sin un modelo especifico, el estado del arte es generico.
4. **Tiempo limitado:** 1 semana para 5 propuestas + 16 semanas para todo el proyecto.
