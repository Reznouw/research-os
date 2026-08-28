# 22 Pipeline de ingesta multimodal

## Proposito

Definir un flujo de ingesta que no dependa solo de texto plano. El objetivo es obtener informacion de calidad desde PDFs, PPT/PPTX, imagenes, documentos escaneados, tablas, figuras y formulas, preservando trazabilidad y nivel de confianza.

## Principio central

No todo debe procesarse visualmente. Primero se extrae cobertura automatica; luego se aplica lectura visual/OCR solo a paginas o slides criticos.

Flujo base:

```text
Fuente original -> texto automatico -> deteccion de zonas criticas -> imagen/visual selectivo -> ficha trazable -> claims auditados
```

## Tipos de fuente

| Tipo | Primera capa | Segunda capa | Uso de lectura visual |
| --- | --- | --- | --- |
| PDF con texto | PyMuPDF/pymupdf4llm | paginas criticas a imagen | figuras, tablas, formulas, resultados |
| PDF escaneado | render a imagen | OCR/lectura visual | toda pagina relevante |
| PPT/PPTX | texto interno/notas si existen | slide como imagen | casi siempre necesaria para layout |
| Imagen suelta | lectura visual directa | ficha de figura/tabla | obligatoria |
| DOCX/Markdown | texto directo | imagenes embebidas si existen | solo figuras/tablas criticas |
| Dataset/CSV | lectura estructurada | muestras y diccionario | no visual salvo graficas |

## Niveles de confianza

| Etiqueta | Significado | Uso permitido |
| --- | --- | --- |
| `AUTO_TEXT` | Texto extraido automaticamente | screening, resumen, busqueda |
| `AUTO_LOCATOR` | Texto automatico con pagina/seccion | cita contextual no numerica |
| `VISUAL_READ` | Texto o figura leida desde imagen | descripcion y soporte moderado |
| `TABLE_VERIFIED` | Tabla verificada contra imagen/PDF | parametros y resultados tabulares |
| `FORMULA_VERIFIED` | Formula revisada visualmente | metodo/modelo matematico |
| `FIGURE_INTERPRETED` | Figura descrita con mensaje, ejes y limites | soporte conceptual o grafico |
| `CLAIM_READY` | Claim conectado a fuente, locator, metodo, variable/metrica y limitacion | puede entrar a borrador |
| `PENDING` | Dato incompleto o no verificado | no usar en conclusion |

## Clasificacion de paginas o slides

Cada pagina/slide debe clasificarse cuando sea relevante:

| Clase | Indicadores | Accion |
| --- | --- | --- |
| `normal_text` | parrafos sin tablas ni graficas | texto automatico suficiente |
| `method` | metodo, simulation setup, protocol, algorithm | lectura nivel 2 o 3 |
| `parameters` | Table, parametros, setup, constants | verificar tabla visualmente |
| `formula` | ecuaciones, simbolos, modelos | verificar visualmente |
| `architecture` | diagramas, bloques, flujo | interpretar figura |
| `results` | graficas, tablas de resultados | verificar visualmente antes de claims |
| `limitations` | threats, limitations, discussion | lectura textual cuidadosa |
| `references` | bibliografia | usar para rastreo, no como evidencia directa |

## Estrategia por tamano

| Tamano | Estrategia |
| --- | --- |
| Paper 8-25 paginas | extraer texto completo; renderizar todo si es barato; analizar visualmente solo paginas criticas |
| Documento 26-60 paginas | texto completo; renderizar solo paginas con figuras/tablas/metodo/resultados |
| Documento 60+ paginas | screening textual; mapa de secciones; seleccion de 10-20 paginas criticas |
| PPT 10-40 slides | exportar todos los slides a imagen; ficha por slide critico |
| PPT 40+ slides | texto/notas + thumbnails; lectura visual de slides criticos |

## Campos minimos de ficha multimodal

Para cada fuente importante:

- Identidad: titulo, autores, ano, venue, DOI/URL/ruta.
- Tipo de fuente: PDF, PPT, imagen, dataset, web.
- Metodo de extraccion usado.
- Mapa de paginas/slides criticos.
- Texto automatico disponible.
- Tablas verificadas.
- Figuras interpretadas.
- Formulas verificadas.
- Claims reutilizables.
- Claims prohibidos.
- Datos pendientes.
- Decision: usar, usar con cautela, descartar, pendiente.

## Reglas para calidad

- No citar resultados numericos desde `AUTO_TEXT` si hay tabla/grafica original pendiente.
- No interpretar una figura como evidencia clinica si solo es conceptual.
- No tratar un PPT como paper; registrar que es material de clase, exposicion o soporte visual.
- No tratar notas de YouTube/blogs como evidencia cientifica de dominio; usarlas como workflow si corresponde.
- Si una pagina esta en dos columnas, priorizar imagen o locator por pagina antes de extraer claims.
- Si una formula aparece corrupta, marcar `FORMULA_PENDING` hasta transcripcion visual.

## Resultado esperado

La ingesta no debe terminar en un resumen. Debe terminar en una ficha que permita decidir que se puede afirmar y que no.

Salida minima:

```text
source_id:
tipo:
ruta/url:
metodo_extraccion:
paginas_criticas:
claims_ready:
claims_pending:
claims_prohibidos:
decision:
proximo_paso:
```

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Herramientas usadas: PyMuPDF, pymupdf4llm, render_pdf_pages.py |
| `23_protocolo_pdf_ppt_imagenes.md` | Flujo detallado para PDF/PPT/imagenes — decide textual vs visual |
| `24_flujo_ingesta_a_markdown.md` | Como la salida de este pipeline llega a los markdowns |
| `25_protocolo_latex.md` | Despues de extraer y auditar, el contenido se produce en PDF/Word |
| `26_protocolo_transcripcion_audio.md` | Flujo complementario para contenido de audio |
| `27_protocolo_zotero.md` | Los PDFs guardados en Zotero se procesan con este pipeline |
| `herramientas/extract_pdfs_ibarra.py` | Metodo textual: extraccion completa de PDFs |
| `herramientas/render_pdf_pages.py` | Metodo visual: renderiza paginas criticas a PNG |
