# 🛠️ Notas Técnicas – Projeto DermatoLens

## 🔧 Ambiente de Desenvolvimento Local

- **Python recomendado:** 3.10.11
- **Motivo:** Evita conflitos de compatibilidade com TensorFlow
- **Gerenciador de pacotes:** pip >= 23

## ✅ Pacotes essenciais

```
streamlit==1.32.0
pandas==1.4.4
numpy==1.21.5
tensorflow==2.11.0
scikit-learn==1.1.3
tqdm==4.67.1
fpdf==1.7.2
Pillow==9.4.0
```

---

## 🚫 Problema conhecido com Python 3.12

- **Erro:** TensorFlow 2.12 não possui wheel compatível com Python 3.12
- **Impacto:** O deploy no Streamlit Cloud falha se usar `tensorflow==2.12.0`
- **Solução:** Usar `tensorflow==2.11.0` no `requirements.txt` do repositório

---

## 📦 Outras boas práticas

- Nunca versionar `.venv/` ou `__pycache__/`
- Verificar conflitos entre `streamlit`, `tensorflow` e `numpy` em ambientes mistos
- Validar deploy com `streamlit run app/app.py` antes de push final

---

🧠 Este arquivo serve como referência de ambiente para desenvolvimento e deploy.