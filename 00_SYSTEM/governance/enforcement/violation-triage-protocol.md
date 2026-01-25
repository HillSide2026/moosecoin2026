---
id: GOV-2026-003
title: Violation Triage Protocol
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-01-21
effective_date: 2026-01-21
tags: [enforcement, triage, violations]
provenance:
  decided_by: ML1
  decided_on: 2026-01-21
  context: Defines enforceable response protocol for taxonomy/metadata violations
---

# Violation Triage Protocol

Explicit, enforceable response protocol when taxonomy or metadata violations are detected.

---

## 1. Scope

### What counts as a violation

| Type | Description |
|------|-------------|
| **Violation** | Breach of authority, canon, or audience rules that MUST be remediated |
| **Warning** | Missing optional metadata or style deviation; MAY be deferred |

### Directories in scope

All directories are in scope for compliance checks:
- `00_SYSTEM/` — canon, binding
- `01_DOCTRINE/` — canon, binding
- `02_PLAYBOOKS/` — canon, procedural
- `03_TEMPLATES/` — canon, procedural
- `04_PROJECTS/` — work, non-authoritative
- `05_RUNS/` — event, immutable
- `06_OUTPUTS/` — work
- `07_RESEARCH/` — library
- `08_REFERENCE/` — library
- `09_INBOX/` — intake
- `10_ARCHIVE/` — archive, immutable

---

## 2. Roles & Decision Rights

| Role | Can Detect | Can Draft Fix | Can Approve Fix | Can Modify Canon |
|------|------------|---------------|-----------------|------------------|
| **ML1** | Yes | Yes | Yes | Yes |
| **ML2 Maintainer** | Yes | Yes | No | No |
| **LL Consumer** | No | No | No | No |

### Actions requiring ML1 approval

- Promoting any artifact to canon
- Changing `status: approved` on any artifact
- Modifying content in canon folders
- Overriding quarantine decisions
- Closing P0 violations

---

## 3. Severity Levels

| Severity | Name | Description | Examples |
|----------|------|-------------|----------|
| **P0** | Critical | Authority breach; immediate risk of LL consuming invalid canon | `source_of_truth: true` in 04_PROJECTS; `binding` authority in non-canon |
| **P1** | Major | Canon integrity issue; blocks promotion or causes drift | Missing `provenance` on approved doctrine; orphaned file in canon |
| **P2** | Minor | Metadata incomplete; no immediate authority risk | Missing optional tags; style deviation |

---

## 4. Timeframes (SLA)

| Severity | Response Time | Resolution Time | Quarantine |
|----------|---------------|-----------------|------------|
| **P0** | Immediate | 24 hours | MUST quarantine immediately |
| **P1** | 24 hours | 5 business days | SHOULD quarantine |
| **P2** | 5 business days | Next release | No quarantine required |

---

## 5. Required Response Workflow

### Detection
- [ ] Run Artifact Compliance Checklist (`GOV-2026-002`)
- [ ] Record all violations found

### Record
- [ ] Log violation in `00_SYSTEM/governance/enforcement/violation-log.md`
- [ ] Assign severity (P0/P1/P2)
- [ ] Assign owner

### Quarantine (P0/P1)
- [ ] Set `audience.scope: ml2_internal`
- [ ] Set `ll_consumable: false`
- [ ] Move to `09_INBOX/triaged/` if location is part of violation
- [ ] Add `quarantined: true` to violation log

### Remediate
- [ ] Draft fix in `06_OUTPUTS/drafts/` (MUST NOT edit canon directly)
- [ ] Verify fix passes compliance checklist

### Promote (if canon change required)
- [ ] Follow Gold Promotion Protocol (`GOV-2026-001`)
- [ ] Obtain ML1 approval
- [ ] Log promotion in DECISION_LOG.md

### Verify
- [ ] Re-run compliance checklist
- [ ] Confirm violation resolved

### Close
- [ ] Update violation log with closure date
- [ ] Remove quarantine flags if applicable

---

## 6. Quarantine Rules (Non-negotiable)

