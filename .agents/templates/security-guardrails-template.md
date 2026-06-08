# Template: Security Guardrails

This file defines the template for security guardrails for a specific project. Copy this content to your rule file under `.agents/rules/` (e.g. `security-and-secrets.md`) and adjust the paths and allowed/denied commands.

```markdown
Deny list:
- command(rm)
- command(Remove-Item)
- command(del)
- command(rd)
- write_file(<path_to_project>/.env)

Allow list:
- read_file(<path_to_project>)
- write_file(<path_to_project>/data)
- command(pytest)
- command(python)

Ask list:
- mcp(*)
- command(pip install)
```
