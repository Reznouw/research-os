# Ficha de Clase Día 1 - 2026-08-25 (Prof. Del Carpio Damián, Christian Carlos)

> **Fuente:** Audio de la primera clase del curso 1AEL0260 Proyecto de Investigación
> **Archivo:** `Grabadora - 20260825-1414.m4a.mp4` (2h20m43s, 198.9 MB)
> **Fecha de clase:** 2026-08-25
> **Profesor:** Del Carpio Damián, Christian Carlos
> **Lugar:** `fuentes_originales/transcripciones/Grabadora - 20260825-1414.m4a_transcripcion.md` (3513 segmentos) + `*_texto.txt`
> **Fecha de ficha:** 2026-08-26
> **Modelo ASR:** faster-whisper medium (es, prob=1.0)

---

## Resumen ejecutivo

Esta es la primera clase del curso. El profesor explica el **reglamento completo** artículo por artículo, con aclaraciones prácticas, ejemplos reales, y detalles operativos que **no están en el reglamento escrito**. La clase define el marco del curso: es **formulación, no implementación**; el tema debe definirse en las primeras 3 semanas; el estado del arte es el 90% del trabajo inicial.

**Lo más importante que dijo el profesor (no escrito en el reglamento):**
1. Ya habilitó el aula virtual (sección 6140) con reglamento, PNCTI, ficha de acta, plantillas y ejemplos para EX1.
2. La semana 2 ya deben tener profesor evaluador asignado (después de que se formen grupos).
3. EX1 permite **máximo 2 propuestas**; desde EX2 en adelante solo 1. Si no aprueban en Practica 3, **jalan el curso**.
4. Los 20 minutos de EX1 son a **1x velocidad** — penalidad si ponen video en 2x.
5. El video de EX1 se sube como **enlace en TXT**, no el archivo de video (penalidad si suben el video).
6. Si trabajan con dron, uno del grupo debe tener **licencia MTC**; si trabajan con leche materna, necesitan **permiso del banco de leche**.
7. La tasa de jalados es muy baja — solo jalan los que se cierran en un tema rechazado o descuidan entregables.

---

## 1. Contexto del curso (min 0-15)

### Lo que dijo:
- Octavo ciclo, curso transversal a 3 carreras: Mecatrónica, Biomédica, Electrónica.
- 34 alumnos en la sección 6140.
- **Primer curso donde se formula la tesis** — es muy importante.
- Solo se evalúa **formulación**: problema, objetivos, costo aproximado, métodos, variables, métricas.
- **No hay implementación** en este curso. La implementación es en Proyecto 1 y Proyecto 2 (Capstone, 8 meses total: 4+4, verano no cuenta).
- El curso "no es complicado" si se siguen las pautas; lo complicado es **encontrar el tema**. Una vez definido, el resto fluye.

### Regla práctica:
> El tema debe quedar aprobado máximo en la Practica 3 (semana 12-13). Si no, jalan. Lo normal es que se apruebe en Practica 2 o Parcial (semanas 5-8).

---

## 2. Estado del arte (min 15-35)

### Lo que dijo:
- **90% de lo mencionado** está relacionado con el estado del arte.
- Sirve para saber **qué se ha hecho** y **qué aporte** da tu tesis.
- Sin estado del arte no sabes si lo que haces es distinto a lo ya existente.
- Difieren por áreas (procesamiento de señales, imágenes, IoT) según la carrera.
- Hay artículos de postgrado muy complejos — no hace falta usar sus métodos exactos.
- Hay otra gran parte de artículos con **técnicas similares** a las que usaremos — esos son la guía.
- A partir de ellos se propone: qué mejorar, qué adaptar, qué técnica comparar.

### Estrategias que mencionó:
- Buscar artículos, patentes, productos comerciales.
- Encontrar métodos existentes y proponer: mejora, adaptación, comparación de métodos.
- Lo más importante es **definir el tema** primero.

### Carreras y áreas:
- **Electrónica:** más amplio, procesamiento de señales incluye visión computacional, IA (Machine Learning, Deep Learning), control.
- **Mecatrónica:** más detallado en el reglamento.
- **Biomédica:** también detallado.

