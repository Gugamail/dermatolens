import streamlit as st
from components.painel_educacional import painel_educacional

st.set_page_config(layout="wide")
st.title("📚 Painel Educacional")
painel_educacional()
