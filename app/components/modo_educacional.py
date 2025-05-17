import streamlit as st

# Mapeamento de classes para nomes completos e explicações
CLASSES_NOMES = {
    "melanoma": "Melanoma",
    "bcc": "Carcinoma Basocelular",
    "scc": "Carcinoma Espinocelular",
    "ak": "Queratose Actínica",
    "nevus": "Nevo Melanocítico",
    "df": "Dermatofibroma",
    "infl": "Lesão Inflamatória",
    "outros": "Lesão Indeterminada"
}

EXPLICACOES = {
    "melanoma": "A imagem apresentou assimetria, bordas irregulares, múltiplas tonalidades ou variações abruptas de cor — características associadas ao melanoma, uma lesão maligna agressiva.",
    "bcc": "A lesão mostra brilho perolado, vasos visíveis (telangiectasias) e bordas elevadas — sinais típicos do carcinoma basocelular, o câncer de pele mais comum e de crescimento lento.",
    "scc": "A superfície apresenta escamas, crostas ou ulcerações — padrões visualmente compatíveis com o carcinoma espinocelular, de risco intermediário.",
    "ak": "A IA detectou áreas ásperas, com escamação fina e tonalidade rósea ou amarronzada — características comuns em queratoses actínicas, que são pré-cancerosas.",
    "nevus": "A imagem possui bordas regulares, coloração homogênea e simetria — padrões típicos de nevos melanocíticos benignos.",
    "df": "A IA identificou uma coloração firme e estrutura centrada com pigmentação periférica — sugerindo dermatofibroma, uma lesão cutânea benigna comum.",
    "infl": "A imagem mostra sinais de inflamação, vasos dilatados ou eritema difuso — padrões compatíveis com lesões vasculares ou inflamatórias, geralmente não malignas.",
    "outros": "A lesão não apresenta sinais claros o suficiente para classificar como melanoma, nevo ou outra classe — a IA rotulou como “indeterminada” por precaução."
}

def rodar_modo_educacional(img_pil, classe_predita, confianca):
    st.subheader("🎓 Modo Educacional")

    st.markdown("Antes de ver o resultado da IA, qual é a sua hipótese visual para esta imagem?")
    escolha = st.selectbox(
        "Escolha uma opção:",
        list(CLASSES_NOMES.keys()),
        format_func=lambda x: CLASSES_NOMES[x]
    )

    st.image(img_pil, caption="Imagem em análise", use_column_width=True)

    st.divider()
    st.subheader("🔍 Resultado da IA")

    nome_predito = CLASSES_NOMES.get(classe_predita, classe_predita)
    explicacao = EXPLICACOES.get(classe_predita, "A IA não forneceu explicações adicionais.")

    if escolha == classe_predita:
        st.success(f"✔️ A IA sugeriu a **mesma classificação** que você selecionou: **{nome_predito}**.")
    else:
        st.warning(f"⚠️ A IA sugeriu uma **classificação diferente**: **{nome_predito}**.")

    st.markdown(f"**Nível de confiança estimado:** {confianca:.2%}")
    st.markdown(f"📘 **Explicação da IA:** {explicacao}")
    st.info("Este exercício tem finalidade exclusivamente educativa.")
