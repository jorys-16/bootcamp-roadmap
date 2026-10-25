# Setup Instructions

This bootcamp assumes a Windows 11 machine (your current setup), but everything works on macOS or Linux too.

## Tools to Install

1. **Git** — [git-scm.com/downloads](https://git-scm.com/downloads). Verify: `git --version`
2. **VS Code** — [code.visualstudio.com](https://code.visualstudio.com/). Install the extensions: ESLint, Prettier, GitLens, Live Server.
3. **Node.js LTS** — [nodejs.org](https://nodejs.org/). Prefer the LTS release. Verify:
   ```
   node --version
   npm --version
   ```
4. **PostgreSQL** — [postgresql.org/download](https://www.postgresql.org/download/) (install in Month 4; a managed DB like Neon or Supabase also works).
5. **Python 3.12+** — [python.org](https://www.python.org/) (needed in Month 6). Verify: `python --version`

## Repository Workflow

- Clone this repository and work in feature branches: `git switch -c week-05-dom`.
- Commit at least once per study session with clear messages.
- Push to GitHub after every completed exercise.

## Conventions

- `notes/` — one file per topic, written in your own words.
- `progress/week-XX.md` — fill in each week; update [PROGRESS.md](PROGRESS.md) checkboxes as you finish.
- `exercises/<topic>/` — numbered exercise folders with a short `README.md` and your solution.
- `docs/decisions.md` — record any meaningful technical decision and why.

## Weekly Routine (repeat 28 times)

1. Pick one objective from the current month's curriculum.
2. Study the material.
3. Build and test something small.
4. Record what you learned in `notes/` and `progress/`.
5. Update the [PROGRESS.md](PROGRESS.md) checklist.
