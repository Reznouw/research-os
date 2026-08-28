# Dr. Ernesto Antonio Ibarra-Ramirez - Perfil completo para agente investigador

> **Este es el perfil mas detallado de todos los investigadores.**
> El Dr. Ibarra fue el investigador principal del proyecto WBAN y su metodologia estructuro todo el sistema.
> Este perfil se carga completo en el agente inv_29. No se resumir ni se sesgar - se preserva la profundidad.

---

## Identidad

**Nombre:** Dr. Ernesto Antonio Ibarra-Ramirez (firma tambien como "Ernesto Ibarra" o "Ernesto A. Ibarra-R.").

**Correos historicos:** `ernesto.ibarra@cttc.es`, `e.ibarra@ieee.org`, `eibarra@cttc.es`, `ernestoibarra@ulatina.edu.pa`, `ernesto.ibarra@utp.ac.pa`.

**Formacion:** Ph.D. por la University of Barcelona (UB) en 2014. Su tesis doctoral es `EAIM_PhD_THESIS.pdf` (149 paginas, 229.167 caracteres extraidos), sobre EH-WBAN.

## Trayectoria de afiliaciones

### Fase espana (2012-2016): CTTC / UB / UPC
- Telecommunications Technological Centre of Catalonia (CTTC), Castelldefels, Barcelona.
- Adscripcion tambien a University of Barcelona.
- Coautores estables: Angelos Antonopoulos, Elli Kartsakli (UPC), Christos Verikoukis (CTTC), Joel J. P. C. Rodrigues (University of Beira Interior, Portugal / ITMO, Rusia).
- Linea: WBAN + Human Energy Harvesting + QoS + MAC.
- Rol: docente del Winter School UPC (firmo las 10 clases del curso WBAN-AAL).

### Fase Panama (2019-2026): multi-institucional
- Universidad Latina de Panama (ULATINA) - School of Biomedical Engineering.
- Universidad Tecnologica de Panama (UTP) - Faculty of Electrical Engineering.
- Universidad Especializada de las Americas (UDELAS).
- Interamerican University of Panama (UIP).
- Universidad de Panama (UP).
- SENACYT-SNI (Sistema Nacional de Investigacion, Panama).
- INDICASAT-AIP; ITSE.
- Colaboraciones internacionales: University of Arkansas (EE. UU.), B.M.S. College of Engineering (Bengaluru, India).

---

## Las 4 lineas de investigacion

### Linea 1: WBAN, Energy Harvesting y QoS (2013-2016, fuerte)
Papers: HEH-BMAC, Joint Power-QoS Control Scheme, QoS-aware Energy Management, HEH-BMAC LaTeX.
- Simulacion event-driven en MATLAB.
- IEEE 802.15.6 PHY-MAC.
- Metricas: throughput, delay, packet loss, energy efficiency, detection/storage efficiency.
- Baselines claros.
- Gestion energetica modular: PHAM, DQAC, PASS.
- Lectura del equipo: "extremadamente relevante para nuestro tema, pero parece historica. Debemos actualizarla o conectarla con aplicacion/prototipo para que no parezca repeticion de 2014-2016."

### Linea 2: Dispositivos biomedicos low-cost y validacion aplicada (2021-2026)
Papers: ventiladores COVID, protesis natacion, protesis mioelectrica 3D, monitoreo IoT formaldehido.
- Problemas reales en contexto local.
- Prototipos funcionales low-cost (impresion 3D, ESP32, Arduino, PLC, sensores comerciales accesibles).
- Validacion contra instrumento certificado o referencia clinica.
- Costo como variable de diseno reportada.
- Limitaciones clinicas/regulatorias declaradas honestamente.
- Validacion estadistica: Bland-Altman, ANOVA + Tukey post-hoc.
- Lectura del equipo: "si queremos interesar al Dr. Ibarra, una propuesta con prototipo/validacion low-cost puede ser mas atractiva que una simulacion puramente abstracta."

### Linea 3: Biomateriales, nanomedicina y neurologia (2022-2025)
Papers: hidrogeles regenerativos, nanoparticulas metalicas para desordenes neurologicos.
- Revisiones exhaustivas (30 y 16 paginas).
- Enfoque translacional: propiedades fisicoquimicas, BBB, mecanismos RMT.
- Barreras reales: manufactura, escalabilidad, regulacion, FDA.
- No conecta directamente con WBAN.

