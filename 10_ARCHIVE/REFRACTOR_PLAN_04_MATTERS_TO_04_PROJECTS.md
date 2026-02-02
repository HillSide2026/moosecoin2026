---
id: ARCHIVE-REFACTOR-04-MATTERS-TO-PROJECTS
title: Refactor Plan — 04_MATTERS → 04_PROJECTS (Design Only)
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [archive, refactor]
---

# Refactor Plan — 04_MATTERS → 04_PROJECTS (Design Only)

## Objective
Rename the legacy folder `04_MATTERS/` to `04_PROJECTS/` and migrate references
safely while preserving history, links, and interpretability.

This document defines a refactor plan only. No execution is authorized by this file.

---

## Preconditions
1. `LEGACY_TERMS.md` declares: Matter → Project.
2. System identity instructs agents to interpret Matter as Project.
3. Repository working tree is clean.
4. A baseline tag exists prior to refactor execution.
5. An inventory of references to legacy paths and terms has been identified.

---

## Refactor Strategy

### Phase 3A — Dual-Path Compatibility
- Introduce `04_PROJECTS/` alongside `04_MATTERS/`.
- Migrate a limited subset of items initially.
- Add a notice file in `04_MATTERS/` indicating legacy status.

### Phase 3B — Full Cutover
- Migrate remaining items to `04_PROJECTS/`.
- Update all structural references, schemas, templates, and maps.
- Remove or archive `04_MATTERS/` after verification.

---

## Discovery Requirements
Identify all references to:
- `04_MATTERS`
- "Matter" used as a structural or schema term

Expected locations include:
- `00_SYSTEM/FOLDER_MAP.md`
- `00_SYSTEM/SCHEMAS.md`
- `00_SYSTEM/MATTER_SCHEMA.md`
- Templates and playbooks
- Automation or tooling scripts

---

## Execution Checklist (When Authorized)
1. Create baseline tag.
2. Execute folder migration according to selected strategy.
3. Update folder maps and declared structures.
4. Update schema and template headers to reflect "Project (legacy: Matter)".
5. Validate system integrity.
6. Commit changes as a single refactor unit.
7. Verify absence of active `04_MATTERS` references.
8. Confirm agent interpretation.

---

## Rollback
- Revert refactor commit.
- Restore `04_MATTERS/` as canonical path.
- Retain semantic mappings.

---

## Success Criteria
- Canonical work-unit location is `04_PROJECTS/`.
- Structural documentation reflects updated paths.
- Agents and humans consistently use "Project".
- Legacy references remain auditable.
