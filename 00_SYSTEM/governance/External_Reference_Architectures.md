---
id: GOVERNANCE-EXTERNAL-REFERENCE-ARCHITECTURES
title: External Reference Architectures
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [governance, references]
provenance:
  decided_by: ML1
  decided_on: 2026-01-22
  context: Defines constraints on external reference architectures.
---

# External Reference Architectures

## Definition
An **External Reference Architecture** is a non-binding comparative input:
a system, framework, or methodology referenced for vocabulary, contrast,
or failure-mode awareness. It does not grant permission, impose behavior,
or establish inheritance.

**Core rule:** Reference ≠ permission ≠ inheritance.

## Authority
- ML1 retains final judgment over all system decisions.
- ML2 does not inherit behavior, permissions, or structure from any
  external reference.
- Referencing an architecture does not authorize its adoption.

## Reuse Requirement
Any reuse of an external reference component must be:
1. Explicitly mapped to an ML2 artifact (schema, governance doc, or template).
2. Approved by ML1.
3. Recorded in DECISION_LOG.md.

Absent all three, the component remains informational only.

---

## Non-Adoption List (Explicit Defaults)

The following categories are **prohibited by default** unless explicitly
authorized through the reuse requirement above:

| Category | Default Status | Notes |
|----------|---------------|-------|
| Agent frameworks | PROHIBITED | No autonomous agent behavior from external systems |
| Automated write-back | PROHIBITED | No external system may write to ML2 without ML1 prompt |
| RAG / embedding pipelines | PROHIBITED (write) | Read-only analysis permitted; no write-back |
| Tooling assumptions (e.g., VS Code primacy) | NOT ASSUMED | ML2 is tool-agnostic |
| External tool write access | PROHIBITED | No external tool may modify ML2 state |

---

## Component Mapping: Iwo Szapar Second Brain

| Component | Status in ML2 | Boundary |
|-----------|---------------|----------|
| File-based knowledge base | Informative / partial overlap | Structure may differ; no inheritance |
| Schemas & conventions | Informative | May inspire ML2 schemas; not binding |
| RAG layer | Read-only analysis permitted | No write-back to ML2 |
| Agent framework | PROHIBITED by default | No autonomous execution |
| External tool write access | PROHIBITED by default | No modification of ML2 state |

Reference location: `07_REFERENCE/external_systems/iwo_szapar_second_brain/`

---

## Drift Signals

If any of the following occur, **stop and log**:

- An external system begins acting or executing without explicit ML1 prompts.
- ML2 artifacts begin reflecting external structure without a DECISION_LOG entry.
- Agent behavior references external architecture as authority.
- Write operations occur from external tooling without ML1 authorization.

Drift events should be logged in DECISION_LOG.md and escalated to ML1.

---

## Change Control

Amendments to this document require a DECISION_LOG entry with:
- What changed
- Why
- ML1 approval confirmation
