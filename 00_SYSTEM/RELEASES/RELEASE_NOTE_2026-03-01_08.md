---
id: RELEASE-2026-03-01-08
title: /00_SYSTEM Release Note 2026-03-01 (08)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (08)

## Version Bump
- From: v1.0
- To: v1.1

## Change Summary
- Renumbered canonical `01_DOCTRINE` taxonomy to sequential `01` through `07`:
  - `01_INVARIANTS/`
  - `02_PRINCIPLES/`
  - `03_INTERPRETIVE/`
  - `04_POLICIES/`
  - `05_CAPABILITY_PROFILES/`
  - `06_PROTOCOLS/`
  - `07_PROCEDURAL/`
- Kept `RULES/` and `TESTS/` as unnumbered doctrine support folders.
- Updated active system doctrine-structure references to match the renumbering.

## Impacted Artifacts
- 01_DOCTRINE/README.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/SYSTEM_BACKLOG.md

## Migration Notes (What changes for authors?)
- Use `01_DOCTRINE/06_PROTOCOLS/` (doctrine-level protocols), not `01_DOCTRINE/03_PROTOCOLS/`.
- Use `01_DOCTRINE/07_PROCEDURAL/` for procedural doctrine.
- Existing historical references may keep prior numbering for provenance.
