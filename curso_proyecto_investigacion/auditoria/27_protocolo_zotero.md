# 27 Protocolo de gestion bibliografica con Zotero

> **Como usar Zotero para guardar papers, gestionar referencias, exportar BibTeX, y producir bibliografia para LaTeX/Word.**
> Herramienta: `Zotero` (local) + `Better BibTeX` (plugin pendiente).
> Conecta con: protocolo 25 (LaTeX), herramienta `transcribir_audio.py`, scripts de extraccion PDF.

---

## Pipeline

```
Paper PDF / URL / DOI / ISBN
    ↓
Zotero (guardar + metadatos + PDF adjunto)
    ↓
Better BibTeX (exportar .bib estable)
    ↓
LaTeX: \bibliography{references}
    Word: styles APA/Vancouver desde Zotero
```

---

## Comandos de uso

### Abrir Zotero

```powershell
& "C:\Program Files\Zotero\zotero.exe"
```

### Guardar paper desde PDF local

1. Zotero → archivo → Importar...
2. Seleccionar PDF
3. Zotero busca metadatos automaticamente (via DOI)
4. Verificar: autor, titulo, year, DOI, abstract

### Guardar paper desde URL/DOI

1. Copiar DOI/URL
2. Zotero → boton "Add Item(s) by Identifier" (catalogo icon)
3. Pegar DOI/URL
4. Zotero busca metadatos + descarga PDF si esta disponible

### Guardar paper desde navegador (Zotero Connector)

1. Instalar Zotero Connector (Chrome/Firefox/Edge)
2. En la pagina del paper → click icono Zotero
3. Se guarda automaticamente con PDF adjunto

---

## Exportar a BibTeX (para LaTeX)

### Opcion A: Better BibTeX (RECOMENDADO, pendiente instalar)

1. Instalar Better BibTeX desde https://retorque.re/zotero-better-bibtex/
2. En Zotero → clic derecho en coleccion/item → Exportar coleccion
3. Seleccionar "Better BibTeX"
4. Guardar como `references.bib` en `latex/proyecto/`
5. Better BibTeX genera keys estables que no cambian al re-exportar

### Opcion B: BibTeX nativo (sin Better BibTeX)

1. Zotero → Exportar coleccion → formato "BibTeX"
2. Guardar como `references.bib`
3. Limitacion: los keys cambian al re-exportar si no se fijan manualmente

---

## Estructura de la biblioteca

### Colecciones sugeridas

```
Mi Biblioteca
├── Proyecto_Tesis_FPGA
│   ├── Edge_AI_Literature
│   ├── FPGA_Synthesis
│   ├── Model_Compression
│   ├── Hardware_Design
│   └── Ultralytics_YOLO
├── Curso_1AEL0260
│   ├── Syllabus_y_reglamento
│   └── Papers_del_curso
└── Papers_Interes_General
```

### Tags sugeridos

- `tipo:paper`, `tipo:tesis`, `tipo:libro`, `tipo:conferencia`
- `tema:fpga`, `tema:edge-ai`, `tema:model-compression`, `tema:quantization`
- `relevancia:alta`, `relevancia:media`, `relevancia:baja`
- `metodo:simulacion`, `metodo:experimental`, `metodo:revision`
- `estado:leido`, `estado:por-leer`, `estado:fichado`

---

## Flujo completo con el sistema de investigacion

```
1. Guardar paper en Zotero (PDF + metadatos)
   ↓
2. Leer paper con scripts de extraccion (protocolo 21-23):
   py herramientas/extract_pdfs_ibarra.py (si es PDF largo)
   py herramientas/render_pdf_pages.py (si hay figuras criticas)
   ↓
3. Crear ficha del paper en propuesta/fichas_papers/
   ↓
4. Exportar BibTeX desde Zotero → references.bib
   ↓
5. Usar en LaTeX (protocolo 25):
   \cite{key_del_paper} en el .tex
   \bibliography{references} al final
   ↓
6. Compilar: latexmk -pdf main.tex
```

---

## Better BibTeX - Instalacion pendiente

Better BibTeX es un plugin de Zotero que:
- Genera keys BibTeX estables (no cambian al re-exportar)
- Permite auto-actualizar el .bib cuando se agregan papers
- Soporta citation keys personalizadas
- Se instala desde la interfaz de Zotero: Tools → Add-ons → Install Add-on From File

**Estado actual:** Pendiente. Se instala cuando el usuario confirme que tiene Zotero abierto y listo.

---

## Verificacion

```powershell
# Verificar que Zotero esta instalado
& "C:\Program Files\Zotero\zotero.exe" --version

# Verificar Better BibTeX (despues de instalar)
# En Zotero: Tools → Add-ons → Better BibTeX debe aparecer como activo
```

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Registra Zotero como herramienta instalada |
| `22_pipeline_ingesta_multimodal.md` | Cuando se extrae texto de un PDF guardado en Zotero, sigue ese pipeline |
| `23_protocolo_pdf_ppt_imagenes.md` | Los PDFs guardados en Zotero se procesan con los flujos de este protocolo |
| `24_flujo_ingesta_a_markdown.md` | La ficha del paper se genera desde la extraccion → markdown |
| `25_protocolo_latex.md` | El .bib exportado desde Zotero se usa en \bibliography{references} |
| `26_protocolo_transcripcion_audio.md` | Si hay audio de una clase, se transcribe y se referencia en la bibliografia si aplica |
| `herramientas/extract_pdfs_ibarra.py` | Extrae texto de PDFs que pueden estar guardados en la carpeta de Zotero |
| `herramientas/render_pdf_pages.py` | Renderiza figuras criticas de papers guardados en Zotero |
