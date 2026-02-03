# 🎓 App de Predicción de Retención Estudiantil

Aplicación interactiva de Machine Learning para predecir si un estudiante se graduará, abandonará o continuará inscrito en educación superior.

## 📋 Características

- ✅ Predicción individual de estudiantes
- ✅ Predicción por lote (carga CSV masiva)
- ✅ Visualización de probabilidades interactiva
- ✅ Modelo Random Forest con 85%+ de precisión
- ✅ Interfaz amigable con Streamlit

## 🚀 Instalación Paso a Paso

### Paso 1: Requisitos Previos

Asegúrate de tener instalado:
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

Verifica tu versión de Python:
```bash
python --version
# o
python3 --version
```

### Paso 2: Descargar el Proyecto

Descarga y descomprime el archivo `student_retention_app.zip` o clona el repositorio.

```bash
# Si usas Git
git clone <tu-repositorio>
cd student_retention_app

# Si descargaste el ZIP
unzip student_retention_app.zip
cd student_retention_app
```

### Paso 3: Crear Entorno Virtual (Recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará:
- streamlit
- pandas
- numpy
- scikit-learn
- plotly

### Paso 5: Colocar el Dataset

Coloca tu archivo `datos_estudiantes.csv` en la carpeta del proyecto:

```
student_retention_app/
├── datos_estudiantes.csv  ← Coloca tu CSV aquí
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

### Paso 6: Entrenar el Modelo

```bash
python train_model.py
```

Este script:
1. ✅ Carga los datos
2. ✅ Entrena el modelo Random Forest
3. ✅ Guarda 4 archivos:
   - `model.pkl` - Modelo entrenado
   - `scaler.pkl` - Escalador de datos
   - `label_encoder.pkl` - Codificador de etiquetas
   - `feature_names.pkl` - Nombres de características

### Paso 7: Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en:
```
http://localhost:8501
```

Si no se abre automáticamente, copia y pega esa URL en tu navegador.

## 📖 Uso de la Aplicación

### Modo 1: Predicción Individual

1. Selecciona "📊 Predicción Individual" en el sidebar
2. Completa los datos del estudiante en los formularios
3. Haz clic en "🔮 Predecir"
4. Observa el resultado y las probabilidades

### Modo 2: Predicción por Lote

1. Selecciona "📁 Predicción por Lote" en el sidebar
2. Prepara un CSV con las mismas columnas que el dataset original (sin la columna Target)
3. Sube el archivo
4. Haz clic en "🔮 Predecir Todos"
5. Descarga los resultados con el botón "📥 Descargar Resultados"

## 📊 Estructura del Proyecto

```
student_retention_app/
├── app.py                    # Aplicación Streamlit principal
├── train_model.py            # Script de entrenamiento
├── requirements.txt          # Dependencias
├── README.md                 # Este archivo
├── datos_estudiantes.csv     # Dataset (debes agregarlo)
├── model.pkl                 # Modelo entrenado (se genera)
├── scaler.pkl                # Escalador (se genera)
├── label_encoder.pkl         # Codificador (se genera)
└── feature_names.pkl         # Nombres de características (se genera)
```

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Error: "No se encuentra el archivo model.pkl"
```bash
python train_model.py
```

### Error: Puerto 8501 ocupado
```bash
streamlit run app.py --server.port 8502
```

### Error al cargar datos
Asegúrate de que `datos_estudiantes.csv` esté en la carpeta correcta y tenga el formato adecuado.

## 📈 Características del Modelo

- **Algoritmo:** Random Forest Classifier
- **Número de estimadores:** 200 árboles
- **Precisión esperada:** ~85%+
- **Clases predichas:**
  - 🎓 Graduate (Graduado)
  - ❌ Dropout (Abandono)
  - 📚 Enrolled (Inscrito)

## 🎯 Variables más Importantes

Las 10 características más importantes según el modelo:
1. Unidades curriculares aprobadas (1er y 2do semestre)
2. Calificaciones promedio
3. Unidades evaluadas
4. Edad al inscribirse
5. Modo de aplicación
6. Y más...

## 💡 Consejos

- **Para mejor precisión:** Asegúrate de que todos los datos estén completos
- **Predicciones masivas:** Usa el modo por lote para analizar múltiples estudiantes
- **Interpretación:** Las probabilidades te indican la confianza del modelo

## 📝 Notas

- El modelo fue entrenado con datos históricos de educación superior
- Las predicciones son estimaciones basadas en patrones, no garantías
- Se recomienda re-entrenar el modelo periódicamente con nuevos datos

## 🤝 Soporte

Si encuentras problemas:
1. Revisa que todas las dependencias estén instaladas
2. Verifica que el archivo CSV tenga el formato correcto
3. Asegúrate de haber ejecutado `train_model.py` antes de la app

## 📜 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

---

¡Disfruta prediciendo la retención estudiantil! 🎓✨
