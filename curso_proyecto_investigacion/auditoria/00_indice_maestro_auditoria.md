# 00 Indice maestro de auditoria

> **Este archivo es el indice de todo lo que hay en `auditoria/`.**
> Cada vez que se agregue un protocolo, herramienta o script nuevo, se actualiza este indice.
> Asi cualquier sesion sabe que existe y donde esta, sin tener que adivinar.

---

## Protocolos (01-25)

| # | Archivo | Que define | Herramientas que usa | Scripts que implementa |
|---|---|---|---|---|
| 01 | `01_silabus_como_regla.md` | Reglas del curso 1AEL0260 extraidas del syllabus | - | - |
| 21 | `21_herramientas_instaladas.md` | Herramientas instaladas (PyMuPDF, pymupdf4llm, Pandoc, Zotero, LaTeX Live) + scripts locales | PyMuPDF, pymupdf4llm, Pandoc, Zotero, LaTeX Live | `herramientas/render_pdf_pages.py`, `herramientas/extract_pdf_text_manifest.py`, `herramientas/extract_pdfs_ibarra.py` |
| 22 | `22_pipeline_ingesta_multimodal.md` | Pipeline de ingesta: cuando usar texto automatico vs imagen/OCR selectivo | PyMuPDF, pymupdf4llm | `herramientas/render_pdf_pages.py`, `herramientas/extract_pdf_text_manifest.py` |
| 23 | `23_protocolo_pdf_ppt_imagenes.md` | Flujos especificos para PDFs, PPT/PPTX, imagenes, tablas, figuras, formulas | PyMuPDF, pymupdf4llm | `herramientas/render_pdf_pages.py`, `herramientas/extract_pdfs_ibarra.py` |
| 24 | `24_flujo_ingesta_a_markdown.md` | Como la informacion extraida llega a los markdowns y actualiza ESTADO.md | - | - |
| 25 | `25_protocolo_latex.md` | Como producir PDF (LaTeX) o Word (Pandoc) desde markdown | LaTeX Live, Pandoc | Plantillas en `latex/plantillas/` |
| 26 | `26_protocolo_transcripcion_audio.md` | Como convertir audio (clases, grabaciones) en texto/markdown | faster-whisper 1.2.1, ffmpeg 9.0 | `herramientas/transcribir_audio.py` |
| 27 | `27_protocolo_zotero.md` | Gestion bibliografica: guardar papers, exportar BibTeX, producir bibliografia para LaTeX/Word | Zotero, Better BibTeX (pendiente) | - |

---

## Scripts Python disponibles

| Script | Ruta | Que hace | Comando de uso | Protocolo que lo define |
|---|---|---|---|---|
| `render_pdf_pages.py` | `INVESTIGACION/herramientas/render_pdf_pages.py` | Convierte paginas PDF a PNG | `py herramientas/render_pdf_pages.py "paper.pdf" --pages 1,3,5-7 --dpi 200` | 21, 22, 23 |
| `extract_pdf_text_manifest.py` | `INVESTIGACION/herramientas/extract_pdf_text_manifest.py` | Extrae texto de PDFs recursivamente + manifest CSV | `py herramientas/extract_pdf_text_manifest.py "carpeta" --out "salida"` | 21, 22 |
| `extract_pdfs_ibarra.py` | `INVESTIGACION/herramientas/extract_pdfs_ibarra.py` | Extrae texto + markdown de PDFs con PyMuPDF + pymupdf4llm | `py herramientas/extract_pdfs_ibarra.py` | 21, 23 |
| `transcribir_audio.py` | `INVESTIGACION/herramientas/transcribir_audio.py` | Transcribe audio a texto/markdown con faster-whisper | `py herramientas/transcribir_audio.py "audio.mp3"` | 26 |

---

## Plantillas LaTeX disponibles

| Plantilla | Ruta | Para que sirve | Protocolo que la define |
|---|---|---|---|
| `entregable_upc.tex` | `INVESTIGACION/latex/plantillas/entregable_upc.tex` | Entregable generico del curso | 25 |
| `tesis_upc.tex` | `INVESTIGACION/latex/plantillas/tesis_upc.tex` | TF1 (40%) con todas las secciones del syllabus | 25 |
| `slides_defensa.tex` | `INVESTIGACION/latex/plantillas/slides_defensa.tex` | Diapositivas Beamer para defensa oral | 25 |

---

## Herramientas externas instaladas

| Herramienta | Version | Ruta de verificacion | Uso | Protocolo |
|---|---|---|---|---|
| PyMuPDF | 1.28.0 | `py -c "import fitz"` | Extraccion texto PDF | 21, 22, 23 |
| pymupdf4llm | instalado | `py -c "import pymupdf4llm"` | PDF a Markdown | 21, 22, 23 |
| Pandoc | 3.10 | ruta absoluta WinGet | Markdown a LaTeX/Word/PDF | 25 |
| Zotero | disponible | `C:\Program Files\Zotero\zotero.exe` | Gestion bibliografia | 21 |
| LaTeX Live | disponible | `pdflatex`, `latexmk`, `xelatex`, `biber` | Compilacion PDF | 25 |
| faster-whisper | 1.2.1 | `py -c "from faster_whisper import WhisperModel"` | Transcripcion audio | 26 |
| ffmpeg | 9.0 | `ffmpeg -version` | Procesamiento audio/video | 26 |

---

## Regla de actualizacion

Cada vez que se agregue o modifique:
1. Un protocolo nuevo → append a la tabla de protocolos (01-25).
2. Un script nuevo → append a la tabla de scripts.
3. Una plantilla nueva → append a la tabla de plantillas.
4. Una herramienta externa → append a la tabla de herramientas.
5. Actualizar ESTADO.md con lo que se agrego.
6. Actualizar DECISIONES.md con la decision de agregarlo.
7. Si el protocolo/script conecta con otros, documentar la conexion aqui.

**Este indice es el puente entre `auditoria/` y `ESTADO.md`/`DECISIONES.md`.**
