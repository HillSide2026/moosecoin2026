---
id: DOCTRINE-2026-00X
title: Run Protocol (Draft)
owner: ML1
status: draft
created_date: 2026-02-09
last_updated: 2026-03-01
effective_date: 2026-02-09
supersedes:
tags: [runs, execution, governance, protocol]
provenance:
  decided_by: ML1
  decided_on: 2026-02-09
  context: Draft run protocol to establish a safe, inspectable execution path

lifecycle: { folder_class: canon }
authority: { level: binding, source_of_truth: false }
audience: { scope: ml1_only, ll_consumable: false }
---

# Run Protocol (Draft)

## Purpose
Define the minimum, auditable structure required to initiate, execute, and close a Run. A Run is the only authorized execution container for actions derived from ML1‑approved intent.

## Scope
**In Scope**
- Run creation, contents, and completion criteria
- Required linkages to project and decision artifacts
- Auditability and traceability requirements

**Out of Scope**
- Trading strategy creation
- Platform selection
- Execution logic or trade decision content

## Core Principles
- Runs are **inspectable** and **auditable**
- Runs require **explicit ML1 approval** to start
- Runs must trace to **approved decisions**
- Runs never create authority; they only execute approved intent

## Workflow Definition
- **Trigger:** ML1-approved decision exists and run initiation is explicitly approved.
- **Inputs:** Approved decision artifacts, approved input set, and project linkage.
- **Outputs:** Recorded run outputs with traceability to decisions and inputs.
- **Completion Gate:** Audit completed and run status closed by ML1.

## Step Sequence
1. **Initiate:** Create run artifacts and capture required approvals.
2. **Execute:** Record inputs, decisions, and outputs while enforcing halt conditions.
3. **Close:** Complete audit, verify traceability, and mark run closed.

## Role Responsibilities
- **ML1:** Approves run start, resolves deviations, and approves closure.
- **ML2:** Maintains run records, enforces structure, and flags violations.
- **Execution Environment:** Performs only explicitly authorized actions linked to approved decisions.

## Run Lifecycle

### 1) Initiation
A Run may be created only when:
- A project is in **Execution** stage or has explicit ML1 authorization
- A specific, ML1‑approved decision exists and is referenced
- Required run protocol files are created and populated

### 2) Execution
During execution:
- Inputs, decisions, and outputs are recorded in the run folder
- Any deviation from approved intent **halts the run** and requires ML1 review

### 3) Closure
A Run is closed when:
- Outputs are recorded and linked to decision artifacts
- Audit section is completed
- ML1 marks the run as closed

## Required Run Structure
Each run must use the following folder structure:

```
05_RUNS/YYYY/MM/run-id/
  00_RUN_OVERVIEW.md
  01_INPUTS.md
  02_DECISIONS.md
  03_OUTPUTS.md
  04_AUDIT.md
```

## Required Linkages
- `00_RUN_OVERVIEW.md` MUST reference:
  - Project ID
  - Decision ID(s)
  - ML1 approval timestamp
- `02_DECISIONS.md` MUST point to the specific approved decision artifacts
- `03_OUTPUTS.md` MUST link each output to a decision and input set

## Run-ID Format
`YYYYMMDD-SEQ-short-label`
Example: `20260209-001-platform-gating`

## Failure Modes (Must Halt)
- Missing ML1 approval
- Missing decision linkage
- Output not traceable to approved decision
- Any new trading logic introduced during execution

## Change Control
- Any changes to run protocol artifacts require ML1 approval
- All protocol updates must be recorded in Decision Log

## Open Questions (for ML1)
1. Is ML1 the sole approver for starting a run, or is a secondary reviewer required?
