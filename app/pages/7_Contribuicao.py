import streamlit as st
from components.interface_contribuicao_usuario import interface_contribuicao_usuario
from components.interface_contribuicao_coletiva import tratar_contribuicao

st.set_page_config(layout="wide")
st.title("🙋 Contribuição ao Projeto")

classe = st.selectbox("Classe predita para contribuição", ["melanoma", "bcc", "scc", "ak", "nevus", "df", "infl", "outros"])
confianca = st.slider("Confiança da IA", 0.0, 1.0, 0.75, 0.01)

interface_contribuicao_usuario(classe, confianca)