---

## 3. Profesores del curso

| Profesor | Rol | Nota |
|---|---|---|
| Del Carpio Damián, Christian Carlos | Profesor principal (quien da la clase) | Sección 6140 |
| Mayor Sánchez | Profesor evaluador | - |
| Salvador Castañeda | Profesor evaluador | - |
| Becerra Felipe | Profesor evaluador | - |

- Cada profesor evaluador atiende **3-5 grupos** (según división por carrera).
- La asignación se hace la **semana 2** después de formar grupos.
- Verificar en `02_grupos_investigacion_1AEL0260.md` para ver qué grupos son de cada carrera.

---

## 4. Sección y aula virtual (min 35-50)

- Sección: **6140**
- NRC: 6140
- El sílabo aún no está en el sistema (LMS), pero el profesor ya habilitó:
  - Requisitos para Mecatrónica
  - **Reglamento** (el que ya ingestamos)
  - **SLAC nacional** (PNCTI de CONCYTEC)
  - **Ficha de acta de asesoría**
  - **Plantillas** para cada evaluación (informe + PPT)
  - **Ejemplos de referencia** (por ahora solo EX1, del ciclo pasado — no perfectos pero bien ordenados)
  - Material de Unidad 1 (normas IEEE, introducción)
- Formato de referencias: **IEEE**

> El profesor indicó que las plantillas y ejemplos para Practica 2, 3, Parcial y Final se habilitarán conforme avance el curso.

---

## 5. Reglamento — Artículo por artículo (aclaraciones del profesor)

### Art. 1-3: Definición, complejidad, áreas
- El tema debe basarse en conocimientos de la **carrera** — no puede ser de postgrado que requiera 1 año más de estudio.
- **Excepción práctica:** Un curso corto de 1 semana (ej. impresión 3D en FABLAB) sí es válido, aunque no esté en la malla. Un tema de postgrado profundo NO es válido.
- Dentro de procesamiento de señales también entra visión computacional e IA (ML, DL).
- Cada tema debe encajar en las áreas → así se asigna el profesor asesor correcto.

### Art. 4: Continuidad en Proyecto 1 y 2
- El tema formulado aquí se **continúa e implementa** en Proyecto 1 y 2 (Capstone / integradores).
- Ahí se aplica "todo" lo aprendido.

### Art. 5: Innovación y PNCTI
- Tesis de pregrado: **no genera nuevo conocimiento** (eso es doctorado). Maestría plantea soluciones nuevas. Pregrado hace: **mejora de algo existente, actualización, aplicar otra técnica, cambiar escenario**.
- Debe haber **diseño, modelamiento matemático, validación** — no basta decir "ya funcionó".
- El tema debe encajar en un **sector productivo / social** y un **área de conocimiento** del PNCTI — pero esto se detalla recién en Practica 2 (no ahora).

### Art. 6: Actitud y responsabilidad
- Se evalúa: responsabilidad, actitud, llegar temprano, buenas prácticas, comunicación, ética.

### Art. 7-8: Grupos
- **Máximo 2 por grupo**, misma carrera. Individual solo si el número total es impar (tema aritmético).
- Van a estar juntos **1 año y medio**: Investigación + Proyecto 1 + Proyecto 2.
- Si hay discrepancias entre compañeros, se conversa y el profesor ayuda a mantener el grupo.
- Formar grupos: hay lista Excel compartida donde deben poner **apellido paterno**, nombre, código **sin la U** (solo números/letras), NRC (6140), carrera, correo UPC (con U) y Gmail.
- La lista solo estará editable **hoy** — después pasa a solo visualización y solo profesores pueden modificar.
- Si alguien está sin pareja y es de la misma carrera, pueden unirse.
- **Se permite trabajar con compañero de otra sección** (ej. jueves), pero: las condiciones las pone el profesor; si tu compañero es de sección virtual y vienes a presencial, debe asistir a esta sección horarios; las evaluaciones serán en la sección que el profesor decida.

