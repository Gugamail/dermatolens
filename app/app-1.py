import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# === Caminhos ===
MODELO_CAMINHO = "models/modelo_dermatolens"
IMG_SIZE = (224, 224)

# === Carregar modelo treinado ===
@st.cache_resource
def carregar_modelo():
    return tf.keras.models.load_model(MODELO_CAMINHO)

modelo = carregar_modelo()

# === Dicionário de classes ===
classes = list(modelo.class_names) if hasattr(modelo, 'class_names') else ['melanoma', 'nevus', 'outros']

# === Interface ===
st.title("📷 DermatoLens – Triagem Inteligente de Lesões de Pele")
st.markdown("Este aplicativo usa um modelo real treinado para prever a **classificação da lesão** com base em uma imagem enviada. ⚠️ **Não é diagnóstico médico.**")

# === Upload da imagem ===
imagem = st.file_uploader("Envie uma imagem de lesão de pele (JPG ou PNG)", type=["jpg", "jpeg", "png"])

if imagem:
    img = Image.open(imagem).convert("RGB")
    st.image(img, caption="Imagem carregada", use_column_width=True)

    # Pré-processamento
    img_resized = img.resize(IMG_SIZE)
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Previsão
    pred = modelo.predict(img_array)[0]
    classe_predita = classes[np.argmax(pred)]
    confianca = np.max(pred)

    st.subheader("🔍 Resultado da Análise:")
    st.markdown(f"**Classe prevista:** `{classe_predita}`")
    st.markdown(f"**Confiança:** `{confianca:.2%}`")

    st.info("Recomendação: este resultado não substitui consulta com dermatologista. Use apenas como apoio educacional.")
