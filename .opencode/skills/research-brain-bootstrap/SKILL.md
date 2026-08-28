---
name: research-brain-bootstrap
description: Use when starting the research system on a new computer, onboarding a new project, checking portable Research OS readiness, or asking what this workspace can do for papers, theses, literature reviews, defenses, figures, tables, and releases.
---

# Research Brain Bootstrap

## Purpose

Initialize the portable Research OS mindset. Use this skill when the user wants to understand, migrate, clone, restart, or apply the research system to a new topic beyond WBAN.

## Trigger Signals

- "nueva computadora", "subir a GitHub", "portable", "clonar".
- "nuevo proyecto", "nueva tesis", "otro paper", "research system".
- "que puedes hacer", "como usamos este sistema", "desde cero".
- Any cold-start request where the assistant must reconstruct context from files.

## Startup Order

1. Read `AGENTS.md`.
2. Read `RESEARCH_OS.md` if present.
3. Read `.opencode/skills/research-intelligence/SKILL.md`.
4. Read `research_memory/global/learnings/README.md` and recent learning notes if relevant.
5. Read project-specific memory only after identifying the active project.
6. If the active project is WBAN, use `auditoria_investigacion/*.md` as compact memory.

## Cold-Start Checklist

- Identify whether the user wants a paper, thesis, proposal, review, defense, figure/table, or release.
- Identify active project folder or ask only if not inferable.
- State current pipeline stage: intake, scoping, sources, evidence, method, draft, audit, didactic, finalization, release.
- Locate available memory and missing memory.
- Produce one next action, not a generic explanation.

## Output Template

```text
Sistema detectado:
Proyecto activo:
Etapa probable:
Memoria disponible:
Riesgos iniciales:
Siguiente accion:
```

## Rule

Do not treat WBAN as the whole system. Treat WBAN as a benchmark project inside a general Research OS.
