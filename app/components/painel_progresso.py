import streamlit as st
import pandas as pd
import os
import altair as alt

def painel_progresso_usuario(user_id="anonimo"):
    st.subheader("📈 Progresso do Aluno")

    caminho = "educacional.csv"
    if not os.path.exists(caminho):
        st.info("Nenhum dado de progresso registrado ainda.")
        return

    df = pd.read_csv(caminho)
    df = df[df["user_id"] == user_id]

    if df.empty:
        st.info("Nenhuma atividade registrada para este usuário.")
        return

    # Contagem por classe
    progresso = df.groupby("classe_ia").agg(
        total=("classe_ia", "count"),
        acertos=("acertou", "sum")
    ).reset_index()
    progresso["erro"] = progresso["total"] - progresso["acertos"]
    progresso = progresso.melt(id_vars=["classe_ia"], value_vars=["acertos", "erro"],
                               var_name="Resultado", value_name="Quantidade")

    # Gráfico de barras empilhadas
    chart = alt.Chart(progresso).mark_bar().encode(
        x=alt.X("classe_ia:N", title="Classe"),
        y=alt.Y("Quantidade:Q"),
        color=alt.Color("Resultado:N", scale=alt.Scale(range=["#0d6efd", "#e74c3c"]))
    ).properties(
        width=600,
        height=400,
        title=f"Desempenho de {user_id} por classe"
    )

    st.altair_chart(chart, use_container_width=True)
