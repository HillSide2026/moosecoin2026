---
id: RELEASE-2026-03-01-15
title: /00_SYSTEM Release Note 2026-03-01 (15)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (15)

## Version Bump
- From: v1.7
- To: v1.8

## Change Summary
- Captured four system-management agents:
  - `SMA001` Doctrine Integrity Agent
  - `SMA002` Model Governance Agent
  - `SMA003` Execution Audit Agent
  - `SMA004` Release and Change Control Agent
- Upgraded `SYSTEM_MANAGEMENT_AGENTS.md` from placeholder to canonical registry
  with shared mission, hard constraints, and default write locations.
- Added per-agent specs with:
  - purpose
  - reads/writes
  - core checks
  - escalation triggers
  - required output formats
- Updated agent registry to include SMA entries.

## Impacted Artifacts
- 00_SYSTEM/AGENTS/SYSTEM_MANAGEMENT_AGENTS.md
- 00_SYSTEM/AGENTS/SMA001.md
- 00_SYSTEM/AGENTS/SMA002.md
- 00_SYSTEM/AGENTS/SMA003.md
- 00_SYSTEM/AGENTS/SMA004.md
- 00_SYSTEM/AGENTS/README.md
- 00_SYSTEM/GOVERNANCE/agents/AGENT_REGISTRY.md

## Migration Notes (What changes for authors?)
- `SMA` namespace is now defined and populated for system-management workflows.
- `SAA` remains System Admin Agent; `SMA` is System Management Agent.
- Runtime sources for SMA agents are currently `TBD` until executable definitions
  are created.
