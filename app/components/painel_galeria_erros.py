import streamlit as st
import pandas as pd
import os
from PIL import Image

def galeria_erros_por_classe(user_id="anonimo"):
    st.subheader("🖼️ Galeria de Erros por Classe")

    caminho = "educacional.csv"
    if not os.path.exists(caminho):
        st.info("Nenhum erro registrado ainda.")
        return

    df = pd.read_csv(caminho)
    df = df[df["user_id"] == user_id]
    df = df[df["acertou"] == False]

    if df.empty:
        st.success("🎉 Nenhum erro encontrado até agora!")
        return

    classes = df["classe_ia"].unique()
    for classe in classes:
        subset = df[df["classe_ia"] == classe]
        st.markdown(f"### ❌ Erros em: {classe}")
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        for idx, (_, row) in enumerate(subset.iterrows()):
            imagem_path = f"banco_colaborativo/imagens_contribuidas/{row['imagem_id']}.jpg"
            if os.path.exists(imagem_path):
                with cols[idx % 3]:
                    st.image(Image.open(imagem_path), caption=f"Você marcou: {row['classe_escolhida']}", use_column_width=True)
