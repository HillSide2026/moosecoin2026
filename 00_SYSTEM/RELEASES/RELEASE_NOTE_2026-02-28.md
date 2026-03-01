---
id: RELEASE-2026-02-28
title: /00_SYSTEM Release Note 2026-02-28
owner: ML1
status: approved
created_date: 2026-02-28
last_updated: 2026-02-28
tags: [release]
---

# /00_SYSTEM Release Note — 2026-02-28

## Version Bump
- From: v0.2
- To: v0.3

## Change Summary
- Added canonical glossary term `Trading System`.
- Defined `Trading System` as `ML2 + Execution Environment (third-party app(s))`.
- Clarified canonical `ML2` scope as including `00_SYSTEM`, `01_DOCTRINE`, `02_PLAYBOOKS`, and `03_TEMPLATES`.

## Impacted Artifacts
- 00_SYSTEM/GLOSSARY.md

## Migration Notes (What changes for authors?)
- Use `Trading System` when referring to the combined ML2 governance layer and external execution apps.
- Use `ML2` to refer to the in-repo Second Brain layers (including `00_SYSTEM`, `01_DOCTRINE`, `02_PLAYBOOKS`, and `03_TEMPLATES`), not external execution apps.