### Art. 9: Asistencia

| Dato | Valor |
|---|---|
| Total de clases | 14 (aprox) |
| Clases de evaluación (sin asistencia) | 4 (Practica 2, Practica 3, Parcial, Final) |
| Clases con asistencia obligatoria | ~10 |
| Límite de faltas (25% = DPEI) | **~4 faltas** |
| Consecuencia de 25% | No puedes rendir el Trabajo Final → tu nota máxima es 12 aunque tengas 20 en todo lo previo |
| 25% se calcula sobre clases con asistencia |

**Reglas prácticas:**
- El 25% existe porque "siempre podemos tener un imprevisto" (doctor, trabajo, etc.).
- Si no puedes asistir, envía correo al profesor, pero **no por eso te marcan asistencia** — para eso son las 4 faltas permitidas.
- La lista se toma al inicio de clase, pero el profesor evaluador también verifica quién está en asesorías. Si tomas lista y te vas antes de la asesoría sin avisar, te puede poner **falta**.
- Si debes retirarte, avisa a tu profesor evaluador.

### Art. 10-11: Actas y portafolio

#### Actas — detalles clave que enfatizó:
- **Mínimo 2 preguntas técnicas** para que valga como acta. No vale preguntar "¿va a llover?" o "¿cuántas actas tenemos que subir?".
- El profesor **decide si vale como acta** — no es automático.
- **Firma presencial:** solo el mismo día. No después.
- **Acta virtual (email):** debe enviarse **el mismo día** de la asesoría. Si la mandas el domingo en la noche para la evaluación del martes, el profesor puede no responder y **pierdes esa acta**.
- **Nombre del archivo:** `Acta #-NombreProfesor-AAAA-MM-DD.jpg/pdf` — si lo pones diferente, **penalidad sobre la nota total**.
- **Actas mínimas acumulativas:**

| Evaluación | Mínimo | Detalle (corregido por el profesor) |
|---|---|---|
| Practica 1 (EX1, sem 3) | **0** | No se piden actas |
| Practica 2 (EX2, sem 5-6) | **1** | 1 con profesor evaluador |
| Trabajo Parcial (sem 8) | **3** | 3 con profesor evaluador (dijo que el reglamento dice 7 pero corrigió a 6 para EX3) |
| Practica 3 (EX3, sem 12-13) | **6** | 5 con evaluador + 1 con otro profesor |
| Trabajo Final (sem 16) | **8** | 6 con evaluador + 2 con otro profesor/externo |

> El profesor corrigió el reglamento en este punto: dijo "acá es 8 pero acá es 6 y 2" y "no es 7 es 6 con el profesor evaluador". **Usar 6+2 para TF1.**

- Todas son **acumulativas**: si tienes 3 en el parcial, para EX3 necesitas 3 más (total 6).
- Penalidad por no tener actas: **hasta -3** sobre la nota final de la evaluación.
- Máximo 2 actas con profesional externo en todo el ciclo (cuenta como "otro profesor").
- El acta externa debe consignar **especialidad y número de registro** del colegio profesional.

#### Estrategia de actas que recomendó:
- No esperar a la última semana — generar conforme se avanza.
- Lo ideal es generar en **horario de clase**, no ir a buscar al profesor a otro salón.
- No "coleccionar" actas preguntando cualquier cosa — el profesor decide si vale.

#### Portafolio digital:
- Cada grupo tiene uno en **OneDrive** (asignado por el profesor, necesita correos correctos).
- Acceso: solo los 2 integrantes + su profesor evaluador (+ el profesor admin).
- **No pueden modificar información ya evaluada** — borrar informes, PPT, audios, actas, fichas ya evaluadas es **falta grave** (Reglamento de Disciplina).
- Pueden visualizar y actualizar donde tengan permiso de edición.
- Si subes un archivo con error y aún estás **dentro del plazo**, puedes sobrescribir sin problema. Si ya pasó el deadline y sobrescribes, **hay penalidad** (queda registrada la fecha de modificación).
- No poner actas en la carpeta de informes ni viceversa — todo en su carpeta correcta o hay penalidad.

