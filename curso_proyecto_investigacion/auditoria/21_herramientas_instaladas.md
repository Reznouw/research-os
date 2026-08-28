# 21 Herramientas instaladas para el sistema de investigacion

## Proposito

Registrar herramientas externas y scripts locales disponibles para el sistema de investigacion de INVESTIGACION, con uso previsto, forma de verificacion y limites. Esto evita volver a instalar cosas y permite decidir que herramienta usar segun la tarea.

## Estado actual

| Herramienta | Estado | Verificacion | Uso principal |
| --- | --- | --- | --- |
| PyMuPDF | Instalado | `py -c "import fitz; print(fitz.version[0])"` -> `1.28.0` | Extraccion rapida de texto/metadatos desde PDFs |
| pymupdf4llm | Instalado | `py -c "import pymupdf4llm"` -> ok | Conversion de PDFs a Markdown orientado a LLM |
| Pandoc | Instalado | `pandoc 3.10` por ruta absoluta | Conversion Markdown/LaTeX/Word/PDF |
| Zotero | Instalado | `C:\Program Files\Zotero\zotero.exe --version` -> Zotero disponible | Gestion de biblioteca, metadatos y referencias |
| Better BibTeX | Pendiente manual | No instalado/verificado | Exportacion BibTeX estable desde Zotero |
| LaTeX Live | Disponible previamente | `pdflatex`, `latexmk`, `xelatex`, `biber` ya verificados antes | Compilacion final de articulos |

## Scripts locales copiados de WBAN

| Script | Ruta | Uso |
| --- | --- | --- |
| `render_pdf_pages.py` | `herramientas/render_pdf_pages.py` | Convierte paginas seleccionadas de PDF a PNG y crea `manifest_pages.csv` para lectura visual selectiva |
| `extract_pdf_text_manifest.py` | `herramientas/extract_pdf_text_manifest.py` | Extrae texto de PDFs recursivamente + genera manifest CSV con source, text_file, pages, chars, image_objects |
| `extract_pdfs_ibarra.py` | `herramientas/extract_pdfs_ibarra.py` | Extrae texto + markdown de PDFs con PyMuPDF + pymupdf4llm + genera MANIFEST_EXTRACCIONES.md (adaptado de Ibarra, dominio-agnostico) |

### Comando para renderizar paginas criticas de un PDF

```powershell
py herramientas/render_pdf_pages.py "ruta\paper.pdf" --pages 1,4,8-10 --out "ruta\imagenes_criticas" --dpi 200
```

El script solo crea imagenes y `manifest_pages.csv`; no hace OCR ni interpreta automaticamente. La interpretacion se realiza despues con lectura visual selectiva.

### Comando para extraer texto de todos los PDFs en una carpeta

```powershell
py herramientas/extract_pdf_text_manifest.py "ruta\carpeta_con_pdfs" --out "ruta\extracciones" --manifest "ruta\manifest.csv"
```

### Comando para extraer texto + markdown de PDFs (estilo Ibarra)

```powershell
py herramientas/extract_pdfs_ibarra.py
```

Este script busca PDFs en `pdfs/` y genera texto (PyMuPDF) + markdown (pymupdf4llm) + MANIFEST_EXTRACCIONES.md. Adaptar las rutas BASE/PDF_DIR/OUT_TEXT/OUT_MD segun el proyecto.

## Protocolos locales activos

| Protocolo | Archivo | Uso |
| --- | --- | --- |
| Ingesta multimodal | `auditoria/22_pipeline_ingesta_multimodal.md` | Decide cuando usar texto automatico, imagen/OCR selectivo y etiquetas de confianza |
| PDF/PPT/imagenes | `auditoria/23_protocolo_pdf_ppt_imagenes.md` | Define flujos especificos para PDFs cientificos, PDFs escaneados, PPT/PPTX, imagenes, tablas, figuras y formulas |
| Flujo ingesta a markdown | `auditoria/24_flujo_ingesta_a_markdown.md` | Explica como la informacion extraida llega a los markdowns y actualiza el contexto via ESTADO.md |
| LaTeX y Word | `auditoria/25_protocolo_latex.md` | Define flujos para producir PDF (LaTeX) o Word (Pandoc) desde markdown. Plantillas en `latex/plantillas/` |

