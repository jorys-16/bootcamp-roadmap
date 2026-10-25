# Architecture

Diagrams and overviews of the systems you build. Keep this current as projects evolve.

## Student Planning Hub (final form)

```
┌─────────────────────────── Electron App ───────────────────────────┐
│  Main process (Node.js)                        Renderer (React)   │
│  - BrowserWindow, menus, tray                    - UI components   │
│  - dialog, notifications                        - state (hooks)   │
│  - IPC handlers (ipcMain.handle)                    ▲              │
│        ▲ ipcRenderer.invoke / contextBridge ────────┘              │
│        Preload script (narrow window.hubAPI surface)               │
└──────────────────────────────────┬────────────────────────────────┘
                                   │ HTTPS (fetch)
                        ┌──────────▼──────────┐
                        │  Express REST API   │
                        └──────────┬──────────┘
                                   │ SQL
                        ┌──────────▼──────────┐
                        │     PostgreSQL       │
                        └─────────────────────┘
```

## Key rules
- Renderers have no direct Node access; everything goes through the preload bridge (context isolation + sandbox are on by default in modern Electron).
- The API is stateless; the database is the only source of truth.
- The web Campus Resource Guide is static and separate.

## Update triggers
- Week 12: first desktop architecture
- Week 16: add API + database layers
- Week 20: deployment topology
