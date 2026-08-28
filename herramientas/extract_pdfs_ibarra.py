from pathlib import Path
import re
import sys

import fitz
import pymupdf4llm


BASE = Path(__file__).resolve().parent
PDF_DIR = BASE / "pdfs"
OUT_TEXT = BASE / "extracciones_herramientas" / "pymupdf"
OUT_MD = BASE / "extracciones_herramientas" / "pymupdf4llm"


def slug(name: str) -> str:
    value = Path(name).stem.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value, flags=re.I).strip("_")
    return value[:120]


def extract_with_pymupdf(pdf: Path, output: Path) -> tuple[int, int, int, str]:
    doc = fitz.open(pdf)
    parts: list[str] = []
    total_chars = 0
    image_count = 0

    for page_number, page in enumerate(doc, 1):
        text = page.get_text("text")
        total_chars += len(text)
        image_count += len(page.get_images(full=True))
        parts.append(f"\n\n===== PAGE {page_number} =====\n\n{text}")

    output.write_text("\n".join(parts), encoding="utf-8")
    return doc.page_count, total_chars, image_count, "ok"


def extract_with_pymupdf4llm(pdf: Path, output: Path) -> tuple[int, str]:
    markdown = pymupdf4llm.to_markdown(str(pdf))
    output.write_text(markdown, encoding="utf-8")
    return len(markdown), "ok"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    OUT_TEXT.mkdir(parents=True, exist_ok=True)
    OUT_MD.mkdir(parents=True, exist_ok=True)

    rows = []
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        file_id = slug(pdf.name)
        text_path = OUT_TEXT / f"{file_id}.txt"
        md_path = OUT_MD / f"{file_id}.md"

        try:
            pages, text_chars, image_count, text_status = extract_with_pymupdf(pdf, text_path)
        except Exception as exc:  # noqa: BLE001 - manifest should record any extraction failure.
            pages = "?"
            text_chars = 0
            image_count = 0
            text_status = f"error: {exc}"

        try:
            md_chars, md_status = extract_with_pymupdf4llm(pdf, md_path)
        except Exception as exc:  # noqa: BLE001
            md_chars = 0
            md_status = f"error: {exc}"

        rows.append((pdf.name, pages, text_chars, md_chars, image_count, text_status, md_status))

    manifest_lines = [
        "# Manifest de extracciones automaticas",
        "",
        "| PDF | Paginas | PyMuPDF chars | pymupdf4llm chars | Imagenes detectadas | PyMuPDF | pymupdf4llm |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for pdf_name, pages, text_chars, md_chars, image_count, text_status, md_status in rows:
        manifest_lines.append(
            f"| {pdf_name} | {pages} | {text_chars} | {md_chars} | {image_count} | {text_status} | {md_status} |"
        )

    manifest = BASE / "extracciones_herramientas" / "MANIFEST_EXTRACCIONES.md"
    manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    print("\n".join(manifest_lines))


if __name__ == "__main__":
    main()
