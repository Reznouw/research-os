"""Extract text from PDFs into per-document text files and a manifest.

This lightweight extractor is for first-pass coverage. It is not final evidence
for tables, formulas, figures, or numeric results; those still require visual
verification under the multimodal ingestion protocol.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import fitz


def safe_stem(path: Path) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", path.stem).strip("_") or "document"


def extract_pdf(pdf_path: Path, out_dir: Path) -> dict[str, object]:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    out_path = out_dir / f"{safe_stem(pdf_path)}.txt"
    total_chars = 0
    image_count = 0

    with out_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(f"SOURCE: {pdf_path}\n")
        handle.write(f"PAGES: {doc.page_count}\n")
        handle.write("EXTRACTION: PyMuPDF automatic text; verify tables/figures/formulas visually.\n\n")
        for index, page in enumerate(doc, start=1):
            text = page.get_text("text")
            images = len(page.get_images(full=True))
            image_count += images
            total_chars += len(text)
            handle.write(f"\n--- PAGE {index} ---\n")
            handle.write(text)
            if not text.endswith("\n"):
                handle.write("\n")
            if images:
                handle.write(f"[AUTO_NOTE: page has {images} image object(s); consider visual verification.]\n")

    page_count = doc.page_count
    doc.close()
    return {
        "source_pdf": str(pdf_path),
        "text_file": str(out_path),
        "pages": page_count,
        "chars": total_chars,
        "image_objects": image_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Directory containing PDFs recursively")
    parser.add_argument("--out", type=Path, required=True, help="Output directory for text files")
    parser.add_argument("--manifest", type=Path, help="Manifest CSV path")
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = args.out.resolve()
    pdfs = sorted(root.rglob("*.pdf"))
    manifest_path = args.manifest.resolve() if args.manifest else out_dir / "manifest_extraccion_texto.csv"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for pdf in pdfs:
        rows.append(extract_pdf(pdf.resolve(), out_dir))

    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_pdf", "text_file", "pages", "chars", "image_objects"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Extracted {len(rows)} PDF(s)")
    print(f"Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
