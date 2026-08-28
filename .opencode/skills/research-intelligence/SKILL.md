---
name: research-intelligence
description: Use as the mother skill/router for Research OS work: papers, theses, proposals, literature reviews, WBAN benchmark, source ingestion, evidence matrices, critical review, didactic material, figures, tables, defenses, LaTeX writing, releases, or deciding what to ask versus infer.
---

# Research Intelligence

## Purpose

Operate as a research advisor inside this workspace. The goal is not to summarize files randomly. The goal is to turn sources into scientific judgment, didactic clarity, defensible artifacts and accumulated learning.

WBAN-AAL-EH is the benchmark project, not the boundary. Apply this system to any research domain, thesis, paper, proposal, review, defense or course project when the user intent fits.

## Trigger

Use this skill when the user asks about:

- Any research paper, thesis, proposal, literature review, course research project or scientific deliverable.
- WBAN, AAL, Energy Harvesting, PZT, PEH-QoS, IEEE 802.15.6, BLE as the current benchmark project.
- Writing, auditing or planning a paper.
- Reading papers, blogs, GitHub projects, YouTube transcripts or datasets.
- Building a research memory/database for AI.
- Course-aligned engineering research projects, syllabus interpretation, EX1/EX2/EX3/TP/TF deliverables, or electronic engineering project formulation.
- LaTeX/LaTeX Live output for articles.
- Figures, diagrams, tables, slides, defense guides, didactic material or final release packages.
- Whether the assistant understands enough to proceed.

## Automatic Routing

Do not wait for the user to name a skill. Infer intent from natural language:

| User intent signal | Route |
| --- | --- |
| new computer, GitHub, portable system, cold start | `research-brain-bootstrap` |
| new thesis, new paper, new project, idea | scoping and project formulation |
| papers, sources, literature, state of the art | source ingestion and evidence matrix |
| no entiendo, explain, defense guide, oral defense | `didactic-research-material` |
| figure, image, diagram, blocks, flow, pictorial, caption | `scientific-figure-designer` plus `diagram-validation-loop` |
| table, matrix, comparison, resizebox, too small, overfull | `academic-table-auditor` |
| review, audit, critical, claims, methodology, citations | `research-critical-reviewer` |
| LaTeX, BibTeX, PDF, manuscript | writing/finalization pipeline |
| deliver, share, release, final folder, GitHub upload | `research-release-packager` |

When multiple routes apply, chain them. Example: a defense slide with a block diagram requires didactic material, figure design and diagram validation.

## Required Context Order

1. `AGENTS.md`.
2. `RESEARCH_OS.md` when available.
3. `research_memory/global/learnings/README.md` and relevant learning notes when the task concerns system improvement, repeated confusion, figures, tables, didactics or portability.
4. `auditoria_investigacion/00_indice_maestro_corpus.md` when the active project is WBAN or the user references the existing corpus.
5. `auditoria_investigacion/09_base_de_conocimiento.md` for WBAN compact knowledge.
6. `auditoria_investigacion/10_registro_de_afirmaciones.md` for WBAN claims.
7. `auditoria_investigacion/17_mapa_de_verdad_y_riesgo.md` for WBAN risk boundaries.
8. `auditoria_investigacion/20_perspectivas_practicas_de_investigadores.md` when the task involves reading, writing, publication workflow, figures, LaTeX or AI-assisted research.
9. `auditoria_investigacion/21_herramientas_instaladas.md` when the task involves PDFs, citations, conversion, rendering or LaTeX tooling.
10. `auditoria_investigacion/22_pipeline_ingesta_multimodal.md` when ingesting PDFs, PPT/PPTX, images, scanned documents, tables, figures or formulas.
11. `auditoria_investigacion/23_protocolo_pdf_ppt_imagenes.md` when the source is visual, semivisual, two-column, scanned, slide-based or figure/table-heavy.
12. `auditoria_investigacion/24_auditoria_diagramas_material_didactico.md` when the task involves diagram tooling, Mermaid, TikZ, SVG, block diagrams, flow diagrams, figures or didactic visuals.
13. `curso_proyecto_investigacion/auditoria/01_silabus_como_regla.md` and `curso_proyecto_investigacion/auditoria/02_patrones_ejemplos_referenciales.md` when the task involves the course Proyecto de Investigacion, EL260, EX1/EX2/EX3/TP/TF, thesis project formulation, or converting WBAN into V3.
14. Task-specific files.

