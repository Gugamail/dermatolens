import os
import pandas as pd
import uuid
from datetime import datetime

PASTA_COLAB = "banco_colaborativo/imagens"  # 🔴 PONTO DE ADAPTAÇÃO EXPLÍCITO
CSV_COLAB = "banco_colaborativo/dados.csv"
os.makedirs(PASTA_COLAB, exist_ok=True)

def tratar_contribuicao(imagem_pil, classe_predita, confianca):
    id_unico = f"DL-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
    caminho = os.path.join(PASTA_COLAB, f"{id_unico}.jpg")
    imagem_pil.save(caminho, format="JPEG")

    registro = pd.DataFrame([{
        "id_imagem": id_unico,
        "classe_predita": classe_predita,
        "confianca": round(confianca * 100, 2),
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    if os.path.exists(CSV_COLAB):
        registro.to_csv(CSV_COLAB, mode='a', index=False, header=False)
    else:
        registro.to_csv(CSV_COLAB, index=False)
    return id_unico
