# Flujo de ingesta: como la informacion llega a los markdowns

> **Este documento explica el flujo completo: desde que entra un PPT/PDF hasta que la informacion se usa en los entregables.**
> Responde: como se vuelve a utilizar dentro de nuestros markdowns? Se actualiza el contexto? Se guarda en algun lado? Es automatico?

---

## Flujo completo (paso a paso)

```
1. PPT/PDF entra
       ↓
2. Extraccion automatica (Python: python-pptx / PyMuPDF / pymupdf4llm)
       ↓
3. Slides/paginas criticas → convertir a imagen (PNG)
       ↓
4. Leer imagen con modelo de vision (yo leo la imagen y extraigo detalle)
       ↓
5. Ficha por slide/pagina con etiquetas de confianza
       ↓
6. Ficha se guarda en fichas_papers/ o estado_del_arte/
       ↓
7. ESTADO.md se actualiza con lo que se ingirnio
       ↓
8. Cuando se escribe un entregable, la ficha se usa como evidencia
       ↓
9. Las reglas o patrones nuevos se guardan research_memory/global/learnings/
```

---

## Ejemplo concreto

Supongamos que me pasas un PPT del curso 1AEL0260 sobre "como formular el arbol del problema".

### Paso 1-2: Extraccion automatica

Con `python-pptx` extrigo el texto interno del PPT:

```markdown
## Slide 1: El arbol del problema
### Texto visible
- Situacion problemica
- Causas
- Consecuencias
### Notas del orador
"Recuerden que el arbol va de arriba hacia abajo: problema general arriba, causas medias, efectos abajo."

## Slide 2: Ejemplo de arbol
### Texto visible
- (slide tiene solo una imagen de un arbol de problema)

## Slide 3: Formato EX1
### Texto visible
- Entregar informe + exposicion oral
- Rubrica: introduccion, desarrollo, cierre
```

### Paso 3-4: Slides criticas a imagen

El slide 2 tiene solo una imagen (un arbol de problema). El texto automatico no me da nada util. Convierto el slide 2 a PNG y lo leo visualmente:

```markdown
## Slide 2: Ejemplo de arbol (VISUAL_READ)

### Descripcion visual
Imagen muestra un arbol con 3 niveles:
- Nivel 1 (arriba): "Pacientes mayores sin monitoreo de marcha en casa"
- Nivel 2 (medio): "Falta de tecnologia accesible" | "Costo elevado de dispositivos" | "Personal insuficiente"
- Nivel 3 (abajo): "Riesgo de caidas no detectado" | "Hospitalizaciones evitables" | "Costo familiar"

### Mensaje principal
El arbol conecta un problema general con causas tecnicas/economicas y consecuencias humanas.

### Confianza
`FIGURE_INTERPRETED` - figura interpretada visualmente desde imagen del slide.
```

### Paso 5: Ficha se guarda

Creo el archivo `curso_proyecto_investigacion/fichas_ppt/01_arbol_problema.md` con toda la informacion combinada (texto automatico + lectura visual de slides criticos).

### Paso 6: ESTADO.md se actualiza

Agrego a ESTADO.md:
```markdown
- [x] PPT "Arbol del problema" ingestado en fichas_ppt/01_arbol_problema.md
- [x] Slides criticos: slide 2 (arbol como imagen) verificado visualmente
- [x] Regla extraida: el arbol va de arriba hacia abajo (problema → causas → efectos)
```

### Paso 7: Cuando se escribe un entregable

Cuando me digas "escribamos el EX1", yo:

1. Leo `ESTADO.md` (se que hay un PPT sobre arbol del problema ingestado)
2. Leo `curso_proyecto_investigacion/fichas_ppt/01_arbol_problema.md` (la ficha con el detalle)
3. Leo `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md` (las reglas del curso)
4. Escribo el EX1 usando la informacion de la ficha como evidencia

**La ficha se conecta automaticamente al entregable porque ESTADO.md dice donde esta.**

### Paso 8: Reglas nuevas se guardan

Si al procesar el PPT descubro un patron reutilizable (ej. "los PPT del curso siempre tienen el formato EX1/EX2/TP1/TF1 en ese orden"), lo guardo en `research_memory/global/learnings/`.

---

## Como se actualiza el contexto

**No es magico. Es explicito y trazable.**

```
PPT nuevo entra
    ↓
Python extrae texto (automatico)
    ↓
Yo leo las imagenes de slides criticos (visual)
    ↓
Ficha .md se crea en fichas_papers/ o fichas_ppt/
    ↓
ESTADO.md se actualiza: "ingestado X en ruta Y"
    ↓
DECISIONES.md se actualiza si hubo decision (ej. "usar PPT como regla del curso")
    ↓
research_memory/global/learnings/ se actualiza si hubo patron nuevo
    ↓
FLUJO_SESION.md ya dice: leer ESTADO.md primero en cada sesion
    ↓
Por eso la siguiente sesion ya sabe que la ficha existe y donde esta
```

