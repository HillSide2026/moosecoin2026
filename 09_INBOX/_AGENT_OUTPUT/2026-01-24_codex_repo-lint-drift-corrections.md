---
generated_by: codex
generated_on: 2026-01-24
type: report
status: draft
authority:
  level: none
  source_of_truth: false
audience:
  scope: ml1_only
---

# Corrections — Repo Lint & Drift Findings (2026-01-24)

## Acknowledgement (per GOV-2026-006)
This report is advisory only. Existing reports were **not** modified. Corrections are issued as a new report in `09_INBOX/_AGENT_OUTPUT/`.

## Correction Summary
New guidance clarifies that:
- `04_PROJECTS/` **does not require** `open/`, `pending/`, or `closed/` subfolders.
- The system **does not require** top-level folders `05_RUNS/` and `06_OUTPUTS/`.
- Project frontmatter **does not require** `client` or `priority` fields.

Therefore, the earlier lint/drift findings that flagged these items should be treated as **superseded**.

## Impacted Prior Findings
- **REPO_LINT__2026-01-24.md**
  - Remove findings for missing `05_RUNS/` and `06_OUTPUTS/`.
  - Remove findings for missing `client` and `priority` fields in project frontmatter.

- **DRIFT_REPORT__2026-01-24.md**
  - Remove missing entries for `05_RUNS/`, `06_OUTPUTS/`, and their subfolders.
  - Remove missing entries for `04_PROJECTS/open/essential/`, `open/strategic/`, `open/parked/`, `pending/`, and `closed/`.

## Recommendation (Non-Executed)
1. When authorized, update the authoritative structure references (FOLDER_MAP/SCHEMAS) to reflect the clarified requirements.
2. After updates, re-run proto-agents to refresh lint/drift outputs against the corrected structure.
