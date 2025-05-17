from fpdf import FPDF
import os
import pandas as pd
from datetime import datetime

def gerar_pdf_portfolio(user_id, path="portfolio_academico"):
    os.makedirs(path, exist_ok=True)
    csv_path = "educacional.csv"
    if not os.path.exists(csv_path):
        return None

    df = pd.read_csv(csv_path)
    df_user = df[df["user_id"] == user_id]

    if df_user.empty:
        return None

    acertos = df_user["acertou"].sum()
    total = len(df_user)
    acuracia = acertos / total if total else 0

    por_classe = df_user.groupby("classe_ia")["acertou"].agg(["count", "mean"]).reset_index()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Relatório Acadêmico – DermatoLens", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Aluno: {user_id}", ln=True)
    pdf.cell(0, 10, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.cell(0, 10, f"Total de casos analisados: {total}", ln=True)
    pdf.cell(0, 10, f"Acurácia geral: {acuracia:.2%}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Desempenho por classe:", ln=True)

    pdf.set_font("Arial", "", 11)
    for _, row in por_classe.iterrows():
        pdf.cell(0, 8, f"{row['classe_ia']}: {int(row['count'])} casos, acurácia {row['mean']:.2%}", ln=True)

    pdf.ln(8)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Casos com erro:", ln=True)

    pdf.set_font("Arial", "", 11)
    erros = df_user[df_user["acertou"] == False]
    for _, row in erros.iterrows():
        pdf.cell(0, 8, f"{row['data_hora']} | IA: {row['classe_ia']} | Marcado: {row['classe_escolhida']}", ln=True)

    nome_pdf = f"{path}/portfolio_{user_id}.pdf"
    pdf.output(nome_pdf)
    return nome_pdf
