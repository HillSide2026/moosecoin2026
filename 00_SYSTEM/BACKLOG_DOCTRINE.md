---
id: BACKLOG-DOCTRINE-2026-01-23
title: Doctrine Backlog
owner: ML1
status: draft
created_date: 2026-01-23
last_updated: 2026-03-01
tags:
  - backlog
  - doctrine
  - governance
---

# Doctrine Backlog

A structured backlog of high-leverage doctrine candidates. This backlog captures why each doctrine item is needed, what it would cover, and how to validate it once drafted.

---

## ML1 Review Checklist

- Approve rubric and scoring method.
- Confirm top 3 priorities.
- Assign owners (if any beyond ML1).
- Set next release target (version placeholder).

### Proposed Next 3 Doctrine Items

1) Output governance doctrine (LL-facing)
2) Approval semantics doctrine
3) Artifact lifecycle doctrine

---

## Prioritization Rubric

Score each backlog item on a 1–5 scale and calculate:

**Priority = (Frequency + Risk + Leverage) - Effort**

- **Frequency**: How often the issue recurs (1–5)
- **Risk**: Governance/compliance/confusion risk (1–5)
- **Leverage**: Reduction in repeated interpretation once codified (1–5)
- **Effort**: Estimated complexity to codify (1–5)

---

## Backlog Items (Ordered by Priority)

### 1) Output governance doctrine (LL-facing)
- **Problem statement**: Output to LL must be tightly controlled and labeled to prevent unapproved interpretation. There is no binding doctrine that defines what can be emitted or how to label it for downstream consumption.
- **Scope**: All outputs intended for LL consumption across models, protocols, and runs.
- **Non-scope**: Does not define the content of specific outputs or LL delivery formats.
- **Proposed output location(s)**: `01_DOCTRINE/` (primary), references in `02_MODELS/`.
- **Acceptance criteria**:
  - Doctrine defines allowed output categories and required labels: “ML1-approved doctrine,” “Draft for ML1 approval,” “Derived from approved model/protocol vX.Y.”
  - Doctrine explicitly forbids interpretation beyond approved artifacts.
  - Doctrine references where labels must live (frontmatter + output header) and provides examples.
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Governance-first requirement to prevent LL drift; lack of explicit output governance in `00_SYSTEM/SCHEMAS.md` output schema.
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 5, Risk 5, Leverage 5, Effort 3 → **Priority 12**
- **Decision provenance fields**:
  - Prompted by: governance-first policy gap in output labeling.
  - Scope: LL-facing outputs and labels.
  - Effective date: YYYY-MM-DD

### 2) Approval semantics doctrine
- **Problem statement**: The system needs a canonical definition of “ML1-approved doctrine” vs “draft for ML1 approval,” and how approval status is conveyed and cited. Without this, approvals are inferred or inconsistent.
- **Scope**: Approval labels, required metadata, and what constitutes binding approval.
- **Non-scope**: Does not define the substantive content of doctrine items.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `00_SYSTEM/SCHEMAS.md`.
- **Acceptance criteria**:
  - Doctrine defines the approval states and required labels.
  - Doctrine defines what “derived from” means and how derivations must cite sources.
  - Doctrine clarifies where approval status is recorded (frontmatter + optional footer).
- **Dependencies**: Artifact lifecycle doctrine.
- **Provenance**: Need to standardize approval semantics for governance-first outputs; schema defaults do not define approval labels.
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 4, Risk 5, Leverage 5, Effort 2 → **Priority 12**
- **Decision provenance fields**:
  - Prompted by: repeated ambiguity in approval labeling and “derived from” references.
  - Scope: doctrine approval semantics across the system.
  - Effective date: YYYY-MM-DD

### 3) Artifact lifecycle doctrine
- **Problem statement**: The repository lacks binding guidance on lifecycle stages and transitions for artifacts, risking inconsistent status usage and unclear deprecation paths.
- **Scope**: All governed artifacts in canon folders (system, doctrine, models, protocols).
- **Non-scope**: Does not define project/matter lifecycle states.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `00_SYSTEM/SCHEMAS.md`.
- **Acceptance criteria**:
  - Doctrine defines lifecycle states (draft → approved → deprecated → archived).
  - Doctrine defines allowed transitions and who can authorize them.
  - Doctrine specifies where status lives (frontmatter field) and required timestamps.
- **Dependencies**: None.
- **Provenance**: Lifecycle terms exist in `00_SYSTEM/SCHEMAS.md` but are not governed by doctrine.
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 4, Risk 4, Leverage 5, Effort 3 → **Priority 10**
- **Decision provenance fields**:
  - Prompted by: inconsistent lifecycle interpretation across artifacts.
  - Scope: lifecycle states for canon artifacts.
  - Effective date: YYYY-MM-DD

### 4) Protocol governance doctrine
- **Problem statement**: Protocols are source-of-truth artifacts but lack doctrine specifying how protocols become binding, how versions are managed, and how changes propagate.
- **Scope**: Protocol approval, versioning, and binding rules for `03_PROTOCOLS/`.
- **Non-scope**: Does not define the content of specific protocols.
- **Proposed output location(s)**: `01_DOCTRINE/`, with references in `03_PROTOCOLS/`.
- **Acceptance criteria**:
  - Doctrine defines protocol versioning rules and approval thresholds.
  - Doctrine defines how protocol changes are announced and adopted.
  - Doctrine defines how derivative outputs reference protocol version IDs.
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Protocol schema defines version/approval status but lacks governing doctrine (`00_SYSTEM/SCHEMAS.md`).
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 4, Risk 4, Leverage 4, Effort 3 → **Priority 9**
- **Decision provenance fields**:
  - Prompted by: missing policy for protocol binding and version upgrades.
  - Scope: protocol governance across the system.
  - Effective date: YYYY-MM-DD

