import pandas as pd
import numpy as np
import joblib
import streamlit as st

st.set_page_config(page_title="Estimador de Precio de Autos", layout="wide")

model = joblib.load('car_price_model.pkl')

st.title("Estimador de Precio de Autos. 🏎️")
st.write("Complete los datos del vehículo para obtener una estimación.")
st.divider()

if "history" not in st.session_state:
    st.session_state.history = []

with st.form("car_price_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        prod_year = st.slider("Año de Producción", 1990, 2025, 2015)
        engine_volume = st.slider("Volumen del Motor (L)", 1.0, 8.0, 2.0, 0.1)
        cylinders = st.slider("Cilindros", 1, 12, 4)
        airbags = st.slider("Airbags", 0, 20, 6)

    with col2:
        levy = st.slider("Levy", 0, 5000, 0)
        mileage = st.number_input("Kilometraje", min_value=0, max_value=1000000, value=150000)
        category = st.selectbox(
            "Categoría",
            [
                "Jeep", "Hatchback", "Sedan", "Microbus", "Goods wagon",
                "Universal", "Coupe", "Minivan", "Cabriolet",
                "Limousine", "Pickup"
            ]
        )
        leather_interior = st.selectbox("Interior de Cuero", ["Yes", "No"])

    with col3:
        fuel_type = st.selectbox(
            "Tipo de Combustible",
            ["Hybrid", "Petrol", "Diesel", "CNG", "Plug-in Hybrid", "LPG", "Hydrogen"]
        )
        gear_box_type = st.selectbox(
            "Tipo de Caja de Cambios",
            ["Automatic", "Tiptronic", "Variator", "Manual"]
        )
        drive_wheels = st.selectbox("Tracción", ["4x4", "Front", "Rear"])
        wheel = st.selectbox("Volante", ["Left wheel", "Right-hand drive"])
        color = st.selectbox(
            "Color",
            [
                "Silver", "Black", "White", "Grey", "Blue", "Green", "Red",
                "Sky blue", "Orange", "Yellow", "Brown", "Golden",
                "Beige", "Carnelian red", "Purple", "Pink"
            ]
        )

    submit = st.form_submit_button("Calcular Precio")

if submit:
    input_df = pd.DataFrame([
        {
            "Prod. year": prod_year,
            "Engine volume": engine_volume,
            "Cylinders": cylinders,
            "Airbags": airbags,
            "Levy": levy if levy > 0 else np.nan,
            "Mileage": mileage,
            "Category": category,
            "Leather interior": leather_interior,
            "Fuel type": fuel_type,
            "Gear box type": gear_box_type,
            "Drive wheels": drive_wheels,
            "Wheel": wheel,
            "Color": color
        }
    ])

    prediction = model.predict(input_df)[0]

    st.session_state.history.append(
        {"Precio estimado": prediction, **input_df.iloc[0].to_dict()}
    )

    st.subheader("Resultado de la estimación")
    st.metric(label="Precio Estimado", value=f"${prediction:,.2f}")

    st.divider()
    st.subheader("Historial de predicciones")
    st.dataframe(pd.DataFrame(st.session_state.history))
