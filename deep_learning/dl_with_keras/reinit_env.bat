@echo off
REM ==============================================================================
REM All-in-One Python 3.12 & TensorFlow Re-initialization Script for Windows
REM ==============================================================================

echo [1/4] Ensuring Python 3.12 runtime is installed...
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.12 runtime missing. Triggering automatic launcher install...
    py install 3.12
    if %errorlevel% neq 0 (
        echo [ERROR] Automatic installation failed. Please install Python 3.12 manually.
        pause
        exit /b 1
    )
)

echo [2/4] Removing existing .venv folder if present...
if exist .venv (
    rmdir /s /q .venv
)

echo [3/4] Creating fresh Python 3.12 virtual environment (.venv)...
py -3.12 -m venv .venv
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create virtual environment.
    pause
    exit /b 1
)

echo [4/4] Upgrading pip and installing TensorFlow...
call .\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install "tensorflow>=2.16.0" "numpy<2.0.0"

echo.
echo ==============================================================================
echo [SUCCESS] Environment re-initialized and activated!
echo Python Version:
python --version
echo TensorFlow Version:
python -c "import tensorflow as tf; print(tf.__version__)"
echo ==============================================================================
echo.
echo Terminal is ready with active (.venv). Type 'deactivate' when done.
cmd /k
