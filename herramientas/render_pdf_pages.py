"""Render selected PDF pages to PNG images with a small manifest.

Usage examples:
  py herramientas/render_pdf_pages.py paper.pdf
  py herramientas/render_pdf_pages.py paper.pdf --pages 1,3,5-7
  py herramientas/render_pdf_pages.py paper.pdf --out outputs/paper_pages --dpi 200

This is intentionally small: it uses PyMuPDF, already registered in the
research system, and does not perform OCR. The rendered images are meant for
selective visual reading of critical pages.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import fitz


def parse_pages(spec: str | None, page_count: int) -> list[int]:
    if not spec:
        return list(range(page_count))

    pages: set[int] = set()
    for part in spec.split(","):
        token = part.strip()
        if not token:
            continue
        if re.fullmatch(r"\d+", token):
            page = int(token)
            if page < 1 or page > page_count:
                raise ValueError(f"Page {page} is outside 1-{page_count}")
            pages.add(page - 1)
            continue
        match = re.fullmatch(r"(\d+)\s*-\s*(\d+)", token)
        if not match:
            raise ValueError(f"Invalid page token: {token}")
        start, end = int(match.group(1)), int(match.group(2))
        if start > end:
            raise ValueError(f"Invalid page range: {token}")
        if start < 1 or end > page_count:
            raise ValueError(f"Page range {token} is outside 1-{page_count}")
        pages.update(range(start - 1, end))

    return sorted(pages)


def safe_stem(path: Path) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", path.stem).strip("_") or "document"


def render_pdf(pdf_path: Path, out_dir: Path, pages: list[int], dpi: int) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    manifest_path = out_dir / "manifest_pages.csv"

    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["source_pdf", "page", "image", "dpi", "width_px", "height_px"],
        )
        writer.writeheader()
        for page_index in pages:
            page = doc.load_page(page_index)
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            image_name = f"{safe_stem(pdf_path)}_p{page_index + 1:03d}.png"
            image_path = out_dir / image_name
            pix.save(image_path)
            writer.writerow(
                {
                    "source_pdf": str(pdf_path),
                    "page": page_index + 1,
                    "image": str(image_path),
                    "dpi": dpi,
                    "width_px": pix.width,
                    "height_px": pix.height,
                }
            )

    doc.close()
    return manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="PDF file to render")
    parser.add_argument("--pages", help="Pages to render, e.g. 1,3,5-7. Defaults to all pages.")
    parser.add_argument("--out", type=Path, help="Output directory")
    parser.add_argument("--dpi", type=int, default=200, help="Render DPI. Default: 200")
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)
    if args.dpi < 72:
        raise ValueError("DPI must be at least 72")

    doc = fitz.open(pdf_path)
    page_count = doc.page_count
    doc.close()

    pages = parse_pages(args.pages, page_count)
    out_dir = args.out or (pdf_path.parent / f"{safe_stem(pdf_path)}_page_images")
    manifest = render_pdf(pdf_path, out_dir.resolve(), pages, args.dpi)
    print(f"Rendered {len(pages)} page(s) from {pdf_path}")
    print(f"Manifest: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