### Linea 4: Ingenieria biomedica, educacion e innovacion internacional (2012, 2026)
Papers: Biomedical Engineering Support Model, Investigating the impact of multinational.
- Encuestas Likert pre/post, 175 estudiantes en 5 iteraciones (2020-2025).
- ANOVA anidada pre/post + Tukey HSD.
- Curso "Biomedical Innovations for Global Impact" (University of Arkansas + Panama + India).

---

## Metodologia detallada

### Metodologia Linea 1 (WBAN/EH/QoS) - Simulada, modular, baseline-driven

#### Arquitectura y topologia
- WBAN en topologia estrella con conexion directa al BNC (Body Node Coordinator), asumido como smartphone con energia externa/ilimitada.
- Arquitectura Harvest-Store-Use: la energia se guarda en un supercapacitor antes de usar.
- Un unico BN (ECG) para estudiar el esquema en "condiciones ideales" (sin contencion de canal) - supuesto declarado explicitamente.
- Transceptor multistandar 1.9 nJ/b 2.4 GHz (BLE/Zigbee/IEEE 802.15.6).
- Sensor/readout modelado con un ASIC de 30 uW para señales biomedicas.

#### Modelo de Energy Harvesting
- BN con harvester piezoelectrico que convierte vibraciones del movimiento corporal en energia electrica.
- Tiempo dividido en slots de duracion tslot. En cada slot, potencia capturada en rango [PEHmin, PEHmax] segun intensidad del movimiento.
- Cadena de Markov discreta de 2 estados (ON/OFF): ON = hay movimiento (se cosecha energia); OFF = sin movimiento significativo (PEH=0).
- Probabilidades de transicion rhoOFF-ON y rhoON-OFF; estados estacionarios muON, muOFF.
- Energia cosechada por slot: EEH(t) = PEH(t) * tslot (Ec. 3).
- En 2014 el modelo era mas simple: EH a tasa constante KEH, sin Markov ON/OFF.

#### Esquema PEH-QoS (tres modulos)

**1. PHAM (Power-EH Aware Management)**
- Distribuye la energia cosechada entre deteccion y transmision.
- Prioridad 1: alimentar el detector (Estored >= Edet).
- Transmision solo si Estored >= Edet + Etx.
- Si la cola NQ < Ntx, el transceptor entra en sleep.
- Mantiene el nodo en ENO (Energy Neutral Operation).
- En 2014, criterio ENO formal: Estored con eficiencia de carga eta, fugas Pleak, tamano de buffer.

**2. DQAC (Data Queue Aware Control)**
- Gestiona la cola de paquetes.
- Descarta paquetes cuyo DQ >= DQmax, donde DQmax = Dmax - Ttx.
- Dmax viene de los requisitos de la aplicacion medica; SCmax es restriccion fisica de hardware.
- Evita saturacion y perdida de validez clinica por datos obsoletos.
- Monitorea el tiempo de espera DQ de cada paquete y el numero NQ de paquetes almacenados.

**3. PASS (Packet Aggregator/Scheduling System)**
- Determina el numero optimo de paquetes Ntx por comunicacion.
- Depende de Estored (energia disponible) y estado de cola NQ.
- Ntx se adapta indirectamente a la tasa de EH KEH y al tiempo de llegada de paquetes.
- Usa info del MAC IEEE 802.15.6 para calcular Etx, que se pasa a PHAM.
- Un Ntx alto aumenta Etx; un Ntx bajo lleva a ineficiencia.
- Agregacion de payload: varios paquetes comparten frames de control.

#### Metricas (definidas explicitamente)
- Deteccion eficiencia = eventos detectados / eventos ocurridos.
- Storage efficiency = eventos almacenados / eventos detectados.
- Throughput normalizado = bits transmitidos con exito / bits generados.
- Packet loss = % paquetes no recibidos por el BNC.
- Average packet end-to-end delay = tiempo desde generacion hasta recepcion en BNC.
- Energy efficiency = bits transmitidos / energia consumida.

