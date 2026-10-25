# Student Planning Hub

A planner for students: courses, assignments, deadlines, and study sessions. This project grows across the whole bootcamp and becomes the flagship Electron desktop app (cross-platform by nature; you will build and test a Windows installer, with other targets optional).

## Phases
- **Week 8:** Vanilla JS version — tasks with localStorage persistence (`vanilla/`).
- **Week 10:** Rebuilt in React + TypeScript.
- **Weeks 11–12:** Wrapped in **Electron** — IPC bridge through a preload script, security review, local packaged Windows build with Electron Forge. Native menus, dialogs, notifications, tray, and code signing are stretch work.
- **Week 16:** Backed by an Express + PostgreSQL API.
- **Weeks 18–20:** E2E tested, deployed API, CI pipeline, repeatable local installer build (signing optional).

## Stack
React, TypeScript, Electron, Express, PostgreSQL.

## Electron architecture
- Main process: window management, native menus, dialogs, tray, notifications.
- Preload script: narrow `contextBridge` API (`window.hubAPI.*`), context isolation on, sandbox on.
- Renderer: the React app; no Node APIs, talks to main process only via IPC.
- Network calls go through the main process or the API server — never Node-in-renderer.

## Definition of Done
- Add/complete/delete tasks and courses; deadlines (system notifications are stretch work)
- Data persists through the API (offline sync is out of scope — a good capstone extension)
- Packaged installer builds with `electron-forge make`
- Security checklist from the Electron docs reviewed
- E2E test for the critical path
