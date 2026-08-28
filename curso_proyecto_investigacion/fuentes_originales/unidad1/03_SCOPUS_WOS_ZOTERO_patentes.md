# Unidad 1 - Busqueda en SCOPUS, WOS, ZOTERO y Patentes

> **Fuentes:** `EL260-02-Busqueda_SCOPUS`, `EL260-03-Busqueda_WOS`, `1AEL0260-04-ZOTERO-2026`, `1AEL0260-06-PATENTES-2026`
> **Fecha de registro:** 2026-08-27
> **CRITICO:** Herramientas obligatorias para construir el estado del arte. Las rubricas de EX3/TP1/TF1 exigen articulos de Scopus y WOS.

---

## 1. SCOPUS

### Que es

La mayor base de datos de resumenes y citas de publicaciones cientificas revisada por pares. Herramientas para evaluar autores, instituciones, tendencias y revistas.

### Cobertura

- Mas de 66 millones de registros
- Mas de 5,000 editoriales
- 22,748 revistas revisadas por pares (3,476 open access)
- 7.7 millones de actas de conferencias
- Areas: cientificas, tecnicas, medicas, sociales, artes y humanidades

### Para que sirve

- Busqueda de temas/articulos para revision de literatura
- Evaluar produccion cientifica de una institucion
- Comprobar produccion de un investigador, citas, indice h
- Descubrir quien te cita y potenciales colaboradores

### Como acceder (UPC)

1. Ingresar a `https://biblioteca.upc.edu.pe/az.php`
2. Buscar `scopus` -> seleccionar primer resultado
3. Ingresar con usuario UPC -> colocar usuario y contrasena
4. Ya logueado como UPC -> ir a `Documents` -> buscar

### Como buscar (ejemplo del curso)

```
Paso 1: Busqueda general  ->  "PRECISION AGRICULTURE"
Paso 2: Delimitar          ->  + "UAV"
Paso 3: Delimitar mas      ->  + "IMAGE PROCESSING"
Paso 4: Aplicar filtros    ->  para reducir resultados
Paso 5: Ordenar            ->  Relevancia / Mas veces citado / Anadidos reciente
Paso 6: Guardar busquedas / Crear alertas para nuevos articulos
```

### Analisis de resultados

Scopus permite: Analisis de resultados, informe de citas, metricas por autor/institucion/revista.

---

## 2. Web of Science (WOS)

### Que es

Base de datos altamente especializada con las revistas cientificas mas impactantes a nivel internacional.

### Que ofrece

- Informacion de mas de 256 areas (ciencias, sociales, artes, humanidades)
- Identifica e indexa las publicaciones mas importantes
- Acceso a texto completo (segun suscripcion institucional)
- Creacion de bibliografias con gestores bibliograficos
- Comparativos estadisticos en referencias indexadas

### Como acceder (UPC)

1. Ingresar a `https://biblioteca.upc.edu.pe/az.php`
2. Buscar `web of science` -> seleccionar primer resultado
3. Ingresar con usuario UPC
4. Cambiar idioma si es necesario

### Como buscar

```
Campos: AUTOR, TITULO, TEMA, otros
Operadores: AND, OR, NOT
Filtros: Intervalo de fechas, base de datos dentro de WOS
Crear cuenta para guardar busquedas

Ejemplo del curso:
  "PRECISION AGRICULTURE" -> + "UAV" -> + "IMAGE PROCESSING"
  -> Aplicar filtros -> Ordenar por Relevancia/Citas -> Informe de citas -> Analisis
```

---

## 3. ZOTERO (Gestor de referencias)

### Que es

Gestor de referencias bibliograficas **gratuito, de codigo abierto**, asistente personal de investigacion. Recolecta, organiza, cita y comparte fuentes (articulos, libros, paginas web, PDFs).

### Caracteristicas

- Guarda referencias con 1 click desde el navegador (Chrome, Firefox, Safari, Edge) — detecta automaticamente autor, titulo, fecha.
- Organiza en **colecciones** (carpetas) y **etiquetas** (tags).
- Adjunta PDFs, notas, capturas.
- Se integra con **Word, Google Docs, LibreOffice** — inserta citas y genera bibliografias en miles de estilos (APA, Vancouver, **IEEE**, MLA).

### Instalacion

| Paso | Accion |
|---|---|
| 1 | Ir a `https://www.zotero.org/` -> Log In -> crear cuenta |
| 2 | Download -> Zotero 8 para Windows -> instalar -> icono en escritorio |
| 3 | Instalar extension de Zotero para Chrome (permite importar metadatos) |
| 4 | En Word aparece la pestana Zotero |

### Flujo de uso (curso)

