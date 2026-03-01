---
id: RELEASE-2026-03-01-09
title: /00_SYSTEM Release Note 2026-03-01 (09)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (09)

## Version Bump
- From: v1.1
- To: v1.2

## Change Summary
- Finalized `01_DOCTRINE` taxonomy as `01` through `09`.
- Renamed doctrine support folders:
  - `RULES/` -> `08_RULES/`
  - `TESTS/` -> `09_TESTS/`
- Codified directory-level specs for `01_INVARIANTS` through `09_TESTS`:
  - invariants as absolute statements (`always` / `never`)
  - principles as competing strategic preferences
  - interpretive/precedence and ambiguity handling
  - policies as enforceable behavior controls
  - capability profiles as permission boundaries
  - protocols as repeatable workflows
  - procedural as exact steps
  - rules as machine-readable enforcement logic
  - tests as verification layer

## Impacted Artifacts
- 01_DOCTRINE/README.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/SYSTEM_BACKLOG.md

## Migration Notes (What changes for authors?)
- Place enforcement logic under `01_DOCTRINE/08_RULES/`.
- Place verification assets under `01_DOCTRINE/09_TESTS/`.
- Use `01_DOCTRINE/06_PROTOCOLS/` for doctrine-level protocols and `03_PROTOCOLS/` for system protocol artifacts.
