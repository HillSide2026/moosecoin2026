---
id: SYSTEM-BOOT-INSTRUCTIONS
title: Second Brain — System Boot Instructions
owner: ML1
status: approved
created_date: 2026-01-22
last_updated: 2026-01-22
tags: [boot, system]
---

# Second Brain — System Boot Instructions

This repository is a Second Brain system.

## Operating Rules
- Treat this repo as the source of truth.
- Do not invent structure.
- Follow folder purposes as defined in `00_SYSTEM/FOLDER_MAP.md`.
- Do not write outside permitted folders.

## Agents
- Agent governance (rules, guardrails) lives in `00_SYSTEM/governance/agents/`.
- Executable agent definitions live in `.claude/agents/`.
- `00_SYSTEM/AGENTS/` is **deprecated** — do not use.
- Agents are Markdown files that must be followed exactly when invoked.
- When asked to "run an agent", open the agent file from `.claude/agents/` and execute its steps.

## Execution Rules
- Every non-trivial task must create a Run record in `05_RUNS/`.
- Do not modify Doctrine or Playbooks without explicit instruction.
- Prefer writing drafts to `06_OUTPUTS/`.

## Agent Write Guardrail (Non-Negotiable)

**Binding protocol:** `00_SYSTEM/governance/agents/agent-write-guardrail.md` (GOV-2026-006)

- Agents may write **only** to `09_INBOX/_AGENT_OUTPUT/`.
- All other directories are **read-only** for agents.
- Agents must not rename, move, edit, overwrite, or delete any existing files.
- Agents must not call or interact with external systems, APIs, or services.
- All outputs are advisory, draft, and report-only.
- Agents may propose actions but must never execute them.
- If a task would violate these rules: refuse, explain, and offer a draft report instead.

## Safety
- No silent changes.
- No background execution.
- Ask before promoting anything to knowledge.

Acknowledge these rules before proceeding.
