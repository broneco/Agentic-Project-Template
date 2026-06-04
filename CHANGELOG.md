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

### Changed
- Nothing yet.

### Fixed
- Nothing yet.

### Security
- Added rule that secrets must never be committed and must be provided through Azure Key Vault, environment variables, or explicit human handoff.

## [0.1.0] - 2026-05-26

### Added
- First version of agent steering files.