```
1. Buscar articulo en Scopus
2. Seleccionar publicacion -> Full text -> View at Publisher
3. En la revista, con Zotero instalado, click en icono de Zotero en el navegador
   (debe estar abierta la app de escritorio)
   -> Todos los metadatos se extraen automaticamente
4. En Zotero escritorio aparecen los metadatos
5. Repetir para cada articulo

Para citar en Word:
  a) Seleccionar articulo en Zotero
  b) En Word -> pestana Zotero -> Add/Edit Citation
  c) Caja flotante: seleccionar articulo -> doble click
  d) Aparece la citacion en formato IEEE -> Aceptar

Para bibliografia:
  -> Add/Edit Bibliography -> Zotero escanea y coloca todas las referencias
  (cursor debe estar donde se quiere insertar)
```

> Lo mismo aplica para Google Docs (icono Zotero en la barra de herramientas, seleccionar estilo de cita).

### Verificacion

```powershell
& "C:\Program Files\Zotero\zotero.exe"
# Verificar Better BibTeX: Tools -> Add-ons -> debe aparecer si esta instalado
```

---

## 4. Patentes

### Que es una patente

Titulo otorgado por el Estado que confiere a su titular el derecho de **excluir a terceros** de la explotacion de una invencion (reproducir, vender, usar, aprovechar sin consentimiento), por un tiempo y territorio determinados, si cumple los requisitos legales.

### Tipos (Peru)

| Tipo | Que protege | Duracion | Requisitos |
|---|---|---|---|
| **Patente de invencion** | Productos o procedimientos | **20 anos** | Novedad + Nivel inventivo + Aplicacion industrial |
| **Patente de modelo de utilidad** | Solo productos | **10 anos** | Novedad + Ventaja tecnica |

- **Novedad:** No divulgada ni accesible al publico de ninguna forma.
- **Nivel inventivo:** Para una persona con conocimientos tecnicos medios, el invento no se deriva de forma evidente de tecnologias existentes.
- **Ventaja tecnica:** Nueva forma/configuracion/disposicion que permite mejor/diferente funcionamiento, utilizacion o fabricacion.
- **Aplicacion industrial:** Puede ser producido o utilizado en alguna aplicacion particular.

### Bases de datos (~110 millones de documentos)

| Base | Descripcion | Enlace |
|---|---|---|
| **Espacenet** | Oficina Europea de Patentes (EPO). 95+ millones de patentes. | https://worldwide.espacenet.com/ |
| **Patentscope** | OMPI. 50+ millones de documentos (PCT + oficinas nacionales). | https://patentscope.wipo.int/search/en/search.jsf |
| **Google Patents** | Google. 87+ millones de patentes de 17 oficinas. | https://patents.google.com/ |

> Fuentes: Osorio, M. (2017). Guia de patentes para investigadores. Lima: Indecopi.
> Indecopi (2020). Guia para investigadores en el uso de bases de datos de patentes.

### Relevancia para el curso

Las rubricas de EX3/TP1/TF1 piden: "¿Presenta adecuadamente el estado del arte de **soluciones, patentes** y de articulos cientificos de revistas/conferencias indizadas en **Scopus y WOS**?"

-> Cada entrega debe incluir: **productos comerciales + patentes + articulos Scopus/WOS**.

---

## Flujo completo para el estado del arte

```
1. Buscar en SCOPUS / WOS con palabras clave del tema
   (ej. "FPGA Edge AI inference", "quantization FPGA", "HLS neural network")
   -> Guardar busquedas + crear alertas
        ↓
2. Buscar patentes en Espacenet / Patentscope / Google Patents
   (ej. "FPGA neural network accelerator", "quantized CNN FPGA")
        ↓
3. Guardar cada articulo/patente en Zotero (1 click)
   -> Organizar en colecciones por tema
        ↓
4. Leer y fichar cada fuente -> crear ficha en fichas_papers/
   -> Fortalezas, debilidades, contribucion del proyecto
        ↓
5. Citar en el informe/PPT en formato IEEE
   -> Zotero inserta citas [X] y genera bibliografia automaticamente
```

---

## Cross-links

| Documento | Relacion |
|---|---|
| `02_normas_IEEE.md` | Formato IEEE obligatorio para citar lo encontrado en Scopus/WOS |
| `05_situacion_problematica.md` | La situacion problematica debe estar sustentada con este estado del arte |
| `11_plantilla_PPT_EX1.md` | Tabla 1 (productos) + Tabla 2 (publicaciones) provienen de estas busquedas |
| `13_ejemplo_referencial_PPT_EX1.md` | El ejemplo uso Scopus/WOS para sus 5 articulos |
| `27_protocolo_zotero.md` (auditoria) | Protocolo de gestion bibliografica con Zotero |
