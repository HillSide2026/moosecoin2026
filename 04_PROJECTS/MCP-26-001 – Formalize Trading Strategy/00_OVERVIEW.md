---
project:
  id: 26-001-00001
  title: MooseCoin - Formalize Trading Strategy, Approach, and Tactics
  stage: closing
  status: closed
owner:
  ml1: ML1
created_date: 2026-02-03
last_updated: 2026-02-08
dependencies:
  depends_on: []
  blocks: [26-001-00002, 26-001-00003]
tags: [trading, strategy, doctrine]
---

# Project Overview

## Governance

| Property | Value |
|----------|-------|
| Lifecycle Model | Standard 4-stage project lifecycle |
| Authority | ML1 approves transitions between stages |
| Role of ML2 | System-of-record, structure, consistency, audit trail |
| Governance Principle | Risk governance supersedes delivery velocity |

## Objective

Create and revise an operational trading playbook with explicit, inspectable procedures under strict risk governance.

## Key Questions

- What markets are in scope?
- What time horizons exist (strategy vs tactics)?
- What decisions must remain discretionary vs systematized?

## Scope

### In Scope

- Create and revise an operational trading playbook
- Document explicit procedures for entry, stop, target, stand-aside
- Define risk governance rules and non-negotiable constraints
- Define market universe and session constraints at the playbook level

### Out of Scope

- Building or implementing a trading system or risk engine
- Backtesting, walk-forward testing, paper trading, or live pilot execution
- Performance optimization for win rate or frequency
- Latency-sensitive or HFT execution
- AI/ML self-modifying logic in live trading
- Platform selection (deferred to 26-001-00002)
- Website development (deferred to 26-001-00003)

### Assumptions

- Capital owner accepts low trade frequency
- Standing aside is an acceptable outcome

### Constraints

- Hard risk limits (per-trade, daily, weekly)
- No averaging down or position scaling
- Crypto exposure flat by session end
- Single active strategy instance per account

## Definitions

See `01_INITIATION DOCUMENTATION/DEFINITIONS.md` for detailed definitions.

| Term | Definition |
|------|------------|
| Strategy | Enduring principles defining what we achieve and why; long-term, binding, ML1-only decisions |
| Approach | General methodology for implementing strategy; medium-term, procedural guidance |
| Tactics | Specific executable procedures for action; short-term, execution-level checklists |

## Key Dates

| Date | Event |
|------|-------|
| 2026-02-03 | Project opened |
| 2026-02-03 | Initiation outputs drafted |
| 2026-02-06 | Planning stage deliverables received |
| | Planning complete (pending ML1 approval) |
| | Execution complete |
| | Project closed |

## Current Stage

**Stage 3: Trading Playbook** — Complete (2026-02-08)

**Stage 4: Closing** — Complete (2026-02-08)

### Stage 1 Outputs (Initiation)

| Output | Status | Location |
|--------|--------|----------|
| Project Charter | Draft | `01_INITIATION DOCUMENTATION/PROJECT_CHARTER.md` |
| Scope Boundaries | Draft | `01_INITIATION DOCUMENTATION/SCOPE_BOUNDARIES.md` |
| Definitions | Draft | `01_INITIATION DOCUMENTATION/DEFINITIONS.md` |

### Stage 2 Outputs (Planning)

| Output | Status | Location |
|--------|--------|----------|
| Scope Statement | Draft | `00_OVERVIEW.md` (this file, Scope section) |
| Work Breakdown Structure | Draft | `03_DEPENDENCIES.md` |
| Schedule / Roadmap | Draft | `03_DEPENDENCIES.md` |
| Resource Plan | Draft | `03_DEPENDENCIES.md` |
| Budget / Cost Baseline | Draft | `03_DEPENDENCIES.md` |
| Risk Register (Full) | Draft | `02_RISKS.md` |
| Communications Plan | Draft | `01_DECISIONS.md` |
| RACI Matrix | Draft | `01_DECISIONS.md` |
| Change Control Process | Draft | `01_DECISIONS.md` |

## Dependencies

- None (this is the first project in the dependency chain)

## Downstream Projects

- 26-001-00002 (Trading Platform Selection) — blocked until Closing
- 26-001-00003 (Website Development) — blocked until Closing

## Status Summary

Planning stage deliverables received (2026-02-06). Full PMP including scope statement, WBS, schedule, risk register, resource plan, budget baseline, communications plan, RACI matrix, and change control process have been filed across canonical project files.

**Next Step:** Archive project and transition refinement to Project 4.
