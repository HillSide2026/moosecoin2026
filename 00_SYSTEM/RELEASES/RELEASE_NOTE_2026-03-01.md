---
id: RELEASE-2026-03-01
title: /00_SYSTEM Release Note 2026-03-01
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01

## Version Bump
- From: v0.3
- To: v0.4

## Change Summary
- Updated the canonical `ML2` definition.
- Clarified that `ML2` spans all top-level repository directories (`00_SYSTEM` through `10_ARCHIVE`).
- Retained `Trading System = ML2 + Execution Environment (third-party app(s))`.

## Impacted Artifacts
- 00_SYSTEM/GLOSSARY.md

## Migration Notes (What changes for authors?)
- Do not use `ML2` to mean only governance/docs layers.
- Use `ML2` to reference the full in-repo Second Brain scope.
- Use `Trading System` when referencing `ML2` plus third-party execution apps.
