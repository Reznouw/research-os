---
name: didactic-research-material
description: Use when the user says they do not understand, asks for explanation, defense guide, teaching material, oral defense, step-by-step reading, analogies, or wants complex research results made clear and defendable.
---

# Didactic Research Material

## Purpose

Convert technical research into material the author can understand, explain and defend. This skill is not for simplifying by removing rigor; it preserves evidence while lowering cognitive load.

## Trigger Signals

- "no entiendo", "explicame", "me cuesta", "defender", "guia de defensa".
- "hazlo didactico", "paso a paso", "como lo explico", "preguntas del jurado".
- Confusion about metrics, figures, tables, algorithms, methods or results.

## Didactic Contract

Before writing, identify:

- Audience: author, professor, reviewer, jury, student, general technical reader.
- Object: concept, method, result, figure, table, claim, section, full paper.
- Required depth: intuition, technical explanation, defense-ready, publication-ready.
- Evidence boundary: what is proven, conditional, unknown or future work.

## Output Patterns

Use one or more:

- One-sentence core idea.
- Plain-language explanation.
- Technical explanation.
- Step-by-step reading path.
- What to say in defense.
- What not to say.
- Likely jury questions and safe answers.
- Mini-example using the actual variables or metrics.
- Figure/table reading guide.

## Anti-Confusion Rules

- Define every metric before interpreting it.
- Explain zero, null, threshold, average, loss, baseline and normalized units explicitly when they matter.
- Separate mechanism from result: what the model does vs what the experiment shows.
- Do not claim clinical, hardware or deployment implications unless evidence supports them.
- If the user was confused once, add a warning box or note in the didactic material.

## Done Criteria

Material is ready only if a reader can answer:

- What problem is being addressed?
- What was measured?
- What changed between alternatives?
- What conclusion is safe?
- What limitation must be admitted?
