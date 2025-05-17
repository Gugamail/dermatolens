import os
import pandas as pd
from datetime import datetime

CAMINHO_REGISTRO = "triagens.csv"

def registrar_triagem(nome_arquivo, classe_predita, confianca):
    registro = pd.DataFrame([{
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "arquivo": nome_arquivo,
        "classe": classe_predita,
        "confianca": f"{confianca:.2%}"
    }])
    if os.path.exists(CAMINHO_REGISTRO):
        registro.to_csv(CAMINHO_REGISTRO, mode='a', index=False, header=False)
    else:
        registro.to_csv(CAMINHO_REGISTRO, index=False)
