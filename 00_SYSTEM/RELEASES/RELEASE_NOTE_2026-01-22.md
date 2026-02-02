---
id: RELEASE-2026-01-22
title: /00_SYSTEM Release Note 2026-01-22
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [release]
---

# /00_SYSTEM Release Note — 2026-01-22

## Version Bump
- From: v0.1
- To: v0.2

## Change Summary
- Added frontmatter enforcement gate and CI workflow.
- Introduced /00_SYSTEM release process and template.
- Standardized canonical naming to Projects with explicit legacy aliasing.
- Added YAML frontmatter across system documentation.

## Impacted Artifacts
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/README.md
- 00_SYSTEM/RELEASES/RELEASE_PROCESS.md
- 00_SYSTEM/RELEASES/TEMPLATE_RELEASE_NOTE.md
- 00_SYSTEM/tools/check_frontmatter.py

## Migration Notes (What changes for authors?)
- All markdown files must include YAML frontmatter and pass the schema gate.
- Use “Project” as the canonical term; treat “Matter” as legacy only.
- Add a release note for any change under /00_SYSTEM.
