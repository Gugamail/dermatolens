import streamlit as st
from components.identificacao_usuario import registrar_usuario
from components.modo_simulado import rodar_simulado_por_classe

st.set_page_config(layout="wide")
user_id = registrar_usuario()
rodar_simulado_por_classe(user_id=user_id)
