---
name: documentation-policy
description: Rules for updating CHANGELOG.md, creating/updating ADRs, and maintaining project-state or other memory files under .agents/memory/.
activation: Always On
---

# Rule: Documentation, Changelog, and ADR Policy

## Changelog

Update `CHANGELOG.md` whenever the change affects:

- application behavior
- architecture
- dependencies
- infrastructure
- security posture
- developer workflow
- agent instructions

Use these categories under `[Unreleased]`:

- `Added`
- `Changed`
- `Fixed`
- `Security`
- `Deprecated`
- `Removed`

## ADRs

Create or update an ADR for durable decisions.

Examples requiring ADR:

- choosing primary database or storage engines
- introducing new external integrations or search backends
- selecting core frameworks or orchestration libraries
- deciding how security/ACL filtering is enforced
- changing deployment architecture

Examples not requiring ADR:

- renaming a local variable
- adding a small unit test
- fixing a typo
- updating documentation wording

## Design Guides (Mandatory for Complex Features)

For any complex feature, algorithm, workflow, or architectural concept introduced or significantly modified, you MUST create or update a conceptual design guide in `docs/design/` to explain the concept in plain human language.

Purpose:
- Explain conceptually how the feature or system works.
- Focus on business logic, conceptual architecture, and user flows without detailing technical database or code implementations.
- Use clear headings, bullet points, formulas, examples, or ASCII/Mermaid diagrams to illustrate concepts.

Naming convention:
`docs/design/<feature-name>-guide.md` (e.g., `docs/design/hybrid-search-rrf-guide.md`).

## Memory updates

Update `.agents/memory/` only when the information will help future agent sessions.

Good memory entries:

- current project phase
- chosen conventions
- constraints discovered during implementation
- non-secret Azure resource names returned by the human
- known blockers and open questions

Bad memory entries:

- long pasted logs
- secrets
- temporary debugging notes
- duplicate changelog entries
