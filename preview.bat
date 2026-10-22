@echo off
rem Double-click this file to preview the website at http://localhost:8000
cd /d "%~dp0"
python preview.py %*
if errorlevel 9009 py preview.py %*
pause
