---
id: SYSTEM-FOLDER-MAP
title: Folder Map
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [structure, folders]
---

# Folder Map

This document describes the repository as it exists today (descriptive), not an aspirational target structure.

## 00_SYSTEM/
**Purpose:** System governance and mechanics

**Structure:**
- `/governance/` — System-level rules (agents/, authority/, canon/, enforcement/, change-control/)
- `/audits/` — Structural and compliance audit reports
- Key files: CLAUDE.md, DECISION_LOG.md, FOLDER_MAP.md, GLOSSARY.md, LEGACY_TERMS.md, PROJECT_SCHEMA.md, SCHEMAS.md, SYSTEM_BACKLOG.md, TASK_BACKLOG.md, System_Identity.md

**Rules:**
- ML1 write-only
- ML2 read-only
- Never emitted, summarized, or consumed by LL

---

## 01_DOCTRINE/
**Purpose:** Authoritative judgment and constraints

**Structure:**
- `/binding` — Rules that govern behavior
- `/interpretive` — Guidance, principles
- `/constraints` — Limits, prohibitions

**Rules:**
- Source-of-truth eligible
- Requires ML1 approval to bind
- Never auto-generated

---

## 02_PLAYBOOKS/
**Purpose:** Procedural "how-to" guidance

**Structure:**
- (pending declaration — see Phase 3 Structural Diff Report)

**Rules:**
- Never source-of-truth
- May be LL-consumable only if metadata allows (`ll_consumable: true`)
- Must cite Doctrine when relevant

---

## 03_TEMPLATES/
**Purpose:** Structured starting points for outputs

**Structure:**
- `/documents` — Document templates
- `/internal` — Internal-use templates
- `/checklists` — Checklist templates
- `/snippets` — Reusable text fragments

**Rules:**
- Authoritative only as templates
- Instantiated outputs are never canon
- Versioned and approval-gated

---

## 04_PROJECTS/
**Purpose:** Project-specific work

**Structure:**
- `/open/` — Active projects by priority
  - `/essential` — Highest priority
  - `/strategic` — Strategic importance
  - `/standard` — Normal priority
  - `/parked` — On hold
- `/pending/` — Awaiting action or decision
- `/closed/` — Completed projects

**Project ID Format:** `##-###-#####` (legacy: Matter ID)

**Rules:**
- Non-authoritative by default
- Cannot override canon
- High agent access, low authority

---

## Legacy Aliases

- Matter → Project (legacy only; do not use for new work)

## 05_RUNS/
**Purpose:** Audit and execution records

**Structure:**
- `/YYYY/MM/run-id/` — Organized by year and month

**Rules:**
- Immutable
- Never authoritative
- Citable only as provenance

---

## 06_OUTPUTS/
**Purpose:** Human-consumable deliverables

**Structure:**
- `/drafts` — Work in progress
- `/reviews` — Pending review
- `/exports` — Final exports

**Rules:**
- Consumable, not authoritative
- May flow to LL if derived from canon
- Cannot become "Gold"

---

## 07_RESEARCH/
**Purpose:** Exploratory and analytical material

**Structure:**
- By topic domain
- `/facts/` — Extracted facts from projects (by-project/, by-topic/)

**Rules:**
- Reference-only
- No direct emission to LL
- May inform playbooks/templates

---

## 08_REFERENCE/
**Purpose:** External and static sources

**Structure:**
- By reference type
- `/external_systems/` — Non-binding external architectures and notes

**Rules:**
- Read-only
- Never binding
- Contextual use only

---

## 09_INBOX/
**Purpose:** Intake and triage

**Structure:**
- `/untriaged` — New, unprocessed items
- `/triaged` — Processed, awaiting routing
- `/_AGENT_OUTPUT/` — Agent write target (per GOV-2026-006)

**Rules:**
- Time-limited residence
- No authority
- Must be promoted or archived

---

## 10_ARCHIVE/
**Purpose:** Historical preservation

**Structure:**
- By artifact origin

**Rules:**
- Retains original authority status
- Archive ≠ deprecated
- Read-only

---

## Tooling (Not Structural)

The following directories support tooling and are not part of the content structure:

- `.claude/` — Claude Code agent definitions and settings
- `.github/` — GitHub templates and workflows