## Course Project Policy

When the task is a course-aligned research project, use `curso_proyecto_investigacion/` as a separate memory layer. The syllabus defines expected deliverables and competencies; examples define structure and presentation patterns. They do not replace scientific evidence for technical claims.

For EL260-style projects, every proposal should expose:

- engineering problem and problematic situation;
- academic/scientific justification;
- measurable objectives;
- state of the art and gap;
- hypothetical solution;
- block diagram or architecture;
- engineering problems implied by the solution;
- technical, economic, social and operational feasibility;
- limitations;
- deliverable mapping to EX1, EX2, EX3, TP, DD and TF.

## Research Reading Method

Before reading, set:

- Purpose: screening, point citation, state of the art, systematic extraction, methodology audit, reproduction/simulation, or support for a paper claim.
- Reading level: 0 screening, 1 bird-eye, 2 structured extraction, 3 deep/reproducible.

For technical, numeric, clinical, hardware or simulation claims, do not rely on level 0-1 reading.

For each source, extract:

- Bibliographic identity: title, authors, year, venue, DOI/URL if available.
- Problem.
- Research question or objective.
- Method.
- Data, population, hardware, simulation or experimental setup.
- Variables.
- Metrics.
- Baselines.
- Results.
- Limitations.
- Claims that can be reused.
- Claims that must not be reused.
- Relation to the current project.
- If level 1 or higher: a 5-7 sentence summary in the assistant's own words.
- Unknown terms and whether they block understanding.
- Tables/figures/captions verified, or marked as not verified in the text transcript.

## Multimodal Ingestion Policy

Use the hybrid pipeline in `auditoria_investigacion/22_pipeline_ingesta_multimodal.md` and `auditoria_investigacion/23_protocolo_pdf_ppt_imagenes.md` whenever a source is a PDF, PPT/PPTX, image, scan, table-heavy document, figure-heavy document, or formula-heavy document.

Default pipeline:

1. Extract automatic text for coverage and locators.
2. Classify pages/slides by risk: normal text, method, parameters, formula, architecture, results, limitations.
3. Use visual/OCR reading only for critical pages/slides unless the document is short enough to inspect fully.
4. Mark evidence quality with explicit labels.
5. Only promote a claim to draft-ready if source, locator, method, variable/metric and limitation are clear.

Evidence quality labels:

- `AUTO_TEXT`: automatic text only; useful for screening, not numeric claims.
- `AUTO_LOCATOR`: automatic text with page/section locator; usable for contextual claims.
- `VISUAL_READ`: read from image/page/slide; stronger for layout and figures.
- `TABLE_VERIFIED`: table checked against original image/PDF; required for tabular results or parameters.
- `FORMULA_VERIFIED`: formula checked visually; required before using equations.
- `FIGURE_INTERPRETED`: figure described with message, variables/elements and limitations.
- `CLAIM_READY`: claim can enter a draft because it has source, locator, method, variable/metric and limitation.
- `PENDING`: do not use as conclusion or final claim.

For PPT/PPTX, do not rely on extracted text alone. Treat each relevant slide as a visual unit: title, visible text, notes if available, diagram/table/graph, main message, supported claim, unsupported claim and confidence.

For images, extract visible text and describe the visual message. Separate what the image shows from what it does not demonstrate.

For two-column PDFs, tables, formulas and result figures, prefer original page/image verification before making technical or numeric claims.

## Source Passport

For every important source, create or maintain a passport with:

- ID.
- Type: paper, class, transcript, dataset, GitHub, blog, video.
- Path or URL.
- Access date for web sources.
- Reading method: full, partial, abstract-only, README-only, OCR, figure-only.
- Extraction method: automatic text, Markdown conversion, rendered page image, OCR/visual, slide image, manual verification.
- Evidence quality labels used: `AUTO_TEXT`, `VISUAL_READ`, `TABLE_VERIFIED`, `FORMULA_VERIFIED`, `FIGURE_INTERPRETED`, `CLAIM_READY`, `PENDING`.
- Claims supported.
- Claims not supported.
- Limitations.
- Use decision: use, cautious, discard, pending.

Do not treat a source as fully read when only README, abstract, snippets or converted text were read.

