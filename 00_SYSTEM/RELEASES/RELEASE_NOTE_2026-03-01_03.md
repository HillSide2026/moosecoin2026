---
id: RELEASE-2026-03-01-03
title: /00_SYSTEM Release Note 2026-03-01 (03)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (03)

## Version Bump
- From: v0.5
- To: v0.6

## Change Summary
- Renamed canonical Layer 2 folder from `02_PLAYBOOKS/` to `02_MODELS/`.
- Defined `Model` as a decision engine in system docs.
- Added required decision-engine component set for Models:
  - regime filter
  - risk model
  - entry logic
  - exit logic
  - signal generation
  - sizing engine
- Updated active governance/schema references from Playbooks to Models.

## Impacted Artifacts
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/GLOSSARY.md
- 00_SYSTEM/CLAUDE.md
- 00_SYSTEM/LEGACY_TERMS.md
- 00_SYSTEM/governance/enforcement/artifact-compliance-checklist.md
- 00_SYSTEM/governance/enforcement/violation-triage-protocol.md
- 00_SYSTEM/governance/agents/agent-write-guardrail.md
- 00_SYSTEM/governance/canon/gold-promotion-protocol.md
- 00_SYSTEM/governance/canon/matter-to-canon-extraction-doctrine.md
- 00_SYSTEM/governance/canon/matter-to-fact-extraction-protocol.md

## Migration Notes (What changes for authors?)
- Use `02_MODELS/` as the canonical Layer 2 folder.
- Use `Model` (not `Playbook`) for current Layer 2 artifacts.
- Treat historical `Playbook` references as legacy terminology.
