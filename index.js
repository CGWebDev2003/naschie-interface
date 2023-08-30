'use strict';

const { app, BrowserWindow } = require('electron')
const electronReload = require('electron-reload')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        autoHideMenuBar: true,
        icon: __dirname + '/assets/icon.png',
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })
  
    win.loadFile('index.html')
    win.webContents.openDevTools()
  }

  app.whenReady().then(() => {
    createWindow()
  
    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
  })

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
  })