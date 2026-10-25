# Month 5: Testing and Deployment (Weeks 17–20)

**Goal:** Make your work reliable: unit tests, end-to-end tests (including for the Electron app), CI, and real deployment of both the web service and the desktop installer.

## Week 17 — Unit and Integration Testing
- Test pyramid; Vitest or Jest for the API; supertest for endpoints.
- Write tests for the Student Planning Hub API routes and React components.

## Week 18 — End-to-End Testing
- Playwright for the web app; Playwright's `_electron.launch` or WebdriverIO's Electron service for the desktop app.
- Cover one critical user journey: add task → complete task → reload → verify it persisted.

## Week 19 — CI with GitHub Actions
- Run tests on every push; lint and type-check in CI.
- Branch protection and meaningful commit history.

## Week 20 — Deployment
- Deploy the API (Render, Fly.io, or Railway) and the database (managed Postgres).
- Desktop distribution: build installers locally with `electron-forge make`; understand code signing and why it matters for auto-updates (signing itself is an optional, separately configured milestone).
- Write a release checklist in [docs/demo-checklist.md](../docs/demo-checklist.md).

## Deliverables
- CI pipeline green on GitHub Actions.
- Deployed API + database; packaged desktop installer.

## Resources
- [Playwright docs](https://playwright.dev/docs/intro)
- [Vitest docs](https://vitest.dev/)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [Electron docs: Automated testing](https://www.electronjs.org/docs/latest/tutorial/automated-testing)
- [Electron Forge: Publishing and updates](https://www.electronforge.io/)
