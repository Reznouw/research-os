# Ejemplo Referencial Informe EX1 - Ciclo anterior (con evaluacion)

> **Fuente:** Aula virtual 6140 - `Ejemplo 1 - Referencial - EX1 - Informe`
> **Fecha de registro:** 2026-08-26
> **Autores del ejemplo:** Arias Rossell, Jorge Mauricio – 2681 + Cristobal Campos, Rosario de Fatima – 2681
> **Carrera:** Ingenieria Mecatronica
> **Profesor Evaluador:** Del Carpio Damian, Christian Carlos
> **Tema:** Desarrollo de una maquina automatica para el sellado, corte, doblado y empaquetado de envolturas flexibles de polietileno (PET).
> **ADVERTENCIA DEL PROFESOR:** "No es el mejor mejor trabajo pero es uno de los mas buenos que me toco asesorar. Pero no que sea siempre al pie de la letra porque tuvo sus errores tambn"
> **Nota:** El texto original tiene errores de OCR (tildes mal codificadas). Se preserva el contenido semantico; los caracteres con `´` son artefactos de extraccion, no errores de redaccion del autor.

---

## Estructura del informe (secciones 4.3-6 + Referencias)

> **Nota:** El ejemplo disponible comienza en la seccion 4.3 (viabilidad temporal). Las secciones 1-4.2 (tema, descripcion, importancia, solucion, viabilidad tecnica/economica) no estan en el texto proporcionado, pero siguen la misma estructura que el PPT.

---

### 4.3. Viabilidad temporal

```
El proyecto se considera viable en terminos de tiempo, dado que se ha propuesto un tiempo de ejecucion total de 18 meses, abarcando el tiempo de investigacion, diseno, prototipado y las pruebas.
```

### 4.4. Viabilidad operativa

```
El proyecto es tecnicamente viable ya que se empleara tecnologia ya usada en industria como rodillos, actuadores neumaticos, elementos calefactores como nicromo o kanthal, corte hecho por cuchillas o laser y un doblado basado en rodillos para tension y varas para guias.
```

**ERRORES (advertidos):**
- 4.3 y 4.4 estan **intercambiados** igual que en el PPT: 4.3 deberia ser tecnica y 4.4 operativa. En este informe estan igual de cruzados.
- 18 meses es para la tesis completa; para el curso de Investigacion, verificar que la **formulacion** cabe en el semestre + que la **implementacion** cabe en 8 meses (Proyecto 1+2).

---

### 5. Productos y soluciones comerciales

```
En la Tabla 1, se presenta diversas maquinas existentes que solucionan parcialmente la problematica a resolver.

Tabla 1. Productos comerciales existentes
N° | Nombre del producto, modelo y foto | Fabricante y costo | Funcion (breve descripcion) | Ventajas | Desventajas
1 | Selladora de bandas continuas para bolsas de plastico de alimentos LT-PM1800 [1] | YTK / 300$ USD | Es una selladora continua por donde entra la bolsa sin sellar, es transportada entre los elementos termicos y sellada | - Es una selladora continua por lo que no hay maximo de largo / - Sella a una velocidad de 0-12m/min / - Tiene un minimo de grosor de 0.02mm | - Al tener una posicion fija hace inconveniente sellar bolsas de distintos tamanos / - Proceso manual, no tiene corte ni doblado.

2 | Dobladora y cortadora de bolsas SDH-2625 [2] | S-DAI / 20000$ USD | Maquina que dobla, corta y sella bolsas a partir de una pelicula de plastico | - Alta velocidad de produccion 250pcs/min / - Trabaja de manera continua | - Tiene un tamano demasiado grande relativo al tamano de las bolsas salientes / - Produce bolsas de tamano pequeno para vitrina en tienda

3 | Cortadora y selladora de bolsas TW600 [3] | Wenzhou Tuowei / 5000-10000$USD | Sellado lateral y corte en caliente, controlado por computadora. | - Alta velocidad de produccion / - Trabaja de manera automatica | - Requiere un ajuste fino / - No realiza doblado de bolsas

4 | Fabricadora de bolsas con sellado inferior ZXL-A700 [4] | Zhejiang Zhengxin Machinery / 40000-58000$ USD | Produccion automatica de bolsas con sellado inferior. | - Produccion masiva. / - Totalmente automatica. | - Costo excesivo / - No cumple con los requisitos de dimensionado de bolsas del cliente
```

**Observacion:** Mismo contenido que el PPT (4 productos), formato de tabla Word con foto, fabricante, costo, funcion, ventajas, desventajas. En el texto: "En la Tabla 1, se presenta..." — describe la tabla en el parrafo antes.

---

### 6. Publicaciones cientificas/Academicas/Ingenieriles

