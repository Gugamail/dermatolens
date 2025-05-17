import streamlit as st

st.set_page_config(page_title="DermatoLens", layout="wide")

col1, col2 = st.columns([1, 8])
with col1:
    st.image("app/static/logo_clinica_cecilia.png", width=60)
with col2:
    st.title("DermatoLens")

st.markdown("Escolha uma aba no menu lateral para iniciar.")