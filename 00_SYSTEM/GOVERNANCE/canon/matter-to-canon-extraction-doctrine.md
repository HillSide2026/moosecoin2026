---
id: GOV-2026-004
title: Matter → Canon Extraction Doctrine
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-03-01
effective_date: 2026-01-21
tags: [extraction, matters, canon, governance]
provenance:
  decided_by: ML1
  decided_on: 2026-01-21
  context: Defines the only permitted way learning may move from Matters into canon
---

# Matter → Canon Extraction Doctrine

This document exists to:
- Preserve learning from `04_PROJECTS`
- Prevent folklore, precedent leakage, and shadow doctrine
- Ensure no general rule, protocol, or model enters canon without explicit human judgment and approval

---

## Core Doctrine

> **No general rule, protocol, or model may be inferred from a Matter without explicit extraction and approval.**

This sentence is binding system doctrine.

---

## 1. Scope

### What counts as extraction

Extraction is the deliberate, human-initiated process of:
- Identifying a generalizable pattern in a Matter
- Creating a new draft artifact that codifies that pattern
- Promoting the draft to canon via the Gold Promotion Protocol

### What does NOT count as extraction

- Copying text from a Matter into another document
- Informal reuse of Matter content in new work
- Precedent-by-memory ("we did it this way last time")
- Citing a Matter as authority for a decision
- Agent-generated summaries treated as policy

These are **forbidden** paths to canon.

---

## 2. Roles & Authority

| Role | May Identify Pattern | May Draft Artifact | May Promote to Canon | May Approve |
|------|---------------------|-------------------|---------------------|-------------|
| **ML1** | Yes | Yes | Yes | Yes |
| **ML2 Maintainer** | Yes | Yes | No | No |
| **Agents** | No | No | No | No |

- **ML1** — Final authority; approves any canon promotion
- **ML2 Maintainer** — May perform extraction and draft artifacts; MUST NOT approve
- **Agents** — May assist with summarization only; MUST NOT extract or promote

---

## 3. What May Be Extracted

### Allowed extraction targets

- Patterns that recur across multiple matters
- Reusable procedures that proved effective
- Protocol-worthy operational structures
- Risks or constraints worth codifying as rules
- Checklists derived from lessons learned

### Forbidden extraction targets

- One-off judgments specific to a single matter
- Client-specific strategy or preferences
- Matter outcomes treated as precedent
- Confidential or privileged analysis
- Tactical decisions that depend on unique facts

---

## 4. Extraction Forms (Intermediate Artifacts)

Extraction MUST first appear as one of:

| Form | Location | Status |
|------|----------|--------|
| Research note | `08_RESEARCH/` | Non-authoritative |
| Draft model | `06_OUTPUTS/drafts/` | `status: draft` |
| Draft protocol | `06_OUTPUTS/drafts/` | `status: draft` |
| Draft doctrine | `06_OUTPUTS/drafts/` | `status: draft` |

**Direct creation or modification of approved canon is FORBIDDEN.**

---

## 5. Canon Promotion Path (Mandatory)

The only allowed flow:

```
04_PROJECTS (observation)
       ↓
   Extraction (human)
       ↓
   Draft artifact (06_OUTPUTS/drafts/ or 08_RESEARCH/)
       ↓
   Review (status: proposed)
       ↓
   ML1 approval
       ↓
   Canon (01_DOCTRINE / 02_MODELS / 03_PROTOCOLS)
```

### Non-negotiable rules

- No skipping steps
- No retroactive approval
- No "minor edit" exceptions
- No direct Matter → Canon movement
- All promotions logged in DECISION_LOG.md

---

## 6. Provenance & Metadata Requirements

Extracted artifacts MUST include:

```yaml
provenance:
  derived_from: [matter-id]    # Source Matter ID required
  extraction_date: YYYY-MM-DD
  extracted_by: ML1 | ML2
  generalization_rationale: string  # Why this is generalizable
```

Additionally:
- `origin: human` (not agent-generated)
- Clear statement of what was generalized and why

### Enforcement

**Missing provenance invalidates promotion.**

An artifact lacking extraction provenance MUST NOT be promoted to canon. If discovered post-promotion, the artifact is non-compliant and subject to the Violation Triage Protocol.

---

## 7. Agent Involvement (Strict Limits)

### Allowed agent assistance

- Summarizing Matter contents for human review
- Comparing patterns across multiple Matters
- Formatting draft artifacts
- Checking metadata completeness

### Forbidden agent behavior

- Deciding what is generalizable
- Writing doctrine or policy language
- Promoting artifacts to canon
- Extracting patterns autonomously
- Treating Matter content as precedent

### MUST / MUST NOT

| Agents MUST | Agents MUST NOT |
|-------------|-----------------|
| Wait for human instruction | Initiate extraction |
| Flag potential patterns for review | Decide pattern validity |
| Assist with formatting | Write binding rules |
| Check metadata completeness | Approve or promote |

---

## 8. Enforcement Rules

- Any canon artifact lacking extraction provenance is **non-compliant**
- Violations trigger the **Violation Triage Protocol** (GOV-2026-003)
- Non-compliant artifacts MUST be quarantined until resolved
- Severity: P1 (major) minimum; P0 if artifact was LL-consumed

### Quarantine actions

- Set `ll_consumable: false`
- Set `audience.scope: ml2_internal`
- Log in violation-log.md
- Draft compliant replacement via proper extraction path

---

## 9. Examples

### Example A: Correct extraction

**Situation:** Three corporate matters revealed the same shareholder notification timing issue.

**Correct response:**
1. ML2 identifies pattern across matters
2. ML2 creates draft checklist in `06_OUTPUTS/drafts/shareholder-notification-checklist.md`
3. Draft includes `provenance.derived_from: [26-001-00012, 26-001-00018, 26-001-00023]`
4. Draft includes `generalization_rationale: "Timing issue recurred in 3 matters; checklist prevents future misses"`
5. ML1 reviews and approves
6. Artifact promoted to `03_PROTOCOLS/checklists/`
7. Logged in DECISION_LOG.md

### Example B: Incorrect implicit precedent

**Situation:** A Matter contained a creative solution to a deadlock dispute. An agent references it as "the standard approach."

**Why invalid:**
- No extraction occurred
- No draft created
- No ML1 approval
- Pattern was inferred, not extracted
- Matter is non-authoritative by definition

**Correct response:** Treat as potential P1 violation. If pattern is valuable, perform proper extraction.

### Example C: Correct rejection as non-generalizable

**Situation:** A Matter contained an unusual negotiation tactic that worked due to specific counterparty relationship.

**Correct response:**
1. ML2 reviews and determines tactic is fact-dependent
2. No extraction performed
3. Matter remains in `04_PROJECTS/closed/`
4. No draft created
5. Learning preserved in Matter but NOT elevated to canon

This is the correct outcome. Not all Matter insights become canon.

---

## Phase 3 Exit Conditions

- [x] Extraction doctrine exists (GOV-2026-004)
- [x] Canon promotion path is explicit
- [x] Provenance is mandatory
- [x] Agents are constrained
