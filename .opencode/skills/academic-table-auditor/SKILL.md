---
name: academic-table-auditor
description: Use when creating, fixing, or reviewing academic tables, LaTeX tabulars, IEEE two-column tables, result tables, comparison matrices, readability issues, resizebox use, units, captions, and table interpretation.
---

# Academic Table Auditor

## Purpose

Make tables readable, defensible and publication-ready. A table is ready only when it communicates a decision or comparison, not merely when LaTeX compiles.

## Trigger Signals

- "tabla", "cuadro", "matriz", "comparacion", "resultados".
- "se ve pequeno", "no entra", "resizebox", "overfull", "IEEE".
- Numeric results, metrics, baselines, parameters or policy comparisons.

## Audit Checklist

- Message: what should the reader conclude from the table?
- Scope: are there too many columns for the target format?
- Units: are metrics, units and normalization explicit?
- Headers: are they short but unambiguous?
- Precision: are decimals meaningful and consistent?
- Sorting: is the order logical: baseline, variants, proposed, or severity?
- Caption: does it explain context and how to read values?
- Legibility: does it fit without microscopic text?
- Evidence: are numbers traceable to data, script or source?
- Overclaim: does the table imply superiority beyond conditions tested?

## Red Flags

- `\resizebox{\linewidth}{!}{...}` used to hide too many columns.
- Long text paragraphs inside cells in two-column format.
- Metrics without denominator or definition.
- Mixed units in one column.
- Captions that only repeat the title.
- Tables with values but no interpretation in the surrounding paragraph.

## Fix Patterns

- Split one dense table into two purposeful tables.
- Use three columns: item, decision/metric, risk/interpretation.
- Move long explanations to bullets below the table.
- Abbreviate labels only when defined nearby.
- Use `table*` for genuinely wide comparisons.
- Reduce `\tabcolsep` locally before shrinking font aggressively.

## Done Criteria

The table is ready when it compiles, has no significant overflow, fits the target medium, and a reader can state the main conclusion without reading the full section.
