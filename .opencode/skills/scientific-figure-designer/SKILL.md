---
name: scientific-figure-designer
description: Use when creating or improving research figures, block diagrams, flow diagrams, conceptual diagrams, pictorial diagrams, result plots, captions, visual explanations, or figure prompts for papers, theses, slides, and defenses.
---

# Scientific Figure Designer

## Purpose

Design research figures that teach, support claims and survive publication or defense. A figure is not decoration; it is a visual argument.

## Trigger Signals

- "figura", "imagen", "diagrama", "bloques", "flujo", "pictorico".
- "caption", "se ve confuso", "flechas", "cuadros", "grafica", "plot".
- Any request to explain results visually or prepare slides/defense visuals.

## Figure Contract

Before generating, define:

- Message: one sentence the figure must teach.
- Audience: reviewer, jury, author, student, engineer.
- Type: block, flow, pipeline, causal chain, architecture, result plot, concept map, pictorial.
- Evidence source: data, simulation, paper, method, conceptual explanation.
- Variables or entities: exact labels and units if applicable.
- Must include: required nodes, flows, metrics or annotations.
- Must avoid: unsupported claims, extra clutter, ambiguous arrows, tiny text.
- Output format: TikZ, Mermaid, SVG, PNG, PDF, matplotlib, LaTeX table/figure.

## Design Rules

- Prefer fewer elements with stronger hierarchy.
- Use left-to-right for processes, top-to-bottom for abstraction, matrix/regions for tradeoffs.
- Every arrow must mean exactly one relation: data, energy, control, causality, sequence or comparison.
- Do not mix mechanism and result in one figure unless visually separated.
- Captions must explain how to read the figure, not just name it.
- For papers, prefer vector or high-resolution outputs.

## Tool Choice

- Mermaid: fast conceptual flows, simple pipelines, documentation diagrams.
- TikZ: LaTeX-native diagrams, publication control, IEEE integration.
- matplotlib/Python: numeric plots and reproducible result figures.
- SVG renderer/spec: complex block diagrams needing geometry validation.
- Manual LaTeX table/figure: when text precision matters more than graphics.

## Required Output

Return or create:

- figure contract;
- source code/spec;
- rendered artifact when tools allow;
- caption draft;
- validation notes and remaining risks.
