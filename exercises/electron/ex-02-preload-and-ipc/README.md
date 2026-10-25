# 02 : Preload and IPC

Expose window.api.setTitle(title) through contextBridge in a preload script. Renderer calls it; main listens with ipcMain.on. Then convert to the preferred two-way pattern: ipcRenderer.invoke + ipcMain.handle.

## Focus topics
- contextBridge.exposeInMainWorld
- ipcRenderer.send vs invoke
- ipcMain.on vs handle

## My solution

- `solution/` (your code)

## What I learned

- 
