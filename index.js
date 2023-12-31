'use strict';

const { app, BrowserWindow } = require('electron')
const electronReload = require('electron-reload')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1200,
        height: 900,
        autoHideMenuBar: true,
        icon: __dirname + '/assets/icon.png',
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })
  
    win.loadFile('index.html')

    // ANCHOR Turn On/Off DevTools
    // win.webContents.openDevTools()
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