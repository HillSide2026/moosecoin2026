---
id: RELEASE-2026-03-01-07
title: /00_SYSTEM Release Note 2026-03-01 (07)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (07)

## Version Bump
- From: v0.9
- To: v1.0

## Change Summary
- Adopted new canonical `01_DOCTRINE` taxonomy:
  - `01_INVARIANTS/`
  - `01_PRINCIPLES/`
  - `02_INTERPRETIVE/`
  - `02_POLICIES/`
  - `03_CAPABILITY_PROFILES/`
  - `03_PROTOCOLS/`
  - `04_PROCEDURAL/`
  - `RULES/`
  - `TESTS/`
- Updated system structure/schema documentation to declare the new doctrine subdirectory model.
- Updated active doctrine-path references from legacy `binding/interpretive/constraints` to the new taxonomy.

## Impacted Artifacts
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/SYSTEM_BACKLOG.md
- 00_SYSTEM/BACKLOG_DOCTRINE.md
- 01_DOCTRINE/README.md

## Migration Notes (What changes for authors?)
- Do not create new doctrine files under `01_DOCTRINE/binding`, `01_DOCTRINE/interpretive`, or `01_DOCTRINE/constraints`.
- Place new doctrine artifacts in the canonical taxonomy directories under `01_DOCTRINE/`.
- Legacy path mentions may remain in historical logs/reports/releases for provenance.