**La conexion es automatica en este sentido:** cuando yo leo ESTADO.md al inicio de una sesion, veo que la ficha existe y donde esta. No tengo que "recordar" nada — ESTADO.md es mi memoria. Si la ficha no esta en ESTADO.md, no la uso. Si esta, la leo.

---

## Donde se guarda cada cosa

| Que | Donde | Cuando |
|---|---|---|
| Texto extraido automatico | Ficha .md en `fichas_papers/` o `fichas_ppt/` | Al ingestar |
| Lectura visual de slides criticos | Misma ficha .md (seccion "Visual") | Al leer la imagen |
| Etiquetas de confianza (AUTO_TEXT, VISUAL_READ, etc.) | Misma ficha .md | Al clasificar cada dato |
| Estado del proyecto (que se ha ingestado) | `ESTADO.md` | Al terminar la ingesta |
| Decisions (por que se hizo algo) | `DECISIONES.md` | Al tomar una decision |
| Patrones/reglas reutilizables | `research_memory/global/learnings/` | Al descubrir un patron |
| Claims listos para usar | Ficha .md seccion `claims_ready` | Al clasificar |
| Claims prohibidos | Ficha .md seccion `claims_prohibidos` | Al clasificar |
| Datos pendientes | Ficha .md seccion `claims_pending` | Al no poder verificar |

---

## Que pasa con PPTs grandes (+40 slides)

Segun `22_pipeline_ingesta_multimodal.md`:

| Tamano | Estrategia |
|---|---|
| PPT 10-40 slides | Exportar todos los slides a imagen; ficha por slide critico |
| PPT 40+ slides | Texto/notas + thumbnails; lectura visual **solo** de slides criticos |

Para +40 slides:
1. Extrigo texto y notas de todos los slides (python-pptx)
2. No convierto todos a imagen (gastaria recursos)
3. Identifico los slides criticos (objetivos, metodologia, resultados, conclusiones)
4. Convierto solo esos slides criticos a imagen
5. Leo visualmente solo esos
6. El resto queda como `AUTO_TEXT` (suficiente para contexto, no para claims numericos)

---

## Que pasa con PDFs

Mismo flujo pero con PyMuPDF en vez de python-pptx:

```
PDF entra
    ↓
PyMuPDF extrae texto por pagina
pymupdf4llm genera markdown
    ↓
Identifico paginas criticas (metodo, tablas, formulas, resultados, figuras)
    ↓
render_pdf_pages.py convierte paginas criticas a PNG
    ↓
Yo leo los PNG visualmente
    ↓
Ficha .md combinada (texto automatico + lectura visual de paginas criticas)
    ↓
ESTADO.md actualizado
```

---

## Resumen: es automatico o manual?

**Es hibrido:**

| Parte | Automatico | Manual (yo) |
|---|---|---|
| Extraer texto | Python (python-pptx / PyMuPDF) | - |
| Convertir slides/paginas a imagen | render_pdf_pages.py / LibreOffice | - |
| Identificar slides/paginas criticas | - | Yo (segun protocolo 23) |
| Leer imagen y extraer detalle | - | Yo (modelo de vision) |
| Crear ficha .md | - | Yo (escribo el .md) |
| Actualizar ESTADO.md | - | Yo (lo escribo) |
| Guardar reglas/patrones | - | Yo (si los descubro) |
| Usar la ficha en entregables | - | Yo (la leo cuando escribo) |

**Lo automatico es la extraccion de texto y conversion a imagen. Lo manual es la interpretacion de la imagen, la creacion de la ficha, y la actualizacion del estado.**

Pero gracias a ESTADO.md, una vez que la ficha se guarda, las siguientes sesiones la encuentran automaticamente — porque ESTADO.md es lo primero que se lee.

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Herramientas usadas: PyMuPDF, pymupdf4llm, python-pptx, render_pdf_pages.py |
| `22_pipeline_ingesta_multimodal.md` | Pipeline general que decide textual vs visual |
| `23_protocolo_pdf_ppt_imagenes.md` | Flujos especificos para cada tipo de archivo |
| `25_protocolo_latex.md` | Despues de extraer, el contenido se produce en PDF/Word |
| `26_protocolo_transcripcion_audio.md` | Flujo complementario para audio — genera .md que tambien llega a ESTADO.md |
| `27_protocolo_zotero.md` | Los PDFs de Zotero se procesan y sus fichas se conectan via ESTADO.md |
| `herramientas/extract_pdfs_ibarra.py` | Extrae texto de PDFs → ficha → ESTADO.md |
| `herramientas/render_pdf_pages.py` | Renderiza paginas criticas → imagenes → lectura visual → ficha |