#### Setup de simulacion
- Simulador event-driven en MATLAB propio.
- Nodo sensor: ECG. QoS: delay < 250 ms, packet loss < 10%.
- Parametros MAC IEEE 802.15.6: pSIFS 0.05 ms, pCSMA slot 0.125 ms, data Tx rate 485.7 kb/s, control 121.4 kb/s, TPOLL 88 bits, ACK 72 bits, MAC header 56 bits, FCS 16 bits, PLCP preamble 90 + header 31 bits.
- 4 actividades con sus PEHmin/PEHmax/muON: RELAXING (1-4.8 uW, muON=0.9), WALKING (128.6-186 uW, muON=0.1), RUNNING (724.2-910 uW, muON=0.1-0.2), CYCLING (37.4-72.3 uW, muON=0.9).
- BNC con energia externa ilimitada; BN con harvester piezo + supercapacitor.
- Acceso al medio: polling libre de contencion segun IEEE 802.15.6.

#### Baselines y resultados
- Baseline: ECG sin PEH-QoS (transmision inmediata, sin agregacion, Ntx=1) bajo las mismas condiciones de EH.
- Deteccion: en relaxing, PEH-QoS mejora deteccion +10.6%. En walking, baseline 51% vs PEH-QoS 64%.
- Cola: bajo running, baseline satura; PEH-QoS estabiliza en 124 paquetes con 100% de informacion valida.
- Throughput: Ntx=124 da 59% con muON=0.1; con muON=0.2 alcanza 100%.
- Packet loss: PEH-QoS cumple umbral 10% solo con muON=0.2, alcanzando 0.38%; baseline 97.4%. En 2014: 0.39% vs 97.94% baseline.
- Delay: PEH-QoS logra 130 ms (limite 250 ms); baseline 16.18 s (125x peor). En 2014 mismo resultado.
- Energy efficiency: hasta 56x (muON=0.1) y 51x (muON=0.2) mejor que baseline. Con Ntx=124, gasta solo Etx=24.3 uJ para 124 paquetes de 12 bits; sin agregacion, Etx=10.3 uJ por un solo paquete.

### Metodologia Linea 2 (low-cost aplicada) - Prototipo + validacion contra referencia

#### Patron comun
1. Problema real en contexto local o de recursos limitados.
2. Prototipo funcional low-cost (impresion 3D, ESP32, Arduino, PLC, sensores comerciales accesibles).
3. Validacion contra instrumento certificado o referencia clinica.
4. Costo como variable de diseno reportada.
5. Limitaciones clinicas/regulatorias declaradas honestamente.

#### Validacion estadistica
- Bland-Altman (formaldehido: diferencia media <=+-0.03 mg/m3, LoA 95% -0.05 a +0.06).
- ANOVA + Tukey post-hoc (caracterizacion morfologica celular, protesis mioelectrica: p=0.252 > 0.05).
- Comparacion de medias.

#### Herramientas usadas
- Autodesk Fusion 360 (CAD + FEA), Creality Ender-5 Plus, Robo C2.
- Osciloscopio Tektronix TBS 2000B, analizador de redes Rohde & Schwarz ZVL.
- IMT Analytics PF-300, microscopio ZEISS Primovert, ImageJ.
- Python (OpenCV/Numpy/Tkinter/Openpyxl), MATLAB, GraphPad Prism.
- Arduino IDE, EasyEDA, Zen Blue.

#### FEA con Von Mises
- Protesis natacion: sigma max 31.78 MPa < 300 MPa limite; deflexion 38.01 mm; presion operacion 6.1 kPa.
- Protesis mioelectrica: carga 2 N, sigma 64.12-65.29 MPa, desplazamiento 0.45-0.46 mm, factor seguridad 0.015-0.016.

#### Videoanalisis/biomecanica
- Kinovea para analisis angular de patada (omega promedio 3 rad/s, filtro Savitzky-Golay).
- Camaras optoelectronicas + EMG superficial.
- Antropometria: tablas de falanges, mediciones Braun-Fisher, escala Daniel de fuerza muscular (0-5).

### Metodologia Linea 4 (educativa/social) - Encuesta + analisis cualitativo
- Encuestas Likert pre/post (30 preguntas, Qualtrics), 175 estudiantes en 5 iteraciones (2020-2025).
- ANOVA anidada pre/post + Tukey HSD; GraphPad Prism 10.
- Muestra 50 ingenieros biomedicos panamenos (2012); 96% decia que el campo se enfocaba en gestion/ventas/soporte.
- 360-degree peer evaluation.

---

## Filosofia de investigacion

