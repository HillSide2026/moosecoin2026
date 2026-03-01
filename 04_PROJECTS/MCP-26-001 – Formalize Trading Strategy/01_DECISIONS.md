---
id: 26-001-00001-DECISIONS
title: Decisions - Formalize Trading Strategy
owner: ML1
status: draft
created_date: 2026-02-06
last_updated: 2026-02-08
tags: [trading, strategy, decisions]
---

# Decisions

Record of ML1 decisions, pending decision requests, and rationale.

---

## Approved Decisions

| # | Decision | Rationale | Approved By | Date |
|---|----------|-----------|-------------|------|
| D-001 | Risk governance supersedes delivery velocity | Any conflict between schedule, scope, and risk is resolved in favor of risk | ML1 | 2026-02-06 |
| D-002 | No change increases risk without capital owner approval | Change control principle | ML1 | 2026-02-06 |
| D-003 | Approve Initiation stage outputs | Project Charter, Scope Boundaries, Definitions approved | ML1 | 2026-02-08 |
| D-004 | Approve Planning stage baseline | PMP, scope, schedule, risk register, change control process approved | ML1 | 2026-02-08 |
| D-005 | Revise project scope to operational playbook only | Narrow scope to creating and revising the trading playbook | ML1 | 2026-02-08 |
| D-006 | Approve Go/No-Go for Stage 3 (Trading Playbook) | Stage 3 authorized | ML1 | 2026-02-08 |
| D-007 | Mark Stage 3 complete | Trading playbook, principles, strategy, and platform gating checklist completed | ML1 | 2026-02-08 |
| D-008 | Approve project closure | Closing artifacts approved | ML1 | 2026-02-08 |

## Pending Decision Requests

| # | Request | Context | Requested By | Date |
|---|---------|---------|--------------|------|
| None |  |  |  |  |

---

## Change Control Process

### Change Triggers

- Proposed rule modification
- Risk limit adjustment
- Asset universe expansion

### Process

1. Change request documented
2. Impact analysis (risk, scope, schedule)
3. Risk authority review
4. Sponsor approval required
5. Versioned deployment

### Principle

No change is allowed that increases risk without explicit capital owner approval.

---

## Communications Plan

| Audience | Information | Frequency | Channel |
|----------|-------------|-----------|---------|
| Capital Owner | Status, risk | Bi-weekly | Report |
| Project Team | Tasks, blockers | Weekly | Stand-up |
| Risk Reviewer | Rule changes | As needed | Review memo |

---

## RACI Matrix

| Activity | Sponsor | Designer | Engineer | Risk | Operator |
|----------|---------|----------|----------|------|----------|
| Strategy Rules | A | R | C | C | I |
| Risk Engine | I | C | R | A | I |
| Testing | I | C | R | A | I |
| Deployment | A | C | R | C | I |
| Live Monitoring | I | I | I | C | R |

R = Responsible, A = Accountable, C = Consulted, I = Informed

---

*Note: Decisions are project-specific. They do not constitute doctrine or precedent. See GOV-2026-004.*
