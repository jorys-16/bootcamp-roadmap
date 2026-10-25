# Month 3: React, TypeScript, and Electron (Weeks 9–12)

**Goal:** Learn TypeScript and React, then use Electron to build a cross-platform desktop app — the Student Planning Hub. You will build and test a Windows installer on your machine; macOS and Linux targets are stretch goals.

## Week 9 — TypeScript + npm Tooling
- Tooling you need before React and Electron: `npm init`, `package.json`, npm scripts, dependencies vs devDependencies, ESM modules.
- Types, interfaces, generics, narrowing; typing functions and data.
- Convert a small JS exercise to TypeScript.

## Week 10 — React
- Components, props, state, hooks (`useState`, `useEffect`).
- Lists and keys, conditional rendering, simple forms.
- Rebuild the Student Planning Hub UI in React + TypeScript.

## Week 11 — Electron Fundamentals
- What Electron is: Chromium + Node.js in one runtime; when to choose it vs. native (you already compared it with WinUI 3 — Electron trades binary size and memory for web-tech reuse and speed of development).
- The process model: one **main process** (Node.js, window and lifecycle management), **renderer processes** (web content), **preload scripts** (run before renderer content, bridge via `contextBridge`), and **utility processes** for heavy or crash-prone work.
- Follow the official tutorial's [Building your First App](https://www.electronjs.org/docs/latest/tutorial/tutorial-first-app): `npm init`, install Electron as a devDependency, `main.js` creates a `BrowserWindow`, `preload.js` exposes a narrow API, renderer is plain HTML/CSS/JS.
- Wrap the React Student Planning Hub in Electron.

## Week 12 — IPC, Security, and a First Build
- IPC patterns: renderer-to-main one-way (`ipcRenderer.send` / `ipcMain.on`), two-way with `ipcRenderer.invoke` / `ipcMain.handle` (preferred), and main-to-renderer (`webContents.send`).
- **Required milestone:** a working IPC bridge through a preload script, a security review, and a local packaged build.
- Stretch work if time allows: native menus, file dialogs (`dialog.showOpenDialog`), system notifications, tray icons, and your first Electron E2E test.
- Security by default: context isolation (default since Electron 12), renderer sandboxing (default since Electron 20), no Node integration in renderers (default since 5), load only HTTPS remote content, handle permission requests with `session.setPermissionRequestHandler`, and set a Content Security Policy.
- Package locally with **Electron Forge** (the officially recommended tool). To bring the app you built in Week 11 under Forge, run `npx create-electron-app@latest import` from your project directory — it installs Forge's CLI and adds the `start`, `package`, and `make` scripts plus a `forge.config.js`. Then `npm run package` and `npm run make` produce a local Windows build and installer. (For a brand-new project you would instead scaffold with `npx create-electron-app@latest my-app` and `cd my-app`.) Code signing is explained but optional at this stage — treat it as a stretch milestone.

## Deliverables
- Student Planning Hub desktop app (React + TypeScript + Electron).
- Working IPC bridge and a local packaged Windows build (Forge). Code signing and cross-platform targets are stretch goals.
- Security checklist review in [docs/code-review.md](../docs/code-review.md).

> Workload note: weeks can repeat. If Week 12 overflows, push native features and E2E testing into Week 17-18 and keep going — the roadmap bends, the streak matters.

## Exercises
- [Electron exercise set](../exercises/electron/README.md)

## Resources
- [Electron tutorial: Building your First App](https://www.electronjs.org/docs/latest/tutorial/tutorial-first-app)
- [Electron docs: Process model](https://www.electronjs.org/docs/latest/tutorial/process-model)
- [Electron docs: IPC](https://www.electronjs.org/docs/latest/tutorial/ipc)
- [Electron docs: Security](https://www.electronjs.org/docs/latest/tutorial/security)
- [Electron docs: Automated testing](https://www.electronjs.org/docs/latest/tutorial/automated-testing)
- [Electron docs: Distributing with Forge](https://www.electronjs.org/docs/latest/tutorial/forge-overview)
- [React docs](https://react.dev/learn)
- [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
