import streamlit as st
import pandas as pd

def render():
    st.title("Optimización de carga")

    capacity = st.number_input("Capacidad del camión", 50, 500, 200)

    data = pd.DataFrame(
        {
            "Paquete": ["A", "B", "C", "D", "E"],
            "Peso": [50, 70, 30, 60, 40],
            "Valor": [60, 100, 120, 90, 30],
        }
    )

    st.dataframe(data)

    if st.button("Optimizar carga"):

        df = data.sort_values("Valor", ascending=False)

        total_weight = 0
        selected = []

        for _, row in df.iterrows():
            if total_weight + row["Peso"] <= capacity:
                selected.append(row["Paquete"])
                total_weight += row["Peso"]

        st.write("Paquetes seleccionados:", selected)
        st.progress(total_weight / capacity)

