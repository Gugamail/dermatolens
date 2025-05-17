import streamlit as st
from components.painel_progresso import painel_progresso_usuario

st.set_page_config(layout="wide")
st.title("📈 Progresso Individual do Aluno")
painel_progresso_usuario()