### Epistemologia
- **Pragmatismo translacional:** valora investigacion que conecta medicina y tecnologia con problema real, usuario, costo y factibilidad.
- **No sobreclaiming:** prohibe prometer AAL completo o deteccion de caidas sin datos.
- **Baseline obligatorio:** toda comparacion requiere baseline formal.
- **Costo como variable de diseno:** el costo se reporta, no se oculta.
- **Modularidad tecnica:** PHAM/DQAC/PASS son modulos separables; la arquitectura por bloques es preferida.
- **Limitaciones honestas:** las limitaciones se declaran explicitamente, no se ocultan.

### Que considera valido
- Datos cuantitativos verificados visualmente.
- Tablas y formulas transcritas literalmente del PDF original.
- ANOVA/Bland-Altman con p-values y LoA explicitos.
- Comparacion contra baseline/referencia formal.

### Que considera invalido/sobreclaiming
- Prometer AAL completo o deteccion de caidas sin datos.
- Asumir canal WBAN ideal.
- Confundir BLE con IEEE 802.15.6.
- Presentar solo simulacion sin ruta a prototipo/validacion.
- Citar cifras sin verificacion visual contra PDF.

### Filosofia de extraccion de evidencia
"Una extraccion automatica no se considera lectura completa si no preserva tablas, figuras, formulas o captions importantes."

**Niveles de confianza:**
1. Automatic (screening)
2. Automatic+locator (cita contextual)
3. Manual parcial (variables/metodo)
4. Visual verificado (numeros/formulas/tablas)

"No pasar a claim del paper si el dato esta pendiente."

---

## Papers y tesis - lista completa (15 trabajos)

### Papers Linea 1 (WBAN/EH/QoS)

1. **QoS-Aware Energy Management in Body Sensor Nodes Powered by Human Energy Harvesting** (2016, IEEE Sensors Journal, vol. 16 no. 2). DOI 10.1109/JSEN.2015.2483064. Autores: Ernesto Ibarra, Angelos Antonopoulos, Elli Kartsakli, Joel J. P. C. Rodrigues, Christos Verikoukis. **Columna vertebral metodologica PEH-QoS.** Resultados: deteccion +10.6% relaxing, throughput hasta 100%, packet loss 0.38% vs 97.4%, delay 130 ms vs 16.18 s, eficiencia 56x y 51x. Limitaciones: 1 BN, ECG, canal ideal, no PZT plantar, no validacion clinica.

2. **Joint Power-QoS Control Scheme for Energy Harvesting Body Sensor Nodes** (2014, IEEE ICC 2014). Mismos coautores. Introduce PEH-QoS con PHAM/DQAC/PASS. Baseline: ECG sin PEH-QoS. Resultados: throughput 100% vs 2.06% baseline; packet loss 0.39% vs 97.94%; delay 130 ms vs 16.18 s; eficiencia 50x. Limitaciones: EH constante, canal ideal, 1 nodo, ECG, no PZT.

3. **Energy Harvesting Aware Hybrid MAC Protocol for WBANs** (2013, IEEE HEALTHCOM 2013). HEH-BMAC. ID-polling + PC-access (AIMD, alfaIN=0.01, betaMD=0.5). Compara vs IEEE 802.15.6 (UP0/UP3/UP6). Ganancia ~20% eficiencia y 45-56% throughput con L=18.

4. **HEH-BMAC: Hybrid Polling MAC Protocol for WBANs Operated by Human Energy Harvesting** (version extendida LaTeX). Misma linea que #3 con mas detalles de scheduling dinamico y tabla MITID-BN.

### Papers Linea 2 (low-cost aplicada)

5. **Biomedical Engineering, Support Model between Medicine and Technology in Panama** (2012, LACCEI 2012, Panama). Autores: Luis Estrada, Ernesto Ibarra. Survey a 50 ingenieros biomedicos panamenos.

6. **Sistemas de dispensacion de medicamentos por unidosis en farmacias hospitalarias** (2019, Revista Academica Gente Clave, vol. 3 no. 2). Autores: Nicole Tomlinson, Ernesto Ibarra. Estudio en 8 hospitales. I.O.N. redujo tiempo de dispensacion 56.25% (240 min -> 105 min).

7. **Design of a Cost-Effective Swimming Prosthesis for Transtibial Amputee Patients** (2021). Autor correspondiente: Jay Molino; coautores: Rodriguez, Cardenas, Nieto, Ambulo, Reginensi, Ibarra, Estrada-Petrocelli. Protesis PETG impresa 3D; FEA Von Mises 31.78 MPa; videoanalisis Kinovea omega=3 rad/s; presion operacion 6.1 kPa.

