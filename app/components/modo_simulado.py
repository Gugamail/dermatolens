import streamlit as st
import os
import random
import pandas as pd
from PIL import Image
from datetime import datetime

def rodar_simulado_por_classe(base_dir="data/train", user_id="anonimo"):
    st.subheader("🧪 Simulado por Classe com Feedback")

    # Verifica as classes disponíveis com imagens
    classes = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    classe_escolhida = st.selectbox("Escolha uma classe para testar seu conhecimento:", classes)

    caminho_classe = os.path.join(base_dir, classe_escolhida)
    imagens = sorted(os.listdir(caminho_classe))
    imagens = [img for img in imagens if img.endswith((".jpg", ".jpeg", ".png"))]
    imagens_escolhidas = random.sample(imagens, min(5, len(imagens)))

    respostas = []

    for i, img_nome in enumerate(imagens_escolhidas):
        st.markdown(f"##### Imagem {i+1}")
        img_path = os.path.join(caminho_classe, img_nome)
        img = Image.open(img_path).convert("RGB")
        st.image(img, use_column_width=True)

        col1, col2 = st.columns([3, 1])
        with col1:
            opcao = st.radio(f"Qual é sua classificação para essa lesão?", classes, key=f"resp_{i}")
        with col2:
            enviar = st.button("Ver resposta", key=f"ver_{i}")

        if enviar:
            acertou = opcao == classe_escolhida
            st.success("✅ Correto!") if acertou else st.error(f"❌ Incorreto. Era: {classe_escolhida}")
            respostas.append({
                "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user_id": user_id,
                "classe_ia": classe_escolhida,
                "classe_escolhida": opcao,
                "acertou": acertou,
                "imagem_id": img_nome.split(".")[0]
            })

    # Registro no CSV se houver respostas
    if respostas:
        df = pd.DataFrame(respostas)
        caminho_csv = "educacional.csv"
        if os.path.exists(caminho_csv):
            df.to_csv(caminho_csv, mode="a", header=False, index=False)
        else:
            df.to_csv(caminho_csv, index=False)
        st.success("📥 Resultados registrados com sucesso!")
