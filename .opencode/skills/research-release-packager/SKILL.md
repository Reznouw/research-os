---
name: research-release-packager
description: Use when preparing a final shareable research folder, submission package, GitHub release, thesis/paper delivery, reproducibility bundle, or organizing PDFs, LaTeX sources, figures, scripts, data, slides, defense guide, and manifests.
---

# Research Release Packager

## Purpose

Create a clean, shareable and reproducible package for a research project. The package should let another person understand what is final, what generated it and what is needed to reproduce or inspect it.

## Trigger Signals

- "entregar", "compartir", "subir a GitHub", "carpeta final".
- "release", "paquete", "mandar", "exportar", "organizar".
- End of paper, thesis, defense or project milestone.

## Recommended Structure

```text
release/<project_name>/
  README.md
  MANIFEST.md
  pdfs/
  latex_sources/
  figures/
  tables/
  scripts/
  data_minimal/
  defense_material/
  logs/
```

## Include When Available

- Final paper PDF in every required language.
- LaTeX sources and bibliography.
- Defense guide and slides.
- Final figures and source specs/scripts for generated figures.
- Result CSVs or minimal data needed to reproduce tables/plots.
- Scripts used for simulation, analysis or figure generation.
- Build logs or build instructions.
- `MANIFEST.md` listing file purpose and status.

## Exclude Or Flag

- Temporary LaTeX files unless needed for debugging.
- Huge raw data unless explicitly required.
- Private notes, credentials, cache files and downloaded copyrighted PDFs without permission.
- Drafts that may be confused with final outputs.

## Done Criteria

- A reader can identify final deliverables in under one minute.
- Every final figure/table has a source or provenance note.
- Build or reproduction steps are documented.
- Sensitive/private files are not included.
