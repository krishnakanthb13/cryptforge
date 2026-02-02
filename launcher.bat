@echo off
setlocal
title CryptForge Launcher

:: -----------------------------------------------------------------------------
:: CryptForge Launcher for Windows
:: Checks environment and launches the tool.
:: -----------------------------------------------------------------------------

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in your PATH.
    echo Please install Python 3.x from https://python.org
    pause
    exit /b 1
)

:: 2. Check for Requirements
:: We check for 'cryptography' as a sentinel package.
pip show cryptography >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Dependencies not found. Installing from requirements.txt...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
    echo [SUCCESS] Dependencies installed.
)

:: 3. Launch Application
if "%1"=="" (
    python main.py menu
) else (
    echo [INFO] Starting CryptForge with arguments...
    python main.py %*
)
goto END

:END
echo.
pause
exit /b 0

endlocal
