---
id: SYSTEM-BACKLOG
title: System Backlog
owner: ML1
status: draft
created_date: 2026-01-22
last_updated: 2026-03-01
tags: [backlog]
---

# System Backlog

System-level improvements, structural changes, and governance work.

---

## Format

| # | Item | Category | Added | Status | Notes |
|---|------|----------|-------|--------|-------|
| 1 | Populate 02_MODELS with delivery content | Structure | 2026-01-22 | Open | Deep folder taxonomy exists but no model files |
| 2 | Define Solution options for Project Overview | Schema | 2026-01-22 | Open | Placeholder only in template and schema |
| 3 | Define Corporate practice area scope | Schema | 2026-01-22 | Open | |
| 4 | Define Transactions practice area scope | Schema | 2026-01-22 | Open | |
| 5 | Define integration surfaces (00_SYSTEM/integrations/) | Structure | 2026-01-22 | Open | Each folder gets a mapping/protocol doc: what the system touches in the Second Brain, what flows in/out, and when. No credentials in git. See questions below. |
| 6 | Create client registry (client number mapping) | Schema | 2026-01-22 | Open | Project IDs use 3-digit client numbers with no central lookup |
| 7 | Clean up git: commit pending changes, remove stale tracked files | Admin | 2026-01-22 | Open | 3.a_Matters/.gitkeep deletion, untracked CLAUDE.md |
| 8 | Reconcile doctrine files with 01_DOCTRINE taxonomy | Structure | 2026-01-23 | Open | Use canonical doctrine subdirectories (`01_INVARIANTS`, `02_PRINCIPLES`, `03_INTERPRETIVE`, `04_POLICIES`, `05_CAPABILITY_PROFILES`, `06_PROTOCOLS`, `08_RULES`, `09_TESTS`). |
| 9 | Reconcile 02_MODELS structure with FOLDER_MAP | Structure | 2026-01-23 | Open | Actual: /delivery/{practice-area}. Declared: /ll-marketing-sales, /ll-client, /ll-solution, /admin, /secondary-business. Lint finding 5.2. |
| 10 | Route or reclassify 09_INBOX/TASK_BACKLOG.md | Admin | 2026-01-23 | Open | Not in declared INBOX structure (/untriaged, /triaged). May belong in 00_SYSTEM/. Lint finding 5.3. |
| 11 | Acknowledge GLOSSARY.md and integrations/ in FOLDER_MAP | Structure | 2026-01-23 | Open | Both are legitimate 00_SYSTEM files not reflected in FOLDER_MAP. Lint finding 5.4. |

---

## Categories

- **Schema** — Definitions, formats, field options
- **Structure** — Folder hierarchy, new locations, reorganization
- **Governance** — Rules, protocols, enforcement
- **Admin** — Git, cleanup, housekeeping
