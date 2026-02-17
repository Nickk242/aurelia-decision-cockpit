import streamlit as st

def render():
    st.title("Definición del problema")

    s = st.text_area("S — Estado")
    a = st.text_area("A — Acción")
    t = st.text_area("T — Transición")
    g = st.text_area("G — Objetivo")
    c = st.text_area("C — Coste")
    r = st.text_area("R — Restricciones")

    hard = st.checkbox("Restricciones hard")
    soft = st.checkbox("Restricciones soft")

    if st.button("Generar st

