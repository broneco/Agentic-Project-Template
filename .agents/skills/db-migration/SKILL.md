---
name: db-migration
description: Guide and tools for creating and running database migrations in PostgreSQL using Alembic. Use this when you modify database schemas or need to run migrations.
---

# Database Migration Skill

Follow this guide when creating, running, or verifying database migrations in this project.

## Workflow

1. **Create migration script**:
   Use the helper script under `scripts/create_migration.py` or run Alembic:
   ```bash
   alembic revision --autogenerate -m "description"
   ```
2. **Review migration script**:
   Verify that the generated migration file (under `alembic/versions/`) correctly handles schema changes and vector indices (pgvector) if relevant.
3. **Apply migration**:
   Run the migration locally using:
   ```bash
   alembic upgrade head
   ```

## Verification

- Verify the database schema matches the expected model state.
- Run tests to check database connectivity and model operations.
