---
name: testing-policy
description: Testing requirements for backend logic, repository queries, retrieval pipelines, LLM prompts/evals, and actions to take when tests cannot run.
activation: Always On
---

# Rule: Testing Policy

## Required principle

Every behavior change needs verification.

## Backend tests

Prefer these test layers:

- unit tests for pure logic
- repository tests for database access when schema exists
- integration tests for API endpoints
- retrieval evals (if search/retrieval is used)
- agent evals (if LLM/prompts are used)

## Retrieval-specific tests (when applicable)

When changing retrieval or search capabilities, test at least one of:

- query mapping or enrichment
- query/request construction
- ranking or fusion behavior
- access control / security filtering
- citation/source preservation

## Agent and LLM tests / evals (when applicable)

When changing prompts, model routing, or orchestrations, add or update eval cases that check:

- groundedness / factual correctness
- source citation presence
- correct mode/profile selection
- safe handling when inputs or evidence are insufficient

## Test Explanations (Mandatory)

For every test file created or modified (e.g., `tests/test_foo.py` or similar), you MUST create or update a corresponding markdown explanation file in `docs/test_explained/test_foo.md` to explain what the test does in plain human language.

Naming convention:
`docs/test_explained/test_<name>.md` explaining `tests/test_<name>.py` (or the equivalent test file).

Format requirements:
- Title: `# Test Explanation: `test_<name>.py``
- A summary paragraph describing what the test suite verifies in plain language.
- A `## Individual Tests` section listing each test case with:
  - **High-Level Purpose**: The business logic, capability, or user-facing flow being verified.
  - **Low-Level Technical Details**: Details on libraries, endpoints, inputs, mocked dependencies, and specific assertions.

## If tests cannot run

State exactly:

- which command should be run
- why it could not be run
- what risk remains
- what the next human or agent should verify
