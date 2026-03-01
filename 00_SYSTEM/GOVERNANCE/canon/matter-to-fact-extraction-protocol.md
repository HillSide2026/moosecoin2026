---
id: GOV-2026-005
title: Matter → Fact Extraction Protocol
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-03-01
effective_date: 2026-01-21
tags: [extraction, facts, matters, reference]
provenance:
  decided_by: ML1
  decided_on: 2026-01-21
  context: Defines how factual information may be extracted from Matters without normative force
---

# Matter → Fact Extraction Protocol

This document exists to:
- Allow the system to identify and preserve **facts of record** from `04_PROJECTS`
- Prevent accidental elevation of facts into rules, guidance, or precedent
- Enable retrieval and aggregation of facts **without normative force**

---

## Core Doctrine

> **Facts may be extracted from a Matter without implying significance, generality, or normative force.**

This sentence is binding system doctrine.

---

## 1. Definition of a "Fact" (System Definition)

A fact is:
- **Time-bound** — occurred at a specific point or period
- **Context-bound** — specific to a matter, party, or situation
- **Non-prescriptive** — does not recommend or require action
- **Non-generalizing** — does not claim applicability beyond its context

### Valid facts

| ✔ Valid Fact |
|--------------|
| "Shareholder agreement was signed on 2026-01-15" |
| "Court filing deadline was January 30, 2026" |
| "Client approved the revised terms on 2026-01-18" |
| "Opposing counsel rejected the initial offer" |
| "Filing fee was $350" |

### Invalid facts (these are NOT facts)

| ✖ Invalid — Actually a... |
|---------------------------|
| "The 30-day notice period worked well" — evaluation |
| "This approach should be used for similar matters" — prescription |
| "Early engagement with opposing counsel reduces delays" — lesson/generalization |
| "The client's aggressive timeline was a risk factor" — interpretation |
| "We should always file within 15 days" — rule |

---

## 2. What May Be Extracted

### Extractable as facts

- Procedural events (filings, signatures, deliveries)
- External actions (court orders, regulator responses, counterparty decisions)
- Client decisions or approvals
- Outcomes or responses (acceptances, rejections, amendments)
- Dates, deadlines, thresholds
- Amounts, fees, quantities
- Communications sent/received (that X occurred, not what it means)

### MUST NOT be extracted as facts

- Strategic rationale
- Risk assessments or judgments
- "What worked" or "what didn't work"
- "What should be repeated"
- Lessons learned
- Causal explanations
- Evaluations of quality or effectiveness

---

## 3. Who May Extract Facts

| Role | May Extract | May Normalize | May Interpret | Approval Required |
|------|-------------|---------------|---------------|-------------------|
| **ML2 Maintainer** | Yes | Yes | No | No |
| **Agents** | Propose only | Yes | No | N/A |
| **ML1** | Yes | Yes | Yes | N/A |

### ML2 Maintainer (human)
- May extract facts from Matters
- May normalize wording for consistency
- May tag, categorize, and de-duplicate
- MUST NOT add interpretation or meaning

### Agents
- May propose candidate facts for human review
- May summarize factual sequences
- May normalize formatting
- MUST NOT assert meaning, lessons, or generality
- MUST flag any statement that implies prescription

### ML1
- Approval is NOT required for fact extraction
- Fact extraction is a non-judgmental, mechanical act
- ML1 retains authority over any later generalization or canon promotion

---

## 4. Where Facts Live

Extracted facts reside in:

```
08_RESEARCH/facts/
  /by-matter/
  /by-topic/
```

### Rules

- Facts do NOT live in canon folders (01_DOCTRINE, 02_MODELS, 03_PROTOCOLS)
- Facts are **reference-only** (`authority.level: reference`)
- Facts may be aggregated, searched, and retrieved safely
- Aggregation does NOT create authority

---

## 5. Required Metadata for Facts

```yaml
---
id: FACT-{matter-id}-{seq}
title: string
type: fact
authority:
  level: reference
  source_of_truth: false
normative: false
generalizable: false
provenance:
  derived_from: {matter-id}
  extraction_date: YYYY-MM-DD
  extracted_by: ML2 | agent-assisted
created_date: YYYY-MM-DD
tags: []
---
```

### Mandatory flags

