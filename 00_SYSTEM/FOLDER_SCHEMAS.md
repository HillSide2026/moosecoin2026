---
id: SYSTEM-FOLDER-SCHEMAS
title: Folder Schemas
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [schemas, folders, structure]
---

# Folder Schemas

Canonical folder-level structure for MooseCoin2026.

This document defines what each top-level folder is for and what structure is
expected inside it. For artifact metadata/frontmatter requirements, see
`00_SYSTEM/SCHEMAS.md`.

If this document conflicts with descriptive examples elsewhere, this document
wins for folder structure expectations.

---

## 00_SYSTEM/

**Purpose:** System governance and mechanics

**Expected structure:**
- `GOVERNANCE/`
- `AGENTS/`
- `ORCHESTRATION/`
- `AUDITS/`
- `RELEASES/`
- `TOOLS/`
- system-level markdown files (for example: `FOLDER_MAP.md`, `SCHEMAS.md`)

**Constraints:**
- Changes require `/00_SYSTEM` release notes.
- No project-specific execution artifacts belong here.
- `AGENTS/` stores agent specs plus prompt/system-instruction artifacts only.
- `AGENTS/` excludes trading strategy logic and general reference content.
- `ORCHESTRATION/` stores run graphs/workflows, schedules/triggers, and dependency maps.

---

## 01_DOCTRINE/

**Purpose:** Binding/authoritative doctrine

**Expected structure:**
- `01_INVARIANTS/`
- `02_PRINCIPLES/`
- `03_INTERPRETIVE/`
- `04_POLICIES/`
- `05_CAPABILITY_PROFILES/`
- `06_PROTOCOLS/`
- `08_RULES/`
- `09_TESTS/`

**Constraints:**
- Doctrine is authoritative only when `status: approved`.
- Doctrine files require doctrine schema fields from `00_SYSTEM/SCHEMAS.md`.
- `01_INVARIANTS` statements must be absolute (`always` / `never`).
- `06_PROTOCOLS` files must include workflow definition, step sequence, and role responsibilities.

---

## 02_MODELS/

**Purpose:** Procedural decision engines derived from doctrine

**Expected structure:**
- Flexible by domain/workflow

**Constraints:**
- May not override doctrine.
- If relevant, models must cite doctrine IDs.
- A model is a decision engine and must include:
  - regime filter
  - risk model
  - entry logic
  - exit logic
  - signal generation
  - sizing engine

---

## 03_PROTOCOLS/

**Purpose:** Operational protocol layer

**Expected structure:**
- `risk/`
- `execution/`
- `incident/`
- `review/`
- `documents/` (supporting/legacy protocol documents)
- `internal/`

**Constraints:**
- Protocols are authoritative only when approved.
- Protocol instances and derived outputs are non-canon by default.

---

## 04_PROJECTS/

**Purpose:** Project-specific work records

**Expected structure:**
- Project folders directly under `04_PROJECTS/`
- Naming format: `YY-CCC-NNNNN Client Name - Description`
- Optional stage folders inside a project:
  - `01_INITIATION DOCUMENTATION/`
  - `02_PLANNING DOCUMENTATION/`
  - `03_EXECUTION DOCUMENTATION/`
  - `04_CLOSING DOCUMENTATION/`

**Constraints:**
- No intermediary status directories such as `open/`, `pending/`, or `closed/`.
- Projects are non-authoritative by default.

---

## 05_RUNS/

**Purpose:** Run/execution audit records

**Expected structure:**
- `YYYY/MM/run-id/` when run artifacts exist

**Constraints:**
- Completed run records are immutable.

---

## 06_OUTPUTS/

**Purpose:** Human-consumable deliverables

**Expected structure:**
- `drafts/`
- `reviews/`
- `exports/`

**Constraints:**
- Outputs are consumable, not authoritative.

---

## 07_REFERENCE/

**Purpose:** External/static references

**Expected structure:**
- Grouping by reference type/domain

**Constraints:**
- Reference-only; never binding.

---

## 08_RESEARCH/

**Purpose:** Exploratory analysis and research artifacts

**Expected structure:**
- Grouping by topic/domain
- Optional `facts/` subtree for extracted facts

**Constraints:**
- Research is reference-only; not doctrine.

---

## 09_INBOX/

**Purpose:** Intake and triage

**Expected structure:**
- `untriaged/`
- `triaged/`
- `_AGENT_OUTPUT/`

**Constraints:**
- Inbox residence is temporary.
- Inbox artifacts have no authority.

---

## 10_ARCHIVE/

**Purpose:** Historical preservation

**Expected structure:**
- Grouping by origin/source

**Constraints:**
- Archive is read-only and historical.
- Archive does not grant authority.
