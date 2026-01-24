---
id: SCHEMA-MATTER-001
title: Matter Schema
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-01-21
tags: [schema, matters, structure]
---

# Matter Schema

Defines the structure, contents, and constraints for artifacts in `04_MATTERS/`.

---

## Authority Status

```yaml
lifecycle: { folder_class: work }
authority: { level: none, source_of_truth: false }
audience: { scope: ml2_internal, ll_consumable: false }
agents: { read: allow, write: allow }
```

**Matters are non-authoritative by definition.** They cannot:
- Define truth for the system
- Govern behavior
- Be cited as precedent
- Become canon without explicit extraction and approval

---

## Matter ID Format

`##-###-#####`

| Segment | Meaning | Example |
|---------|---------|---------|
| First (2 digits) | Year matter was opened | `26` = 2026 |
| Second (3 digits) | Client number within the firm | `998` = 998th client |
| Third (5 digits) | Matter number for that client | `00001` = 1st matter |

**Full example:** `26-998-00001` = Year 2026, Client #998, Matter #1 for that client

---

## Matter Folder Naming

```
##-###-##### Client Name - Description
```

**Example:** `26-001-00001 Acme Corp - Share Purchase Agreement`

---

## Matter Location

```
04_MATTERS/
├── open/
│   ├── essential/
│   ├── strategic/
│   ├── standard/
│   └── parked/
├── pending/
└── closed/
```

Matters are organized by `status` and `priority` (delivery status).

---

## Matter Frontmatter

```yaml
---
id: ##-###-#####
title: {Client Name} - {Description}
client: {Client Name}
owner: ML1
status: open | pending | closed
priority: essential | strategic | standard | parked
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: []
---
```

---

## Internal Structure

```
##-###-##### Client Name - Description/
├── 00_OVERVIEW.md
├── 01_FACTS.md
├── 02_RECORDS/
│   ├── 02_1_CLIENT_DOCUMENTS/
│   └── 02_2_EMAILS/
├── 03_ANALYSIS.md
├── 04_ROADMAP.md
├── 05_OUTPUTS/
└── 06_ACTIONS.md
```

---

## Component Definitions

### 00_OVERVIEW.md

| Property | Value |
|----------|-------|
| **Is** | Snapshot of the Matter right now; parties, posture, objectives, status |
| **Is NOT** | Doctrine; stable over time; citable as truth later |
| **Think** | Dashboard, not record |

**Contents:**
- Parties and contacts
- Scope and objectives
- Key dates
- Practice Area (at least one)
- Solution (one or more)
- Current status summary

#### Practice Area

Classification only — answers "What kind of legal work is this about?"

| Practice Area | Scope |
|---------------|-------|
| Corporate | |
| Contract | Franchising |
| Compliance | Data Security, Cannabis, Financial Regulatory |
| Transactions | |

**Practice Area does:**
- Group Matters into stable domains
- Help with routing, reporting, staffing, and finding similar Matters

**Practice Area does NOT:**
- Determine what you should do
- Imply a service type, strategy, or outcome
- Become precedent or doctrine

#### Solution

Type of service being provided. A Matter may have one or more Solutions.

---

### 01_FACTS.md

| Property | Value |
|----------|-------|
| **Is** | Factual assertions specific to this Matter; time-bound, scoped, contextual |
| **Is NOT** | Precedent; "generally true"; reusable as-is |
| **Note** | Source for Phase 3A fact extraction, but not itself a fact registry |

**Contents:**
- Chronological factual timeline
- Key factual assertions
- Non-normative: no interpretation, no lessons, no recommendations

**Extraction:** Facts may be extracted per GOV-2026-005 (Matter → Fact Extraction Protocol).

---

### 02_RECORDS/

| Property | Value |
|----------|-------|
| **Is** | Raw, unchallenged records; documents, emails, correspondence |
| **Is NOT** | Assertions; facts; interpretations |
| **Key property** | These are inputs, not assertions |

**Rule:** Records support facts; they are not facts themselves.

**Subfolders:**
- `02_1_CLIENT_DOCUMENTS/` — Documents received from or sent to client
- `02_2_EMAILS/` — Email correspondence

---

### 03_ANALYSIS.md

| Property | Value |
|----------|-------|
| **Is** | Judgment exercised in context; legal reasoning; strategy rationale |
| **Is NOT** | Guidance; a playbook; a "lesson learned" |
| **Risk** | This is where thinking lives, and where exaggeration risk is highest if not properly contained |

**Contents:**
- Legal issues identification
- Risk assessment
- Strategic options analysis
- Recommendations (matter-specific, not generalizable)

**Extraction:** Patterns may be extracted per GOV-2026-004 (Matter → Canon Extraction Doctrine) only with explicit approval.

---

### 04_ROADMAP.md

| Property | Value |
|----------|-------|
| **Is** | Forward-looking execution plan; tasks, steps, sequencing |
| **Is NOT** | A procedure for reuse; a general workflow |
| **Key property** | Roadmaps expire with the Matter |

**Contents:**
- Milestones and target dates
- Deliverables schedule
- Timeline visualization
- Dependencies and constraints

---

### 05_OUTPUTS/

| Property | Value |
|----------|-------|
| **Is** | Drafted or delivered artifacts; filings, letters, memos |
| **Is NOT** | Authoritative; truth-defining |
| **Critical rule** | Outputs are derivative artifacts, never authoritative |

**Audience:** May be LL-consumable, but they do not define truth.

**Contents:**
- Work product generated for this matter
- Drafts and final versions
- Deliverables

---

### 06_ACTIONS.md

| Property | Value |
|----------|-------|
| **Is** | Executed steps; completed actions; audit trail of what was done |
| **Is NOT** | Justification; evidence of correctness; precedent |

**Contents:**
- Active action items
- Pending actions (blocked)
- Completed actions log
- Next steps

---

## Constraints

### What Matters CANNOT Do

- Define `source_of_truth: true`
- Have `authority.level: binding` or `procedural`
- Be cited as precedent for other matters
- Become canon without explicit extraction (GOV-2026-004)
- Generate facts without extraction protocol (GOV-2026-005)

### What Matters CAN Do

- Store contextual, matter-specific information
- Support fact extraction (as source, not registry)
- Support pattern identification (for human review)
- Be read and written by agents
- Be closed and archived

---

## Lifecycle

| Status | Location | Meaning |
|--------|----------|---------|
| `open` | `04_MATTERS/open/{delivery status}/` | Active work |
| `pending` | `04_MATTERS/pending/` | Awaiting action or decision |
| `closed` | `04_MATTERS/closed/` | Completed |

**Movement:** Matters move between status folders as their state changes.

**Archive:** Closed matters may be moved to `10_ARCHIVE/` for long-term preservation.

---

## Related Governance

- **GOV-2026-004:** Matter → Canon Extraction Doctrine
- **GOV-2026-005:** Matter → Fact Extraction Protocol
- **GOV-2026-003:** Violation Triage Protocol (for non-compliance)

---

## Template

A matter template is available at:

```
03_TEMPLATES/internal/matter-template/
```

To create a new matter: copy template → rename → move to appropriate status folder.
