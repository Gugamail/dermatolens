import streamlit as st
import pandas as pd
import os

CAMINHO_EDUCACIONAL = "educacional.csv"

def painel_educacional():
    st.divider()
    st.subheader("🎓 Painel de Aprendizado Visual")

    if not os.path.exists(CAMINHO_EDUCACIONAL):
        st.info("Nenhuma interação educacional registrada ainda.")
        return

    df = pd.read_csv(CAMINHO_EDUCACIONAL)

    # Filtro por nickname
    usuarios = sorted(df["user_id"].dropna().unique())
    filtro_usuario = st.selectbox("Filtrar por estudante:", ["Todos"] + usuarios)

    if filtro_usuario != "Todos":
        df = df[df["user_id"] == filtro_usuario]

    st.markdown(f"Total de interações: **{len(df)}**")

    # Acurácia por classe
    st.markdown("#### Acurácia por classe (educacional)")
    acuracia = df.groupby("classe_ia")["acertou"].agg(["count", "mean"]).rename(columns={"count": "Total", "mean": "Acurácia"})
    st.dataframe(acuracia.round(2), use_container_width=True)

    # Classe com maior erro
    classe_erro = acuracia["Acurácia"].idxmin()
    if len(df) > 0:
        st.warning(f"📉 Classe com maior taxa de erro: **{classe_erro}**")
