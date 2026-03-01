---
id: RELEASE-2026-03-01-11
title: /00_SYSTEM Release Note 2026-03-01 (11)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (11)

## Version Bump
- From: v1.3
- To: v1.4

## Change Summary
- Renamed core `/00_SYSTEM` subdirectories to uppercase:
  - `audits/` -> `AUDITS/`
  - `governance/` -> `GOVERNANCE/`
  - `tools/` -> `TOOLS/`
- Updated active path references to use uppercase naming in system and governance documentation.
- Updated schema gate path reference to `00_SYSTEM/TOOLS/check_frontmatter.py`.

## Impacted Artifacts
- 00_SYSTEM/CLAUDE.md
- 00_SYSTEM/System_Identity.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/GOVERNANCE/enforcement/artifact-compliance-checklist.md
- 00_SYSTEM/GOVERNANCE/enforcement/violation-triage-protocol.md
- 00_SYSTEM/GOVERNANCE/canon/gold-promotion-protocol.md

## Migration Notes (What changes for authors?)
- Use uppercase paths for system internals: `00_SYSTEM/GOVERNANCE/`, `00_SYSTEM/AUDITS/`, `00_SYSTEM/TOOLS/`.
- Historical logs and audits may keep legacy lowercase path references for provenance.
