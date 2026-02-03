@echo off
echo ========================================
echo   Iniciando App Retencion Estudiantil
echo ========================================
echo.

call venv\Scripts\activate.bat
streamlit run app.py

pause
