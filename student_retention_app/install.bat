@echo off
echo ========================================
echo   INSTALADOR - App Retencion Estudiantil
echo ========================================
echo.

echo [1/5] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python 3.8+ desde python.org
    pause
    exit /b 1
)
echo.

echo [2/5] Creando entorno virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)
echo.

echo [3/5] Activando entorno virtual...
call venv\Scripts\activate.bat
echo.

echo [4/5] Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo.

echo [5/5] Entrenando modelo...
python train_model.py
if %errorlevel% neq 0 (
    echo ERROR: No se pudo entrenar el modelo
    pause
    exit /b 1
)
echo.

echo ========================================
echo   INSTALACION COMPLETADA!
echo ========================================
echo.
echo Para ejecutar la app, usa:
echo   run_app.bat
echo.
pause
