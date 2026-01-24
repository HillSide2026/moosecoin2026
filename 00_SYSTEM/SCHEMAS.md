# Artifact Schemas

All markdown files in this repository MUST begin with YAML frontmatter.

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
| `procedural` | How-to (playbooks/templates) |
| `binding` | Rules/policy (doctrine) |

### C. authority.source_of_truth
Can this artifact define truth for the system?

- `true` — Only for canon artifacts that can be cited as "this is the rule/template"
- `false` — Everything else (including Matters)

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

### 01_DOCTRINE/binding/
```yaml
lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```

### 01_DOCTRINE/interpretive/
```yaml
lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```

### 01_DOCTRINE/constraints/
```yaml
lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```

### 02_PLAYBOOKS/
```yaml
lifecycle: { folder_class: canon }
authority: { level: procedural, source_of_truth: false }
audience: { scope: ll_consumable, ll_consumable: partial }
agents: { read: allow, write: deny }
```
*Note: `ll_consumable: partial` requires per-artifact override.*

### 03_TEMPLATES/
```yaml
lifecycle: { folder_class: canon }
authority: { level: procedural, source_of_truth: true }
audience: { scope: ll_consumable, ll_consumable: true }
agents: { read: allow, write: deny }
```
*Note: Template itself is source-of-truth; instantiated outputs are not.*

### 04_MATTERS/
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

### 07_RESEARCH/
```yaml
lifecycle: { folder_class: library }
authority: { level: reference, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow }
```

### 08_REFERENCE/
```yaml
lifecycle: { folder_class: library }
authority: { level: reference, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: deny }
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

### Playbook Schema
Additional fields for `/02_PLAYBOOKS/`:

```yaml
---
audience:
  ll_consumable: true | false    # Override partial default
cites_doctrine: []               # List of doctrine IDs this playbook derives from
---
```

### Template Schema
Additional fields for `/03_TEMPLATES/`:

```yaml
---
version: string                  # e.g., "1.0", "2.1"
approval_status: draft | approved
---
```

### Matter Schema
For `/04_MATTERS/`:

**Matter ID Format:** `##-###-#####`
- First segment: Year matter was opened (2-digit)
- Second segment: Client number within the firm (3-digit)
- Third segment: Matter number for that client (5-digit)

Example: `26-998-00001` = Year 2026, Client #998, Matter #1 for that client

**Matter Folder Naming:** `##-###-##### Client Name - Description`

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

**Matter Internal Structure:**

```
04_MATTERS/{status}/
└── ##-###-##### Client Name - Description/
    ├── 00_OVERVIEW.md        # Matter summary, parties, key dates
    ├── 01_FACTS.md           # Factual record (non-normative)
    ├── 02_RECORDS/           # Source documents
    │   ├── 02_1_CLIENT_DOCUMENTS/
    │   └── 02_2_EMAILS/
    ├── 03_ANALYSIS.md        # Legal/strategic analysis
    ├── 04_ROADMAP.md         # Timeline, milestones, deliverables
    ├── 05_OUTPUTS/           # Work product for this matter
    └── 06_ACTIONS.md         # Current and pending action items
```

| File/Folder | Purpose |
|-------------|---------|
| `00_OVERVIEW.md` | Matter summary, parties, scope, key dates |
| `01_FACTS.md` | Chronological factual record (non-normative) |
| `02_RECORDS/` | Source documents and communications |
| `02_1_CLIENT_DOCUMENTS/` | Documents received from or sent to client |
| `02_2_EMAILS/` | Email correspondence |
| `03_ANALYSIS.md` | Legal analysis, risk assessment, strategy |
| `04_ROADMAP.md` | Timeline, milestones, deliverables schedule |
| `05_OUTPUTS/` | Work product generated for this matter |
| `06_ACTIONS.md` | Current and pending action items |

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
related_matter: matter-id | null
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
derived_from: []                 # Source doctrine/playbook/template IDs
audience:
  target: LL | internal | external
---
```
