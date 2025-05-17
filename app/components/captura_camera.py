import streamlit as st
import tempfile
import os
from PIL import Image
from datetime import datetime
import uuid
import pandas as pd

CAMINHO_IMAGENS = "banco_colaborativo/imagens_contribuidas"
CAMINHO_CSV = "banco_colaborativo/registro_contribuicoes.csv"
os.makedirs(CAMINHO_IMAGENS, exist_ok=True)

def capturar_imagem_da_camera():
    st.subheader("📸 Capturar imagem com a câmera")

    img_bytes = st.camera_input("Tire uma foto com seu celular ou webcam")

    if img_bytes:
        img = Image.open(img_bytes).convert("RGB")
        st.image(img, caption="Imagem capturada", use_column_width=True)

        enviar = st.checkbox("Quero enviar esta imagem para ajudar no aprimoramento do sistema")

        if enviar:
            id_unico = f"DL-CAM-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}"
            nome_arquivo = f"{id_unico}.jpg"
            caminho_arquivo = os.path.join(CAMINHO_IMAGENS, nome_arquivo)
            img = img.resize((224, 224))
            img.save(caminho_arquivo)

            novo = pd.DataFrame([{
                "image_id": id_unico,
                "image_year": datetime.now().year,
                "image_source": "user_camera",
                "image_name": nome_arquivo,
                "patient_id": "anonymous",
                "sex": "unknown",
                "age_approx": -1,
                "anatom_site_general_challenge": "unknown",
                "diagnosis": "unknown",
                "benign_malignant": "unknown",
                "target": -1
            }])

            if os.path.exists(CAMINHO_CSV):
                novo.to_csv(CAMINHO_CSV, mode="a", header=False, index=False)
            else:
                novo.to_csv(CAMINHO_CSV, index=False)

            st.success(f"✅ Imagem enviada com sucesso com ID `{id_unico}`")

        return img  # PIL.Image
    return None
