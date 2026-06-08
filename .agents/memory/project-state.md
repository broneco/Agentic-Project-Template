# Project State Memory

Last updated: 2026-05-26

## Product summary

[AGENT PROMPT: Proactively ask the user for a summary of the application to be built. Once provided, update this file.]

Generic application summary placeholder. Describe the application purpose, target users, and core value proposition here.

## Current phase

Phase 0: Technical spike / Initialization.

Primary goal: [Define the primary goal of Phase 0, e.g., prove the minimal core flow or skeleton setup].

## Current recommended slice

[AGENT PROMPT: Proactively ask the user what the first slice should focus on, or suggest one based on the application summary.]

Build the smallest backend skeleton that can later support:

1. health endpoint
2. typed configuration
3. core service interfaces
4. local test harness

Do not deploy cloud resources until the first local skeleton and configuration contracts exist.

## Target roadmap

[AGENT PROMPT: Help the user design a multi-phase roadmap for their specific application. Use the template below as a starting point.]

1. Phase 0: Technical spike / Initialization
   - Core skeleton / framework setup
   - Minimal database connectivity proof
   - Simple end-to-end flow validation (e.g., API-only demo)
   - Typed configuration contract

2. Phase 1: Core functionality
   - Integration of primary data store / storage
   - Implementation of core services and logic
   - Standard API endpoints
   - Basic automated tests / verification suite

3. Phase 2: Integration and productization
   - Identity, Authentication & Authorization setup
   - Front-end integration
   - Core workflow implementation
   - Initial telemetry and monitoring

4. Phase 3: Enterprise hardening & scaling
   - Fine-grained access control
   - Robust observability and alerting
   - Performance optimization & caching
   - Administrative portals / dashboards

## Active architectural constraints

[AGENT PROMPT: Ask the user to define their strategic platform, programming language, database, and library constraints. Update this section accordingly.]

- Cloud provider strategy (e.g., Azure-first, multi-cloud, etc.)
- Primary programming language and framework
- Database strategy (SQL, NoSQL, Vector DB)
- External provider abstractions (interfaces for all key external dependencies)
- Code separation (ensure core business logic does not leak vendor-specific details)

## Current known blockers

[AGENT PROMPT: Proactively ask the user if there are any immediate blockers or unknown requirements before starting the first phase.]

- Application specifications and requirements are yet to be defined by the user.
- Target cloud environment details are not finalized.
- Tech stack choices need verification.

## Next slice recommendation

Define application scope, technical constraints, and create the initial repository skeleton.
