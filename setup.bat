@echo off
REM Text-to-Speech Application Setup Script for Windows
REM This script sets up both backend and frontend dependencies

echo ========================================
echo Text-to-Speech Application Setup
echo ========================================
echo.

REM Check Python installation
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)
echo Python is installed
echo.

REM Check Node.js installation
echo [2/6] Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
echo Node.js is installed
echo.

REM Create virtual environment
echo [3/6] Creating Python virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Install Python dependencies
echo [4/6] Installing Python backend dependencies...
echo This may take several minutes as it downloads ML models...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r backend_requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)
echo Backend dependencies installed successfully
echo.

REM Install Node.js dependencies
echo [5/6] Installing Node.js frontend dependencies...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install Node.js dependencies
    pause
    exit /b 1
)
echo Frontend dependencies installed successfully
echo.

REM Create audio output directory
echo [6/6] Creating directories...
if not exist generated_audio (
    mkdir generated_audio
    echo. > generated_audio\.gitkeep
    echo Created generated_audio directory
)
echo.

echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To start the application:
echo.
echo 1. Start the backend (in Terminal 1):
echo    venv\Scripts\activate
echo    python app.py
echo.
echo 2. Start the frontend (in Terminal 2):
echo    npm start
echo.
echo 3. Open your browser to http://localhost:3000
echo.
echo ========================================
pause
