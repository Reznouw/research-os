# 23 Protocolo PDF, PPT e imagenes

## Proposito

Definir como procesar fuentes visuales o semivisuales para obtener informacion confiable. Este protocolo complementa `22_pipeline_ingesta_multimodal.md`.

## PDF cientifico

### Flujo

1. Extraer texto por pagina con PyMuPDF.
2. Extraer Markdown con pymupdf4llm si conviene para lectura IA.
3. Crear mapa de paginas: abstract, introduccion, metodo, tablas, figuras, resultados, limitaciones.
4. Convertir a imagen solo paginas criticas o todas si el paper es corto.
5. Leer visualmente paginas con dos columnas, tablas, formulas, graficas o diagramas.
6. Crear ficha con etiquetas de confianza.

### Paginas que casi siempre son criticas

- Primera pagina: titulo, autores, abstract y contribucion.
- Metodo/simulation setup.
- Tabla de parametros.
- Formulas del modelo.
- Figuras de arquitectura.
- Graficas de resultados.
- Discusion y limitaciones.
- Conclusion.

### Regla

Para claims tecnicos fuertes, los resultados deben estar verificados en pagina/figura/tabla original, no solo en texto convertido.

## PDF escaneado

### Flujo

1. Renderizar paginas a imagen.
2. Aplicar OCR/lectura visual por pagina o por zonas.
3. Separar columnas manualmente si el orden de lectura falla.
4. Registrar resolucion y calidad.

### Regla

Si la resolucion no permite leer texto pequeno o formulas, marcar `PENDING` y pedir mejor imagen/PDF.

## PPT/PPTX

### Por que no basta extraer texto

Un PPT contiene significado en layout, flechas, diagramas, capas, imagenes y relaciones espaciales. Extraer solo bullets puede destruir el mensaje.

### Flujo

1. Extraer texto interno y notas si la herramienta lo permite.
2. Exportar slides a imagen o convertir PPT a PDF y luego a imagen.
3. Crear ficha por slide critico.
4. Interpretar diagramas, tablas y graficas como elementos visuales.
5. Separar datos mostrados de conclusiones inferidas.

### Ficha por slide

```text
slide:
titulo:
texto_visible:
notas_presentador:
elementos_visuales:
tabla/grafica:
mensaje_principal:
claim_soportado:
claim_no_soportado:
confianza:
```

### Slides criticos

- Objetivos.
- Hipotesis o contribuciones.
- Arquitectura.
- Metodologia.
- Dataset/hardware.
- Resultados.
- Tablas.
- Graficas.
- Conclusiones.
- Limitaciones.

### Regla

Un PPT es evidencia de lo que el expositor/material presenta, no necesariamente evidencia cientifica final. Si se usa para claims de paper, debe conectarse con una fuente primaria.

## Imagen suelta

### Flujo

1. Extraer texto visible.
2. Describir elementos visuales.
3. Interpretar el mensaje probable del autor.
4. Separar lo que la imagen muestra de lo que no demuestra.
5. Guardar ficha si la imagen sera reutilizada.

### Ficha de imagen

```text
image_id:
ruta:
texto_visible:
descripcion_visual:
mensaje_autor:
uso_permitido:
claims_no_permitidos:
confianza:
```

## Tablas

### Regla

Toda tabla usada para parametros, comparacion o resultados debe estar marcada `TABLE_VERIFIED`.

Si la tabla se extrae mal:

- conservar captura o pagina;
- transcribir solo filas necesarias;
- marcar celdas dudosas;
- no calcular resultados derivados hasta verificar.

## Figuras

### Pasaporte de figura

- Figura y pagina.
- Caption.
- Que muestra.
- Variables/ejes si existen.
- Fuente de datos.
- Mensaje principal.
- Limitacion.
- Claim permitido.
- Claim prohibido.
- Confianza.

## Formulas

### Regla

Las formulas extraidas automaticamente son de alto riesgo.

Antes de usarlas:

- revisar visualmente simbolos;
- transcribir a LaTeX si son centrales;
- explicar variables;
- conectar con metodo y simulacion.

## Decision de herramienta

| Necesidad | Herramienta ligera | Herramienta futura si no basta |
| --- | --- | --- |
| Texto PDF | PyMuPDF | Docling |
| Markdown PDF | pymupdf4llm | Marker/Docling |
| Imagen de pagina PDF | `herramientas/render_pdf_pages.py` | OCRmyPDF/Tesseract/PaddleOCR |
| PPT a imagen/PDF | PowerPoint/LibreOffice si disponible | Docling |
| Metadata/referencias | Zotero/manual | GROBID |
| Tablas PDF texto | PyMuPDF/manual | Camelot/Tabula |

Comando local para renderizar paginas criticas de un PDF:

```powershell
py herramientas/render_pdf_pages.py "ruta\paper.pdf" --pages 1,4,8-10 --out "ruta\imagenes_criticas" --dpi 200
```

El script solo crea imagenes y `manifest_pages.csv`; no hace OCR ni interpreta automaticamente. La interpretacion se realiza despues con lectura visual selectiva.

## Veredicto operativo

El sistema debe priorizar calidad sobre volumen. La lectura automatica da cobertura; la lectura visual selectiva da confianza. Un claim solo debe avanzar a borrador cuando su fuente, locator, metodo, variable/metrica y limitacion estan claros.

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Herramientas usadas: PyMuPDF, pymupdf4llm, render_pdf_pages.py, Zotero |
| `22_pipeline_ingesta_multimodal.md` | Pipeline general que decide textual vs visual |
| `24_flujo_ingesta_a_markdown.md` | La salida de este protocolo llega a markdowns via este flujo |
| `25_protocolo_latex.md` | Despues de extraer y auditar, se produce en PDF/Word |
| `26_protocolo_transcripcion_audio.md` | Flujo complementario para audio |
| `27_protocolo_zotero.md` | Los PDFs de Zotero se procesan con estos flujos |
| `herramientas/extract_pdfs_ibarra.py` | Metodo textual: extraccion completa |
| `herramientas/render_pdf_pages.py` | Metodo visual: renderiza paginas a PNG |