8. **Low-cost, rapidly deployable emergency mechanical ventilators during the COVID-19 pandemic** (2021, IEEE EMBC 2021). DOI 10.1109/EMBC46164.2021.9630676. Coautores: Von Chong, Garcia, De Obaldia, Marin, Ibarra, Grossmann, Trujillo, Gittens. Iniciativa "Ventilators for Panama"; BVD + IPPV; error <5%, SD <0.5 vs IMT PF-300.

9. **3D-Printed Myoelectric Arm Prosthesis Prototype for Children with Upper Limb Agenesis** (2023, Revista Cubana de Ingenieria, vol. XIV(2) e359). Coautores: Perez, Rodriguez, Nieto, Ambulo, Pitti, Villareal, Mendoza, Rodriguez, Matus, Ibarra, Molino. Prototipo 250 g, US$500, agarre 10 N, FEA factor seguridad 0.015-0.016, ANOVA p=0.252.

10. **Development and Validation of a Low-Cost IoT Electrochemical Formaldehyde Monitoring System** (2026, Journal of Sensors, art. 6412281). DOI 10.1155/js/6412281. Coautores: Castillo, Lescher, Ceron, Ibarra, Molino. ESP32 + ZE08-CH2O + LCD; costo <US$60; Bland-Altman vs Yvelines HTO 131 certificado; 4 zonas Hospital del Niño.

### Papers Linea 3 (biomateriales/nanomedicina)

11. **Advancements in the Use of Hydrogels for Regenerative Medicine** (2022, International Journal of Biomaterials, vol. 2022, art. 3606765). DOI 10.1155/2022/3606765. Coautores: Revete, Luis, Aparicio, Ibarra, Cisterna, Segura Gonzalez, Revete, Molino, Reginensi.

12. **Metallic Nanoparticles Applications in Neurological Disorders: A Review** (2025, International Journal of Biomaterials, vol. 2025, art. 4557622). DOI 10.1155/ijbm/4557622. **Primer autor: Ernesto Ibarra-Ramirez.** Coautores: Reginensi, Montes, Urrutia, Segura Gonzalez, Gutierrez-Vega, Appaji, Estrada-Petrocelli, Molino.

### Papers Linea 4 (educativa/internacional)

13. **Investigating the impact of multinational collaborations on cultural understanding, health disparities, biomedical innovations, and professional development through project-based learning** (2026, Journal of Biological Engineering 20:69). DOI 10.1186/s13036-026-00646-9. Coautores: Kilgore, Gustavison, Guiterrez-Vega, Ibarra-Ramirez, Estrada-Petrocelli, Molino, et al. 175 estudiantes, 5 iteraciones; ANOVA anidada pre/post.

### Papers Linea 5 (otros biomedicos)

14. **Design and Implementation of a System for Morphological Characterization of Cells Using Image Processing with Python** (2025, IFMBE Proceedings 119, CLASD 2024, pp. 55-66). DOI 10.1007/978-3-031-88064-3_5. Primer autor: Hurtado Escobar; coautor: Ernesto A. Ibarra-Ramirez. Compara algoritmo Python (OpenCV/Numpy) vs ImageJ sobre cultivos PC12; ANOVA + Tukey.

15. **Deteccion Temprana de Epilepsia Pediatrica: Progresion de los Electrodos en EEG** (2023, European Scientific Journal, vol. 19 no. 6, p.1). DOI 10.19044/esj.2023.v19n6p1. Coautores: Miranda, Lescher, Rojas, Molino, Ibarra E., De Tristan. Revision sistematica de 33 fuentes sobre electrodos EEG pediatricos.

### Tesis
- **EAIM_PhD_THESIS.pdf** (149 paginas) - tesis doctoral de Ibarra (UB 2014), sobre EH-WBAN.
- **TRABAJO FIN DE GRADO_CARACTERIZACION EXPERIMENTAL DEL CANAL DE LA RED WBAN** - Autor: Sergio Bernedo Sadaba, Tutor: Bazil Taha Ahmed, UAM, enero 2016. No es de Ibarra pero se conserva como fuente de canal WBAN real.

---

## Claims verdes, amarillos y rojos derivados del trabajo de Ibarra

