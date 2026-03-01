---
id: SYSTEM-AGENTS-README
title: AGENTS Directory Specification
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [agents, specs, prompts]
---

# AGENTS Directory Specification

## What Goes Here

- Agent specs (purpose, allowed actions, inputs/outputs)
- Prompts/system instructions

## What Does NOT Go Here

- Trading strategy logic
- General reference

## Notes

- Governance and guardrails remain in `00_SYSTEM/GOVERNANCE/agents/`.
- Executable runtime agent definitions remain in `.claude/agents/`.
- System-admin agent capture:
  - `00_SYSTEM/AGENTS/SYSTEM_ADMIN_AGENTS.md`
  - `00_SYSTEM/AGENTS/SAA001.md`
  - `00_SYSTEM/AGENTS/SAA002.md`
  - `00_SYSTEM/AGENTS/SAA003.md`
- System-management agent capture:
  - `00_SYSTEM/AGENTS/SYSTEM_MANAGEMENT_AGENTS.md`
- Current system-management agent specs:
  - `00_SYSTEM/AGENTS/SMA001.md`
  - `00_SYSTEM/AGENTS/SMA002.md`
  - `00_SYSTEM/AGENTS/SMA003.md`
  - `00_SYSTEM/AGENTS/SMA004.md`
- Project-management agent capture:
  - `00_SYSTEM/AGENTS/PROJECT_MANAGEMENT_AGENTS.md`
- Current project-management agent specs:
  - `00_SYSTEM/AGENTS/PMA001.md`
  - `00_SYSTEM/AGENTS/PMA002.md`
  - `00_SYSTEM/AGENTS/PMA003.md`
- Terminology:
  - `SAA` = System Admin Agent
  - `SMA` = System Management Agent
  - `PMA` = Project Management Agent
