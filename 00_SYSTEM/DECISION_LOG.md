# Decision Log

This log records all system-level decisions affecting the Second Brain.

## Format
- Date
- Decision
- Approved by
- Artifacts impacted
- Notes

## 2026-01-04 — Establish Layer 1 repository structure

**Decision:** Formalized Layer 1 knowledge repository with governed structure  
**Approved by:** ML1  
**Artifacts impacted:** Entire repository  
**Notes:** Commits 1–3 establish system spine, domain boundaries, and authority model

## 2026-01-04 — Approve Doctrine 2026-001 (What Qualifies as Doctrine)

**Decision:** Approved foundational doctrine defining what constitutes authoritative doctrine  
**Approved by:** ML1  
**Artifacts impacted:** /01_DOCTRINE/DOCTRINE-2026-001-what-qualifies-as-doctrine.md  
**Notes:** Establishes authority criteria and prevents implicit or automated doctrine creation

## 2026-01-04 — Approve Doctrine 2026-002 (Authority Hierarchy)

**Decision:** Approved doctrine defining authority hierarchy between ML1, ML2, and LL  
**Approved by:** ML1  
**Artifacts impacted:** /01_DOCTRINE/DOCTRINE-2026-002-authority-hierarchy-ml1-ml2-ll.md  
**Notes:** Establishes non-delegable human authority and execution-only role of LL

## 2026-01-04 — Approve Doctrine 2026-003 (Promotion Rules)

**Decision:** Approved doctrine defining promotion lifecycle from Inbox to Research to Doctrine
**Approved by:** ML1
**Artifacts impacted:** /01_DOCTRINE/DOCTRINE-2026-003-promotion-rules.md
**Notes:** Establishes controlled pathway for authority creation and prevents implicit promotion

## 2026-01-21 — Approve Doctrine 2026-004 (Gold Promotion Protocol)

**Decision:** Approved doctrine establishing the firewall between drafts and authoritative canon
**Approved by:** ML1
**Artifacts impacted:** /01_DOCTRINE/binding/DOCTRINE-2026-004-gold-promotion-protocol.md
**Notes:** Defines where drafts live, who promotes, promotion steps, and prohibited actions

## 2026-01-21 — Approve Playbook 2026-001 (Artifact Compliance Checklist)

**Decision:** Approved playbook for manual compliance verification
**Approved by:** ML1
**Artifacts impacted:** /02_PLAYBOOKS/admin/artifact-compliance-checklist.md
**Notes:** Seven-check lint covering metadata, authority leaks, authority creep, unauthorized emission, orphans, immutability, and retention

## 2026-01-21 — Establish 00_SYSTEM/governance/ structure

**Decision:** Created governance subfolder for system-level rules (rules about rules)
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/{authority,canon,enforcement,agents,change-control}/
**Notes:** Separates system governance from firm doctrine. Governance constrains the system itself, not LL behavior.

## 2026-01-21 — Relocate Gold Promotion Protocol to governance

**Decision:** Moved from 01_DOCTRINE/binding/ to 00_SYSTEM/governance/canon/
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/canon/gold-promotion-protocol.md (was DOCTRINE-2026-004, now GOV-2026-001)
**Notes:** Correctly classified as system governance (rules about promotion), not firm doctrine

## 2026-01-21 — Relocate Artifact Compliance Checklist to governance

**Decision:** Moved from 02_PLAYBOOKS/admin/ to 00_SYSTEM/governance/enforcement/
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/enforcement/artifact-compliance-checklist.md (was PLAYBOOK-2026-001, now GOV-2026-002)
**Notes:** Correctly classified as system enforcement, not operational playbook

## 2026-01-21 — Approve GOV-2026-003 (Violation Triage Protocol)

**Decision:** Approved enforcement protocol for taxonomy and metadata violations
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/enforcement/violation-triage-protocol.md
**Notes:** Defines severity levels (P0/P1/P2), SLAs, quarantine rules, permitted/forbidden actions, and promotion firewall

## 2026-01-21 — Establish Violation Log

**Decision:** Created violation tracking log for compliance enforcement
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/enforcement/violation-log.md
**Notes:** Weekly compliance runs + pre-release checks. Completes Phase 2 Exit Criteria.

## 2026-01-21 — Approve GOV-2026-004 (Matter → Canon Extraction Doctrine)

**Decision:** Approved doctrine defining the only permitted way learning may move from Matters into canon
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/canon/matter-to-canon-extraction-doctrine.md
**Notes:** Core doctrine: "No general rule, template, or playbook may be inferred from a Matter without explicit extraction and approval." Prevents folklore and shadow doctrine. Completes Phase 3 Exit Criteria.

## 2026-01-21 — Approve GOV-2026-005 (Matter → Fact Extraction Protocol)

**Decision:** Approved protocol for extracting non-normative facts from Matters
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/canon/matter-to-fact-extraction-protocol.md, /07_RESEARCH/facts/
**Notes:** Core doctrine: "Facts may be extracted from a Matter without implying significance, generality, or normative force." Facts live in 07_RESEARCH/facts/. Completes Phase 3A Exit Criteria.

## 2026-01-21 — Approve Matter Schema (SCHEMA-MATTER-001)

**Decision:** Approved comprehensive schema defining Matter structure, contents, and constraints
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/MATTER_SCHEMA.md, /03_TEMPLATES/internal/matter-template/
**Notes:** Defines internal structure (00-06), Is/Is NOT clarifications for each component, authority constraints, and lifecycle. Records support facts but are not facts. Analysis is where exaggeration risk is highest.

## 2026-01-23 — Approve GOV-2026-006 (Agent Write Guardrail)

**Decision:** Approved non-negotiable write constraints for all proto-agents operating in this repository
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/governance/agents/agent-write-guardrail.md, /00_SYSTEM/CLAUDE.md, /09_INBOX/_AGENT_OUTPUT/
**Notes:** Agents may only write new files to 09_INBOX/_AGENT_OUTPUT/. All other directories are read-only. Agents must not rename, move, edit, overwrite, or delete files. Agents must not interact with external systems. Violations are P0 severity. Establishes foundation for proto-agent development.

## 2026-01-23 — Deprecate 00_SYSTEM/AGENTS/

**Decision:** Deprecated 00_SYSTEM/AGENTS/ directory; agent governance lives in 00_SYSTEM/governance/agents/, executable agents live in .claude/agents/
**Approved by:** ML1
**Artifacts impacted:** /00_SYSTEM/CLAUDE.md, /00_SYSTEM/AGENTS/ (removed)
**Notes:** The directory created ambiguity between governance (rules about agents) and runtime (agent definitions Claude discovers). Canonical doctrine path: 00_SYSTEM/governance/agents/. Runtime path: .claude/agents/. No files existed in the deprecated directory.

