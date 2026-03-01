---
id: SCHEMA-CORE-001
title: Artifact Schemas
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-03-01
tags: [schemas, metadata]
---

# Artifact Schemas

All markdown files in this repository MUST begin with YAML frontmatter.

## Scope of This File

This file defines artifact metadata/frontmatter schemas.
Folder-level structural schemas are defined in `00_SYSTEM/FOLDER_SCHEMAS.md`.

## Schema Gate (Frontmatter Enforcement)

The repo-wide gate runs `00_SYSTEM/TOOLS/check_frontmatter.py` against tracked
markdown files. It fails when frontmatter is missing and prints:
“Missing YAML frontmatter. Add a frontmatter block per 00_SYSTEM/SCHEMAS.md.”
There are no frontmatter exemptions unless explicitly listed here.

---

## Core Metadata Fields

### A. lifecycle.folder_class
Where the artifact lives and how it's treated.

| Value | Meaning |
|-------|---------|
| `canon` | Enduring, governed, can be Gold |
| `work` | Drafts / working material |
| `event` | Time-stamped logs (runs) |
| `library` | Reference + research |
| `inbox` | Intake |
| `archive` | Historical |

### B. authority.level
How much the artifact can govern behavior.

| Value | Meaning |
|-------|---------|
| `none` | Cannot guide action (notes, logs) |
| `reference` | Context only (research, external) |
| `procedural` | Decision-engine and protocol logic (models/protocols) |
| `binding` | Rules/policy (doctrine) |

### C. authority.source_of_truth
Can this artifact define truth for the system?

- `true` — Only for canon artifacts that can be cited as "this is the rule/protocol"
- `false` — Everything else (including Projects; legacy: Matters)

### D. audience.scope
Who may consume this artifact.

| Value | Meaning |
|-------|---------|
| `ml1_only` | ML1 eyes only |
| `ml2_internal` | System-internal use |
| `ll_consumable` | May flow to Levine Law |

---

## Folder Defaults

Artifacts inherit these defaults based on their location. Override in frontmatter when needed.

### 00_SYSTEM/
```yaml
lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: true }
audience: { scope: ml1_only, ll_consumable: false }
agents: { read: allow, write: deny }
```

### 01_DOCTRINE/ (all doctrine subdirectories)
```yaml
lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```
*Applies to: `01_INVARIANTS/`, `02_PRINCIPLES/`, `03_INTERPRETIVE/`,
`04_POLICIES/`, `05_CAPABILITY_PROFILES/`, `06_PROTOCOLS/`,
`08_RULES/`, `09_TESTS/`.*

### 02_MODELS/
```yaml
lifecycle: { folder_class: canon }
authority: { level: procedural, source_of_truth: false }
audience: { scope: ll_consumable, ll_consumable: partial }
agents: { read: allow, write: deny }
```
*Note: `ll_consumable: partial` requires per-artifact override.*

### 03_PROTOCOLS/
```yaml
lifecycle: { folder_class: canon }
authority: { level: procedural, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```
*Note: Protocol artifact is source-of-truth; instantiated outputs are not.*

### 04_PROJECTS/ (legacy: 04_MATTERS)
```yaml
lifecycle: { folder_class: work }
authority: { level: none, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow }
```

### 05_RUNS/
```yaml
lifecycle: { folder_class: event, immutability: immutable }
authority: { level: none, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: deny }
```

### 06_OUTPUTS/
```yaml
lifecycle: { folder_class: work }
authority: { level: none, source_of_truth: false }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: allow }
```

### 07_REFERENCE/
```yaml
lifecycle: { folder_class: library }
authority: { level: reference, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: deny }
```

### 08_RESEARCH/
```yaml
lifecycle: { folder_class: library }
authority: { level: reference, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow }
```

### 09_INBOX/
```yaml
lifecycle: { folder_class: inbox, retention: 7_days }
authority: { level: none, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow }
```

### 10_ARCHIVE/
```yaml
lifecycle: { folder_class: archive, immutability: immutable }
authority: { level: reference, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: deny }
```

---

## Base Schema (All Artifacts)

```yaml
---
id:
title:
owner: ML1
status: draft | proposed | approved | deprecated
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: []

# Override folder defaults when needed:
# lifecycle: { folder_class: ... }
# authority: { level: ..., source_of_truth: ... }
# audience: { scope: ..., ll_consumable: ... }
---
```

---

## Artifact-Specific Schemas

### Doctrine Schema
Additional fields for `/01_DOCTRINE/`:

```yaml
---
effective_date: YYYY-MM-DD
supersedes: doctrine-id | null
provenance:
  decided_by: ML1
  decided_on: YYYY-MM-DD
  context: string
---
```

### Model Schema
Additional fields for `/02_MODELS/`:

```yaml
---
audience:
  ll_consumable: true | false    # Override partial default
model_type: decision_engine
model_components:
  regime_filter: required
  risk_model: required
  entry_logic: required
  exit_logic: required
  signal_generation: required
  sizing_engine: required
cites_doctrine: []               # List of doctrine IDs this model derives from
---
```

### Protocol Schema
Additional fields for `/03_PROTOCOLS/`:

```yaml
---
protocol_type: risk | execution | incident | review
version: string                  # e.g., "1.0", "2.1"
approval_status: draft | approved
---
```

### Project Schema (legacy: Matter Schema)
For `/04_PROJECTS/`:

**Project ID Format:** `##-###-#####` (legacy: Matter ID)
- First segment: Year project was opened (2-digit)
- Second segment: Client number (3-digit)
- Third segment: Project number for that client (5-digit)

Example: `26-998-00001` = Year 2026, Client #998, Project #1 for that client

**Project Folder Naming:** `##-###-##### Client Name - Description`

```yaml
---
id: ##-###-#####
title:
client:
owner: ML1
status: open | pending | closed
priority: essential | strategic | standard | parked
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: []
---
```

**Project Internal Structure:**

Project folder structure is governed by:
- `00_SYSTEM/FOLDER_SCHEMAS.md`
- `00_SYSTEM/PROJECT_SCHEMA.md`

This file governs metadata schemas, not folder topology.

### Run Schema
For `/05_RUNS/`:

```yaml
---
id: RUN-YYYY-MM-DD-{slug}
title:
status: started | completed | failed
created_date: YYYY-MM-DD
completed_date: YYYY-MM-DD | null
triggered_by: ML1 | agent | scheduled
related_project: project-id | null   # legacy: matter-id
inputs: []
outputs: []
---
```

**Run records are immutable once completed.**

### Output Schema
For `/06_OUTPUTS/`:

```yaml
---
id:
title:
status: draft | review | exported
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
derived_from: []                 # Source doctrine/model/protocol IDs
audience:
  target: LL | internal | external
---
```
