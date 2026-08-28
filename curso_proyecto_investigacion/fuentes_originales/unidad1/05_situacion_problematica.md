# Unidad 1 - Situacion Problematica (1AEL0260-05)

> **Fuente:** `1AEL0260-05-SITUACION_PROBLEMATICA-2026` (PPT oficial de Unidad 1)
> **Fecha de registro:** 2026-08-27
> **CRITICO:** Este documento define COMO se formula el titulo de la tesis y la situacion problematica. Es el corazon del curso.

---

## 1. Tesis de Ingenieria (pregrado) - Conceptos base

```
PROBLEMA  +  APORTE  =>  SOLUCION
  |            |
  v            v
Aplicacion y/o adaptacion del conocimiento
(modelo, metodo, algoritmo, procedimiento, herramienta, etc.)
para resolver un problema
```

| Principio | Definicion |
|---|---|
| **ORIGINALIDAD** | No puede haber dos temas iguales. No puede haber dos propuestas con el mismo problema, la misma tecnica y el mismo escenario. |
| **PROFUNDIDAD** | La tesis de grado requiere una mejora/innovacion de conocimiento para poder resolver un problema. |
| **APORTE** | Es la parte MAS importante: aplicacion y/o adaptacion y/o mejora de conocimiento (equipo, sistema, maquina, etc.) para resolver un problema. |
| **VALIDACION** | Comprobacion que el aporte desarrollado esta bien (funcionalidad, usabilidad, eficiencia, etc.) y que alcanza los objetivos. |
| **SOSTENIBILIDAD** | Todo lo que se afirme debe tener sustento, sea en fuentes validas o en inferencias basadas en afirmaciones validas. |

---

## 2. Titulo del tema de investigacion

### Formula

```
Titulo = APORTE (1) + PROBLEMA (2) + TECNICA (3, opcional) + ESCENARIO (4, opcional)
1+2+3+4 = Titulo inicial propuesto
```

- **APORTE (1) - OBLIGATORIO:** Debe quedar claro con nivel de abstraccion: sistema, equipo, algoritmo, metodo, etc.
- **PROBLEMA (2) - OBLIGATORIO:** Se define especificamente el problema que se busca solucionar.
- **TECNICA (3) - Opcional:** Metodo/tecnica a usar.
- **ESCENARIO (4) - Opcional:** Donde se aplica.

### Ejemplo Electronica

> **"Desarrollo de un sistema de conteo y medicion del largo y el ancho de los alevines de tilapia basado en procesamiento digital de imagenes para el centro piscicola de la UNALM"**
> - APORTE: SISTEMA
> - PROBLEMA: CONTEO Y MEDICION DEL LARGO Y ANCHO DE LOS ALEVINES INADECUADO
> - TECNICA: PROCESAMIENTO DIGITAL DE IMAGENES
> - ESCENARIO: CENTRO PISCICOLA DE LA UNALM

### Ejemplo Mecatronica

> **"Desarrollo de una maquina de envasado de frutos en base a su tamano usando robots paralelos tipo delta y robotica blanda para la empresa Agroindustrias Verdeflor S.A.C."**
> - APORTE: MAQUINA
> - PROBLEMA: ENVASADO DE FRUTOS EN BASE AL TAMANO
> - TECNICA: ROBOTS PARALELOS Y ROBOTICA BLANDA
> - ESCENARIO: AGROINDUSTRIAS VERDEFLOR

### Ejemplo Biomedica

> **"Desarrollo de un equipo biomedico orientado a la medicion del rango de movimiento de extremidades usando sensores de efecto hall para el Centro Universitario de Salud de UPC"**
> - APORTE: EQUIPO
> - PROBLEMA: MEDICION DEL RANGO DE MOVIMIENTO DE EXTREMIDADES
> - TECNICA: SENSORES DE EFECTO HALL
> - ESCENARIO: CENTRO UNIVERSITARIO DE SALUD UPC

### Aplicacion para Grupo 15 (FPGA Edge AI)

> **"Desarrollo de una arquitectura reconfigurable para inferencia Edge AI basada en FPGA DE25-Nano mediante co-diseno hardware-modelo para [escenario por definir]"**
> - APORTE: ARQUITECTURA RECONFIGURABLE
> - PROBLEMA: INFERENCIA EDGE AI INEFICIENTE EN RECURSOS/LATENCIA
> - TECNICA: CO-DISENO HARDWARE-MODELO (quantization, pruning, HLS)
> - ESCENARIO: [por definir - ej. dispositivo edge para telesalud / IoT / etc.]

