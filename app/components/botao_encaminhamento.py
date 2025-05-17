import streamlit as st
from datetime import datetime
import uuid

def mostrar_botao_encaminhamento(classe_predita):
    st.divider()
    st.subheader("📨 Encaminhar para Especialista")

    st.markdown("Este botão simula o encaminhamento da triagem para um(a) especialista. Nenhum dado pessoal é enviado.")

    if st.button("📤 Encaminhar esta triagem para análise especializada"):
        protocolo = f"ENC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}"
        st.success("✅ Triagem registrada para encaminhamento.")
        st.markdown(f"**Número de protocolo:** `{protocolo}`")
        st.markdown("Um profissional da clínica poderá visualizar esta triagem no painel administrativo.")
        st.info("Este recurso é simulado e tem fins de demonstração.")