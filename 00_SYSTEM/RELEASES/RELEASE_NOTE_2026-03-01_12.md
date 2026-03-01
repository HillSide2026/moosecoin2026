---
id: RELEASE-2026-03-01-12
title: /00_SYSTEM Release Note 2026-03-01 (12)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (12)

## Version Bump
- From: v1.4
- To: v1.5

## Change Summary
- Added `00_SYSTEM/AGENTS/` as a canonical system directory for:
  - Agent specs (purpose, allowed actions, inputs/outputs)
  - Prompt/system-instruction artifacts
- Added `00_SYSTEM/ORCHESTRATION/` as a canonical system directory for:
  - Run graphs/workflows
  - Schedules/triggers
  - Dependency maps
- Clarified exclusions for both folders:
  - No trading strategy logic
  - No general reference content
- Updated system maps/schemas/boot instructions to reflect these directories.

## Impacted Artifacts
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/CLAUDE.md
- 00_SYSTEM/AGENTS/README.md
- 00_SYSTEM/ORCHESTRATION/README.md

## Migration Notes (What changes for authors?)
- Place agent specification and prompt content in `00_SYSTEM/AGENTS/`.
- Place orchestration pipelines/schedules/dependency maps in `00_SYSTEM/ORCHESTRATION/`.
- Continue to use `00_SYSTEM/GOVERNANCE/agents/` for guardrails and registry.
