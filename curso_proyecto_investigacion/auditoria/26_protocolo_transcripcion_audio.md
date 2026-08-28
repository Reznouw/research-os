# 26 Protocolo de transcripcion de audio

> **Como convertir archivos de audio (clases, grabaciones, entrevistas) en texto/markdown.**
> Herramienta: `faster-whisper 1.2.1` (OpenAI Whisper optimizado) + `ffmpeg 9.0`.
> Script: `herramientas/transcribir_audio.py`.

---

## Pipeline

```
Audio (MP3/WAV/M4A/OGG/FLAC/MP4)
    ↓
transcribir_audio.py
    ↓
3 archivos de salida:
  ├── *_transcripcion.md    ← Formato academico con timestamps y metadata
  ├── *_metadata.json       ← Datos estructurados para procesamiento programatico
  └── *_texto.txt           ← Texto plano para Renzosky (material bruto)
    ↓
Actualizacion de ESTADO.md + DECISIONES.md
```

---

## Comandos de uso

### Basico (espanol, modelo medium)

```powershell
py herramientas/transcribir_audio.py "ruta\clase_semana1.mp3"
```

### Modelo mas grande (mejor precision)

```powershell
py herramientas/transcribir_audio.py "ruta\audio.mp3" --model large-v3 --language es
```

### Con directorio de salida especifico

```powershell
py herramientas/transcribir_audio.py "ruta\audio.mp3" --out "ruta\transcripciones"
```

### Modelos disponibles

| Modelo | Velocidad | Precision | Uso recomendado |
|---|---|---|---|
| tiny | Muy rapida | Baja | Pruebas rapidas, audio limpio |
| base | Rapida | Basica | Audio limpio, poco ruido |
| small | Media | Aceptable | Clases con algo de ruido |
| medium | Lenta | Buena | **Recomendado** - balance velocidad/calidad |
| large-v3 | Muy lenta | Excelente | Audio con mucho ruido, multiples hablantes |

---

## Flujo completo para una clase del curso

```
1. Obtener audio de la clase (MP3, grabacion, etc.)
   ↓
2. Transcribir:
   py herramientas/transcribir_audio.py "audio_clase.mp3" --out "transcripciones/"
   ↓
3. Leer el .md generado, identificar secciones clave
   ↓
4. Crear ficha Renzosky del tema de la clase (si aplica)
   ↓
5. Actualizar ESTADO.md con el nuevo material
```

---

## Limitaciones conocidas

- **Idioma:** Por defecto detecta espanol. Cambiar con `--language en` si es ingles.
- **Multiples hablantes:** Whisper no distingue hablantes. El texto sale corrido.
- **Audio muy largo (>1 hora):** Funciona pero es lento en CPU. El modelo large-v3 puede tardar 10-20x la duracion del audio.
- **Ruido de fondo:** El filtro VAD ayuda, pero audio muy ruido puede generar texto incorrecto.
- **No hace OCR ni diarizacion:** Solo transcripcion. Para identificar hablantes, usar herramientas externas.

---

## Verificacion

```powershell
py -c "from faster_whisper import WhisperModel; print('faster-whisper OK')"
ffmpeg -version
```

---

## Cross-links

| Protocolo/Script | Relacion con este protocolo |
|---|---|
| `21_herramientas_instaladas.md` | Herramientas: faster-whisper 1.2.1, ffmpeg 9.0 |
| `22_pipeline_ingesta_multimodal.md` | El audio es un tipo de contenido que ingresa al sistema — complementa el pipeline multimodal |
| `23_protocolo_pdf_ppt_imagenes.md` | Si el audio viene con material visual (ej. grabacion de pantalla), se procesa con este protocolo |
| `24_flujo_ingesta_a_markdown.md` | La transcripcion .md se guarda y conecta via ESTADO.md como cualquier otra ficha |
| `25_protocolo_latex.md` | La transcripcion puede ser fuente de contenido para entregables LaTeX |
| `27_protocolo_zotero.md` | Si el audio es una conferencia o entrevista, se guarda en Zotero como fuente |
| `herramientas/transcribir_audio.py` | Script que implementa este protocolo |
