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
- Generalized all agent operating instructions, memory, rules, and workflows to remove specific references to the "AI Search Application", replacing them with a generic application scope and proactive initialization prompts for the agent.
- Deleted search-specific design decision file `docs/adr/ADR-0001-use-postgresql-pgvector-for-mvp.md` and duplicate/obsolete template `docs/adr/ADR-0002-template.md`.
- Updated ADR numbering process in `.agents/workflows/write-adr.md` and `.agents/templates/adr-template.md` to track the next ADR number within the template and require incrementing it upon writing a new ADR.
- Added a mandatory rule and workflow step requiring the creation/updating of markdown explanation files under `docs/test_explained/` for every new or modified test file, including a dedicated template at `.agents/templates/test-explanation-template.md` and an example file at `docs/test_explained/test_health.md`.
- Added a mandatory rule and workflow step requiring the creation/updating of conceptual design guides under `docs/design/` for complex features or conceptual changes, including a template at `.agents/templates/design-guide-template.md` and an example guide at `docs/design/hybrid-search-rrf-guide.md`.
- Explicitly documented the "Local/Contained First" principle in `.agents/AGENTS.md` and `.agents/rules/azure-deployment-handshake.md`, directing the agent to always prioritize self-contained local solutions and request cloud/Azure resources only when strictly necessary or when they significantly simplify the system.
- Replaced hardcoded absolute path references in `.agents/rules/security-and-secrets.md` with `<ABSOLUTE_PATH_TO_PROJECT_ROOT>` placeholders.
- Created `initial_setup.md` in the root workspace to automate initial configuration for the agent upon first environment startup, including steps to inspect `docs/design/`, replace placeholders in security rules, configure application roadmap/memory, and self-delete the setup file.
- Created root `README.md` to guide the user on template initialization, git history resets, and specification placement.
- Updated root `AGENTS.md` to list `initial_setup.md` as the very first file the agent must read and execute.
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
