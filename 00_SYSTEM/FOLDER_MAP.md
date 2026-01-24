# Folder Map

## 00_SYSTEM/
**Purpose:** System governance and mechanics

**Contents:**
- Agents
- Schemas
- Governance rules

**Rules:**
- ML1 write-only
- ML2 read-only
- Never emitted, summarized, or consumed by LL

---

## 01_DOCTRINE/
**Purpose:** Authoritative judgment and constraints

**Structure:**
- `/binding` — Rules that govern behavior
- `/interpretive` — Guidance, principles
- `/constraints` — Limits, prohibitions

**Rules:**
- Source-of-truth eligible
- Requires ML1 approval to bind
- Never auto-generated

---

## 02_PLAYBOOKS/
**Purpose:** Procedural "how-to" guidance

**Structure:**
- `/ll-marketing-sales` — Marketing and sales workflows
- `/ll-client` — Client-facing procedures
- `/ll-solution` — Solution delivery workflows
- `/admin` — Administrative procedures
- `/secondary-business` — Non-core business workflows

**Rules:**
- Never source-of-truth
- May be LL-consumable only if metadata allows (`ll_consumable: true`)
- Must cite Doctrine when relevant

---

## 03_TEMPLATES/
**Purpose:** Structured starting points for outputs

**Structure:**
- `/documents` — Document templates
- `/internal` — Internal-use templates
- `/checklists` — Checklist templates
- `/snippets` — Reusable text fragments

**Rules:**
- Authoritative only as templates
- Instantiated outputs are never canon
- Versioned and approval-gated

---

## 04_MATTERS/
**Purpose:** Case- or project-specific work

**Structure:**
- `/open/` — Active matters by priority
  - `/essential` — Highest priority
  - `/strategic` — Strategic importance
  - `/standard` — Normal priority
  - `/parked` — On hold
- `/pending/` — Awaiting action or decision
- `/closed/` — Completed matters

**Matter ID Format:** `##-###-#####`

**Rules:**
- Non-authoritative by default
- Cannot override canon
- High agent access, low authority

---

## 05_RUNS/
**Purpose:** Audit and execution records

**Structure:**
- `/YYYY/MM/run-id/` — Organized by year and month

**Rules:**
- Immutable
- Never authoritative
- Citable only as provenance

---

## 06_OUTPUTS/
**Purpose:** Human-consumable deliverables

**Structure:**
- `/drafts` — Work in progress
- `/reviews` — Pending review
- `/exports` — Final exports

**Rules:**
- Consumable, not authoritative
- May flow to LL if derived from canon
- Cannot become "Gold"

---

## 07_RESEARCH/
**Purpose:** Exploratory and analytical material

**Structure:**
- By topic domain

**Rules:**
- Reference-only
- No direct emission to LL
- May inform playbooks/templates

---

## 08_REFERENCE/
**Purpose:** External and static sources

**Structure:**
- By reference type

**Rules:**
- Read-only
- Never binding
- Contextual use only

---

## 09_INBOX/
**Purpose:** Intake and triage

**Structure:**
- `/untriaged` — New, unprocessed items
- `/triaged` — Processed, awaiting routing

**Rules:**
- Time-limited residence
- No authority
- Must be promoted or archived

---

## 10_ARCHIVE/
**Purpose:** Historical preservation

**Structure:**
- By artifact origin

**Rules:**
- Retains original authority status
- Archive ≠ deprecated
- Read-only
