# 04 : Security Audit and Packaging

Audit against the Electron security checklist: context isolation on, sandbox on, no Node integration in renderers, HTTPS-only remote content, CSP defined, permission handler set (see [docs/code-review.md](../../../docs/code-review.md)). Then package with Electron Forge: from inside your existing app's directory, run `npx create-electron-app@latest import` to add Forge (it creates the `start`, `package`, and `make` scripts plus a `forge.config.js`), then `npm run package` and `npm run make` to produce a Windows installer.

## Focus topics
- security checklist
- Forge: npx create-electron-app, npm run make
- code signing basics

## My solution

- `solution/` (your code)

## What I learned

- 