```
A continuacion, en la Tabla 2, se presentan varias publicaciones cientificas entorno al proyecto a desarrollar.

Tabla 2. Publicaciones cientificas/academicas/Ingenieriles
N° | Titulo de la publicacion | Datos de la publicacion | Fortalezas de la publicacion | Debilidades de la publicacion | Contribucion de la propuesta
1 | Estimating minimum required dwell time for the heat sealing of talc containing polypropylene/low-density polyethylene packaging films | - Tipo de Publicacion: Articulo / - Autores: Ilhan, Ilknur van; Drongelen, Martin; ten Klooster, Roland; Gibson, Ian / - Medio indexado y datos: Wiley Online Library / - DOI: doi.org/10.1002/pts.2716 / - ISSN: 0894-3214 / - Volumen: pp. 349 - 361 / - Ano: 2023 | - Analiza el proceso de sellado por temperatura en peliculas plasticas / - Determina el tiempo minimo de sellado basado parametros fisicos como conduccion de calor / - Relaciona variables de temperatura, tiempo y propiedades de deformacion. | - Se enfoca en materiales PP/PE, no especificamente en PET. / - No incluye diseno de maquinaria. / - No integra procesos de doblado ni corte. | - Implementa estos modelos en un sistema real de sellado para PET. / - Integra el control termico con corte sincronizado. / - Realiza la teoria en una maquina funcional automatizada.

2 | AUTOMATIC FOLDING AND COUNTING TSHIRTS USING PLC | - Tipo de Publicacion: Conference Paper / - Autores: M. Thangatamilan; S.J. Suji Prasad; R. Sureshkumar; T. Subiksha; D. Vigneshwaran; P. Pradeep / - Medio indexado y datos: iTech SECOM / - DOI: doi.org/10.1109/iTechSECOM64750.2025.11307494 / - ISBN: 979-833157175-7 / - Volumen: pp. 1-6 / - Ano:2019 | - Propone un sistema automatizado basado en PLC para doblado, a materiales flexibles. / - Sustituye procesos manuales, mejorando productividad y precision. / - Usa sensores y control industrial, alineado con el enfoque del proyecto | - Aplicado a textiles (camisetas), no a peliculas plasticas. / - No integra procesos de sellado y corte. / - Nivel de prototipo, no industrial. | - Adapta el doblado a manga plastica continua de PET. / - Integra el doblado con sellado y corte en linea. / - Implementa control PLC en un proceso industrial completo.

3 | Design of Automatic Feed Packaging Machine with Robotic Arm | - Tipo de Publicacion: Conference paper / - Autores: Peiming Peng; Weilin Zheng; Xiaolan Tan; Lianyao Tang; Yage Wang / - Medio indexado y datos: Lecture Notes in Mechanical Engineering / - DOI: doi.org/10.1007/978-981-97-7887-4_4 / - ISSN: 2195-4356 / - Volumen: pp. 41-53 / - Ano: 2025 | - Disena una maquina automatica que realiza formado de bolsa, sellado y corte. / - Incluye mecanismos de alimentacion, transporte y sellado termico. / - Presenta una arquitectura completa de sistema industrial automatizado. | - Enfocado en empaquetado de productos granulados, no en fabricacion desde manga PET. / - Uso de robot industrial puede aumentar complejidad y costo. / - No detalla sistema de doblado. | - Simplifica el sistema para uso academico/industrial accesible. / - Anade modulo de doblado previo. / - Reduce costo y complejidad manteniendo funcionalidad.

4 | Packaging and storage of spices | - Tipo de Publicacion: Book Chapter / - Autores: S. Anandakumar; R. Visvanathan / - Medio indexado y datos: Springer Nature Link / - DOI: doi.org/10.1007/978-981-19-3728-6_68 / - ISBN: 978-981193728-6, 978-981193727-9 / - Volumen: pp. 4263-4292 / - Ano:2023 | - Sustenta la integracion de mecanismos, sensores y lazos de control. / - Apoya el diseno estructural de maquinaria automatizada. / - Enfoque en eficiencia y optimizacion de procesos. | - No esta enfocado en bolsas plasticas. / - No aborda procesos como sellado termico o corte. / - Requiere adaptacion de los conceptos. | - Aplica estos principios a un caso real especifico (bolsas PET). / - Integra mecanica, control y proceso en una maquina funcional.

5 | Reconfigurable Magnetic Origami Actuators with On-Board Sensing for Guided Assembly | - Tipo de Publicacion: Article / - Autores: Ha, Minjeonga; Canon Bermudez, Gilbert Santiagoa; Liu, Jessica A.-C.b; Oliveros Mata, Eduardo Sergioa; Evans, Benjamin A. / - Medio indexado y datos: Wiley Online Library / - DOI: doi.org/10.1002/adma.202008751 / - ISSN: 09359648 / - Volumen: 33 / - Ano:2021 | - Proporciona bases avanzadas sobre polimeros. / - Permite entender comportamiento mecanico para el doblado de materiales / - Relacionado con tecnologias modernas de procesamiento. | - Enfoque en materiales avanzados, no en maquinaria. / - Aplicacion mas teorica que practica. / - No incluye integracion de procesos industriales. | - Traduce propiedades del material a parametros reales de maquina. / - Aplica teoria a sellado, doblado y corte de PET. / - Conecta ciencia de materiales con manufactura aplicada.
```

**Observacion:** 5 publicaciones con datos completos: tipo, autores, medio, DOI, ISSN, volumen, ano, fortalezas, debilidades, contribucion. En el texto: "A continuacion, en la Tabla 2, se presentan..."

