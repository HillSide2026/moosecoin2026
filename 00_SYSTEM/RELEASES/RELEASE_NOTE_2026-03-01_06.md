---
id: RELEASE-2026-03-01-06
title: /00_SYSTEM Release Note 2026-03-01 (06)
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [release]
---

# /00_SYSTEM Release Note — 2026-03-01 (06)

## Version Bump
- From: v0.8
- To: v0.9

## Change Summary
- Completed taxonomy migration from `03_TEMPLATES/` to `03_PROTOCOLS/`.
- Established protocol framing as canonical for this layer:
  - Risk protocol
  - Execution protocol
  - Incident protocol
  - Review protocol
- Updated run artifact documents to protocol naming (`PROTOCOL-RUN-*`, protocol tags).
- Aligned governance and backlog language from legacy template/playbook terms to protocol/model terms where these are active system references.

## Impacted Artifacts
- 03_PROTOCOLS/README.md
- 03_PROTOCOLS/documents/run-protocols/00_RUN_OVERVIEW.md
- 03_PROTOCOLS/documents/run-protocols/01_INPUTS.md
- 03_PROTOCOLS/documents/run-protocols/02_DECISIONS.md
- 03_PROTOCOLS/documents/run-protocols/03_OUTPUTS.md
- 03_PROTOCOLS/documents/run-protocols/04_AUDIT.md
- 00_SYSTEM/FOLDER_MAP.md
- 00_SYSTEM/FOLDER_SCHEMAS.md
- 00_SYSTEM/SCHEMAS.md
- 00_SYSTEM/GLOSSARY.md
- 00_SYSTEM/BACKLOG_DOCTRINE.md
- 00_SYSTEM/SYSTEM_BACKLOG.md
- 01_DOCTRINE/constraints/DOCTRINE-2026-00X-run-protocol-draft.md

## Migration Notes (What changes for authors?)
- Create new governed procedure artifacts under `03_PROTOCOLS/`, not `03_TEMPLATES/`.
- Prefer `protocol`/`model` terminology in active canon docs.
- For run documentation scaffolds, use the `run-protocols` path and `PROTOCOL-RUN-*` IDs.
- Historical records (older release notes, audits, inbox outputs, and historical decision notes) may retain legacy terms for provenance.
