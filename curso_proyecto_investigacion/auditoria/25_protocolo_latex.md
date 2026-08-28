# Protocolo LaTeX y Word para entregables

> **Como se producen documentos finales en PDF o Word desde los markdowns del proyecto.**
> Herramientas: LaTeX Live (pdflatex, latexmk, xelatex, biber) + Pandoc.
> Todas verificadas y funcionando.

---

## Pipeline de produccion

```
Entregable en markdown (.md)
    ↓
Gate de auditoria (paper-audit)
    ↓
¿Que formato necesita el curso?
    ├── PDF (LaTeX)  →  latex/main.tex → pdflatex/latexmk → main.pdf
    ├── Word (.docx) →  pandoc main.md -o main.docx
    └── Ambos       →  pandoc main.md -o main.tex  →  pdflatex → main.pdf
```

---

## Flujo 1: Markdown → PDF via LaTeX

### Paso 1: Crear estructura LaTeX

Crear `latex/main.tex` desde el markdown del entregable. Dos opciones:

**Opcion A (automatica con Pandoc):**
```powershell
$pandoc = "C:\Users\ASUS\AppData\Local\Microsoft\WinGet\Packages\JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe\pandoc-3.10\pandoc.exe"
& $pandoc "ruta\entregable.md" -o "ruta\latex\main.tex" --standalone
```

**Opcion B (manual, mas control):**
Usar la plantilla `latex/plantillas/entregable_upc.tex` y pegar el contenido del markdown en la estructura LaTeX.

### Paso 2: Compilar a PDF

```powershell
cd "ruta\latex"
latexmk -pdf main.tex
```

O si hay errores:
```powershell
pdflatex main.tex
pdflatex main.tex   # segunda pasada para referencias
```

### Paso 3: Si hay bibliografia

```powershell
biber main           # procesa references.bib
latexmk -pdf main.tex  # recompila con referencias
```

---

## Flujo 2: Markdown → Word (.docx)

```powershell
$pandoc = "C:\Users\ASUS\AppData\Local\Microsoft\WinGet\Packages\JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe\pandoc-3.10\pandoc.exe"
& $pandoc "ruta\entregable.md" -o "ruta\entregable.docx" --standalone
```

Pandoc convierte markdown a Word con formato academico aceptable.

---

## Flujo 3: Markdown → PDF directo (sin LaTeX intermedio)

```powershell
& $pandoc "ruta\entregable.md" -o "ruta\entregable.pdf" --pdf-engine=pdflatex
```

Pandoc usa pdflatex internamente. Util si no se necesita control fino del LaTeX.

---

## Estructura de carpeta latex/

```
INVESTIGACION/latex/
├── PROTOCOLO_LATEX.md          ← Este archivo
├── plantillas/
│   ├── entregable_upc.tex        ← Plantilla generica para entregables del curso
│   ├── tesis_upc.tex             ← Plantilla para TF1 (40%)
│   └── slides_defensa.tex        ← Plantilla para diapositivas de defensa (Beamer)
└── proyecto/                    ← Donde se ponen los .tex del entregable activo
    ├── main.tex                  ← Archivo principal del entregable
    ├── references.bib            ← Bibliografia (BibTeX)
    └── figuras/                  ← Imagenes/PDFs vectoriales
```

---

## Cuando usar cada flujo

| Entregable | Formato recomendado | Flujo | Razon |
|---|---|---|---|
| EX1, EX2 | Word (.docx) | Flujo 2 | El curso pide Word/PowerPoint en PDF |
| TP1 | PDF (LaTeX) | Flujo 1 | Formulacion formal con diagramas |
| EX3 | PDF (LaTeX) o Word | Flujo 1 o 2 | Segun preferencia del profesor |
| DD1 | PDF (LaTeX) + diapositivas | Flujo 1 + slides | Individual, ABET 3, exige multimedia |
| TF1 | PDF (LaTeX) | Flujo 1 | 40%, proyecto completo, formato formal |

---

## Reglas de calidad

1. **Antes de compilar, pasar gate de auditoria.** No compilar algo no auditado (`/paper-audit`).
2. **Figuras vectoriales obligatorias.** PNG/JPEG solo si no hay alternativa. Ver protocolo 23 (Chuscience).
3. **Usar `\input{}` para secciones largas.** No meter todo en un .tex gigante.
4. **Bibliografia en BibTeX.** No referencias a mano en el texto.
5. **Compilar con `latexmk -pdf` primera vez.** Si falla, usar `pdflatex` directo para ver el error.
6. **Para Word, usar Pandoc directo.** No pasar por LaTeX intermedio para Word.
7. **Guarda el .tex y el .pdf en `latex/proyecto/`.** No en la carpeta del entregable.

---

## Comando /latex-build

El comando `/latex-build` del opencode.json ya esta configurado:
- Verifica que el .tex existe
- Verifica que comandos LaTeX estan disponibles
- Usa la compilacion minima segura
- Si falla, explica el error y aplica fixes pequenos
- Vuelve a verificar

---

## Plantillas disponibles

### entregable_upc.tex (entregable generico)
Plantilla basica para cualquier entregable del curso 1AEL0260 con estructura: titulo, autor, fecha, secciones.

### tesis_upc.tex (TF1 - 40%)
Plantilla completa para el Trabajo Final con todas las secciones que pide el syllabus: resumen, situacion problematica, fundamentos teoricos, causas, problemas de ingenieria, justificacion, estado del arte, arbol de objetivos, objetivos especificos, diagrama de bloques, cronograma Gantt, alcances y limitaciones, viabilidad, conclusiones.

### slides_defensa.tex (Beamer)
Plantilla para diapositivas de defensa oral con Beamer. Para DD1 (ABET 3) y todas las exposiciones.

---

## Verificacion rapida

```powershell
# Verificar que todo sigue funcionando
$pandoc = "C:\Users\ASUS\AppData\Local\Microsoft\WinGet\Packages\JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe\pandoc-3.10\pandoc.exe"
& $pandoc --version     # Pandoc
pdflatex --version     # LaTeX
latexmk --version      # latexmk
```

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Herramientas: Pandoc, LaTeX Live (pdflatex, latexmk, xelatex, biber) |
| `22_pipeline_ingesta_multimodal.md` | El contenido extraido con este pipeline se produce en PDF/Word con este protocolo |
| `23_protocolo_pdf_ppt_imagenes.md` | Los PDFs/PPT procesados aqui se convierten en entregables con este protocolo |
| `24_flujo_ingesta_a_markdown.md` | El markdown resultante se compila a PDF/Word con este protocolo |
| `26_protocolo_transcripcion_audio.md` | La transcripcion de audio puede ser fuente de contenido para entregables LaTeX |
| `27_protocolo_zotero.md` | El .bib exportado desde Zotero se usa en \bibliography{references} |
| `latex/plantillas/*.tex` | Plantillas: entregable_upc, tesis_upc, slides_defensa |
| `herramientas/transcribir_audio.py` | Audio transcripcion puede generar contenido para entregables LaTeX |
