---
id: DOCTRINE-README
title: Doctrine
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-03-01
tags: [doctrine]
effective_date: 2026-01-22
supersedes: null
provenance:
  decided_by: ML1
  decided_on: 2026-01-22
  context: Defines the scope of doctrinal artifacts.
---

# Doctrine

This folder contains **ML1-approved doctrine**: policies, standards, principles, and rules.

Canonical doctrine subdirectories:
- `01_INVARIANTS/`
- `02_PRINCIPLES/`
- `03_INTERPRETIVE/`
- `04_POLICIES/`
- `05_CAPABILITY_PROFILES/`
- `06_PROTOCOLS/`
- `08_RULES/`
- `09_TESTS/`

## Directory Specs

### 01_INVARIANTS/
- Hard, non-negotiable constraints.
- Covers authority boundaries, risk ceilings, release requirements, versioning requirements, and no-silent-mutation rules.
- Format: absolute statements (`always` / `never`).

### 02_PRINCIPLES/
- Guiding strategic preferences.
- Includes simplicity over complexity, auditability over speed, structure over convenience, and explicitness over assumption.
- Principles can compete. Invariants cannot.

### 03_INTERPRETIVE/
- Definitions, precedence, and ambiguity resolution.
- Includes term definitions, doctrine hierarchy rules, conflict resolution logic, and edge-case handling.

### 04_POLICIES/
- Enforceable rule sets that govern behavior.
- Includes change control policy, approval policy, naming policy, archival policy, access policy, and publication policy.

### 05_CAPABILITY_PROFILES/
- Permission boundaries for system components.
- Includes system management agent allowed actions, model agent read/write scope, execution environment authorized interfaces, and external integration data-flow limits.

### 06_PROTOCOLS/
- Standard operating workflows.
- Includes doctrine release protocol, model promotion protocol, incident response protocol, weekly review protocol, and system audit protocol.
- Protocols define repeatable sequences.
- Each protocol file must include:
  - Workflow definition
  - Step sequence
  - Role responsibilities

### 08_RULES/
- Machine-readable enforcement logic.
- Includes schema rules, lint rules, metadata requirements, and structural validation.

### 09_TESTS/
- Verification layer for doctrine and enforcement behavior.

Rules:
- Doctrine must include YAML frontmatter per `/00_SYSTEM/SCHEMAS.md`
- Status must be `approved` to be treated as authoritative
- Superseded doctrine is moved to `/10_ARCHIVE` and linked via `supersedes`