---

### Referencias

```
[1] Zhejiang Lianteng Intelligent Equipment Co., Ltd. "LT-PM1800 Industrial Continuous Plastic Food Bag Band Sealer Machine with Inkjet Printer" [Online]. Available: https://www.liantengmachines.com [Accessed: Apr. 14, 2026].
[2] S-DAI INDUSTRIAL CO., LTD. "Side Sealing Machine Auxiliary Equipment" [Online]. Available: https://www.s-dai.com.tw/en/machines/bag_folding_machine.html [Accessed: Apr. 14, 2026].
[3] TOWIN MACHINERY. "High Speed Computer Hot Cutting Side Sealing Bag Making Machine" [Online]. Available: https://cuttingmachine.en.made-in-china.com [Accessed: Apr. 14, 2026].
[4] Zhejiang Zhengxin Machinery Co., Ltd. "Maquina para fabricar bolsas no tejidas ZX multifuncion de ultra alta velocidad, para camisetas, bolsas con cordon de corte en D, 2 unidades" [Online]. Available: https://www.alibaba.com/product-detail/ZXL-A700 [Accessed: Apr. 14, 2026].
[5] Wiley Online Library "Estimating minimum required dwell time for the heat sealing of talc containing polypropylene/low-density polyethylene packaging films" [Online]. Available: doi.org/10.1002/pts.2716 [Accessed: Apr. 14, 2026].
[6] iTech SECOM "AUTOMATIC FOLDING AND COUNTING TSHIRTS USING PLC" [Online]. Available: doi.org/10.1109/iTechSECOM64750.2025.11307494 [Accessed: Apr. 14, 2026].
[7] Lecture Notes in Mechanical Engineering "Design of Automatic Feed Packaging Machine with Robotic Arm" [Online]. Available: doi.org/10.1007/978-981-97-7887-4_4 [Accessed: Apr. 14, 2026].
[8] Springer Nature Link "Packaging and storage of spices" [Online]. Available: doi.org/10.1007/978-981-19-3728-6_68 [Accessed: Apr. 14, 2026].
[9] Wiley Online Library "Reconfigurable Magnetic Origami Actuators with On-Board Sensing for Guided Assembly" [Online]. Available: doi.org/10.1002/adma.202008751 [Accessed: Apr. 14, 2026].
```

**9 referencias totales** (4 productos + 5 publicaciones), formato IEEE, con URL y fecha de acceso [Accessed: Apr. 14, 2026].

---

## Diferencias entre PPT e Informe (observadas)

| Aspecto | PPT (20 slides) | Informe (Word) |
|---|---|---|
| Viabilidad | Diapositivas separadas por tipo (4 bullets) | Texto corrido por parrafo (4.x) |
| Productos | Tabla 1 repetida en 4 slides (uno por producto) | Tabla 1 unica con 4 filas |
| Publicaciones | Tabla 2 repetida en 5 slides (uno por articulo) | Tabla 2 unica con 5 filas |
| Referencias | 2 slides (productos + publicaciones) | Lista final continua |
| Extension | 20 diapositivas | ~5 paginas (estimado) |

---

## Que aprendemos para Grupo 15 (FPGA Edge AI)

| Aspecto | Leccion del ejemplo | Aplicacion a nuestro proyecto |
|---|---|---|
| Viabilidad | Error: etiquetas cruzadas | Verificar que cada viabilidad tenga el contenido correcto |
| Productos comerciales | Buscar 4 (minimo 3) con: foto, fabricante, costo, funcion, ventajas, desventajas | Buscar aceleradores FPGA, placas DE10-Nano, Jetson Nano, Coral Edge TPU, etc. |
| Publicaciones | 5 articulos con: fortalezas, debilidades, contribucion del proyecto | Buscar 5 papers sobre FPGA + Edge AI, quantization, HLS, etc. |
| Tablas | Enumeradas (Tabla 1, Tabla 2), descritas en el texto ("En la Tabla X...") | Misma regla para nuestro informe |
| Referencias | 9 referencias IEEE con DOI y fecha de acceso | Usar Zotero + formato IEEE |
| Nivel del ejemplo | "Uno de los mas buenos" pero con errores | Apuntar a superar este nivel corrigiendo los errores |

---

## Cross-links

| Documento | Relacion |
|---|---|
| `13_ejemplo_referencial_PPT_EX1.md` | PPT del mismo proyecto (formato diapositivas) |
| `11_plantilla_PPT_EX1.md` | Plantilla oficial de PPT de EX1 (estructura que sigue este ejemplo) |
| `12_plantilla_informe_EX1.md` | Plantilla oficial de informe de EX1 |
| `FICHA_CLASE_DIA1_2026-08-25.md` | Clase donde se presento este ejemplo como referencial |
| `06_reglamento_tituloIV_entregables.md` | Art. 20-21: nombres EXACTOS de archivos |
| `07_reglamento_tituloV_evaluacion.md` | Figura 3: rubrica EX1 + Art. 27: requisitos de informe |
