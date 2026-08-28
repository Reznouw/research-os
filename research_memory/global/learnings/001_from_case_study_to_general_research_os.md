# 001 From Case Study To General Research OS

## Context

A research case study showed that producing a manuscript is not enough. The system also needs to help the author understand the method, defend results, build readable figures and tables, and package outputs reproducibly.

## Reusable Lessons

| Observation | Risk | General pattern |
| --- | --- | --- |
| A table can compile but remain unreadable | False completion | Audit legibility, not just compilation |
| Shrinking dense tables hides design problems | Microscopic text | Reduce columns, split tables, or use wider formats |
| The author can misread their own metric | Weak defense | Explain metrics with definition, example, and safe interpretation |
| Diagrams with crossed arrows confuse readers | Message loss | Use figure contracts and validation loops |
| Numeric results need narrative | Readers see numbers without meaning | Translate results into diagnostic interpretation |
| Defense material is part of research readiness | The author cannot defend the paper | Generate didactic material as part of the pipeline |
| Strong claims are easy to overstate | Academic credibility risk | Maintain claim boundary audits |
| Final files scatter across folders | Hard to share or reproduce | Build release packages with manifests |

## Incorporated Rules

- If the user does not understand, activate didactic mode.
- If a figure or table supports a claim, validate message, caption, legibility, and evidence boundary.
- If a correction required multiple iterations, record the pattern to avoid repeating it.
