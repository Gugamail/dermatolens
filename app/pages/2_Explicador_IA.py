import streamlit as st
from PIL import Image
from components.modo_educacional import rodar_modo_educacional

st.set_page_config(layout="wide")
st.subheader("🧠 Explicador de IA")

imagem = st.file_uploader("Envie uma imagem de lesão", type=["jpg", "jpeg", "png"])
classe_predita = st.selectbox("Classe predita pela IA", ["melanoma", "bcc", "scc", "ak", "nevus", "df", "infl", "outros"])
confianca = st.slider("Confiança da IA", min_value=0.0, max_value=1.0, step=0.01, value=0.8)

if imagem:
    img_pil = Image.open(imagem).convert("RGB")
    rodar_modo_educacional(img_pil, classe_predita, confianca)