### Art. 12: Aspectos legales, ambientales, normas técnicas

> Este artículo es crítico — el profesor dio ejemplos concretos:

- **Drones:** Si tu proyecto involucra dron, **uno de los 2 integrantes debe tener licencia MTC** para volar. El permiso de dónde volar no es el problema; la licencia personal sí. Sin licencia, el proyecto no va.
- **Aceite de cannabis:** Requiere permisos y protocolos — no cualquiera puede hacerlo.
- **Leche materna:** Un proyecto del ciclo pasado quería trabajar con leche materna. Pregunta clave: ¿de dónde sacan las muestras? No vale decir "una amiga que está lactando" (muy variable, corto tiempo). Deben gestionar permisos con un **banco de leche** indicando que es para investigación. Después en Proyecto 1/2 generarán artículo y les preguntarán el origen.
- Cualquier componente/sistema debe considerar legal, ambiental y normas técnicas (nacionales e internacionales).

### Art. 13: Innovación vs copia
- Proyecto puede ser **idea completamente nueva** o **mejora/valor agregado** a productos existentes (hardware/software) — lo normal en pregrado.
- No se puede copiar total o parcialmente procesos/diseños de internet y presentarlos como propios → **sanción muy severa**.
- **Es prudente citar:** "Este artículo es exactamente lo que quiero hacer, se cita y se menciona, pero a partir de eso digo qué le falta y qué le agregaré / qué otro método probaré". Eso sí es válido.
- **Confidencialidad:** No compartan su tema con compañeros de otra sección que no sea su evaluador — hubo un caso donde un grupo le contó su tema a otro compañero de otra sección, este lo presentó igual, y el profesor se dio cuenta. Al final se verifica en semana 15 que ningún tema sea **exactamente igual**.
- Temas de otros cursos (ej. "sistemas embebidos" con el prof. Rubén) no todos sirven como tema de tesis — normalmente son solo para fin de curso, no para tesis. 1-2 temas sí llegaron a patente/publicación, pero la mayoría no.

### Art. 14-15: Patrocinador / Aporte al estado del arte
- Patrocinador (carta de empresa/institución) es **opcional**, a criterio del profesor, puede dar un plus a la nota del **Trabajo Final**. Se entrega máximo **semana 15**.
- Si los objetivos del cliente implican un proyecto **netamente tecnológico y poco ingenieril** (no requiere conocimientos mínimos de diseño/fundamentos), se debe priorizar el **aporte al estado del arte**.

### Art. 16-19: Profesores
- Cada clase: 1 hora a 1h15 de clase inicial + luego **asesorías por grupo** con el profesor evaluador.
- Cada asesoría dura **máximo 15 minutos** por grupo.
- Los profesores del curso son los **únicos autorizados** para aceptar/rechazar un proyecto y para ingresar notas.
- El profesor evaluador es responsable del seguimiento y de evaluar ítems + exposición + diapositivas + informes.

### Art. 20-21, 29-32: Entregables y evaluaciones

#### EX1 (semana 3, 10%, 20 min) — Muy detallado por el profesor:

| Entregable | Nombre | Detalle |
|---|---|---|
| PPT diapositivas | `EX1-PPT-PI-6140-2026-2-Apellido1-Apellido2.ppt` | Formato según plantilla |
| PDF diapositivas | `EX1-PPT-PI-6140-2026-2-Apellido1-Apellido2.pdf` | - |
| Word informe | `EX1-Informe-PI-6140-2026-2-Apellido1-Apellido2.doc` | - |
| PDF informe | `EX1-Informe-PI-6140-2026-2-Apellido1-Apellido2.pdf` | Por compatibilidad de versiones |
| Video | Enlace en TXT: `EX1-Video-PI-6140-2026-2-Apellido1-Apellido2` | **Enlace, no archivo de video** |

