---
id: GOV-2026-006-REG
title: Agent Registry
owner: ML1
status: approved
created_date: 2026-02-09
last_updated: 2026-03-01
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
- **system-admin agent (SAA)**: A proto-agent focused on system structure, schema, and inbox governance checks.
- **system-management agent (SMA)**: Agents focused on integrity, governance, execution audit, and release/change control for ML2; definitions in `00_SYSTEM/AGENTS/SYSTEM_MANAGEMENT_AGENTS.md`.
- **project-management agent (PMA)**: Approved agents for project, program, and portfolio coordination across `04_PROJECTS/`; definitions in `00_SYSTEM/AGENTS/PROJECT_MANAGEMENT_AGENTS.md`.

## Registry

| agent | legacy_name | type | runtime_source | system_spec |
|-------|-------------|------|----------------|-------------|
| `SAA001` | `repo-linter` | system-admin agent (proto-agent) | `.claude/agents/repo-linter.md` | `00_SYSTEM/AGENTS/SAA001.md` |
| `SAA002` | `folder-map-drift` | system-admin agent (proto-agent) | `.claude/agents/folder-map-drift.md` | `00_SYSTEM/AGENTS/SAA002.md` |
| `project-manager` | `project-manager` | approved agent | `.claude/agents/project-manager.md` | `00_SYSTEM/AGENTS/PMA001.md` |
| `program-manager` | `program-manager` | approved agent | `.claude/agents/program-manager.md` | `00_SYSTEM/AGENTS/PMA002.md` |
| `portfolio-manager` | `portfolio-manager` | approved agent | `.claude/agents/portfolio-manager.md` | `00_SYSTEM/AGENTS/PMA003.md` |
| `SAA003` | `inbox-triage` | system-admin agent (proto-agent) | `.claude/agents/inbox-triage.md` | `00_SYSTEM/AGENTS/SAA003.md` |
| `SMA001` | `doctrine-integrity` | system-management agent | TBD | `00_SYSTEM/AGENTS/SMA001.md` |
| `SMA002` | `model-governance` | system-management agent | TBD | `00_SYSTEM/AGENTS/SMA002.md` |
| `SMA003` | `execution-audit` | system-management agent | TBD | `00_SYSTEM/AGENTS/SMA003.md` |
| `SMA004` | `release-change-control` | system-management agent | TBD | `00_SYSTEM/AGENTS/SMA004.md` |
| `moosecoin2026_system_architect` | `moosecoin2026_system_architect` | approved agent | `.claude/agents/moosecoin2026_system_architect.md` | |
| `moosecoin_trading_strategist` | `moosecoin_trading_strategist` | approved agent | `.claude/agents/moosecoin_trading_strategist.md` | |
