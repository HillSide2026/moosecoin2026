---
id: SYSTEM-AGENTS-SMA-REGISTRY
title: System Management Agents Registry
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [agents, registry, sma]
---

# System Management Agents Registry

Canonical capture of system-management agents (`SMA###`) within
`00_SYSTEM/AGENTS/`.

## Mission

Maintain ML2 integrity, consistency, auditability, and change-control.
System-management agents do not trade, do not create doctrine, and do not
approve anything.

## Shared Constraints (All SMA Agents)

- Never modify `01_DOCTRINE/` except by generating drafts in `09_INBOX/` (or an
  approved drafts location) for ML1 review.
- Never change meaning of an existing doctrine file; propose edits as drafts
  only.
- Never delete files. Archive-only moves must be proposed, not executed, unless
  explicitly allowed by policy.
- If conflict or ambiguity exists, escalate to ML1 with a structured
  "Decision Needed" memo.

## Allowed Write Locations (Default)

- `00_SYSTEM/AUDITS/` (reports)
- `00_SYSTEM/RELEASES/` (release-note drafts unless allowed otherwise)
- `06_OUTPUTS/` (agent output artifacts)
- `09_INBOX/` (drafts/items needing ML1 review)

## Agents

| Agent ID | Name | Purpose | Spec |
|----------|------|---------|------|
| `SMA001` | Doctrine Integrity Agent | Detect doctrine contradictions, drift, and violations | `00_SYSTEM/AGENTS/SMA001.md` |
| `SMA002` | Model Governance Agent | Govern model structure/completeness/versioning and doctrine linkage | `00_SYSTEM/AGENTS/SMA002.md` |
| `SMA003` | Execution Audit Agent | Audit run/output alignment against doctrine/models | `00_SYSTEM/AGENTS/SMA003.md` |
| `SMA004` | Release & Change Control Agent | Classify changes and produce release and impact drafts | `00_SYSTEM/AGENTS/SMA004.md` |

## Terminology

- `SAA` = System Admin Agent
- `SMA` = System Management Agent
