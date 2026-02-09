---
id: TEMPLATE-RUN-00-OVERVIEW
title: Run Overview Template
owner: ML1
status: draft
created_date: 2026-02-09
last_updated: 2026-02-09
tags: [runs, template, overview]
---

# Run Overview

```yaml
run:
  id: YYYYMMDD-SEQ-short-label
  project_id: YY-CCC-NNNNN
  decision_ids: []
  stage: execution
  status: in_progress | paused | blocked | closed
owner:
  ml1: ML1
approvals:
  started_by: ML1
  started_on: YYYY-MM-DD
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
links:
  project_path:
  decisions:
  inputs:
  outputs:
  audit:
```

## Purpose
Snapshot of this run: why it exists, what it is allowed to do, and its governing approvals.
