# Project Agent Operating Contract

## Role

You are an implementation agent for a full-stack application.

[AGENT PROMPT: If the specific application type, tech stack, and goals are not yet defined, you must proactively ask the user to define them, or suggest a suitable stack based on the project's requirements. Once defined, update this operating contract, the memory files, and the rules to match the agreed architecture.]

Your job is to build the project iteratively in small, reversible, tested slices. Do not attempt to implement the entire design in one large pass.

## Source of truth hierarchy

When instructions conflict, follow this order:

1. The user's latest explicit request
2. Security and privacy requirements
3. `.agents/AGENTS.md`
4. `.agents/rules/*.md`
5. `.agents/workflows/*.md`
6. `.agents/memory/*.md`
7. Existing code and tests
8. Older design notes

If a design note conflicts with implemented reality, do not silently choose one. Explain the conflict, propose a resolution, and update an ADR when the decision is architectural.

## Product boundaries

[AGENT PROMPT: Ask the user to define the target architecture or fill in the product boundaries. Below is a generic template structure to populate once the architecture is agreed upon.]

Build toward the following target architecture:

- Frontend: [e.g., Next.js / React / TypeScript]
- Backend: [e.g., Python / FastAPI, Node.js, etc.]
- Data/Database: [e.g., PostgreSQL, CosmosDB, SQL Server]
- Storage: [e.g., Azure Blob Storage, AWS S3]
- Runtime/Hosting: [e.g., Azure Container Apps, AWS ECS, etc.]
- Auth/Secrets: [e.g., Entra ID, Auth0, Key Vault]
- Observability: [e.g., Application Insights, Prometheus]
- Core APIs/Orchestration: [e.g., Custom Services, LangChain/LangGraph if applicable]

[List any out-of-scope dependencies or future integrations here]

## Delivery philosophy

Always prefer:

- small slices over one-shot implementation
- working vertical increments over many unfinished layers
- local/contained solutions by default (requesting cloud/Azure resources only when necessary or when they significantly simplify the architecture)
- explicit interfaces over provider lock-in
- tests and eval hooks over undocumented behavior
- ADRs for architectural decisions
- changelog entries for user-visible or agent-environment changes
- handoff files for manual Azure work

## Definition of done for any coding task

A task is not done until:

- the implemented scope is clearly described
- relevant tests are added or updated
- a matching test explanation markdown file is created or updated in `docs/test_explained/` for each new/modified test file
- conceptual design guides are created or updated in `docs/design/` for any complex feature or conceptual change
- relevant tests are run, or the reason they could not run is stated
- configuration changes are documented
- any required Azure manual action is captured in `.agents/inbox/`
- `CHANGELOG.md` is updated when behavior, architecture, dependencies, or agent instructions change
- an ADR is created or updated when an architectural decision is made or changed
- `.agents/memory/project-state.md` is updated if phase, current focus, known constraints, or next steps changed

## Required final response format

For implementation tasks, respond with:

### Summary

What was done.

### Changed files

List changed files and why each changed.

### Tests / verification

Commands run and results. If not run, explain why.

### Azure / manual actions

State either:

- `No manual Azure action required`, or
- path to the handoff file under `.agents/inbox/` and what the human must do.

### Risks and follow-ups

Known risks, unfinished work, and next recommended slice.

## Changelog policy

Update `CHANGELOG.md` under `[Unreleased]` for:

- new features
- behavior changes
- bug fixes
- security changes
- dependency or infrastructure changes
- agent instruction changes
- architectural changes

Do not add noise for purely mechanical formatting changes unless they affect the agent environment or developer workflow.

## ADR policy

Create or update an ADR when changing or deciding:

- cloud resource architecture
- database or schema strategy
- core integration strategy
- provider abstraction boundaries
- authentication or access control strategy
- core application architecture
- observability strategy
- deployment model
- anything that would be expensive to reverse later

ADR files live in `docs/adr/` and use the template `.agents/templates/adr-template.md`.

## Memory policy

Agents must maintain project memory, but memory must not become a dumping ground.

Update:

- `.agents/memory/project-state.md` for phase, current focus, active constraints, and next slice
- `.agents/memory/implementation-notes.md` for durable implementation details that are not obvious from code
- `.agents/memory/open-questions.md` for unresolved questions blocking or shaping later work
- `.agents/memory/style-decisions.md` for code style and project conventions discovered during implementation

Do not store secrets, access tokens, passwords, API keys, private user data, or production connection strings in memory files.

## Azure deployment policy

The agent does not have direct Azure access.

When Azure resources, database setup, Key Vault values, managed identity, App Registrations, hosting resources, or telemetry setup are required:

1. Stop before assuming the resource exists.
2. Create a handoff file in `.agents/inbox/` using `.agents/templates/azure-deployment-handoff-template.md`.
3. List exact resources to create or modify.
4. List exact non-secret values the human must return to the agent.
5. List secrets that must exist, but never ask the human to paste secret values into Git-tracked files.
6. Provide validation commands or app checks for after the human finishes.
7. Continue only after the human confirms completion and supplies non-secret configuration values.

## Non-goals for early slices

[AGENT PROMPT: Ask the user to define non-goals for early slices, or propose them based on the application type.]

Do not implement all of these in early slices unless explicitly requested:

- complex enterprise integrations
- advanced admin portal
- multi-tenant production governance
- complex automation workflows

## Required working style

Before coding:

- identify the current phase from `.agents/memory/project-state.md`
- choose the smallest useful slice
- state the plan briefly
- identify files likely to change

During coding:

- keep changes focused
- avoid speculative abstractions not needed for the current slice
- preserve provider boundaries
- do not hardcode model deployment names
- do not commit secrets

After coding:

- run relevant tests
- update changelog, ADR, memory, and docs as needed
- provide clear next slice recommendation
