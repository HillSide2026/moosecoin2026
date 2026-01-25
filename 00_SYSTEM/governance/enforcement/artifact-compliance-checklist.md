---
id: GOV-2026-002
title: Artifact Compliance Checklist v1.0
owner: ML1
status: approved
created_date: 2026-01-21
last_updated: 2026-01-21
effective_date: 2026-01-21
tags: [compliance, lint, enforcement]
provenance:
  decided_by: ML1
  decided_on: 2026-01-21
  context: Manual lint for verifying system integrity
---

# Artifact Compliance Checklist v1.0

Manual lint for verifying system integrity. Run periodically or before commits.

---

## 1. Required Metadata Check

For each artifact, verify YAML frontmatter includes:

- [ ] `id` — present and follows naming convention
- [ ] `title` — present
- [ ] `owner` — present (default: ML1)
- [ ] `status` — present and valid for artifact type
- [ ] `created_date` — present, format YYYY-MM-DD
- [ ] `last_updated` — present, format YYYY-MM-DD
- [ ] `tags` — present (may be empty array)

**Folder-specific required fields:**

| Folder | Additional Required Fields |
|--------|---------------------------|
| 00_SYSTEM/governance | `provenance.decided_by`, `provenance.decided_on` |
| 01_DOCTRINE | `effective_date`, `provenance.decided_by`, `provenance.decided_on` |
| 02_PLAYBOOKS | `cites_doctrine` (may be empty) |
| 03_TEMPLATES | `version`, `approval_status` |
| 04_PROJECTS | `priority` |
| 05_RUNS | `triggered_by`, `related_matter` |
| 06_OUTPUTS | `derived_from`, `audience.target` |

---

## 2. Authority Leak Check

Verify `source_of_truth: true` appears ONLY in:

- [ ] `00_SYSTEM/`
- [ ] `01_DOCTRINE/`
- [ ] `03_TEMPLATES/`

**Violation:** Any file outside these folders with `source_of_truth: true`

---

## 3. Authority Creep Check

Verify `authority.level` in `04_PROJECTS/`:

- [ ] No file has `authority.level: binding`
- [ ] No file has `authority.level: procedural`

**Allowed values in 04_PROJECTS:** `none` only (or omitted, inherits default)

---

## 4. Unauthorized Emission Check

For any artifact with `ll_consumable: true`, verify:

- [ ] File is in an LL-consumable folder (01_DOCTRINE, 03_TEMPLATES, 06_OUTPUTS)
- [ ] OR file has explicit approval metadata

**Violation:** `ll_consumable: true` in 00_SYSTEM, 04_PROJECTS, 05_RUNS, 07_RESEARCH, 08_REFERENCE, 09_INBOX, 10_ARCHIVE without override justification

---

## 5. Orphan Check

Verify all files exist within defined folder structure:

- [ ] No files at repository root (except LICENSE, README.md)
- [ ] No files in undefined subfolders
- [ ] No empty folders without `.gitkeep` or content

---

## 6. Immutability Check

For files in immutable folders (05_RUNS, 10_ARCHIVE):

- [ ] `status: completed` or `status: failed` files have not been modified since completion
- [ ] No `status` field changes after initial completion

---

## 7. Retention Check

For files in `09_INBOX/`:

- [ ] `created_date` is within retention period (default: 7 days)
- [ ] Files exceeding retention are flagged for triage or archival

---

## Run Log

| Date | Run By | Issues Found | Resolved |
|------|--------|--------------|----------|
| | | | |

---

## Notes

- This checklist is manual v1.0
- Future: automate as pre-commit hook or CI check
- Violations should be logged in DECISION_LOG.md if they require ML1 judgment
