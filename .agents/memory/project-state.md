# Project State Memory

Last updated: 2026-05-26

## Product summary

Full-stack AI Search Application for company knowledge and documents.

The system should provide a web UI and backend API for hybrid search over documents, combining vector similarity, full-text search, metadata filters, freshness validation, ACL filtering, and LLM-generated answers with citations.

## Current phase

Phase 0: Technical spike.

Primary goal: prove the minimal RAG flow without overbuilding the whole target architecture.

## Current recommended slice

Build the smallest backend skeleton that can later support:

1. health endpoint
2. typed configuration
3. provider interfaces for LLM, embeddings, and retrieval
4. local test harness

Do not deploy Azure resources until the first local skeleton and configuration contracts exist.

## Target roadmap

1. Phase 0: Technical spike
   - FastAPI skeleton
   - PostgreSQL/pgvector proof
   - one document embedded
   - vector query
   - simple model answer
   - minimal web UI or API-only demo

2. Phase 1: Ingestion and retrieval
   - Blob Storage integration
   - document extraction
   - chunking
   - embeddings
   - PostgreSQL full-text search
   - hybrid ranking
   - metadata filtering
   - eval dataset

3. Phase 2: Agent and productization
   - flash agent
   - thinking agent
   - source citations
   - freshness validation
   - feedback
   - audit
   - frontend
   - Entra ID auth

4. Phase 3: Enterprise hardening
   - ACL filtering
   - production monitoring
   - rate limiting
   - cost tracking
   - ingestion worker scaling
   - reindexing
   - admin endpoints
   - security review

5. Phase 4: Channel expansion
   - Teams interface
   - Outlook interface
   - API for internal systems
   - optional specialized search backend

## Active architectural constraints

- Azure-first.
- Microsoft Azure is the only accepted strategic vendor lock-in.
- Backend primary language: Python 3.11+.
- Backend framework: FastAPI.
- MVP data/search layer: Azure Database for PostgreSQL Flexible Server + pgvector + PostgreSQL full-text search.
- Azure AI Search is not part of MVP.
- Chroma may be used only for local experiments, not production.
- LangChain/LangGraph may be used inside orchestration/providers but must not leak through the whole domain model.
- LLM provider, embedding provider, and search backend must be replaceable through project interfaces.
- Model deployment names must be configuration, not code.

## Current known blockers

- First document sources are not yet chosen.
- Expected document/chunk volume is unknown.
- ACL mapping from source systems is not yet designed.
- Exact Azure model deployments are not known.
- Pilot environment is not chosen.

## Next slice recommendation

Create repository skeleton and backend configuration contract before creating Azure resources.
