# Research OS

Research OS is a portable AI-assisted research workspace for papers, theses, proposals, literature reviews, defenses, figures, tables, and reproducible research packages.

The goal is to turn an AI coding/research assistant into a practical research advisor: it should reason with evidence, detect weak claims, produce understandable artifacts, and learn from repeated mistakes.

## What This Repository Contains

- `AGENTS.md`: operating rules for the assistant.
- `RESEARCH_OS.md`: architecture, pipeline, routing, and quality gates.
- `.opencode/skills/`: local skills for research workflows.
- `research_memory/global/learnings/`: reusable learning notes and improvement patterns.
- `templates/`: starter templates for source passports, claim audits, and project manifests.
- `docs/`: supporting notes and tool audits.

## What This Repository Does Not Include

This public repository intentionally excludes private papers, course materials, local corpora, PDFs, transcripts, datasets, and project-specific research folders. Treat it as the reusable system layer, not as a publication corpus.

## How To Use

1. Clone the repository.
2. Open it with OpenCode or another compatible agent runtime.
3. Start with a natural request such as:
   - `I want to start a research project from zero.`
   - `Help me turn these papers into a literature review.`
   - `I do not understand this result; make it defense-ready.`
   - `Audit this table for an IEEE two-column paper.`
   - `Prepare a final release folder for this paper.`
4. The assistant should infer the right workflow without requiring exact skill names.

## Core Skills

- `research-intelligence`: mother skill and routing layer.
- `research-brain-bootstrap`: cold start and onboarding.
- `didactic-research-material`: explanations, defense guides, and teaching material.
- `research-critical-reviewer`: claim, method, evidence, citation, and limitation review.
- `scientific-figure-designer`: figure contracts and scientific visual design.
- `diagram-validation-loop`: render/check/iterate visual artifacts.
- `academic-table-auditor`: readable and defensible academic tables.
- `research-release-packager`: shareable and reproducible final packages.

## Design Principle

The user should not need to say "use this skill". The system should infer intent from the conversation and act like a research advisor.
