---
id: GOV-2026-006-REG
title: Agent Registry
owner: ML1
status: approved
created_date: 2026-02-09
last_updated: 2026-02-09
effective_date: 2026-02-09
tags: [agents, registry, governance]
provenance:
  decided_by: ML1
  decided_on: 2026-02-09
  context: Canonical registry of executable agents and their type classifications
---

# Agent Registry

Canonical registry of executable agents and their type classification.

## Definitions

- **proto-agent**: An agent fully bound by GOV-2026-006 with no exceptions.
- **approved agent**: An explicitly approved agent with carve-outs defined in GOV-2026-006.

## Registry

| agent | type | source |
|-------|------|--------|
| `repo-linter` | proto-agent | `.claude/agents/repo-linter.md` |
| `folder-map-drift` | proto-agent | `.claude/agents/folder-map-drift.md` |
| `project-manager` | approved agent | `.claude/agents/project-manager.md` |
| `inbox-triage` | proto-agent | `.claude/agents/inbox-triage.md` |
| `moosecoin2026_system_architect` | approved agent | `.claude/agents/moosecoin2026_system_architect.md` |
| `moosecoin_trading_strategist` | approved agent | `.claude/agents/moosecoin_trading_strategist.md` |