## Notas de PATH

Despues de instalar con `winget`, la terminal actual puede no reconocer inmediatamente `pandoc` o `zotero` en PATH. Reiniciar OpenCode o abrir una nueva terminal deberia cargar el PATH actualizado.

Rutas verificadas:

```text
C:\Users\ASUS\AppData\Local\Microsoft\WinGet\Packages\JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe\pandoc-3.10\pandoc.exe
C:\Program Files\Zotero\zotero.exe
```

## Uso recomendado por tarea

### Leer un PDF nuevo

Primero usar PyMuPDF/pymupdf4llm porque es ligero.

Salida esperada:

- Markdown o texto limpio.
- Paginas/locators conservados si es posible.
- Nota si tablas, figuras o formulas no fueron preservadas.

Si el PDF contiene dos columnas, tablas, formulas, figuras o resultados, aplicar `22_pipeline_ingesta_multimodal.md` y verificar visualmente paginas criticas antes de usar claims tecnicos o numericos.

### Leer PPT/PPTX o imagenes

Tratar PPT/PPTX e imagenes como fuentes visuales. Extraer texto si existe, pero no confiar solo en bullets o texto interno. Convertir o revisar slides/imagenes criticas visualmente y producir ficha con claims permitidos, claims no permitidos y nivel de confianza.

### Convertir borrador Markdown a LaTeX

Usar Pandoc solo cuando el borrador ya tenga estructura razonable.

No usar Pandoc como sustituto de auditoria: antes debe pasar matriz de evidencia, claim audit y citation check.

### Gestionar referencias

Usar Zotero para guardar PDFs, metadatos, DOI, tags y colecciones.

Instalar Better BibTeX desde la interfaz de Zotero cuando empecemos a cerrar `references.bib`.

### Compilar paper

Usar LaTeX Live local. Pandoc puede ayudar a generar `.tex`, pero `latexmk`/`pdflatex`/`xelatex` siguen siendo la verificacion final.

## Herramientas no instaladas todavia

| Herramienta | Motivo de espera |
| --- | --- |
| Docling | Mas pesado; instalar solo si PyMuPDF no conserva layout/tablas suficientes |
| Marker | Mas pesado; instalar solo si necesitamos formulas/tablas complejas desde PDF |
| GROBID | Requiere Java/servicio; esperar hasta tener muchas referencias que extraer |
| RAG local BM25 + embeddings | Requiere diseno de indice, chunks y evaluacion; fase posterior |
| last30days | No necesario para WBAN inmediato |

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `22_pipeline_ingesta_multimodal.md` | Decide que herramienta usar para extraer contenido segun tipo de archivo |
| `23_protocolo_pdf_ppt_imagenes.md` | Flujos especificos para PDF, PPT, imagenes — usa las herramientas de esta tabla |
| `24_flujo_ingesta_a_markdown.md` | La extraccion de texto llega a markdowns via este flujo |
| `25_protocolo_latex.md` | Pandoc y LaTeX Live se usan para producir PDF/Word desde markdown |
| `26_protocolo_transcripcion_audio.md` | faster-whisper + ffmpeg para transcripcion de audio |
| `27_protocolo_zotero.md` | Zotero para gestion bibliografica, Better BibTeX para exportar .bib |
| `herramientas/extract_pdfs_ibarra.py` | Script de extraccion PDF+markdown |
| `herramientas/render_pdf_pages.py` | Script de renderizado de paginas a PNG |
| `herramientas/extract_pdf_text_manifest.py` | Script de extraccion masiva con manifest CSV |

## Regla operativa

No instalar herramientas pesadas solo por disponibilidad. Instalar cuando haya una tarea concreta que lo justifique y registrar el resultado aqui.