### What quarantine means

Quarantine isolates a violating artifact from LL consumption and canon use.

### Acceptable quarantine mechanisms

- Set `audience.scope: ml2_internal`
- Set `ll_consumable: false`
- Move file to `09_INBOX/triaged/`
- Add warning comment in frontmatter: `# QUARANTINED: [reason]`

### Enforcement

- Quarantined artifacts MUST NOT be used for LL outputs
- Quarantined artifacts MUST NOT be cited as authority
- Quarantine MUST be logged

---

## 7. Permitted vs Forbidden Actions

### Permitted

- Fix missing metadata keys (non-authority fields)
- Move artifact to correct folder (with logging)
- Downgrade `audience.scope` to more restrictive
- Create draft replacement in `06_OUTPUTS/drafts/`
- Add quarantine flags

### Forbidden

- Adding `approved`/`approver` metadata solely to satisfy lint
- Editing canon content without promotion
- Changing `source_of_truth: true` outside canon folders
- Setting `authority.level: binding` or `procedural` in 04_PROJECTS
- Removing quarantine without ML1 approval
- Closing P0 without ML1 sign-off

---

## 8. Promotion Firewall

Changes to canon occur ONLY via the Gold Promotion Protocol:

1. Draft created in `06_OUTPUTS/drafts/`
2. Status: `draft` → `proposed`
3. ML1 reviews and approves
4. Status: `proposed` → `approved`
5. File moved to canon folder
6. Logged in DECISION_LOG.md

### No silent canon edits

- Direct edits to `status: approved` are FORBIDDEN
- Direct edits to `provenance` block are FORBIDDEN
- All canon changes MUST flow through promotion

---

## 9. Violation Log Spec

**Path:** `00_SYSTEM/governance/enforcement/violation-log.md`

### Required fields

| Field | Description |
|-------|-------------|
| `date_found` | YYYY-MM-DD |
| `file_path` | Full path to violating file |
| `artifact_id` | `id` from frontmatter |
| `severity` | P0 / P1 / P2 |
| `description` | Brief violation description |
| `quarantined` | Y / N |
| `owner` | Who is responsible for fix |
| `target_date` | Expected resolution date |
| `closure_date` | Actual resolution date |
| `notes` | Additional context |

### Log format

```markdown
| date_found | file_path | artifact_id | severity | description | quarantined | owner | target_date | closure_date | notes |
|------------|-----------|-------------|----------|-------------|-------------|-------|-------------|--------------|-------|
| 2026-01-21 | /path/file.md | ID-001 | P1 | Missing provenance | Y | ML2 | 2026-01-26 | | |
```

---

## 10. Appendix: Example Scenarios

### Scenario A: `source_of_truth: true` in 04_PROJECTS

**Severity:** P0
**Response:**
1. Quarantine immediately (set `ll_consumable: false`)
2. Log violation
3. Remove `source_of_truth` field or set to `false`
4. Verify no LL outputs cited this artifact
5. Close with ML1 approval

### Scenario B: LL-consumable output missing derivation

**Severity:** P1
**Response:**
1. Quarantine (set `ll_consumable: false`)
2. Log violation
3. Add `derived_from` field citing approved canon
4. If no valid canon source exists, demote to `ml2_internal`
5. Verify and close

### Scenario C: Canon doc approved but missing provenance

**Severity:** P1
**Response:**
1. Quarantine
2. Log violation
3. Draft replacement with complete `provenance` block
4. Promote via Gold Promotion Protocol
5. Archive original
6. Verify and close

### Scenario D: Reference material in canon folder

**Severity:** P1
**Response:**
1. Log violation
2. Move file to `08_REFERENCE/`
3. Update any citations
4. Verify placement correct
5. Close

---

## Phase 2 Exit Criteria

- [x] Artifact Compliance Checklist exists (`GOV-2026-002`)
- [x] Violation Triage Protocol exists (`GOV-2026-003`)
- [ ] Violation Log exists (`violation-log.md`)
- [ ] Cadence defined: weekly or pre-release compliance runs
