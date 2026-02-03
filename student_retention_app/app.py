"""
🎓 App de Predicción de Retención Estudiantil
Aplicación interactiva para predecir si un estudiante se graduará, abandonará o continuará
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Configuración de página
st.set_page_config(
    page_title="Predicción Retención Estudiantil",
    page_icon="🎓",
    layout="wide"
)

# Cargar modelos y artefactos
@st.cache_resource
def load_models():
    """Carga el modelo entrenado y artefactos"""
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    with open('feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    return model, scaler, label_encoder, feature_names

# Título y descripción
st.title("🎓 Predictor de Retención Estudiantil")
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir si un estudiante:
- 🎓 **Graduará** (Graduate)
- ❌ **Abandonará** (Dropout)  
- 📚 **Continuará inscrito** (Enrolled)

---
""")

# Cargar modelos
try:
    model, scaler, label_encoder, feature_names = load_models()
    st.success("✅ Modelo cargado correctamente")
except Exception as e:
    st.error(f"❌ Error cargando el modelo: {e}")
    st.stop()

# Sidebar con opciones
st.sidebar.header("⚙️ Opciones")
modo = st.sidebar.radio(
    "Modo de predicción:",
    ["📊 Predicción Individual", "📁 Predicción por Lote"]
)

if modo == "📊 Predicción Individual":
    st.header("📊 Predicción Individual")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("👤 Información Personal")
        marital_status = st.selectbox("Estado Civil", [1, 2, 3, 4, 5, 6], help="1=Soltero, 2=Casado, etc.")
        gender = st.selectbox("Género", [0, 1], help="0=Femenino, 1=Masculino")
        age = st.number_input("Edad al inscribirse", 17, 70, 20)
        nationality = st.number_input("Nacionalidad (código)", 1, 25, 1)
        international = st.selectbox("¿Internacional?", [0, 1])
        
    with col2:
        st.subheader("📚 Información Académica")
        application_mode = st.number_input("Modo de aplicación", 1, 20, 1)
        application_order = st.number_input("Orden de aplicación", 0, 9, 1)
        course = st.number_input("Código del curso", 1, 20, 1)
        attendance = st.selectbox("Asistencia", [0, 1], help="0=Vespertino, 1=Diurno")
        prev_qualification = st.number_input("Calificación previa", 1, 20, 1)
        
    with col3:
        st.subheader("👨‍👩‍👧 Información Familiar")
        mother_qual = st.number_input("Calificación de la madre", 1, 44, 1)
        father_qual = st.number_input("Calificación del padre", 1, 44, 1)
        mother_occup = st.number_input("Ocupación de la madre", 0, 195, 0)
        father_occup = st.number_input("Ocupación del padre", 0, 195, 0)
    
    col4, col5 = st.columns(2)
    
    with col4:
        st.subheader("📖 Primer Semestre")
        cu1_credited = st.number_input("Unidades acreditadas 1S", 0, 20, 0)
        cu1_enrolled = st.number_input("Unidades inscritas 1S", 0, 26, 6)
        cu1_evaluations = st.number_input("Evaluaciones 1S", 0, 45, 0)
        cu1_approved = st.number_input("Unidades aprobadas 1S", 0, 26, 6)
        cu1_grade = st.number_input("Calificación 1S", 0.0, 20.0, 12.0, 0.1)
        cu1_without_eval = st.number_input("Sin evaluación 1S", 0, 12, 0)
    
    with col5:
        st.subheader("📖 Segundo Semestre")
        cu2_credited = st.number_input("Unidades acreditadas 2S", 0, 20, 0)
        cu2_enrolled = st.number_input("Unidades inscritas 2S", 0, 23, 6)
        cu2_evaluations = st.number_input("Evaluaciones 2S", 0, 33, 0)
        cu2_approved = st.number_input("Unidades aprobadas 2S", 0, 20, 6)
        cu2_grade = st.number_input("Calificación 2S", 0.0, 20.0, 12.0, 0.1)
        cu2_without_eval = st.number_input("Sin evaluación 2S", 0, 12, 0)
    
    col6, col7 = st.columns(2)
    
    with col6:
        st.subheader("💰 Información Económica/Social")
        displaced = st.selectbox("¿Desplazado?", [0, 1])
        special_needs = st.selectbox("¿Necesidades especiales?", [0, 1])
        debtor = st.selectbox("¿Deudor?", [0, 1])
        tuition_up_to_date = st.selectbox("¿Matrícula al día?", [0, 1])
        scholarship = st.selectbox("¿Becado?", [0, 1])
    
    with col7:
        st.subheader("📊 Indicadores Económicos")
        unemployment = st.number_input("Tasa de desempleo", 0.0, 20.0, 10.0, 0.1)
        inflation = st.number_input("Tasa de inflación", -5.0, 5.0, 1.0, 0.1)
        gdp = st.number_input("PIB", -10.0, 10.0, 0.0, 0.1)
    
    # Botón de predicción
    if st.button("🔮 Predecir", type="primary", use_container_width=True):
        # Crear array de características
        features = np.array([[
            marital_status, application_mode, application_order, course, attendance,
            prev_qualification, nationality, mother_qual, father_qual, mother_occup,
            father_occup, displaced, special_needs, debtor, tuition_up_to_date,
            gender, scholarship, age, international, cu1_credited, cu1_enrolled,
            cu1_evaluations, cu1_approved, cu1_grade, cu1_without_eval,
            cu2_credited, cu2_enrolled, cu2_evaluations, cu2_approved, cu2_grade,
            cu2_without_eval, unemployment, inflation, gdp
        ]])
        
        # Escalar y predecir
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        
        # Decodificar predicción
        prediction_label = label_encoder.inverse_transform([prediction])[0]
        
        # Mostrar resultados
        st.markdown("---")
        st.header("🎯 Resultado de la Predicción")
        
        # Colorear según predicción
        if prediction_label == "Graduate":
            st.success(f"### 🎓 Predicción: **{prediction_label}** (Graduará)")
            color = "green"
        elif prediction_label == "Dropout":
            st.error(f"### ❌ Predicción: **{prediction_label}** (Abandonará)")
            color = "red"
        else:
            st.info(f"### 📚 Predicción: **{prediction_label}** (Continuará)")
            color = "blue"
        
        # Gráfico de probabilidades
        fig = go.Figure(data=[
            go.Bar(
                x=label_encoder.classes_,
                y=probabilities * 100,
                text=[f"{p:.1f}%" for p in probabilities * 100],
                textposition='auto',
                marker_color=['#FF6B6B' if c == 'Dropout' else '#4ECDC4' if c == 'Enrolled' else '#95E1D3' 
                             for c in label_encoder.classes_]
            )
        ])
        
        fig.update_layout(
            title="Probabilidades de cada resultado",
            xaxis_title="Categoría",
            yaxis_title="Probabilidad (%)",
            yaxis_range=[0, 100],
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detalles de probabilidades
        st.subheader("📊 Detalle de Probabilidades")
        prob_df = pd.DataFrame({
            'Resultado': label_encoder.classes_,
            'Probabilidad': [f"{p:.2%}" for p in probabilities]
        })
        st.dataframe(prob_df, use_container_width=True, hide_index=True)

else:  # Predicción por lote
    st.header("📁 Predicción por Lote")
    st.markdown("""
    Sube un archivo CSV con las características de múltiples estudiantes para obtener predicciones masivas.
    
    **Formato requerido:** El CSV debe tener las mismas 34 columnas que los datos de entrenamiento (sin la columna Target).
    """)
    
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Leer archivo
            df_batch = pd.read_csv(uploaded_file, encoding='utf-8-sig')
            
            st.success(f"✅ Archivo cargado: {len(df_batch)} estudiantes")
            st.dataframe(df_batch.head(), use_container_width=True)
            
            if st.button("🔮 Predecir Todos", type="primary"):
                # Verificar columnas
                if len(df_batch.columns) != len(feature_names):
                    st.error(f"❌ El archivo debe tener {len(feature_names)} columnas")
                else:
                    # Escalar y predecir
                    X_scaled = scaler.transform(df_batch)
                    predictions = model.predict(X_scaled)
                    probabilities = model.predict_proba(X_scaled)
                    
                    # Decodificar
                    predictions_labels = label_encoder.inverse_transform(predictions)
                    
                    # Crear DataFrame de resultados
                    results_df = df_batch.copy()
                    results_df['Predicción'] = predictions_labels
                    results_df['Prob_Dropout'] = probabilities[:, 0]
                    results_df['Prob_Enrolled'] = probabilities[:, 1]
                    results_df['Prob_Graduate'] = probabilities[:, 2]
                    
                    st.success("✅ Predicciones completadas!")
                    
                    # Resumen
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        dropout_count = (predictions_labels == 'Dropout').sum()
                        st.metric("❌ Abandonarán", dropout_count, 
                                 f"{dropout_count/len(predictions_labels)*100:.1f}%")
                    
                    with col2:
                        enrolled_count = (predictions_labels == 'Enrolled').sum()
                        st.metric("📚 Continuarán", enrolled_count,
                                 f"{enrolled_count/len(predictions_labels)*100:.1f}%")
                    
                    with col3:
                        graduate_count = (predictions_labels == 'Graduate').sum()
                        st.metric("🎓 Graduarán", graduate_count,
                                 f"{graduate_count/len(predictions_labels)*100:.1f}%")
                    
                    # Gráfico de distribución
                    fig = px.pie(
                        values=[dropout_count, enrolled_count, graduate_count],
                        names=['Dropout', 'Enrolled', 'Graduate'],
                        title='Distribución de Predicciones',
                        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#95E1D3']
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Mostrar resultados
                    st.subheader("📊 Resultados Detallados")
                    st.dataframe(results_df, use_container_width=True)
                    
                    # Descargar resultados
                    csv = results_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Descargar Resultados",
                        csv,
                        "predicciones.csv",
                        "text/csv",
                        key='download-csv'
                    )
                    
        except Exception as e:
            st.error(f"❌ Error procesando el archivo: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🤖 Powered by Machine Learning | 🐍 Python + Streamlit</p>
</div>
""", unsafe_allow_html=True)
