# 001 Aprendizajes de WBAN para un Research OS general

## Contexto

Durante el desarrollo del paper WBAN-AAL-EH se produjo manuscrito en ingles y espanol, guia de defensa, figuras, tablas, resultados de simulacion y ajustes de LaTeX. El proceso mostro que producir un paper no basta: el sistema debe hacer que el autor entienda, defienda y empaquete el trabajo.

## Aprendizajes

| Observacion | Riesgo | Patron general |
| --- | --- | --- |
| Una tabla puede compilar pero ser ilegible | Falsa sensacion de finalizacion | Auditar legibilidad, no solo compilacion |
| `resizebox` puede esconder problemas de diseno | Texto microscopico en IEEE dos columnas | Preferir menos columnas, abreviar etiquetas o usar tabla de ancho completo |
| El autor puede malinterpretar una metrica propia | Defensa debil o conclusion equivocada | Explicar metricas con definicion, ejemplo y lectura esperada |
| Figuras con flechas cruzadas confunden aunque sean tecnicamente correctas | Perdida de mensaje | Usar contrato visual y loop de validacion |
| Resultados numericos necesitan narrativa | El lector ve numeros sin significado | Traducir resultados a diagnostico: que mejora, donde falla, bajo que condicion |
| Guia de defensa no es extra | El autor necesita apropiarse del paper | Generar material didactico como parte del pipeline |
| Claims sobre salud, hardware o novedad se exageran facil | Riesgo academico alto | Mantener auditoria de claims verdes/amarillos/rojos |
| Archivos finales quedan dispersos | Dificil compartir o reproducir | Crear release pack con manifiesto |

## Reglas incorporables

- Si el usuario dice que no entiende, activar modo didactico y no asumir que el documento esta listo.
- Si una figura o tabla se usa para defender un resultado, debe tener mensaje central, caption interpretativo y criterio de legibilidad.
- Si se genera una figura, debe existir una ruta de verificacion: render, inspeccion, correccion y aceptacion.
- Si una mejora surgio por varias iteraciones, registrar el patron para evitar repetir el ciclo.
- Si se prepara un paper, preparar tambien su defensa y su carpeta final cuando el usuario lo necesite.

## Estado

Aplicado como base para las nuevas skills locales del Research OS.