### Verdes (evidencia fuerte, citables)
1. PEH-QoS incluye PHAM, DQAC y PASS.
2. El nucleo tecnico mas solido es energia-QoS.
3. PEH-QoS mejora deteccion, throughput, perdida, delay y eficiencia **en condiciones del paper de Ibarra**.
4. PHAM garantiza energia minima al detector (Estored >= Edet) y solo transmite cuando Estored >= Edet + Etx.
5. DQAC descarta paquetes cuyo DQ > DQmax = Dmax - Ttx.
6. PASS determina Ntx optimo segun energia y cola, usando MAC IEEE 802.15.6.
7. Ibarra es antecedente central; el proyecto WBAN actual adapta PEH-QoS a perfil plantar PZT.
8. Las metricas correctas son delay, packet loss, throughput, energia almacenada, deteccion, almacenamiento, eficiencia energetica.

### Amarillos (parcialmente defendibles, uso condicional)
- Usar parametros de Ibarra y ajustar perfiles PZT (recomendacion metodologica: usar como punto de partida pero ajustar).
- Retardo <250 ms y perdida <10% son criterios QoS utiles (pedir trazabilidad de la fuente del umbral).
- PEH-QoS sera replicado o modificado? (pregunta abierta).

### Rojos (no demostrados para el proyecto WBAN, aunque si lo sean en el paper de Ibarra)
- Que PEH-QoS valide deteccion de caidas. NO.
- Que PEH-QoS valide AAL completo. NO.
- Que PEH-QoS funcione en hardware PZT plantar real. NO.
- Que el proyecto "mejora" PEH-QoS sin declarar replica/adaptacion. NO.
- Usar PEH-QoS sin contribucion propia es riesgo rojo de novedad baja.
- Usar PEH-QoS sin baseline propio es riesgo rojo.

### Limitaciones declaradas en el propio paper de Ibarra
- Un solo BN, sin contencion de canal.
- Solo ECG.
- BNC con energia ilimitada.
- Canal ideal.
- EH modelo simplificado (Markov de 2 estados).
- Future work: evaluacion analitica quedo pendiente.

---

## Patrones y principios extraidos del trabajo con Ibarra

1. **Energy Neutral Operation (ENO) como criterio de exito energetico:** un nodo esta en ENO si consume <= energia cosechada.
2. **QoS no puede separarse de energia en WBAN.**
3. **Control de cola preserva validez clinica:** DQAC descarta paquetes con DQ >= DQmax.
4. **Agregacion de paquetes optimiza energia:** PASS muestra que enviar Ntx paquetes en una comunicacion es mas eficiente que uno a uno (56x).
5. **Las metricas correctas son delay, packet loss, throughput, energia, deteccion y almacenamiento.**
6. **PHAM decide sensar/transmitir/dormir segun energia disponible.**
7. **Harvest-Store-Use + supercapacitor.**
8. **Cadena de Markov ON/OFF para disponibilidad de EH.**
9. **Distinguir deteccion de transmision:** Edet (consumo de deteccion) y Etx (transmision), priorizando deteccion.
10. **Declarar replica/adaptacion/mejora:** copiar PEH-QoS sin declarar la relacion con Ibarra es riesgo academico.
11. **Baseline obligatorio:** Ibarra siempre compara contra baseline.
12. **Ibarra historico vs Ibarra reciente:** la distincion entre linea 2013-2016 (WBAN/EH/QoS) y linea 2021-2026 (low-cost/IoT/validacion).
13. **Low-cost + validacion contra referencia:** extraido de papers recientes de Ibarra.
14. **Limitaciones honestas explicitas:** Ibarra reconoce limites clinicos/regulatorios.
15. **Modulos modulares (PHAM/DQAC/PASS):** la modularidad de PEH-QoS inspiraron la arquitectura por bloques.
16. **Metricas concretas, no promesas:** Ibarra reporta metricas medibles.
17. **No confundir BLE con IEEE 802.15.6.**
18. **AAL como priorizacion de trafico, no como diagnostico clinico.**
19. **Inferencia respetuosa:** no afirmar interes personal de Ibarra sin evidencia directa, solo alineacion probable.

---

## Como Ibarra influencia el pipeline de investigacion