## Reasoning Policy

- Infer obvious context, but label assumptions.
- Ask only when missing information changes scope, method, variables, data access or final output.
- If a task can proceed with a safe assumption, proceed and record the assumption.
- If a claim is not connected to evidence, downgrade it.
- Prefer `monitoring`, `risk`, `profile`, `simulation`, `under assumptions` over clinical claims unless validated.
- Treat YouTube transcripts and practical advice as workflow sources, not scientific evidence for domain claims.
- Use AI/RAG to explain and retrieve, but return to the original source before making claims.

## Evidence Levels

- Green: directly supported by local source or verified external source.
- Yellow: plausible but conditional; needs cautious language.
- Red: not demonstrated; only motivation, limitation or future work.

## Claim Audit Labels

- SUPPORTED: directly supported by source and locator.
- PARTIAL: partly supported or needs conditional wording.
- OVERSTATED: claim is stronger than evidence.
- UNSUPPORTED: no sufficient source.
- UNVERIFIED: source or locator unavailable.

High-risk claims require audit before final text: clinical detection, prevention, AAL completeness, SAR, hardware viability, BLE/IEEE equivalence, numeric results, novelty and superiority.

## Practical Research Workflow Rules

- One paper should have one central idea. If the thesis contains several independent promises, split or downgrade secondary claims.
- Contributions must be refutable claims linked to variables, metrics, methods, evidence, limitations and sections.
- Methods are mandatory reading when a source supports numbers, models, simulations, hardware, energy, QoS, datasets or comparisons.
- Figures need passports: message, data/source, variables, metrics, format, caption, legibility and overclaim risk.
- Venue selection should be based on fit, scope, audience, format, indexation, APC/open access and desk-reject risk, not prestige alone.
- Peer review responses should be point-by-point, courteous, evidence-linked and traceable.
- If retrieval finds no evidence, say so; do not fill gaps from memory.
- If the user struggles to understand, generate didactic material and record the confusion if it is reusable.
- If a figure/table required multiple corrections, extract the reusable design rule into `research_memory/global/learnings/`.
- A visual artifact is not ready until message, caption, legibility and evidence boundary are checked.

## Pipeline Gates

Use the local pipeline in `auditoria_investigacion/18_pipeline_academico.md`.

Do not advance to drafting unless these exist:

- Research question or scoped objective.
- Method or study design.
- Variables and metrics.
- Source map.
- Evidence matrix.
- Known limitations.

Do not advance to finalization unless these pass:

- Claim audit.
- Citation check.
- Methodology review.
- Limitations section.
- LaTeX/BibTeX build plan if PDF is required.
- Didactic pass when the output will be defended or taught.
- Figure/table legibility pass when visual artifacts carry claims.
- Release manifest when the user asks to deliver, share or upload.

## Learning Loop

At the end of substantial research work, especially after confusion or repeated corrections, extract learning:

- What went wrong or was confusing?
- Why did it matter academically or didactically?
- What pattern fixed it?
- Should this become a rule, checklist, skill update, template or memory note?
- Where was it recorded?

Store reusable system-level lessons under `research_memory/global/learnings/`. Keep project-specific facts in the project memory.

## Output Rule

Every substantial research output should include one of:

- A decision.
- A matrix.
- A draft section.
- A list of missing evidence.
- A next action.

Do not leave the user with passive knowledge only.

## Sci-Hub / Paywalled Sources

Do not automate unauthorized article downloads. If a source is paywalled, ask the user to provide a legal/local PDF, an institutional link, an open-access version, an abstract, or permission to search for alternatives.

## LaTeX Policy

Use LaTeX Live for final documents when requested. Before compiling, verify available commands such as `pdflatex`, `xelatex`, `latexmk` or `biber`. Fix minimal build errors and keep source traceability.

For Markdown/LaTeX conversion or PDF ingestion, check `auditoria_investigacion/21_herramientas_instaladas.md` first. Prefer the lightest sufficient tool: PyMuPDF/pymupdf4llm for PDF text, Pandoc for conversion, Zotero/Better BibTeX for references.

## External Skill Adaptation Policy

External research skills can inspire workflows, but do not install or copy large suites by default. Extract patterns, adapt locally, and preserve traceability. Ask before installing tools, MCP servers, hooks, global skills, package managers or anything that changes the environment.
