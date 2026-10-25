# Code Review Checklist

Run this on yourself before marking any project milestone complete.

## General
- [ ] Code runs from a fresh clone (README has the exact steps)
- [ ] No secrets in code or git history (`.env` is gitignored)
- [ ] Commit history is clean and tells a story

## Frontend
- [ ] Works at 375px (mobile) and desktop widths
- [ ] Keyboard navigation works; focus states are visible
- [ ] Images have alt text; forms have labels
- [ ] Loading, empty, and error states exist for every async action

## Electron-specific
Per the [official security checklist](https://www.electronjs.org/docs/latest/tutorial/security):
- [ ] Context isolation on (default since Electron 12); not disabled
- [ ] Renderer sandbox on (default since Electron 20)
- [ ] `nodeIntegration` disabled in renderers (default since Electron 5)
- [ ] Remote content loaded over HTTPS only; no mixed content (`allowRunningInsecureContent` stays off)
- [ ] A Content Security Policy is defined (HTTP header, or `<meta>` for `file://` pages)
- [ ] Preload exposes a minimal API via `contextBridge` — nothing broad like `require`
- [ ] Permission requests handled with `session.setPermissionRequestHandler`
- [ ] `webSecurity` not disabled; no `experimentalFeatures` or `enableBlinkFeatures`
- [ ] IPC channels are named and validated: validate the sender (`event.senderFrame`) and sanitize arguments; never pass unvalidated data to shell, Node, or file APIs
- [ ] Navigation limited: a `will-navigate` handler blocks or allow-lists destinations (compare URL origins with a real URL parser, not `startsWith`)
- [ ] New-window creation limited via `setWindowOpenHandler` / `webContents` handlers; `<webview>` creation verified in `will-attach-webview`, no `allowpopups`

Note on architecture: plain `fetch` from the renderer is fine — it is a browser API, not Node integration. Routing network calls through the main process is a design choice (e.g., to keep auth tokens out of the renderer), not a security requirement.

## Backend
- [ ] Input validation on every route
- [ ] Errors return proper status codes, never stack traces
- [ ] SQL queries parameterized (no string concatenation)
- [ ] N+1 queries checked

## Tests
- [ ] Unit tests for core logic; E2E for one critical path
- [ ] CI runs tests on every push