---

## 3. Situacion problematica - Estructura completa

> La situacion problematica es el resultado de comparar el comportamiento real con el comportamiento ideal. Si ambos son iguales, no hay situacion problematica; si hay desigualdad, si la hay.

### 3.1. Breves conceptos, fundamentos y definiciones teoricas introductorias

- Solo conceptos **ajenos a la especialidad** de electronica/mecatronica/biomedica que ayudan a entender la situacion problematica.
- No explicar el proyecto en si, solo el contexto.
- Debe estar argumentado a partir del estado del arte.

### 3.2. Descripcion de la situacion, proceso o procedimiento + problema general

- Describir el proceso/procedimiento donde se genera la situacion problematica.
- **Obligatorio: utilizar ilustraciones.**
- Si hay cliente potencial, consignar:
  - Nombre de la empresa/institucion y ubicacion geografica
  - Rubro y actividades
  - Lugar especifico donde se presenta la problematica (departamento, laboratorio, seccion)
  - Actividades del departamento, ubicacion dentro de la empresa, profesionales, equipamiento disponible
- Concluir con el **enunciado del problema**.

### 3.3. Causas y consecuencias

```
Causa 1: (Redactar la causa comenzando por un adjetivo)
  Descripcion.-

Causa 2: (Redactar la causa comenzando por un adjetivo)
  Descripcion.-

Consecuencia 1: (Redactar la consecuencia)
  Descripcion.-

Consecuencia 2: (Redactar la consecuencia)
  Descripcion.-
```

- Causas: comenzar por un **adjetivo** (ej. "Deficiente gestion...", "Inadecuado diseno...").
- Consecuencias: describir que pasa si NO se soluciona.

### 3.4. Enunciado del problema general y arbol del problema

- En base a la problematica, enunciar el **problema general** y elaborar el **arbol del problema**.
- Reglas del arbol:
  - Indicar y senalizar: problema general + nombres de causas y consecuencias.
  - El problema general y las causas primarias/secundarias deben empezar con **adjetivos**.

### Adjetivos sugeridos

> (Imagen en el PPT - lista de adjetivos para iniciar causas/problema)

### Esquema del arbol del problema

```
                    [CONSECUENCIAS]
                         ^
                         |
              [PROBLEMA GENERAL]  <- con adjetivo
                         ^
                         |
              [CAUSAS PRIMARIAS]  <- con adjetivo
                         ^
                         |
              [CAUSAS SECUNDARIAS]  <- con adjetivo
```

### Relacion arbol del problema -> arbol de objetivos

> El fin del proyecto son las consecuencias positivas que se espera lograr con la solucion del problema.
> Cada problema se convierte en objetivo.

```
Arbol del problema          ->    Arbol de objetivos
Problema general            ->    Objetivo general
Causas                      ->    Objetivos especificos
Consecuencias               ->    Fines / impactos
```

### Ejemplo referencial 1 de arbol de problema

> (Imagen en el PPT - ejemplo concreto)

### 3.5. Requerimientos ingenieriles, tecnicos y operativos

- Lista de requerimientos establecidos para la solucion.
- Especifica requerimientos tecnicos, operativos, funcionales, etc.
- **Se requieren datos cuantitativos** (ej. latencia < X ms, precision > Y%, consumo < Z W).

### 3.6. Problemas de ingenieria

```
Problema de Ingenieria 1:
  - Descripcion del problema (enfatizando los requerimientos cuantitativos correspondientes).
  - Metodos cientificos/ingenieriles hipoteticos de solucion del problema.

Problema de Ingenieria 2:
  - Descripcion del problema (enfatizando los requerimientos cuantitativos correspondientes).
  - Metodos cientificos/ingenieriles hipoteticos de solucion del problema.
```

---

## Cross-links

| Documento | Relacion |
|---|---|
| `01_introduccion_fundamentos.md` | Tipos de investigacion, logto de Unidad 1 |
| `11_plantilla_PPT_EX1.md` | EX1 pide describir problema, causas, consecuencias |
| `13_ejemplo_referencial_PPT_EX1.md` | El ejemplo PET sigue esta estructura (describio 5 etapas + empresa Tecnofilm) |
| `FICHA_CLASE_DIA1_2026-08-25.md` | Clase Dia 1 explico situacion problematica y arbol del problema |
| `03_reglamento_tituloI_caracteristicas.md` | Art. 5: sectores productivos / PNCTI donde encaja el problema |
