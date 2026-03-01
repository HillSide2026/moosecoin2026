---
id: PROTOCOL-RUN-00-OVERVIEW
title: Run Overview Protocol
owner: ML1
status: draft
created_date: 2026-02-09
last_updated: 2026-03-01
tags: [runs, protocol, overview]
protocol_type: execution
version: "1.0"
approval_status: draft
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
