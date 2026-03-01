---
id: SYSTEM-FOLDER-MAP
title: Folder Map
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-03-01
tags: [structure, folders]
---

# Folder Map

This document describes the repository as it exists today (descriptive), not an aspirational target structure.

## 00_SYSTEM/
**Purpose:** System governance and mechanics

**Structure:**
- `/GOVERNANCE/` — System-level rules (agents/, authority/, canon/, enforcement/, change-control/, trading/)
- `/GOVERNANCE/agents/AGENT_REGISTRY.md` — Canonical executable agent registry
- `/AGENTS/` — Agent specifications and prompt/system-instruction artifacts
- `/ORCHESTRATION/` — Agent-run workflows, schedules, triggers, and dependency maps
- `/AUDITS/` — Structural and compliance audit reports
- Key files: AGENT_REGISTRY.md, AGENTS/README.md, AGENTS/SYSTEM_ADMIN_AGENTS.md, AGENTS/SYSTEM_MANAGEMENT_AGENTS.md, ORCHESTRATION/README.md, CLAUDE.md, DECISION_LOG.md, FOLDER_MAP.md, FOLDER_SCHEMAS.md, GLOSSARY.md, LEGACY_TERMS.md, PROJECT_SCHEMA.md, SCHEMAS.md, SYSTEM_BACKLOG.md, TASK_BACKLOG.md, System_Identity.md

**Rules:**
- ML1 write-only
- ML2 read-only
- Never emitted, summarized, or consumed by LL
- `AGENTS/` does not contain trading strategy logic or general reference artifacts
- `ORCHESTRATION/` defines execution coordination, not strategy logic

---

## 01_DOCTRINE/
**Purpose:** Authoritative judgment and constraints

**Structure:**
- `/01_INVARIANTS` — Hard non-negotiable constraints (`always` / `never`)
- `/02_PRINCIPLES` — Guiding strategic preferences and tradeoff heuristics
- `/03_INTERPRETIVE` — Definitions, precedence, and ambiguity resolution
- `/04_POLICIES` — Enforceable rule sets governing behavior
- `/05_CAPABILITY_PROFILES` — Permission boundaries by system component
- `/06_PROTOCOLS` — Standard operating workflows including workflow definition, step sequence, and role responsibilities
- `/08_RULES` — Machine-readable enforcement logic
- `/09_TESTS` — Verification layer for doctrine and enforcement behavior

**Rules:**
- Source-of-truth eligible
- Requires ML1 approval to bind
- Never auto-generated

---

## 02_MODELS/
**Purpose:** Procedural decision engines derived from doctrine

**Structure:**
- Model artifacts by strategy/system domain

**Rules:**
- Never source-of-truth
- May be LL-consumable only if metadata allows (`ll_consumable: true`)
- Must cite Doctrine when relevant
- Model artifacts must define: regime filter, risk model, entry logic,
  exit logic, signal generation, and sizing engine

---

## 03_PROTOCOLS/
**Purpose:** Operational protocol layer for governed procedures

**Structure:**
- `/risk` — Risk protocol artifacts
- `/execution` — Execution protocol artifacts
- `/incident` — Incident protocol artifacts
- `/review` — Review protocol artifacts
- `/documents` — Supporting protocol documents (legacy support)
- `/internal` — Internal protocol support files

**Rules:**
- Authoritative as approved protocols
- Protocol instances in working folders are never canon
- Versioned and approval-gated

---

## 04_PROJECTS/
**Purpose:** Project-specific work

**Structure:**
- Projects are stored directly under `04_PROJECTS/` using the Project ID format.
- Standard (optional) stage subfolders:
  - `01_INITIATION DOCUMENTATION/`
  - `02_PLANNING DOCUMENTATION/`
  - `03_EXECUTION DOCUMENTATION/`
  - `04_CLOSING DOCUMENTATION/`

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
- `/YYYY/MM/run-id/` — Organized by year and month (created when runs exist)

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

## 07_REFERENCE/
**Purpose:** External and static sources

**Structure:**
- By reference type

**Rules:**
- Read-only
- Never binding
- Contextual use only

---

## 08_RESEARCH/
**Purpose:** Exploratory and analytical material

**Structure:**
- By topic domain
- `/facts/` — Extracted facts from projects (by-project/, by-topic/)

**Rules:**
- Reference-only
- No direct emission to LL
- May inform models/protocols

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

## Root-Level Allowed Files

Allowed root files:
- `README.md`
- `LICENSE`
- `CLAUDE.md`
