@echo off

taskkill /im pythonw.exe /f >nul
pythonw main.pyw
exit