---
id: MODELS-README
title: Models
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-03-01
tags: [models, decision-engine]
cites_doctrine: []
---

# Models

Models are decision engines derived from doctrine.

A Model includes:
- Regime filter
- Risk model
- Entry logic
- Exit logic
- Signal generation
- Sizing engine

Rules:
- Must include YAML frontmatter per `/00_SYSTEM/SCHEMAS.md`
- May reference doctrine IDs
- If a model conflicts with doctrine, doctrine wins
