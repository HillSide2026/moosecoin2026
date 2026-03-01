---
id: SYSTEM-AGENTS-SAA-REGISTRY
title: System Admin Agents Registry
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [agents, registry, saa]
---

# System Admin Agents Registry

Canonical capture of system-admin agents (SAA) within `00_SYSTEM/AGENTS/`.

## Agents

| Agent ID | Legacy Name | Purpose | Spec |
|----------|-------------|---------|------|
| `SAA001` | `repo-linter` | Repo structure/schema/naming lint | `00_SYSTEM/AGENTS/SAA001.md` |
| `SAA002` | `folder-map-drift` | Declared-vs-actual structure drift detection | `00_SYSTEM/AGENTS/SAA002.md` |
| `SAA003` | `inbox-triage` | Inbox routing recommendations | `00_SYSTEM/AGENTS/SAA003.md` |

## Runtime Source of Prompt/System Instructions

- `.claude/agents/repo-linter.md`
- `.claude/agents/folder-map-drift.md`
- `.claude/agents/inbox-triage.md`

These runtime prompt files remain executable sources. The `00_SYSTEM/AGENTS/`
documents define canonical governance-facing specifications.
