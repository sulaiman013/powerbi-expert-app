@echo off
REM ============================================================
REM Power BI Expert V3 - Quick Launcher
REM ============================================================
REM Double-click this file to launch Power BI Expert
REM Requires Python to be installed
REM ============================================================

title Power BI Expert V3

REM Change to the script's directory
cd /d "%~dp0"

echo.
echo ============================================================
echo   POWER BI EXPERT V3 - LAUNCHING...
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.10+ from https://python.org
    echo.
    pause
    exit /b 1
)

REM Launch the web UI
python web_ui.py

REM If it exits, pause to show any error
if errorlevel 1 (
    echo.
    echo [ERROR] Application exited with an error.
    pause
)
