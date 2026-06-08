# Agentic Project Template

Tento repozitář slouží jako šablona pro zahájení vývoje full-stack aplikací za pomoci autonomních AI agentů (např. Antigravity, Codex nebo Claude Code). Šablona obsahuje procesní pravidla, další šablony a paměťové mechanismy pro iterativní vývoj.

---

## 🚀 Jak začít nový projekt

Pro správnou inicializaci nového projektu ze šablony postupujte podle následujících kroků:

### 1. Inicializace čistého Gitu
Projekt by měl začínat bez historie commitů šablony. Smažte stávající historii a vytvořte čistý repozitář:
```bash
# 1. Smažte starou git historii
Remove-Item -Recurse -Force .git

# 2. Inicializujte nový git
git init

# 3. Přejmenujte hlavní větev na 'main' (Git defaultně stále občas vytváří 'master')
git branch -M main

# 4. Přidejte soubory a vytvořte první commit
git add .
git commit -m "initial commit: project initialized from agentic template"
```

### 2. Vložení zadání a specifikace
Veškeré podklady k novému projektu (požadavky, popisy funkcí, wireframy, datové struktury či koncepty architektury) vložte do složky:
📁 `docs/design/`

*Poznámka: Čím detailnější podklady sem vložíte, tím přesněji se agent zkonfiguruje.*

### 3. Spuštění AI Agenta
Spusťte agenta v tomto workspace. Agent má přednastaveno okamžitě detekovat soubor `initial_setup.md`, ze kterého si načte instrukce pro automatickou konfiguraci:
- Projde dokumenty v `docs/design/`.
- Přepíše absolutní cesty v pravidlech bezpečnosti na cesty vašeho lokálního stroje.
- Vyplní profil aplikace, tech stack a cíle do souborů `.agents/AGENTS.md` a `.agents/memory/project-state.md`.
- **Smaže soubor `initial_setup.md`**, čímž potvrdí dokončení setupu.
- Navrhne vám první konkrétní krok (slice) k implementaci.

---

## 📁 Důležité složky v šabloně

- **📁 `.agents/`**: Srdce šablony. Obsahuje pravidla bezpečnosti a kvality kódu (`rules/`), checklisty pro agenty (`workflows/`), šablony dokumentů (`templates/`) a paměť (`memory/`).
- **📁 `docs/`**: Složka s trvalou dokumentací.
  - `docs/design/` – Místo pro vaše vstupní materiály.
  - `docs/adr/` – Rozhodnutí o architektuře (Architectural Decision Records).
  - `docs/test_explained/` – Lidsky čitelná vysvětlení všech napsaných testů.
