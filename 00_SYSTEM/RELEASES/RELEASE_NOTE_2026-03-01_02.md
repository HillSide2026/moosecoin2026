---
id: RELEASE-2026-03-01-02
title: /00_SYSTEM Release Note 2026-03-01 (02)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (02)

## Version Bump
- From: v0.4
- To: v0.5

## Change Summary
- Added canonical folder-level schema document: `00_SYSTEM/FOLDER_SCHEMAS.md`.
- Clarified in `00_SYSTEM/SCHEMAS.md` that it governs metadata/frontmatter schemas, while folder topology is governed by `00_SYSTEM/FOLDER_SCHEMAS.md`.
- Removed stale project internal structure block from `00_SYSTEM/SCHEMAS.md` and redirected to `00_SYSTEM/FOLDER_SCHEMAS.md` and `00_SYSTEM/PROJECT_SCHEMA.md`.
- Updated references in `00_SYSTEM/FOLDER_MAP.md` and precedence in `00_SYSTEM/PROJECT_SCHEMA.md`.

## Impacted Artifacts
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/PROJECT_SCHEMA.md

## Migration Notes (What changes for authors?)
- Use `00_SYSTEM/FOLDER_SCHEMAS.md` for folder structure expectations.
- Use `00_SYSTEM/SCHEMAS.md` for frontmatter/metadata requirements.
- For project-specific structure, apply `00_SYSTEM/PROJECT_SCHEMA.md` plus `00_SYSTEM/FOLDER_SCHEMAS.md`.
