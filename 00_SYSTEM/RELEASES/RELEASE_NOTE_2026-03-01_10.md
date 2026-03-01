---
id: RELEASE-2026-03-01-10
title: /00_SYSTEM Release Note 2026-03-01 (10)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (10)

## Version Bump
- From: v1.2
- To: v1.3

## Change Summary
- Consolidated `01_DOCTRINE/06_PROTOCOLS/` and `01_DOCTRINE/07_PROCEDURAL/` into a single protocol layer at `01_DOCTRINE/06_PROTOCOLS/`.
- Removed `01_DOCTRINE/07_PROCEDURAL/`.
- Standardized protocol-document expectations so each protocol file includes:
  - Workflow definition
  - Step sequence
  - Role responsibilities
- Updated doctrine structure declarations to remove `07_PROCEDURAL` and preserve conceptual clarity inside protocol documents.

## Impacted Artifacts
- 01_DOCTRINE/README.md
- 01_DOCTRINE/06_PROTOCOLS/DOCTRINE-2026-00X-run-protocol-draft.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/SYSTEM_BACKLOG.md

## Migration Notes (What changes for authors?)
- Do not create doctrine files under `01_DOCTRINE/07_PROCEDURAL/`.
- Place procedural detail inside each `01_DOCTRINE/06_PROTOCOLS/` document.
- Keep protocol documents self-contained using the three required sections.
