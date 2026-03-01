---
id: RELEASE-2026-03-01-04
title: /00_SYSTEM Release Note 2026-03-01 (04)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (04)

## Version Bump
- From: v0.6
- To: v0.7

## Change Summary
- Classified `repo-linter`, `folder-map-drift`, and `inbox-triage` as system-admin agents (SAA).
- Assigned canonical SAA names:
  - `SAA001` (legacy: `repo-linter`)
  - `SAA002` (legacy: `folder-map-drift`)
  - `SAA003` (legacy: `inbox-triage`)
- Updated canonical registry and agent definition metadata to reflect SAA naming.

## Impacted Artifacts
- 00_SYSTEM/governance/agents/AGENT_REGISTRY.md
- .claude/agents/repo-linter.md
- .claude/agents/folder-map-drift.md
- .claude/agents/inbox-triage.md

## Migration Notes (What changes for authors?)
- Use `SAA001`, `SAA002`, and `SAA003` as canonical names in new governance references.
- Treat `repo-linter`, `folder-map-drift`, and `inbox-triage` as legacy names.
