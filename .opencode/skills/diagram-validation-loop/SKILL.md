---
name: diagram-validation-loop
description: Use after generating Mermaid, TikZ, SVG, PNG, PDF, block diagrams or flow diagrams, especially when checking syntax, renderability, geometry, crossings, legibility, captions, and whether the visual actually communicates the intended research message.
---

# Diagram Validation Loop

## Purpose

Render, inspect and improve diagrams before declaring them ready. Passing syntax is not enough; the diagram must be legible and semantically correct.

## Trigger Signals

- After any generated diagram or figure.
- "validar", "revisar imagen", "captura", "render", "se ve mal".
- Tables/figures in LaTeX that compile but may be unreadable.

## Loop

1. Restate intended message.
2. Render or compile using available local tools.
3. Check hard failures: syntax error, missing asset, LaTeX error, no output.
4. Check layout: text size, overlap, arrow crossings, cramped columns, excessive nodes.
5. Check semantics: arrows mean what the caption says, no unsupported implication, no missing variable.
6. Fix only the highest-impact issue.
7. Repeat up to three iterations, then switch representation if still unclear.
8. Record final acceptance criteria.

## Validation Criteria

- The main message is visible in under 10 seconds.
- Labels are readable in the target medium: paper column, full-page, slide or screen.
- No line crosses through unrelated blocks.
- Arrow direction is unambiguous.
- Legend/caption resolves colors, symbols and axes.
- The figure does not imply a stronger claim than the evidence supports.

## Mermaid Notes

When Mermaid is used, validate syntax before presenting final code. If rendering tools are unavailable, state that only syntax-level or source-level review was possible.

## LaTeX Notes

For LaTeX figures/tables, inspect logs for `LaTeX Error`, `Undefined control sequence`, `Overfull` and missing files. `Underfull` is usually cosmetic unless severe readability is affected.
