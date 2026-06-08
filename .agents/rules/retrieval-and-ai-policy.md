---
name: retrieval-and-ai-policy
description: Design rules for AI/LLM integration, external services, and data retrieval policies when applicable.
activation: Always On
---

# Rule: Retrieval and AI Policy

[AGENT PROMPT: If the application uses AI/LLM components, use this policy as a guideline. If not, this policy can be archived, removed, or ignored. Update this file as the project's AI/retrieval requirements are defined by the user.]

## Retrieval pipeline target (when applicable)

Build toward this pipeline:

```text
user query
  -> normalize query
  -> detect language
  -> enrich with knowledge base (optional)
  -> extract metadata/search constraints
  -> database/vector search
  -> ACL/security filtering
  -> metadata filtering
  -> ranking / fusion
  -> freshness validation (if relevant)
  -> context packing
  -> LLM answer with citations / references
```

## Evidence rule (when applicable)

LLM answers must be grounded in retrieved evidence unless a task explicitly asks for brainstorming or implementation help.

For product chat/search answers:

- include source citations when evidence is used
- distinguish current vs stale sources
- say when evidence is insufficient
- do not use data chunks failing ACL filters

## Agent modes (when applicable)

`flash` mode:

- fast, cheaper, fewer steps
- use for simple factual lookup and short summaries

`thinking` mode:

- multi-step reasoning
- can run follow-up retrieval/queries
- must detect conflicts and missing evidence

## Model profiles (when applicable)

Never hardcode model deployment names.

Use model profiles:

- `flash`
- `thinking`
- `embedding`

Deployment names must come from environment/config/admin settings.
