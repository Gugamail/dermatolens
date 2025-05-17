import streamlit as st

TRADUCAO_CLASSES = {
    "melanoma": "uma lesão possivelmente maligna (melanoma)",
    "nevus": "uma pinta provavelmente benigna (nevus)",
    "outros": "um tipo de lesão que não foi classificada como melanoma ou nevus"
}

def interface_resultado(classe, confianca):
    st.subheader("🔎 O que a IA encontrou na imagem")

    explicacao = TRADUCAO_CLASSES.get(classe, classe)
    st.markdown(f"🧠 A inteligência artificial analisou sua imagem e encontrou indícios de **{explicacao}**.")
    st.markdown(f"📊 O nível de confiança estimado pelo sistema foi de **{confianca:.2%}**.")

    st.markdown("⚠️ Este é apenas um resultado preliminar gerado por um algoritmo. Ele **não substitui uma avaliação médica presencial com um(a) dermatologista.**")

    if classe == "melanoma":
        st.error("⚠️ Procure um especialista o quanto antes. Detecção precoce salva vidas.")
    elif classe == "nevus":
        st.success("✅ Parece ser algo benigno, mas é importante manter o acompanhamento.")
    else:
        st.info("ℹ️ Não foi possível determinar com clareza. Uma avaliação médica pode ajudar.")
