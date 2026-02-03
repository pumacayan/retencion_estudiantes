#!/bin/bash

echo "========================================"
echo "  INSTALADOR - App Retención Estudiantil"
echo "========================================"
echo ""

echo "[1/5] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python no está instalado"
    echo "Por favor instala Python 3.8+ desde python.org"
    exit 1
fi
python3 --version
echo ""

echo "[2/5] Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo crear el entorno virtual"
    exit 1
fi
echo ""

echo "[3/5] Activando entorno virtual..."
source venv/bin/activate
echo ""

echo "[4/5] Instalando dependencias..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi
echo ""

echo "[5/5] Entrenando modelo..."
python train_model.py
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo entrenar el modelo"
    exit 1
fi
echo ""

echo "========================================"
echo "  INSTALACIÓN COMPLETADA!"
echo "========================================"
echo ""
echo "Para ejecutar la app, usa:"
echo "  ./run_app.sh"
echo ""
