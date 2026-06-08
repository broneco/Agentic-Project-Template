# Initial Setup Guide (For AI Agent Execution)

> [!IMPORTANT]
> **AGENTS MUST READ THIS FILE IMMEDIATELY ON INITIALIZATION AND EXECUTE THESE STEPS IN ORDER.**
> Once setup is complete, the agent MUST run a command to delete this file (`initial_setup.md`).

---

## Step 1: Read Project Design Materials
First, inspect the `docs/design/` directory. The user has placed the project requirements, architecture diagrams, and specifications there. Read these files to understand what application is being built.

## Step 2: Configure Workspace Paths in Security Rules
Search for the placeholder `<ABSOLUTE_PATH_TO_PROJECT_ROOT>` in `.agents/rules/security-and-secrets.md` and replace it with the actual absolute path of this project directory (always use forward slashes, e.g., `C:/Users/name/.../Project-Folder`).

## Step 3: Populate Project Architecture & Memory
Based on the design documents found in `docs/design/`, update the following files with concrete details:
1. **`.agents/AGENTS.md`**: Fill in the **Product boundaries** section (Frontend, Backend, Database, Storage, Telemetry, etc.).
2. **`.agents/memory/project-state.md`**: Update the **Product summary**, **Current phase**, **Roadmap**, and **Active architectural constraints**.
3. **`.env.example`**: Customize the environment variables to match the actual tech stack.

It is critical that this is done right, so don't hesitate to ask the user questions or give suggestions so that you have complete information for the future!

## Step 4: Self-Delete
Run a terminal command to delete this setup file immediately so that future agent runs start with a clean slate:
```powershell
Remove-Item -Path "initial_setup.md"
```
Once this file is deleted, commit the initial configuration and report back to the user that setup is complete and the first development slice is ready to be proposed.
