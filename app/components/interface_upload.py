import streamlit as st
from PIL import Image

def interface_upload():
    imagem_upada = st.file_uploader("Escolha uma imagem (JPG ou PNG)", type=["jpg", "jpeg", "png"])
    if imagem_upada:
        img = Image.open(imagem_upada).convert("RGB")
        st.image(img, caption="Imagem enviada", use_column_width=True)
        return imagem_upada, img
    return None, None
