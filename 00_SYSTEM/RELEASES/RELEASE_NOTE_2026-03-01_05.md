---
id: RELEASE-2026-03-01-05
title: /00_SYSTEM Release Note 2026-03-01 (05)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (05)

## Version Bump
- From: v0.7
- To: v0.8

## Change Summary
- Addressed SAA001 advisory item for root-file allowance by explicitly allowing `CLAUDE.md` at repository root.
- Addressed SAA001/SAA002 advisory item for research facts structure by creating:
  - `08_RESEARCH/facts/`
  - `08_RESEARCH/facts/by-project/`
  - `08_RESEARCH/facts/by-topic/`
- Updated compliance checklist orphan-check language to include `CLAUDE.md` as an allowed root file.

## Impacted Artifacts
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/governance/enforcement/artifact-compliance-checklist.md
- 08_RESEARCH/facts/.gitkeep
- 08_RESEARCH/facts/by-project/.gitkeep
- 08_RESEARCH/facts/by-topic/.gitkeep

## Migration Notes (What changes for authors?)
- Root `CLAUDE.md` is now explicitly allowed by governance.
- Use `08_RESEARCH/facts/by-project/` and `08_RESEARCH/facts/by-topic/` for extracted-fact storage.