- **Máximo 2 propuestas** solo en EX1. Si presentan 2, las dos van en el mismo video/PPT/informe.
- Si ya tienen tema claro y lo conversaron con el profesor, pueden presentar **solo 1**.
- Desde **EX2 en adelante solo se presenta 1 tema**. Si no aprobaron EX1, presentan tema nuevo en EX2; si no aprueban EX2, en Parcial; si no aprueban Parcial, en Practica 3. Si no aprueban en Practica 3, **jalan**.
- El video de EX1 es **asíncrono** (no sincrónico). Cada integrante puede estar en su casa, se conectan por Meet/Zoom/WebEx/OBS, comparten diapositiva, **cámara encendida**, presentan cada uno su parte, descargan el video y suben el **enlace** (OneDrive, Drive, etc.) en un TXT. No subir el archivo de video → penalidad.
- **No usar YouTube** (tema confidencialidad para futura patente/artículo) — usar OneDrive/Drive privado.
- **20 minutos a 1x** — no poner video en 2x. Penalidad si excede aunque sea 1 segundo.
- Plantilla EX1: ya uniformizada. Todo lo azul se borra. Distribución de tareas: si ambos ven la propuesta, poner ambos nombres. Si solo uno ve una propuesta, solo su nombre. Si solo hay 1 propuesta, **eliminar la diapositiva de segunda propuesta**.
- Detalle por diapositiva EX1:

| Diapositiva | Qué debe contener |
|---|---|
| Tema de propuesta 1 | "Desarrollo de un sistema/equipo/software/hardware/máquina..." — solo el título |
| Descripción e importancia | ¿Qué pasa? ¿Dónde ocurre? Cada ítem debe contestar y estar **sustentado** |
| Importancia | ¿Por qué es relevante? ¿Consecuencias? ¿A quién beneficia? ¿Aporte al conocimiento? Cada ítem sustentado |
| Breve descripción de la solución | Contribución, 1-2 diapositivas, puede usar imágenes/figuras |
| Viabilidad | 4 puntos: **técnica** (conocimientos + dispositivos), **económica** (no cuadro detallado, solo idea si el costo es asumible), **temporal** (8 meses total Proy 1+2, verificar que el proyecto cabe en ese tiempo), **operativa** (acceso a datos, infraestructura especial) |
| Productos comerciales | **Mínimo 3**, con referencia. Tablas **enumeradas** (Tabla 1, 2, 3). Imágenes con referencia si no son propias |
| Publicaciones científicas | **5 artículos**, con referencia |

#### EX2 (semana 5-6, 10%, 20 min exp + 10 min preguntas) — Asíncrono también (video? ver Titulo siguiente) + presencial

#### TP1 / Parcial (semana 8, 15%, 20 min, síncrono) — Solo exposición, sin preguntas (porque hay muchos grupos)

#### EX3 (semana 12-13, 15%, 25 min exp + 10 min preguntas) — Mitad en sem 12, mitad en sem 13

#### TF1 (semana 16, 40%, 25 min, síncrono) — Todos los grupos

> Los días de evaluación **no hay clases** — solo se va a exponer y uno puede retirarse después.

#### Fondos
- La universidad tiene **concursos de investigación** anuales, pero el responsable del dinero es el **profesor**, no los alumnos.
- Fondos para **publicaciones** (se pagan) y **patentes** (gastos notariales, etc.) — la universidad puede apoyar.
- Normalmente estos fondos se dan en Proyecto 1/2, no en Investigación.

#### Notas — detalles críticos:

| Concepto | Detalle |
|---|---|
| Fórmula PF | 0.10*EX1 + 0.10*EX2 + 0.15*TP1 + 0.15*EX3 + 0.10*DD + 0.40*TF1 |
| TF1 vale 40% | Es donde sale la mejor nota y protege el promedio |
| DPEI (desaprobado por inasistencia) | Si faltas 25%, automáticamente TF1 = 0 → máximo 12 aunque tengas 20 en todo lo demás |
| 25% = ~4 faltas | Sobre ~10 clases con asistencia |
| Evaluaciones no recuperables | Inasistencia a evaluación = 0 |
| Cada evaluación tiene ficha | Exposición (17p) + Informe (3p) + Actas (0 a -3) + Penalizaciones (0 a -3) |
| Cronograma división | Un profesor tiene 4-5 grupos → mitad evalúa semana 5, mitad semana 6 (y viceversa para semana 12-13) |