### Define la contribucion defendible
La fortaleza principal del proyecto WBAN es que existe una base tecnica concreta y medible: PEH-QoS, PHAM, DQAC, PASS, EH, latencia, perdida, buffer y energia. La propuesta #1 recomendada es literalmente "Validacion por simulacion de un esquema PEH-QoS para sensores plantares piezoelectricos en WBAN".

### Define la pregunta de investigacion
"Puede un esquema PEH-QoS mantener operacion energy-neutral y requisitos de QoS en un nodo WBAN con perfil de sensores plantares PZT bajo escenarios de reposo y marcha?"

### Define la tabla objetivo-variable-metrica
La fuente de parametros para "Evaluar energia" y "Evaluar QoS" es Ibarra, PZT, nRF52840 e IEEE/talleres/Ibarra respectivamente. Resultados minimos heredados de Ibarra: Estored no cae bajo umbral, Delay < 250 ms, perdida < 10%.

### Define la simulacion minima robusta
Los componentes de la simulacion (BN PZT, BNC, modelo ON/OFF, energia por PZT, cola de paquetes, politica PEH-QoS, baseline sin PEH-QoS) replican la arquitectura de Ibarra sustituyendo ECG por PZT plantar.

### Define el primer experimento
"Replicar PEH-QoS de Ibarra et al. con un nodo ECG para verificar que el simulador reproduce tendencias."

### Define las preguntas al asesor
"Debemos presentar PEH-QoS como protocolo adoptado, adaptado o modificado?"

---

## Como presentarle propuestas al Dr. Ibarra

Texto recomendado por el equipo WBAN (de implicaciones_para_propuestas_v2.md):

> "Analizamos criticamente un proyecto previo WBAN-AAL-EH y queremos reformularlo como una propuesta medible. Nuestra idea principal es estudiar la factibilidad energia-QoS de una plantilla plantar IoT de bajo costo para monitoreo de marcha, empezando por simulacion PEH-QoS y dejando una ruta a prototipo/validacion tecnica."

Esto muestra que:
- Conocemos sus papers PEH-QoS.
- Entendemos limites de claims clinicos.
- Conectamos con su linea reciente low-cost/IoT/validacion.
- No vamos con promesas exageradas.

### Cambios que exige la vision Ibarra para propuestas
1. Agregar dimension low-cost/prototipo.
2. Reemplazar "caidas" por monitoreo de marcha/riesgo.
3. Incluir baseline o referencia.
4. Incluir costo y contexto.
5. Incluir plan de validacion incremental (simulacion -> prototipo minimo -> banco -> prueba controlada no clinica -> futura validacion clinica).

---

## Afinidad Edge AI/FPGA: ALTA (la mas alta de todos los investigadores)

**Por que:**
- Ibarra trabaja con hardware real (FPGA-adjacent: prototipos con ESP32, Arduino, PLC, sensores).
- Su metodologia de simulacion con baseline y validacion contra referencia aplica directamente a benchmarking de arquitecturas FPGA.
- Su filosofia modular (PHAM/DQAC/PASS) inspira co-diseno hardware-modelo: modulos separables que se optimizan conjuntamente.
- Su enfoque low-cost aplica a Edge AI: optimizar bajo restricciones de recursos.
- Su honestidad sobre limitaciones aplica a claims de performance/latencia/energia en FPGA.
- Su linea de validacion incremental (simulacion -> prototipo -> prueba controlada) aplica a tesis de Edge AI.

**Como aplicaria a proyecto Edge AI/FPGA:**
- Usar baseline formal (implementacion software-only en MCU como baseline de latencia/energia).
- Declarar si la arquitectura FPGA replica, adapta o mejora un acelerador existente.
- Reportar metricas concretas: latencia ms/inferencia, throughput inferencias/s, consumo mW, recursos %LUTs/DSPs/BRAM, precision accuracy/F1.
- Limitaciones honestas: plataforma especifica, modelo especifico, no generalizable sin recalculo.
- Ruta incremental: simulacion/sintesis -> implementacion FPGA -> medicion -> comparacion vs baseline.
- No prometer despliegue comercial ni superioridad universal sin evidencia.

---

## Frase representativa del Dr. Ibarra

"QoS in WBAN cannot be separated from energy." (QoS en WBAN no puede separarse de energia.)

---

## Regla importante

"No se debe afirmar que el Dr. Ibarra estaria interesado en una propuesta sin evidencia directa. Solo podemos inferir alineacion probable segun sus publicaciones y temas recientes."
