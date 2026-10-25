# Electron Exercises

Four exercises that take you from a first window to a packaged, secure app. The core path for Weeks 11–12 is ex-01, ex-02, and ex-04; ex-03 (native features) is stretch work. Official tutorial: [Building your First App](https://www.electronjs.org/docs/latest/tutorial/tutorial-first-app) and [Using Preload Scripts](https://www.electronjs.org/docs/latest/tutorial/tutorial-preload).

## ex-01-window-and-lifecycle
Create a minimal app: main process creates a `BrowserWindow`, loads a local `index.html`, and quits correctly when all windows are closed (macOS dock behavior included).

## ex-02-preload-and-ipc
Expose a `window.api.setTitle(title)` function through a preload script with `contextBridge`; the renderer calls it, the main process listens with `ipcMain.on` and updates the window title. Then convert it to the preferred two-way pattern: `ipcRenderer.invoke` + `ipcMain.handle`.

## ex-03-native-features (stretch)
Add an application menu with a File → Open entry that uses `dialog.showOpenDialog`, show a system notification when a deadline is near, and minimize to tray.

## ex-04-security-audit-and-package
Audit your app against the [Electron security checklist](https://www.electronjs.org/docs/latest/tutorial/security) (context isolation, sandbox, no Node integration in renderers, HTTPS-only remote content, CSP, permission handler). Then package it with Electron Forge: scaffold with `npx create-electron-app@latest my-app`, run with `npm start`, and produce a Windows installer with `npm run make` (Forge getting-started: [electronforge.io](https://www.electronforge.io/)).

## Rules
- Every exercise gets its own folder with a `README.md` (task, what you learned, gotchas).
- Never disable security flags to "make it work" — find the secure pattern instead.