#### Vestimenta

| Evaluación | Qué ponerse |
|---|---|
| EX1, EX2, Practica 3, Parcial | **Ropa de vestir**: camisa (puede ser con jean y zapatillas, pero no shorts/sandalias). Si es virtual, basta la camisa |
| Trabajo Final | **Terno** (varones) / **Traje cocktail** (damas) |

#### Portafolio — aclaraciones prácticas:
- Deadline: **martes hasta la 1:00 PM** (ejemplo del profesor).
- Si subiste un archivo con error antes del deadline, puedes sobrescribir sin problema.
- Si subes/actualizas **después del deadline**, queda registrada la fecha y hay penalidad.
- Si el portafolio ya fue evaluado y borras/modificas, es falta grave.

---

## 6. Grupos y formación (min 50-90)

- 18 grupos totales (según lista).
- Grupo 17 (Candela Espinoza) incompleto — sin pareja.
- Delegada del curso: María Fernanda (Carbajal Jaeger).
- El profesor sortea grupos por **carrera** — no elige por tema.
- Todos llevan por primera vez el curso (salvo algunos en virtual).
- Semana 2 ya deben estar definidos los grupos + profesores evaluadores → empezar asesorías.
- La nota de exposición es **individual** (diferenciada por alumno): cada uno expone su parte, y puede haber diferencia por la calidad de su exposición o por penalidad (ej. uno llega tarde 5-10 min).
- La nota de informe, formulación y diapositivas es **grupal**.
- Se puede ser proactivo y venir el martes con propuestas en papel para consultar al profesor evaluador.

---

## 7. Información adicional — correos

- Correo Gmail puede ser cualquier correo (no necesariamente gmail, puede ser hotmail), lo importante es que funcione para el portafolio OneDrive.
- Algunos alumnos tienen hasta 3 correos por cambio de carrera.

---

## Reglas adicionales extraídas (no en el reglamento escrito)

| # | Regla | Fuente (min aprox) | Impacto |
|---|---|---|---|
| R94 | El sílabo aún no está en el LMS pero el aula virtual 6140 ya tiene materiales habilitados | Clase min 35-40 | Usar el aula virtual para bajar plantillas |
| R95 | Las plantillas y ejemplos para Practica 2, 3, Parcial y Final se habilitarán conforme avance el curso | Clase min 40-45 | No buscar plantillas de esas evaluaciones aún |
| R96 | En EX1, si presentas 1 propuesta, eliminar la diapositiva de segunda propuesta | Clase min 55 | No dejar diapositiva vacía |
| R97 | En EX1, si presentas 2 propuestas, las dos van en el mismo video/PPT/informe | Clase min 50-55 | Un solo set de 5 archivos para las 2 propuestas |
| R98 | El video de EX1 se sube como enlace en TXT, no el archivo .mp4 (penalidad si subes el video) | Clase min 55-60 | -3 o más puntos |
| R99 | No usar YouTube (confidencialidad para patente/artículo) — usar OneDrive/Drive privado | Clase min 60-62 | Riesgo de publicación anticipada |
| R100 | EX1 video: 20 min a 1x, no 2x (penalidad aunque sea 1 segundo demás) | Clase min 60-65 | -3 puntos |
| R101 | La distribución de tareas en la PPT es personalizable (poner nombre según quién hace cada parte) | Clase min 40-50 | No copiar distribución del ejemplo |
| R102 | Lo azul en las plantillas se borra (son instrucciones) | Clase min 50-55 | No dejar comentarios azules en la entrega |
| R103 | Para viabilidad técnica: conocimientos + dispositivos de ambos integrantes | Clase min 70-75 | No decir "sí" sin verificar ambos saben |
| R104 | Para viabilidad económica: no cuadro detallado, solo decir si el costo es asumible y si hay patrocinador | Clase min 70-75 | No inventar montos |
| R105 | Para viabilidad temporal: verificar que el proyecto cabe en 8 meses (Proyecto 1+2, verano no cuenta) | Clase min 70-75 | Proyecto muy extenso = no viable |
| R106 | Si el profesor rechaza tu tema en EX1, lo puedes justificar mejor en semana 4 y volver a presentar en EX2 | Clase min 55-60 | No esperar hasta la evaluación para convencer |
| R107 | Si el tema no es aprobado en Practica 3 (sem 12-13), jalan el curso (no hay siguiente oportunidad) | Clase min 50-55 | Crítico |
| R108 | No compartir tu tema con compañeros de otra sección antes de que sea aprobado | Clase min 40-45 | Riesgo de copia |
| R109 | Para dron: uno del grupo debe tener licencia MTC | Clase min 40-45 | Sin licencia = proyecto rechazado |
| R110 | Para leche materna: permiso del banco de leche, no vale "una amiga" | Clase min 40-45 | Sin permiso = problema ético/normativo |
| R111 | DPEI: 25% de faltas = no puede rendir TF1 (40%) → nota máxima 12 | Clase min 15-20 | Faltar 4 veces = perder el curso |
| R112 | La lista se toma al inicio pero el evaluador también verifica presencia en asesoría | Clase min 15-20 | Tomar lista y irse = falta |
| R113 | El acta virtual debe enviarse el mismo día; si la mandas tarde, el profesor puede no responder y la pierdes | Clase min 25-30 | Acta perdida |
| R114 | Deadline ejemplo: martes 1:00 PM — subir sobrescribiendo antes = OK, después = penalidad | Clase min 80-90 | Registrar fecha de modificación |
| R115 | La nota de exposición es individual (2-3p diferenciables), informe/formulación/diapositivas es grupal | Clase min 90-95 | Uno puede tener más nota que el otro |

