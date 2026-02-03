"""
Script de entrenamiento del modelo de predicción de retención estudiantil
"""
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import warnings
warnings.filterwarnings('ignore')

def train_model(data_path='datos_estudiantes.csv'):
    """
    Entrena el modelo de predicción de retención estudiantil
    """
    print("🔄 Cargando datos...")
    df = pd.read_csv(data_path, encoding='utf-8-sig')
    
    print(f"📊 Dataset: {df.shape[0]} estudiantes, {df.shape[1]-1} características")
    
    # Separar características y target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    print(f"\n📈 Distribución del target:")
    print(y.value_counts())
    
    # Codificar el target
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Split de datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    # Escalar datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\n🤖 Entrenando modelo Random Forest...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=4,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Evaluación
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Modelo entrenado exitosamente!")
    print(f"🎯 Precisión en test: {accuracy:.2%}")
    print(f"\n📊 Reporte de clasificación:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    
    # Importancia de características
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\n🔝 Top 10 características más importantes:")
    print(feature_importance.head(10).to_string(index=False))
    
    # Guardar modelo y artefactos
    print("\n💾 Guardando modelo y artefactos...")
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    with open('label_encoder.pkl', 'wb') as f:
        pickle.dump(le, f)
    
    with open('feature_names.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)
    
    print("✨ Proceso completado!")
    
    return model, scaler, le, X.columns.tolist()

if __name__ == "__main__":
    train_model()