### 5) Deprecation policy doctrine
- **Problem statement**: There is no binding policy describing how artifacts are deprecated, redirected, and archived, creating risk of stale guidance in use.
- **Scope**: Deprecation, redirect, and archive rules for canon artifacts.
- **Non-scope**: Does not define lifecycle states (covered by lifecycle doctrine).
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `10_ARCHIVE/` and `00_SYSTEM/SCHEMAS.md`.
- **Acceptance criteria**:
  - Doctrine defines deprecation triggers and required notices.
  - Doctrine defines redirect behavior and retention expectations.
  - Doctrine defines archive placement and metadata requirements.
- **Dependencies**: Artifact lifecycle doctrine.
- **Provenance**: Archive rules exist in schema defaults but lack governing doctrine (`00_SYSTEM/SCHEMAS.md`).
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 3, Risk 4, Leverage 4, Effort 3 → **Priority 8**
- **Decision provenance fields**:
  - Prompted by: unclear deprecation/redirect behavior across canon artifacts.
  - Scope: deprecation and archive mechanics.
  - Effective date: YYYY-MM-DD

### 6) Decision log standard doctrine
- **Problem statement**: Decision logs exist but lack a binding standard for fields, linking, and affected artifacts, making provenance inconsistent.
- **Scope**: Decision log format, required fields, and linking rules.
- **Non-scope**: Does not decide any substantive policies.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `00_SYSTEM/DECISION_LOG.md`.
- **Acceptance criteria**:
  - Doctrine defines required fields (decision, rationale, scope, affected artifacts, effective date).
  - Doctrine defines linking rules to impacted doctrine/models/protocols.
  - Doctrine defines who can log binding decisions.
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Existing `00_SYSTEM/DECISION_LOG.md` lacks canonical schema guidance.
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 3, Risk 4, Leverage 3, Effort 3 → **Priority 7**
- **Decision provenance fields**:
  - Prompted by: inconsistent decision provenance across system changes.
  - Scope: decision log entries and references.
  - Effective date: YYYY-MM-DD

### 7) Exceptions doctrine
- **Problem statement**: There is no defined process for recording, approving, and timeboxing exceptions to governance rules.
- **Scope**: Exception requests, approvals, timeboxes, and retirement requirements.
- **Non-scope**: Does not define substantive exceptions.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `00_SYSTEM/`.
- **Acceptance criteria**:
  - Doctrine defines exception record fields (scope, reason, approver, expiry).
  - Doctrine defines renewal rules and sunset behavior.
  - Doctrine defines where exception records live.
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Governance-first posture requires explicit exception handling; no current doctrine exists.
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 3, Risk 4, Leverage 3, Effort 3 → **Priority 7**
- **Decision provenance fields**:
  - Prompted by: need to manage deviations without drift.
  - Scope: exception handling for governance rules.
  - Effective date: YYYY-MM-DD

### 8) Naming and taxonomy doctrine
- **Problem statement**: The system uses legacy terms (e.g., Matter vs Project) without binding doctrine for canonical vocabulary, causing ambiguity.
- **Scope**: Canonical naming, taxonomy definitions, and allowed legacy mappings.
- **Non-scope**: Does not rename existing artifacts or folders.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `00_SYSTEM/GLOSSARY.md` and `00_SYSTEM/LEGACY_TERMS.md`.
- **Acceptance criteria**:
  - Doctrine defines canonical vocabulary and mandatory usage.
  - Doctrine specifies how legacy terms map to canonical terms.
  - Doctrine defines enforcement points (protocols, models, documentation).
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Existing glossary and legacy terms are non-binding (`00_SYSTEM/GLOSSARY.md`, `00_SYSTEM/LEGACY_TERMS.md`).
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 3, Risk 3, Leverage 4, Effort 3 → **Priority 7**
- **Decision provenance fields**:
  - Prompted by: inconsistent vocabulary across system artifacts.
  - Scope: canonical naming and taxonomy.
  - Effective date: YYYY-MM-DD

### 9) Runs and outputs linkage doctrine
- **Problem statement**: Outputs are not consistently linked to run records and inputs, reducing auditability and traceability.
- **Scope**: Rules for linking run IDs, inputs, and outputs across `05_RUNS/` and `06_OUTPUTS/`.
- **Non-scope**: Does not define run schemas beyond linkage requirements.
- **Proposed output location(s)**: `01_DOCTRINE/` with references in `05_RUNS/` and `06_OUTPUTS/`.
- **Acceptance criteria**:
  - Doctrine defines required cross-references between run records and outputs.
  - Doctrine defines minimum metadata fields for linkage (run ID, inputs, outputs).
  - Doctrine defines enforcement points for linkage (protocol or model checks).
- **Dependencies**: Approval semantics doctrine.
- **Provenance**: Run/output schemas exist but lack binding linkage rules (`00_SYSTEM/SCHEMAS.md`).
- **Suggested owner/approver**: ML1
- **Draft version placeholder**: v0.1
- **Scoring**: Frequency 3, Risk 3, Leverage 3, Effort 2 → **Priority 7**
- **Decision provenance fields**:
  - Prompted by: missing traceability between runs and outputs.
  - Scope: linkage requirements between run records and outputs.
  - Effective date: YYYY-MM-DD
