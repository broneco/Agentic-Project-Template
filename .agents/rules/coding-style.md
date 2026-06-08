---
name: coding-style
description: General coding style, Python backend conventions (FastAPI, Pydantic), error handling, configuration rules, and frontend TypeScript standards.
activation: Always On
---

# Rule: Coding Style

## General Principles & Standards

- **DRY (Do Not Repeat Yourself)**: Strictly eliminate code redundancy. Code must be modular and easy to maintain. Repetitive logic belongs in shared utilities or components.
- **Best Practices**: Adhere to modern standards of the language and ecosystem (e.g., Python 3.11+, TypeScript, ES6+, FastAPI). Write clean, secure, and performant code that is readable by both humans and machines.
- **Modularity & Cohesion**: Keep modules small and cohesive (small, single-purpose, and cohesive modules). Prefer clear, straightforward (even boring) code over complex and "clever" constructs (`Prefer clear, boring code over clever code`).
- **Domain Explicit naming**: Use explicit names for domain concepts, e.g., `Document`, `Chunk`, `QueryAuditLog`, `ModelProfile`, `RetrievalResult`.
- **Abstraction**: Avoid premature abstractions (`Avoid premature abstractions`), but always preserve clearly defined provider and integration boundaries (`provider boundaries`) based on design.
- **Unit Testing First**: Designing unit tests is an integral part of the planning phase. Tests must verify the application's functionality (resulting effect), not the specific technological approach or implementation details.

## Python backend

- Target Python 3.11+.
- Use FastAPI for HTTP API.
- Use Pydantic models for request/response and configuration contracts.
- Use type hints for all public functions.
- Keep route handlers thin.
- Do not place business logic in FastAPI route functions.
- Use dependency injection for config, database sessions, and providers.
- Prefer async only where the stack is consistently async.

## Errors

- Use explicit domain exceptions for expected failures.
- Do not leak provider-specific errors directly to API responses.
- Include correlation IDs in logs where possible.

## Configuration

- No hardcoded model names, endpoints, tenant IDs, client IDs, connection strings, or secrets.
- Use environment variables and typed settings.
- Secret values belong in Azure Key Vault or local untracked `.env` files.

## Frontend

- Use TypeScript.
- Keep API clients typed.
- Do not duplicate backend business rules in UI.
- UI should display source citations and freshness status when returned by the backend.
