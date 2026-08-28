"""
Script de transcripcion de audio a texto/markdown usando faster-whisper.
Entrada: archivo de audio (MP3, WAV, M4A, OGG, FLAC, MP4, etc.)
Salida: archivo .md con la transcripcion, timestamps, y metadata.

Uso basico:
    py herramientas/transcribir_audio.py "ruta\audio.mp3"

Uso avanzado:
    py herramientas/transcribir_audio.py "ruta\audio.mp3" --model large-v3 --language es --out "ruta\salida"
"""
import argparse
import os
import sys
import json
from pathlib import Path
from datetime import datetime


def transcribir_audio(audio_path, model_size="medium", language="es", out_dir=None):
    """
    Transcribe un archivo de audio usando faster-whisper.
    
    Args:
        audio_path: ruta al archivo de audio
        model_size: tamano del modelo (tiny, base, small, medium, large-v3)
        language: idioma del audio (es, en, etc.)
        out_dir: directorio de salida (por defecto: junto al audio)
    
    Returns:
        dict con el texto completo, segmentos, y metadata
    """
    from faster_whisper import WhisperModel

    audio_path = Path(audio_path)
    if not audio_path.exists():
        print(f"Error: archivo no encontrado: {audio_path}")
        sys.exit(1)

    print(f"Cargando modelo '{model_size}'...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print(f"Transcribiendo: {audio_path.name}")
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )

    # Recopilar segmentos
    segmentos = []
    texto_completo = []
    for seg in segments:
        segmentos.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip()
        })
        texto_completo.append(seg.text.strip())

    # Metadata
    metadata = {
        "audio": str(audio_path),
        "modelo": model_size,
        "idioma": language,
        "duracion_segs": round(info.duration, 1),
        "prob_idioma": round(info.language_probability, 3),
        "fecha_transcripcion": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "num_segmentos": len(segmentos)
    }

    # Preparar directorio de salida
    if out_dir is None:
        out_dir = audio_path.parent
    else:
        out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    nombre_base = audio_path.stem

    # 1. Guardar texto completo como markdown
    md_path = out_dir / f"{nombre_base}_transcripcion.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcripcion: {audio_path.name}\n\n")
        f.write(f"**Fecha:** {metadata['fecha_transcripcion']}  \n")
        f.write(f"**Modelo:** {metadata['modelo']}  \n")
        f.write(f"**Idioma:** {metadata['idioma']} ({metadata['prob_idioma']})  \n")
        f.write(f"**Duracion:** {metadata['duracion_segs']}s  \n")
        f.write(f"**Segmentos:** {metadata['num_segmentos']}  \n\n")
        f.write("---\n\n")
        f.write("## Texto completo\n\n")
        f.write("\n\n".join(texto_completo))
        f.write("\n\n---\n\n")
        f.write("## Segmentos con timestamps\n\n")
        f.write("| # | Inicio | Fin | Texto |\n")
        f.write("|---|---|---|---|\n")
        for i, seg in enumerate(segmentos, 1):
            inicio = seg["start"]
            fin = seg["end"]
            texto = seg["text"].replace("|", "\\|")
            f.write(f"| {i} | {inicio}s | {fin}s | {texto} |\n")
    print(f"Transcripcion markdown: {md_path}")

    # 2. Guardar JSON con metadata + segmentos
    json_path = out_dir / f"{nombre_base}_metadata.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"metadata": metadata, "segmentos": segmentos}, f, ensure_ascii=False, indent=2)
    print(f"Metadata JSON: {json_path}")

    # 3. Guardar texto plano (para usar como material bruto de Renzosky)
    txt_path = out_dir / f"{nombre_base}_texto.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(texto_completo))
    print(f"Texto plano: {txt_path}")

    return {
        "markdown": str(md_path),
        "json": str(json_path),
        "texto": str(txt_path),
        "metadata": metadata,
        "num_segmentos": len(segmentos)
    }


def main():
    parser = argparse.ArgumentParser(description="Transcribir audio a texto/markdown")
    parser.add_argument("audio", help="Ruta al archivo de audio (MP3, WAV, M4A, etc.)")
    parser.add_argument("--model", default="medium", help="Modelo: tiny, base, small, medium, large-v3 (default: medium)")
    parser.add_argument("--language", default="es", help="Idioma del audio (default: es)")
    parser.add_argument("--out", default=None, help="Directorio de salida (default: junto al audio)")

    args = parser.parse_args()
    result = transcribir_audio(args.audio, args.model, args.language, args.out)

    print(f"\n=== Listo ===")
    print(f"Markdown: {result['markdown']}")
    print(f"JSON:     {result['json']}")
    print(f"Texto:    {result['texto']}")
    print(f"Segmentos: {result['num_segmentos']}")


if __name__ == "__main__":
    main()
