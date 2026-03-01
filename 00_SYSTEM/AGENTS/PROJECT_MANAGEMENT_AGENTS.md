---
id: SYSTEM-AGENTS-PMA-REGISTRY
title: Project Management Agents Registry
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [agents, registry, pma]
---

# Project Management Agents Registry

Canonical capture of project-management agents for project, program, and
portfolio orchestration.

## Mission

Maintain delivery coherence across `04_PROJECTS/` by producing structured,
non-authoritative planning and status intelligence for ML1.

These agents do not trade, do not approve, and do not change governance
authority.

## Program Definition

For PMA coordination purposes:

- Program: `Launch Trading System`
- Trading System: `ML2 + Execution Environment (third-party app(s))`

## Shared Constraints (All PMA Agents)

- ML1 remains sole authority for lifecycle gates and approvals.
- Agents may propose stage advancement but cannot execute it autonomously.
- Ambiguity or conflict requires explicit ML1 escalation.
- Outputs are advisory drafts only.

## Allowed Write Locations (Default)

- `09_INBOX/_AGENT_OUTPUT/` (reports)
- `04_PROJECTS/**` (project-local maintenance only when explicitly permitted)

## Agents

| Agent ID | Name | Purpose | Spec |
|----------|------|---------|------|
| `PMA001` | Project Manager Agent | Single-project stage, backlog, and dependency coordination | `00_SYSTEM/AGENTS/PMA001.md` |
| `PMA002` | Program Manager Agent | Multi-project program sequencing and blocker orchestration | `00_SYSTEM/AGENTS/PMA002.md` |
| `PMA003` | Portfolio Manager Agent | Portfolio prioritization, capacity/risk balancing, and ML1 action queue | `00_SYSTEM/AGENTS/PMA003.md` |

## Runtime Source of Prompt/System Instructions

- `.claude/agents/project-manager.md`
- `.claude/agents/program-manager.md`
- `.claude/agents/portfolio-manager.md`

## Terminology

- `PMA` = Project Management Agent
