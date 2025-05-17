import streamlit as st
import pandas as pd
import os

CAMINHO_REGISTRO = "triagens.csv"

def painel_triagens():
    st.divider()
    st.subheader("📊 Histórico de Triagens Realizadas")

    if not os.path.exists(CAMINHO_REGISTRO):
        st.info("Nenhuma triagem registrada ainda.")
        return

    df = pd.read_csv(CAMINHO_REGISTRO)

    # Filtros
    classe_opcoes = ["Todas"] + sorted(df["classe"].unique())
    filtro_classe = st.selectbox("Filtrar por classe:", classe_opcoes)

    if filtro_classe != "Todas":
        df = df[df["classe"] == filtro_classe]

    st.markdown(f"Total de triagens exibidas: **{len(df)}**")

    # Mostrar tabela
    st.dataframe(df.sort_values(by="data_hora", ascending=False), use_container_width=True)

    # Botão de download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Baixar CSV", csv, file_name="triagens_filtradas.csv", mime="text/csv")
