---
name: architecture-boundaries
description: Enforces architectural boundaries between API, schemas, services, providers, and storage layers, and specifies the dependency direction.
activation: Always On
---

# Rule: Architecture Boundaries

## Backend boundaries

The backend must keep these layers separate:

- API routes: HTTP concerns only
- schemas: request and response contracts
- services: core business logic and workflows
- providers: external service clients, cloud storage integrations, database adapters
- storage: database connections and repositories
- observability: logging, tracing, metrics

## Dependency direction

Allowed:

- API calls services/use cases
- services call storage, providers, other services
- providers wrap external services

Avoid:

- API routes directly querying the database without service abstraction
- external client objects leaking into API schemas
- bypassing core business logic/validation filters
- hardcoding environment-specific settings in business logic
- frontend depending on internal backend database shapes

## Provider abstraction rule

Any replaceable external dependency must sit behind a project interface:

- primary database
- cloud storage
- auth identity adapter
- external APIs / third-party services
- telemetry exporter

Interface definitions must not make future replacement impossible.
