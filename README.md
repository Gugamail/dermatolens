# DermatoLens

DermatoLens é uma plataforma educacional e assistiva para apoio à triagem visual de lesões dermatológicas, voltada a estudantes, professores e profissionais de saúde.

## Estrutura do Projeto

- `app.py`: ponto de entrada do aplicativo Streamlit.
- `pages/`: páginas do sistema exibidas como abas laterais.
- `components/`: funções reutilizáveis (interface, gráficos, PDF, câmera, etc.)

## Módulos disponíveis

1. **Simulado** — prática de classificação com feedback.
2. **Explicador IA** — exibe como o modelo toma decisões.
3. **Painel Educacional** — acompanhamento da turma.
4. **Progresso do Aluno** — evolução individual por classe.
5. **Galeria de Erros** — exemplos onde o aluno errou.
6. **Captura por Câmera** — foto direta com consentimento.
7. **Contribuição** — modo de envio colaborativo.
8. **Portfólio PDF** — geração automática de relatórios.
9. **Sobre o Projeto** — propósitos, autores e uso pretendido.

## Execução

```bash
pip install -r requirements.txt
streamlit run app.py
```