import streamlit as st

from modules.model_representation import render as render_representation
from modules.model_ml import render as render_ml
from modules.model_or import render as render_or
from modules.model_hybrid import render as render_hybrid

st.set_page_config(page_title="Aurelia Decision Cockpit", layout="wide")

st.sidebar.title("Aurelia Decision Cockpit")

page = st.sidebar.radio(
    "Navegación",
    [
        "Definición del problema",
        "Predicción ML",
        "Optimización de rutas",
        "Sistema híbrido",
    ],
)

if page == "Definición del problema":
    render_representation()

elif page == "Predicción ML":
    render_ml()

elif page == "Optimización de rutas":
    render_or()

elif page == "Sistema híbrido":
    render_hybrid()

