import streamlit as st
from components.painel_galeria_erros import galeria_erros_por_classe

st.set_page_config(layout="wide")
st.title("❌ Galeria de Erros")
galeria_erros_por_classe()