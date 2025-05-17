import streamlit as st
import os
import pandas as pd
from datetime import datetime
from PIL import Image
import uuid

# === Placeholder para caminho remoto no futuro ===
PASTA_CONTRIBUICAO = "banco_colaborativo/imagens_contribuidas"  # 🔴 Substituir por caminho de servidor no futuro
CSV_CONTRIBUICAO = "banco_colaborativo/registro_contribuicoes.csv"
os.makedirs(PASTA_CONTRIBUICAO, exist_ok=True)

def interface_contribuicao_usuario(classe_predita, confianca):
    st.divider()
    st.subheader("📤 Contribuir com a Base do DermatoLens")

    with st.expander("Quero ajudar a treinar a IA com minha imagem"):
        st.markdown("Você pode, de forma totalmente voluntária, contribuir com o aprimoramento da IA do DermatoLens. Sua imagem será armazenada de forma **anônima e segura**, apenas para fins de pesquisa clínica e educacional.")

        arquivo = st.file_uploader("Envie sua imagem (JPG ou PNG)", type=["jpg", "jpeg", "png"])
        consentimento = st.checkbox("Autorizo o uso da imagem para fins de pesquisa e desenvolvimento da IA, conforme os termos de uso.")

        if arquivo and consentimento:
            try:
                imagem = Image.open(arquivo).convert("RGB")
                imagem = imagem.resize((224, 224))  # Padronização

                id_unico = f"DL-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}"
                nome_arquivo = f"{id_unico}.jpg"
                caminho_final = os.path.join(PASTA_CONTRIBUICAO, nome_arquivo)
                imagem.save(caminho_final, format="JPEG")

                dados = pd.DataFrame([{
                    "image_id": id_unico,
                    "image_year": datetime.now().year,
                    "image_source": "user_contributed",
                    "image_name": nome_arquivo,
                    "patient_id": "anonymous",
                    "sex": "unknown",
                    "age_approx": -1,
                    "anatom_site_general_challenge": "unknown",
                    "diagnosis": classe_predita,
                    "benign_malignant": "benign" if classe_predita in ["nevus", "df"] else "malignant",
                    "target": 1 if classe_predita == "melanoma" else 0
                }])

                if os.path.exists(CSV_CONTRIBUICAO):
                    dados.to_csv(CSV_CONTRIBUICAO, mode="a", header=False, index=False)
                else:
                    dados.to_csv(CSV_CONTRIBUICAO, index=False)

                st.success("✅ Contribuição registrada com sucesso!")
                st.markdown(f"**Número de protocolo:** `{id_unico}`")
                st.caption("Agradecemos pela sua colaboração para tornar o DermatoLens cada vez melhor.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar a imagem: {e}")
        elif arquivo and not consentimento:
            st.warning("Você deve autorizar o uso da imagem para concluir a contribuição.")