---

## Estado de la transcripción

| Métrica | Valor |
|---|---|
| Segmentos | 3513 |
| Caracteres | ~96,000 |
| Duración | 2h20m43s |
| Calidad ASR | Buena (prob_idioma=1.0, modelo medium) |
| Errores detectados | Transliteración de nombres (Del Carpio → Del Carmen), algunos errores de puntuación |

---

## Qué falta (próximas clases)

- Normas IEEE a detalle
- Búsqueda en Scopus / WOS
- Zotero (Sotero en transcripción) — referencias y citas
- Patentes
- Unidad 1 (introducción)
- Plantillas y ejemplos de Practica 2, 3, Parcial y Final

---

## Cross-links

| Documento | Relación |
|---|---|
| `01_silabus_1AEL0260_2026.md` | Sílabo del curso (misma sección 6140) |
| `02_grupos_investigacion_1AEL0260.md` | Lista de 18 grupos, Grupo 15 = Lozano+Reymundo |
| `03_reglamento_tituloI_caracteristicas.md` | Art. 1-6: definición, áreas, PNCTI |
| `04_reglamento_tituloII_desarrollo.md` | Art. 7-15: grupos, asistencia, actas, portafolio, legal |
| `05_reglamento_tituloIII_profesores.md` | Art. 16-19: rol del profesor, 15 min máx |
| `06_reglamento_tituloIV_entregables.md` | Art. 20-21: nombres de archivos EXACTOS |
| `07_reglamento_tituloV_evaluacion.md` | Art. 22-32: fórmula, fichas, cronograma, tiempos, vestimenta |
| `08_reglamento_tituloVI_penalizaciones.md` | Art. 33-36: penalizaciones, reclamos |
| `09_PNCTI_2006_2021.md` | PNCTI referenciado en Art. 5 |
| `10_ficha_acta_asesoria.md` | Plantilla de acta (Figura 1 del reglamento) |
| `transcripciones/*.m4a_transcripcion.md` | Transcripción completa con timestamps |
| `transcripciones/*.m4a_texto.txt` | Texto plano (material bruto para Renzosky) |
| `transcripciones/*.m4a_metadata.json` | Metadatos estructurados (3513 segmentos) |
