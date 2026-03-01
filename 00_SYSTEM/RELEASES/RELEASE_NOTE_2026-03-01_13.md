---
id: RELEASE-2026-03-01-13
title: /00_SYSTEM Release Note 2026-03-01 (13)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (13)

## Version Bump
- From: v1.5
- To: v1.6

## Change Summary
- Captured system-admin agents explicitly in `00_SYSTEM/AGENTS/`:
  - `SAA001` (repo-linter)
  - `SAA002` (folder-map-drift)
  - `SAA003` (inbox-triage)
- Added canonical governance-facing specs for each SAA:
  - purpose
  - allowed actions
  - disallowed actions
  - inputs/outputs
  - prompt/system-instruction capture with runtime source
- Added SAA registry document under `00_SYSTEM/AGENTS/`.

## Impacted Artifacts
- 00_SYSTEM/AGENTS/README.md
- 00_SYSTEM/AGENTS/SYSTEM_ADMIN_AGENTS.md
- 00_SYSTEM/AGENTS/SAA001.md
- 00_SYSTEM/AGENTS/SAA002.md
- 00_SYSTEM/AGENTS/SAA003.md
- 00_SYSTEM/FOLDER_MAP.md

## Migration Notes (What changes for authors?)
- Use `00_SYSTEM/AGENTS/` for canonical SAA specifications.
- Treat `.claude/agents/*.md` as executable runtime prompt sources.
- Keep governance authority and guardrails in `00_SYSTEM/GOVERNANCE/agents/`.
