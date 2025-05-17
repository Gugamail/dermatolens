from fpdf import FPDF
import os
from datetime import datetime

class TriagemPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Documento Educacional – Triagem Automatizada", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | Este não é um laudo médico.", align="C")

def gerar_pdf_triagem(classe_predita, confianca, id_imagem, caminho_saida="triagem.pdf"):
    pdf = TriagemPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    pdf.ln(10)
    pdf.cell(0, 10, f"ID da Triagem: {id_imagem}", ln=True)
    pdf.cell(0, 10, f"Resultado do Algoritmo: {classe_predita}", ln=True)
    pdf.cell(0, 10, f"Nível de confiança: {confianca:.2%}", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, "Este documento é gerado automaticamente com base em triagem de imagem feita por algoritmo de inteligência artificial. "
                          "Seu conteúdo tem fins educativos e informativos, e **não constitui diagnóstico médico, parecer clínico, nem prescrição terapêutica**. "
                          "Para qualquer decisão sobre saúde, é fundamental consultar um(a) profissional de saúde habilitado(a).")

    pdf.output(caminho_saida)
    return caminho_saida
