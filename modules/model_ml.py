import streamlit as st
import numpy as np

def render():
    st.title("Predicción de demanda")

    day = st.slider("Día de la semana", 1, 7, 3)
    weather = st.selectbox("Clima", ["Soleado", "Lluvia"])
    promo = st.selectbox("Promoción", ["No", "Sí"])

    weather_val = 20 if weather == "Lluvia" else 0
    promo_val = 50 if promo == "Sí" else 0

    if st.button("Predecir demanda"):

        noise = np.random.randint(-10, 10)
        demand = 100 + weather_val + promo_val + noise

        st.session_state.predicted_demand = demand

    if "predicted_demand" in st.session_state:
        st.metric("Demanda esperada", st.session_state.predicted_demand)

    st.warning("Esto es una predicción, no una decisión")

