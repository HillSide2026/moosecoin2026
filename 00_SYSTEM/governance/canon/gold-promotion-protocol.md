---
id: GOV-2026-001
title: Draft → Gold Promotion Protocol
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-01-21
effective_date: 2026-01-21
tags: [promotion, governance, canon]
supersedes: null
provenance:
  decided_by: ML1
  decided_on: 2026-01-21
  context: Establishes the firewall between working drafts and authoritative canon
---

# Draft → Gold Promotion Protocol

The firewall between thinking and governing.

---

## Core Principle

**No artifact becomes authoritative without explicit promotion.**

Drafts may inform, but only canon governs.

---

## 1. Where Drafts Live

All draft artifacts reside in `06_OUTPUTS/drafts/` until promotion.

| Draft Type | Draft Location | Target Canon Location |
|------------|----------------|----------------------|
| Doctrine | `06_OUTPUTS/drafts/` | `01_DOCTRINE/{binding,interpretive,constraints}/` |
| Playbook | `06_OUTPUTS/drafts/` | `02_PLAYBOOKS/{domain}/` |
| Template | `06_OUTPUTS/drafts/` | `03_TEMPLATES/{type}/` |
| System governance | `06_OUTPUTS/drafts/` | `00_SYSTEM/governance/{category}/` |

**Rule:** Canon folders contain only approved artifacts. No `status: draft` in canon.

---

## 2. Who Promotes

| Action | Authority |
|--------|-----------|
| Create draft | ML1 or Agent (with `agents.write: allow`) |
| Request promotion | ML1 or Agent |
| Approve promotion | **ML1 only** |
| Execute promotion | ML1 or Agent (under ML1 instruction) |

**Rule:** Agents may propose but never approve.

---

## 3. Promotion Checklist

Before promotion, verify:

- [ ] Artifact passes Compliance Checklist (all required metadata present)
- [ ] `status` is `proposed` (not `draft`)
- [ ] Target folder is appropriate for artifact type
- [ ] No naming collision in target folder
- [ ] `provenance` block is complete (for Doctrine and Governance)
- [ ] `cites_doctrine` is populated (for Playbooks)
- [ ] ML1 has explicitly approved

---

## 4. Promotion Steps

### Step 1: Propose
```
status: draft → status: proposed
```
Artifact is ready for review. No location change.

### Step 2: Approve (ML1 only)
ML1 reviews and approves. Decision recorded in `DECISION_LOG.md`.

### Step 3: Promote
Execute the following:

1. **Update metadata:**
   ```yaml
   status: approved
   last_updated: {today}
   effective_date: {today}
   provenance:
     decided_by: ML1
     decided_on: {today}
     context: {approval context}
   ```

2. **Move file:**
   ```
   06_OUTPUTS/drafts/{artifact}.md → {target-canon-folder}/{artifact}.md
   ```

3. **Log decision:**
   Add entry to `00_SYSTEM/DECISION_LOG.md`

4. **Verify:**
   Run Compliance Checklist on promoted artifact

---

## 5. Metadata Changes on Promotion

| Field | Before | After |
|-------|--------|-------|
| `status` | `proposed` | `approved` |
| `last_updated` | (previous) | (promotion date) |
| `effective_date` | (empty) | (promotion date) |
| `provenance.decided_by` | (empty) | `ML1` |
| `provenance.decided_on` | (empty) | (promotion date) |
| Location | `06_OUTPUTS/drafts/` | `{canon-folder}/` |

---

## 6. Versioning on Promotion

For updates to existing canon:

1. **Minor update (no authority change):**
   - Increment version (e.g., `1.0` → `1.1`)
   - Update in place
   - Log in DECISION_LOG.md

2. **Major update (authority change):**
   - Create new artifact with new ID
   - Set `supersedes: {old-id}` in new artifact
   - Move old artifact to `10_ARCHIVE/`
   - Log in DECISION_LOG.md

---

## 7. Rejection Path

If ML1 rejects promotion:

1. Update `status: draft` (return to working state)
2. Add rejection note to artifact or linked matter
3. No DECISION_LOG entry required for rejections

---

## 8. Prohibited Actions

- Promoting without ML1 approval
- Direct creation in canon folders (bypass drafts)
- Changing `status: approved` without new promotion cycle
- Silent promotions (no DECISION_LOG entry)
- Agent-initiated promotions without explicit ML1 instruction

---

## Decision Log Entry Template

```markdown
## {DATE} — {ARTIFACT-ID} Promoted

**Artifact:** {title}
**From:** 06_OUTPUTS/drafts/
**To:** {canon-folder}/
**Approved by:** ML1
**Context:** {brief rationale}
```
