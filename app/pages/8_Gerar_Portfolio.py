import streamlit as st
from components.gerar_pdf_portfolio import gerar_pdf_portfolio
from components.identificacao_usuario import registrar_usuario

st.set_page_config(layout="wide")
st.title("📄 Portfólio Acadêmico")

user_id = registrar_usuario()
if st.button("📥 Gerar meu portfólio em PDF"):
    path = gerar_pdf_portfolio(user_id)
    if path:
        with open(path, "rb") as file:
            st.download_button("⬇️ Baixar PDF", file.read(), file_name=path.split("/")[-1])
    else:
        st.warning("Você ainda não realizou atividades.")
