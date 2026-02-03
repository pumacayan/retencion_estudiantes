# 🚀 GUÍA RÁPIDA DE INSTALACIÓN

## ⚡ Instalación Express (Recomendado)

### Windows
```bash
1. Doble clic en: install.bat
2. Espera a que termine
3. Doble clic en: run_app.bat
```

### Linux/Mac
```bash
1. chmod +x install.sh run_app.sh
2. ./install.sh
3. ./run_app.sh
```

## 📝 Instalación Manual (Paso a Paso)

### 1️⃣ Abrir Terminal/CMD en la carpeta del proyecto

### 2️⃣ Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Entrenar el modelo
```bash
python train_model.py
```

### 5️⃣ Ejecutar la app
```bash
streamlit run app.py
```

### 6️⃣ Abrir navegador
La app se abrirá automáticamente en: `http://localhost:8501`

## 🎯 ¿Qué hace cada archivo?

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Aplicación Streamlit (interfaz web) |
| `train_model.py` | Script que entrena el modelo ML |
| `requirements.txt` | Lista de dependencias Python |
| `datos_estudiantes.csv` | Dataset de entrenamiento |
| `model.pkl` | Modelo entrenado (se genera) |
| `install.bat` / `install.sh` | Instalador automático |
| `run_app.bat` / `run_app.sh` | Ejecutor de la app |

## ❓ Solución de Problemas

### "Python no reconocido"
- Instala Python desde: https://python.org
- En Windows, marca "Add to PATH" durante instalación

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Puerto ocupado"
```bash
streamlit run app.py --server.port 8502
```

### Modelo no encontrado
```bash
python train_model.py
```

## 💡 Comandos Útiles

```bash
# Ver versión de Python
python --version

# Activar entorno virtual
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Desactivar entorno virtual
deactivate

# Ver paquetes instalados
pip list

# Actualizar streamlit
pip install --upgrade streamlit
```

## 🎓 ¡Listo para usar!

Una vez instalado, simplemente ejecuta:
- Windows: `run_app.bat`
- Linux/Mac: `./run_app.sh`

¡Y comienza a predecir! 🚀
