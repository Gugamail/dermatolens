import streamlit as st

st.set_page_config(layout="wide")
st.title("🔬 Sobre o DermatoLens")

st.markdown("""
O **DermatoLens** é uma plataforma educacional e de triagem assistida desenvolvida para estudantes, médicos em formação e professores de dermatologia.  
Ele une **inteligência artificial aplicada à imagem médica** com práticas pedagógicas baseadas em simulações, avaliações e feedback automatizado.

---

### 🎯 Objetivo do projeto

Criar um ambiente acessível, interativo e confiável para:

- Aprender e revisar padrões visuais de lesões dermatológicas;
- Treinar a capacidade de classificação visual com base em imagens clínicas reais;
- Gerar relatórios informativos de triagens educacionais;
- Apoiar professores em atividades de sala de aula, com indicadores de progresso e desempenho.

---

### ⚙️ O que o DermatoLens oferece

- 🧠 **Simulado visual** com feedback automático por IA
- 📷 **Triagens com câmera ou upload de imagem**
- 📂 **Registro completo de interações por usuário**
- 📊 **Painéis de aprendizado e progresso**
- ❌ **Galeria de erros mais comuns**, por classe e por estudante
- 📄 **Relatórios automatizados** em PDF, com linguagem neutra e sem caráter diagnóstico

---

### ⚠️ Aviso legal

> Este sistema é destinado **exclusivamente para fins educacionais e científicos**.  
> Ele **não realiza diagnósticos médicos**, **não substitui avaliação clínica** e não deve ser usado como ferramenta de apoio à decisão médica em ambientes reais.

---

### 👨‍🏫 Público-alvo

- Estudantes de medicina e enfermagem
- Professores de dermatologia
- Clínicas universitárias
- Projetos de pesquisa em IA médica
- Hackathons e eventos científicos

---

### 🏗️ Como o projeto foi desenvolvido

O DermatoLens é baseado em:

- Dados públicos da competição **ISIC 2020**
- Modelos de IA treinados em redes convolucionais leves
- Interface desenvolvida em **Python + Streamlit**
- Visualizações com **pandas, matplotlib, seaborn**
- Estrutura modular para facilitar testes, extensão e ensino

---

### 🤝 Próximos passos

- Treinar o modelo com mais épocas (atualmente: 5)
- Ampliar o dataset com curadoria especializada
- Implantar em contexto real de sala de aula
- Possível versão PWA ou APK para acesso móvel
- Avaliar uso em projetos de extensão universitária

---

Desenvolvido por **Gustavo Leite** com base em dados públicos, código aberto e compromisso com o ensino.  
Idealizado e coordenado pela **Professora Cecília Leite**, dermatologista e docente da Universidade de Pernambuco – Campus Serra Talhada.
""")