| Field | Required Value | Purpose |
|-------|----------------|---------|
| `authority.level` | `reference` | Cannot govern behavior |
| `authority.source_of_truth` | `false` | Cannot define truth |
| `normative` | `false` | Explicit non-prescription |
| `generalizable` | `false` | Explicit non-generalization |
| `provenance.derived_from` | Matter ID | Traceability |

**Missing provenance invalidates the fact record.**

---

## 6. Language Constraints (Critical)

### Facts MUST

- Be written in **declarative past tense**
- State what occurred, not what it means
- Be specific to time and context
- Use neutral, observational language

### Facts MUST NOT

- Contain modal verbs: "should", "usually", "typically", "best"
- Contain comparative language: "better", "worse", "more effective"
- Contain evaluative language: "successfully", "failed", "worked well"
- Contain recommendations
- Contain causal claims beyond direct observation
- Contain extrapolation to other contexts

### Allowed vs Forbidden Language

| ✔ Allowed | ✖ Forbidden |
|-----------|-------------|
| "The filing was submitted on January 15" | "The filing was submitted promptly" |
| "Client approved the terms" | "Client wisely approved the terms" |
| "Opposing counsel rejected the offer" | "Opposing counsel unreasonably rejected the offer" |
| "The matter closed on March 1" | "The matter closed efficiently" |
| "Three revisions were required" | "Too many revisions were required" |
| "Response was received in 5 days" | "Response was received quickly" |

---

## 7. Agent Constraints

### Agents MAY

- Identify candidate factual statements in Matter content
- Normalize formatting and structure
- Tag and cluster facts by topic or date
- De-duplicate identical facts across matters
- Propose fact records for human review

### Agents MUST NOT

- Add interpretation or meaning
- Add weighting, importance, or significance
- Suggest that a fact implies a pattern
- Promote facts into models, protocols, or doctrine
- Use evaluative language in fact records

### Escalation Rule

> **If a proposed fact begins to imply generality, prescription, or precedent, agents MUST stop and flag for human review.**

The agent must not attempt to "fix" the statement. Human judgment is required.

---

## 8. Enforcement & Boundary Rule

> **Any artifact that asserts prescription, generality, or policy is no longer a fact and must follow canon promotion rules.**

### Boundary test

If a statement answers any of these questions, it is NOT a fact:
- "What should we do?"
- "What works?"
- "What does this mean for other matters?"
- "Is this a pattern?"

### Violations

- Facts containing normative language are non-compliant
- Violations trigger the **Violation Triage Protocol** (GOV-2026-003)
- Severity: P1 minimum
- Remedy: Edit to remove normative content, or reclassify and route to canon promotion

---

## 9. Examples

### Example A: Correct fact extraction

**Matter content:** "We filed the articles of incorporation on January 10, 2026. The state acknowledged receipt on January 12."

**Extracted fact:**
```markdown
- Articles of incorporation filed: 2026-01-10
- State acknowledgment received: 2026-01-12
```
✔ Time-bound, context-bound, non-prescriptive.

---

### Example B: Incorrect extraction implying precedent

**Matter content:** "Filing early gave us buffer time when the state requested corrections."

**Incorrect extraction:** "Early filing provides buffer time for corrections."

✖ This implies a lesson or recommendation. It is NOT a fact.

**Correct extraction:** "Filing submitted 2026-01-10. Correction request received 2026-01-14. Corrected filing submitted 2026-01-15."

---

### Example C: Correct rejection of a "lesson learned"

**Matter content:** "In retrospect, we should have engaged opposing counsel earlier."

**Correct response:** Do not extract. This is a judgment, not a fact. If the underlying events are valuable, extract only the events:
- "First contact with opposing counsel: 2026-02-15"
- "Settlement discussions began: 2026-03-01"

The judgment ("should have engaged earlier") is not extractable as a fact.

---

### Example D: Agent-proposed fact requiring edit

**Agent proposal:** "Client quickly approved the revised shareholder agreement."

✖ "Quickly" is evaluative.

**Human edit:** "Client approved revised shareholder agreement on 2026-01-18 (3 days after delivery)."

✔ Now factual: date-bound, no evaluation.

---

## Phase 3A Exit Conditions

- [x] Facts can be extracted safely
- [x] Facts are non-normative
- [x] Provenance is mandatory
- [x] Agents are constrained
- [x] No implication of precedent
