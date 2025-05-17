import streamlit as st
import uuid
import os
import pandas as pd

def registrar_usuario():
    if "user_id" not in st.session_state:
        st.session_state.user_id = f"user_{uuid.uuid4().hex[:6]}"

    st.sidebar.markdown("## 👤 Identificação")
    nome = st.sidebar.text_input("Seu nome ou apelido", value=st.session_state.user_id)

    st.session_state.user_id = nome.strip() if nome else st.session_state.user_id

    if st.sidebar.checkbox("🔔 Quero ser avisado por e-mail sobre novidades"):
        email = st.sidebar.text_input("Digite seu e-mail")
        if email:
            lead = pd.DataFrame([{
                "user_id": st.session_state.user_id,
                "email": email
            }])
            os.makedirs("leads", exist_ok=True)
            path = "leads/leads.csv"
            if os.path.exists(path):
                lead.to_csv(path, mode="a", header=False, index=False)
            else:
                lead.to_csv(path, index=False)
            st.sidebar.success("📩 E-mail registrado com sucesso!")

    return st.session_state.user_id
