import streamlit as st
from components.captura_camera import capturar_imagem_da_camera
from components.interface_resultado import interface_resultado
from components.gerar_pdf_triagem import *
from components.botao_encaminhamento import mostrar_botao_encaminhamento

st.set_page_config(layout="wide")
st.title("📸 Captura via Câmera")

imagem = capturar_imagem_da_camera()
if imagem:
    classe = st.selectbox("Classe predita", ["melanoma", "bcc", "scc", "ak", "nevus", "df", "infl", "outros"])
    confianca = st.slider("Confiança da IA", 0.0, 1.0, 0.8, 0.01)
    interface_resultado(classe, confianca)
    mostrar_botao_encaminhamento(classe)
    gerar_pdf_triagem(imagem, classe, confianca)
