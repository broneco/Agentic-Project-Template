---
name: security-and-secrets
description: Security principles prohibiting committing secrets/credentials, enforcing pre-LLM ACL filtering, auditing log constraints, and defining hard command execution and file write guardrails.
activation: Always On
---

# Rule: Security and Secrets

## Core rule

The LLM must never receive or persist data the user is not authorized to see.

## Secrets

Never commit or write these into tracked files:

- API keys
- Azure OpenAI keys
- connection strings
- client secrets
- access tokens
- refresh tokens
- private certificates
- production `.env` values

Use placeholders such as:

```text
AZURE_OPENAI_ENDPOINT=<provided by environment>
AZURE_OPENAI_API_KEY=<stored in Key Vault or local untracked env>
```

## Azure secrets

Prefer:

1. managed identity
2. Key Vault references
3. local untracked `.env` for development only

## Retrieval ACL rule

ACL filtering must happen before context packing and before any content is sent to an LLM.

This applies to:

- flash mode
- thinking mode
- follow-up retrieval
- reranking if it sends content to a model
- debug endpoints

## Audit logs

Audit logs must be useful but minimized.

Avoid storing full sensitive prompts or private document content unless explicitly required and approved. Prefer IDs, hashes, metadata, and redacted snippets.

## Security Guardrails

These lists define the security guardrails that the Antigravity IDE automatically enforces when executing actions in this repository.

### Formatting rule (MANDATORY FOR THE AGENT):
Whenever the assistant (AI) proposes, modifies, or writes new security rules for commands, folders, or files, it **must** write them into the lists below (Deny list, Allow list, Ask list) exclusively in the `action(target)` format (e.g., `command(prefix)`, `write_file(absolute_path)`, `read_file(absolute_path)`), so that the Antigravity IDE can correctly parse and enforce them at the security core level.

Deny list:
- command(rm)
- command(Remove-Item)
- command(del)
- command(rd)
- write_file(<ABSOLUTE_PATH_TO_PROJECT_ROOT>/.env)

Allow list:
- command(pytest)
- command(python)
- read_file(<ABSOLUTE_PATH_TO_PROJECT_ROOT>)
- write_file(<ABSOLUTE_PATH_TO_PROJECT_ROOT>)

Ask list:
- mcp(*)
- command(pip install)
