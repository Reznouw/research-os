# Diagram Tooling Audit

## Purpose

Record reusable patterns from external diagram-related tools without making Research OS depend on one specific renderer.

## Findings

| Tool pattern | Useful idea | Limitation | Local decision |
| --- | --- | --- | --- |
| Spec-driven SVG block diagram renderers | Separate architecture/content from geometry | Often domain-specific | Adopt structured figure contracts |
| Mermaid syntax checkers | Validate and repair diagram syntax | Syntax is not visual quality | Use validation loops, not syntax alone |
| Markdown-to-Mermaid renderers | Reproducible diagram exports | May require Docker/Node/CLI | Treat as optional tooling |

## Adopted Pattern

1. Define a figure contract.
2. Choose the lightest sufficient renderer.
3. Render or compile when tools are available.
4. Check syntax, geometry, legibility, caption, and overclaim risk.
5. Iterate only on the highest-impact issue.
6. Switch representation if repeated patches do not improve clarity.
