---
id: SCHEMA-PROJECT-001
title: Project Schema
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-03-01
tags: [schema, projects, structure]
---

# Project Schema

Defines the structure, contents, and constraints for artifacts in `04_PROJECTS/`.

---

## 1. Authority Status

```yaml
lifecycle: { folder_class: work }
authority: { level: none, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow, edit: allow }
```

**Projects are non-authoritative by definition.** They cannot:
- Define truth for the system
- Govern behavior
- Be cited as precedent
- Become canon without explicit extraction and approval

---

## 2. Project Location

Projects are stored directly under `04_PROJECTS/`:

```
04_PROJECTS/
├── MCP-26-001 – Formalize Trading Strategy/
├── MCP-26-002 – Trading Platform Selection/
└── MCP-26-003 – Website Development/
```

No intermediary folders (no `open/`, `pending/`, `closed/` subfolders).

---

## 3. Project Folder Naming

```
YY-CCC-NNNNN Client Name - Description
```

**Example:** `MCP-26-001 – Formalize Trading Strategy`

---

## 4. Project ID Format

`YY-CCC-NNNNN`

| Segment | Meaning | Example |
|---------|---------|---------|
| `YY` | Two-digit year | `26` = 2026 |
| `CCC` | Client number (three digits) | `001` = 1st client |
| `NNNNN` | Sequential project number (five digits, zero-padded) | `00001` = 1st project |

**Full example:** `26-001-00001` = Year 2026, Client #001, Project #1

---

## 5. Lifecycle Model (4 Stages)

Projects use a **standard 4-stage lifecycle**:

1. **Initiation**
2. **Planning**
3. **Execution**
4. **Closing**

### 5.1 Stage Semantics

- Agents may:
  - Infer and *recommend* stage classification
  - Never *advance* a stage without explicit ML1 instruction
- Advancement requires ML1 approval.
- Each stage has an exit gate controlled by ML1.

### 5.2 Stage Definitions

| Stage | Purpose | Key Outputs | Exit Criteria |
|-------|---------|-------------|---------------|
| **Initiation** | Define scope, objectives, constraints | Charter, Scope Boundaries, Definitions | ML1 approval to proceed |
| **Planning** | Design structure, standards, execution plan | Document schema, review cadence, acceptance criteria | ML1 approval to proceed |
| **Execution** | Execute work while monitoring for drift | Draft artifacts, issue logs, consistency checks | ML1 approval to proceed |
| **Closing** | Validate and finalize deliverables | Approved artifacts, archived materials, transition notes | ML1 sign-off |

---

## 6. Internal Structure (Standard Stage Folders)

Projects may use the following **standard stage subfolders**. These are **formalized** and permitted, but **not required**.

```
01_INITIATION DOCUMENTATION/
02_PLANNING DOCUMENTATION/
03_EXECUTION DOCUMENTATION/
04_CLOSING DOCUMENTATION/
```

Rules:
- If these folders are used, the names must match exactly.
- Additional subfolders are allowed when clearly scoped to the project and not in conflict with system structure.

---

## 7. Required Project Files (Minimum Viable Project)

There is **no required file set** for projects. If present, files must follow the metadata rules below.

---

## 8. Required Metadata (Frontmatter)

Each project file MUST include YAML frontmatter.

### 00_OVERVIEW.md Frontmatter (Canonical)

`00_OVERVIEW.md` MUST use the `project:` block schema below. Legacy top‑level fields are deprecated.

```yaml
---
project:
  id: YY-CCC-NNNNN
  title: Client Name - Description
  stage: initiation | planning | execution | closing
  status: in_progress | blocked | paused | waiting_ml1
owner:
  ml1: ML1
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
dependencies:
  depends_on: []
  blocks: []
tags: []
---
```

---

## 9. Project Status Vocabulary

Projects use the following status values:

| Status | Meaning |
|--------|---------|
| `in_progress` | Active work underway |
| `blocked` | Cannot proceed due to dependency or external factor |
| `paused` | Intentionally on hold |
| `waiting_ml1` | Awaiting ML1 decision or approval |

Notes:
- Status is a project-local operational indicator.
- Status does not imply completion or approval.

---

## 10. Dependencies

Projects may declare:

- `depends_on`: list of project IDs this project needs
- `blocks`: list of project IDs this project prevents

Dependencies must be expressed as project IDs, not folder paths.

**Example:**
```yaml
dependencies:
  depends_on: [26-001-00001]
  blocks: [26-001-00003]
```

---

## 11. Component Definitions

### 00_OVERVIEW.md

| Property | Value |
|----------|-------|
| **Is** | Snapshot of the project right now; objectives, status, risks, context |
| **Is NOT** | Doctrine; stable over time; citable as truth |
| **Think** | Dashboard, not record |

**Contents:**
- Project identification
- Current stage and status
- Objectives and scope summary
- Key dates

### 01_DECISIONS.md

| Property | Value |
|----------|-------|
| **Is** | Record of ML1 decisions and pending decision requests |
| **Is NOT** | Precedent; binding doctrine; generalizable guidance |

**Contents:**
- Approved decisions with rationale
- Pending decision requests
- Decision history

### 02_RISKS.md

| Property | Value |
|----------|-------|
| **Is** | Risk and assumptions register |
| **Is NOT** | Guarantees; predictions; commitments |

**Contents:**
- Active risks with impact and likelihood
- Assumptions requiring validation
- Mitigations (proposed and implemented)

### 03_DEPENDENCIES.md

| Property | Value |
|----------|-------|
| **Is** | Dependency map and constraint register |
| **Is NOT** | Workflow; task sequencing; schedule |

**Contents:**
- Upstream dependencies (what this project needs)
- Downstream impacts (what depends on this project)
- External constraints

### 04_CHANGELOG.md

| Property | Value |
|----------|-------|
| **Is** | Audit trail of material changes |
| **Is NOT** | Git log replacement; task completion record |

**Contents:**
- What changed
- When it changed
- Why it changed
- Who authorized it

---

## 12. Agent Maintenance Permissions (Schema-Level)

Agents operating on `04_PROJECTS/**` may perform **maintenance edits**:

### Allowed

- Create missing required project files
- Normalize frontmatter to schema
- Append entries to `01_DECISIONS.md` (pending requests only)
- Append entries to `02_RISKS.md` (identified risks)
- Append entries to `04_CHANGELOG.md` (maintenance actions)
- Update status indicators in `00_OVERVIEW.md`

### Prohibited

- Renaming, moving, deleting project files or folders
- Advancing lifecycle stage without ML1 instruction
- Marking exit criteria satisfied without ML1 instruction
- Overwriting entire files without ML1 instruction

---

## 13. Constraints

### What Projects CANNOT Do

- Define `source_of_truth: true`
- Have `authority.level: binding` or `procedural`
- Be cited as precedent for other projects
- Become canon without explicit extraction

### What Projects CAN Do

- Store contextual, project-specific information
- Support pattern identification (for human review)
- Be read, written, and edited by agents (within guardrails)
- Be closed and archived

---

## 14. Precedence

If there is conflict between system docs:

1. `00_SYSTEM/PROJECT_SCHEMA.md` (this file)
2. `00_SYSTEM/FOLDER_SCHEMAS.md`
3. `00_SYSTEM/SCHEMAS.md`
4. `00_SYSTEM/FOLDER_MAP.md`

Unresolved conflicts must be flagged for ML1.

---

**End of Project Schema**
