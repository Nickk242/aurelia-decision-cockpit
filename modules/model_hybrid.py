import streamlit as st
import pandas as pd

def render():
    st.title("Sistema híbrido ML + OR")

    predicted = st.session_state.get("predicted_demand", 150)

    risk = st.slider("Nivel de riesgo", 0.5, 1.5, 1.0)

    adjusted_capacity = int(predicted * risk)

    st.write("Capacidad ajustada:", adjusted_capacity)

    data = pd.DataFrame(
        {
            "Paquete": ["A", "B", "C", "D", "E"],
            "Peso": [50, 70, 30, 60, 40],
            "Valor": [60, 100, 120, 90, 30],
        }
    )

    if st.button("Recalcular plan"):

        df = data.sort_values("Valor", ascending=False)

        total_weight = 0
        selected = []

        for _, row in df.iterrows():
            if total_weight + row["Peso"] <= adjusted_capacity:
                selected.append(row["Paquete"])
                total_weight += row["Peso"]

        st.write("Plan híbrido:", selected)

