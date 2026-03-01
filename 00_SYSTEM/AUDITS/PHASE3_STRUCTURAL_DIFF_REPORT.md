---
id: AUDIT-PHASE3-STRUCTURAL-DIFF
title: Phase 3 Structural Diff Report
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [audit, phase3]
---

# Phase 3 Structural Diff Report

**Date:** 2026-01-24
**Source of truth:** `00_SYSTEM/FOLDER_MAP.md`
**Snapshot method:** `find` from repo root, excluding `.git/` and `.DS_Store`

---

## 1) DECLARED BUT MISSING

Items explicitly declared in FOLDER_MAP.md but not present in actual tree:

| Declared Path | FOLDER_MAP Section | Notes |
|---------------|-------------------|-------|
| `02_PLAYBOOKS/ll-marketing-sales/` | 02_PLAYBOOKS Structure | Not created |
| `02_PLAYBOOKS/ll-client/` | 02_PLAYBOOKS Structure | Not created |
| `02_PLAYBOOKS/ll-solution/` | 02_PLAYBOOKS Structure | Not created |
| `02_PLAYBOOKS/admin/` | 02_PLAYBOOKS Structure | Not created (was relocated per DECISION_LOG 2026-01-21) |
| `02_PLAYBOOKS/secondary-business/` | 02_PLAYBOOKS Structure | Not created |

**Count:** 5 declared paths missing from actual tree.

---

## 2) EXISTS BUT UNDECLARED

Items present in actual tree but not mentioned in FOLDER_MAP.md:

### 00_SYSTEM/ (undeclared substructure)
| Actual Path | Description |
|-------------|-------------|
| `00_SYSTEM/governance/` | Governance subtree (agents/, authority/, canon/, enforcement/, change-control/) |
| `00_SYSTEM/governance/External_Reference_Architectures.md` | Top-level governance file outside subdirectories |
| `00_SYSTEM/integrations/` | Integration surface folders (calendar/, clio/, email/, onedrive/, sharepoint/, word/) |
| `00_SYSTEM/CLAUDE.md` | Agent instructions file |
| `00_SYSTEM/DECISION_LOG.md` | Decision provenance log |
| `00_SYSTEM/GLOSSARY.md` | Term definitions |
| `00_SYSTEM/LEGACY_TERMS.md` | Legacy terminology mappings |
| `00_SYSTEM/MATTER_SCHEMA.md` | Project schema (legacy: Matter) |
| `00_SYSTEM/REFRACTOR_PLAN_04_MATTERS_TO_04_PROJECTS.md` | Refactor plan (design only) |
| `00_SYSTEM/SCHEMAS.md` | Schema index |
| `00_SYSTEM/SYSTEM_BACKLOG.md` | System-level backlog |
| `00_SYSTEM/System_Identity.md` | System identity declaration |

*Note: FOLDER_MAP lists 00_SYSTEM contents as "Agents, Schemas, Governance rules" but does not enumerate specific files or subfolders.*

### 02_PLAYBOOKS/ (actual structure diverges entirely)
| Actual Path | Description |
|-------------|-------------|
| `02_PLAYBOOKS/delivery/` | Top-level actual folder (not declared) |
| `02_PLAYBOOKS/delivery/contract/` | Practice area |
| `02_PLAYBOOKS/delivery/corporate/` | Practice area (with deep subtree) |
| `02_PLAYBOOKS/delivery/corporate/incorporation/` | Sub-practice |
| `02_PLAYBOOKS/delivery/corporate/ma/` | M&A (asset-purchase/, share-purchase/) |
| `02_PLAYBOOKS/delivery/corporate/shareholder-agreement/` | Sub-practice |
| `02_PLAYBOOKS/delivery/corporate/shareholder-change/` | Sub-practice (buy-out/, issuance/, redemption/, transfer-sale/) |
| `02_PLAYBOOKS/delivery/corporate/shareholder-conflict/` | Sub-practice (deadlock/, majority/, minority/) |
| `02_PLAYBOOKS/delivery/financial-services/` | Practice area (payment-services/, private-lending/) |
| `02_PLAYBOOKS/delivery/franchising/` | Practice area |
| `02_PLAYBOOKS/delivery/fulfillment/` | Practice area |

### 07_RESEARCH/ (undeclared subfolders)
| Actual Path | Description |
|-------------|-------------|
| `07_RESEARCH/facts/` | Fact extraction target |
| `07_RESEARCH/facts/by-matter/` | Facts organized by matter |
| `07_RESEARCH/facts/by-topic/` | Facts organized by topic |

### 09_INBOX/ (undeclared items)
| Actual Path | Description |
|-------------|-------------|
| `09_INBOX/_AGENT_OUTPUT/` | Agent write target (per GOV-2026-006) |
| `09_INBOX/TASK_BACKLOG.md` | Task backlog file (not in /untriaged or /triaged) |

### Root / tooling (not structural)
| Actual Path | Description |
|-------------|-------------|
| `.claude/` | Claude Code agent definitions and settings |
| `.github/` | GitHub templates |
| `LICENSE` | Repository license |

**Count:** 30+ undeclared items (excluding empty placeholder dirs and READMEs).

---

## 3) DECLARED BUT MISALIGNED (Role/Placement)

Items that exist but appear in a different location or structure than declared:

| Item | Declared Location | Actual Location | Nature of Mismatch |
|------|-------------------|-----------------|-------------------|
| Doctrine files (2026-001, -002, -003) | `01_DOCTRINE/binding/`, `/interpretive/`, or `/constraints/` | `01_DOCTRINE/` (root level) | Files at folder root instead of declared subfolders |
| Playbook content | `02_PLAYBOOKS/{ll-marketing-sales, ll-client, ll-solution, admin, secondary-business}` | `02_PLAYBOOKS/delivery/{corporate, contract, franchising, ...}` | Entirely different taxonomy; declared structure is categorical by audience, actual is by practice area |

**Count:** 2 structural misalignments (one individual file placement, one wholesale taxonomy divergence).

---

## Summary

| Category | Count |
|----------|-------|
| Declared but missing | 5 |
| Exists but undeclared | 30+ |
| Declared but misaligned | 2 |

The largest divergence is in `02_PLAYBOOKS/`, where the declared structure (audience-oriented: ll-client, ll-solution, etc.) has no overlap with the actual structure (practice-area-oriented: corporate, contract, franchising, etc.).

---

## Next Actions (Not Executed)

The following decisions are deferred to later Phase 3 steps:

- **Acknowledge:** Update FOLDER_MAP to reflect actual governance/, integrations/, and file inventory in 00_SYSTEM
- **Acknowledge:** Update FOLDER_MAP to reflect actual 07_RESEARCH/facts/ structure
- **Acknowledge:** Update FOLDER_MAP to reflect 09_INBOX/_AGENT_OUTPUT/
- **Resolve:** Decide whether 02_PLAYBOOKS declared structure or actual structure is canonical (or neither)
- **Resolve:** Decide whether doctrine files move into subfolders or subfolders are removed from declaration
- **Route:** Determine correct location for 09_INBOX/TASK_BACKLOG.md
- **Quarantine/Delete:** Assess .gitkeep in 04_MATTERS/ (backlog item #7)
