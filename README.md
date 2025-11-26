# Estimador de Precio de Autos. 🏎️

Este proyecto implementa un sistema completo para predecir el precio de automóviles usados mediante un modelo de Machine Learning entrenado a partir de un conjunto de datos real.  
Incluye:

• Un modelo Random Forest entrenado con ingeniería de características y pipelines de preprocesamiento.  
• Una aplicación web interactiva en Streamlit donde el usuario ingresa las características del auto y obtiene una estimación inmediata.  
• Un sistema de historial que permite revisar predicciones previas dentro de la misma sesión.

El objetivo es demostrar cómo un dataset crudo puede transformarse en un modelo funcional e integrado en una interfaz accesible para usuarios no técnicos.

## Contenidos del proyecto

Este repositorio incluye:

• Código de preprocesamiento y entrenamiento del modelo  
• Pipeline completo con imputación, escalado y codificación categórica  
• Modelo entrenado y guardado (car_price_model.pkl)  
• Aplicación Streamlit lista para ejecución  
• Documentación del flujo y estructura  

## Vista previa de la aplicación

![Interfaz del Estimador](https://raw.githubusercontent.com/AngelBernaal/PriceCarML/main/img.png)


## Flujo completo del proyecto

### 1. Limpieza y preparación de datos

El dataset original (carros.csv) incluye características técnicas y estéticas de vehículos.  
Se realizaron los siguientes pasos clave:

• Eliminación de columnas irrelevantes (ID, Doors)  
• Conversión de Levy de texto a valores numéricos  
• Normalización de campos con valores como "12 km" a 12  
• Conversión de variables categóricas a tipo category  
• Extracción del volumen del motor desde cadenas como "2.5 Turbo"  
• Corrección de kilometraje inválido  
• Identificación y tratamiento de valores faltantes  

### 2. Ingeniería de características

Las variables se agruparon en tres tipos:

• Numéricas: escaladas con StandardScaler  
• Numéricas con imputación: imputadas por mediana y luego escaladas  
• Categóricas: codificadas con OneHotEncoder  

Todo el preprocesamiento se encapsuló en un ColumnTransformer, garantizando reproducibilidad y evitando fugas de datos.

### 3. Entrenamiento del modelo

Se entrenó un RandomForestRegressor con:

• 100 árboles  
• random_state igual a 1 para reproducibilidad  

El modelo se integró dentro de un Pipeline junto al preprocesador.

### 4. Evaluación

Métricas obtenidas:

• RMSE: valor basado en la predicción promedio  
• R² Score: medida del poder explicativo del modelo  

Estas métricas permiten validar que el modelo generaliza adecuadamente.

### 5. Exportación del modelo

El modelo final se guardó usando:

```python
joblib.dump(rf_model, 'car_price_model.pkl')
```
