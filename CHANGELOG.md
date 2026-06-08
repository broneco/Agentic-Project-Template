# Changelog

All notable project and agent-environment changes must be recorded here.

Format follows the spirit of Keep a Changelog: human-readable, chronological, with an `Unreleased` section.

## [Unreleased]

### Added
- Initial `.agents/` operating environment.
- Canonical agent contract in `.agents/AGENTS.md`.
- ADR and changelog requirements.
- Azure manual deployment handoff workflow.
- Iterative slice-based delivery policy.
- Example database migration skill under `.agents/skills/db-migration/`.
- Template for security guardrails under `.agents/templates/security-guardrails-template.md`.

### Changed
- Added required YAML frontmatter (with `name`, `description`, and `activation: Always On`) to all 8 rule files in `.agents/rules/` for compatibility with the Antigravity IDE standard.
- Updated rule `.agents/rules/security-and-secrets.md` to integrate and activate security guardrails (Deny/Allow/Ask lists).
- Extended `.agents/README.md` with documentation and instructions on setting up security guardrails and skills.
- Integrated DRY, Best Practices, Modularity, and Unit Testing First (TDD approach) from project standards into the rule `.agents/rules/coding-style.md`.

### Fixed
- Nothing yet.

### Security
- Added rule that secrets must never be committed and must be provided through Azure Key Vault, environment variables, or explicit human handoff.

## [0.1.0] - 2026-05-26

### Added
- First version of agent steering files.
