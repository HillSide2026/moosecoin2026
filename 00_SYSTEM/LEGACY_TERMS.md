# Legacy Terminology

This system was derived from a prior Second Brain implementation that was
specific to a law firm environment.

Certain terms remain in use for structural continuity but are no longer
semantically binding.

---

## Legacy Terms

### "Matter"
Originally referred to a legal matter.
In MooseCoin2026, this term functions as a **legacy label** for a
**Project**.

A Project is a bounded unit of work, initiative, or effort with defined
scope, participants, and lifecycle.

All references to "Matter" should be interpreted as
"Project (legacy: Matter)" unless and until a structural refactor
replaces the term entirely.

**Canonical replacement term:** Project

### "LL"
Originally referred to Levine Law as an execution environment.

In MooseCoin2026, "LL" functions as a legacy label for a generic execution
environment: the people, tools, and operational surface that consumes approved
outputs and performs work.

All references to "LL" should be interpreted as
"Execution Environment (legacy: LL)" unless and until a structural refactor
replaces the term entirely.

**Canonical replacement term:** Execution Environment

### "Client"
- Appears in: MATTER_SCHEMA.md, matter-template/00_OVERVIEW.md
- Originally: party receiving legal services
- Current function: stakeholder or counterparty in a unit of work

### "Practice Area"
- Appears in: MATTER_SCHEMA.md (lines 124-147), matter template
- Originally: classification of legal service lines (Corporate, Compliance, Transactions)
- Current function: domain categorization for work units

### "Opposing Party" / "Parties"
- Appears in: matter template, matter-to-fact-extraction-protocol.md
- Originally: adversarial legal parties
- Current function: no clear generic equivalent

### "Solution"
- Appears in: MATTER_SCHEMA.md, FOLDER_MAP.md (ll-solution)
- Originally: type of legal service being delivered
- Current function: undefined placeholder (backlog item #2)

---

## Lower-Confidence Legacy Terms

The following terms appear in system files and likely originate from the law
firm context, but may also have general applicability:

- **"Filing" / "Filings"** — court/administrative submissions; used in matter outputs and extraction protocols
- **"Intake" / "Triage"** — law firm onboarding vocabulary; used for 09_INBOX/ routing
- **"Delivery"** (as status/folder concept) — law firm service delivery framing; structures the playbook folder hierarchy
- **"Engagement"** — law firm client-relationship lifecycle term

---

## Structural / Embedded Legacy

### Playbook taxonomy under 02_PLAYBOOKS/delivery/
Contains: corporate/, contract/, franchising/, financial-services/ with
sub-items like M&A, shareholder-conflict, deadlock, redemption — all law
firm practice sub-areas.

These folder names represent deeply embedded legacy structure that would
require significant refactoring to replace.
