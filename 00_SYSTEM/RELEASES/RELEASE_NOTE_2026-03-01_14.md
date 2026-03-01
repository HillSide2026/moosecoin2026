---
id: RELEASE-2026-03-01-14
title: /00_SYSTEM Release Note 2026-03-01 (14)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (14)

## Version Bump
- From: v1.6
- To: v1.7

## Change Summary
- Clarified agent namespace distinction:
  - `SAA` = System Admin Agent
  - `SMA` = System Management Agent
- Preserved existing `SAA001`/`SAA002`/`SAA003` system-admin capture.
- Added reserved draft registry for upcoming SMA definitions:
  - `00_SYSTEM/AGENTS/SYSTEM_MANAGEMENT_AGENTS.md`
- Updated active agent docs to reflect the SAA/SMA distinction.

## Impacted Artifacts
- 00_SYSTEM/AGENTS/README.md
- 00_SYSTEM/AGENTS/SYSTEM_ADMIN_AGENTS.md
- 00_SYSTEM/AGENTS/SAA001.md
- 00_SYSTEM/AGENTS/SAA002.md
- 00_SYSTEM/AGENTS/SAA003.md
- 00_SYSTEM/AGENTS/SYSTEM_MANAGEMENT_AGENTS.md
- 00_SYSTEM/GOVERNANCE/agents/AGENT_REGISTRY.md
- 00_SYSTEM/FOLDER_MAP.md
- .claude/agents/repo-linter.md
- .claude/agents/folder-map-drift.md
- .claude/agents/inbox-triage.md

## Migration Notes (What changes for authors?)
- Continue using `SAA###` for existing system-admin agents.
- Define new system-management agents under the `SMA###` namespace.
