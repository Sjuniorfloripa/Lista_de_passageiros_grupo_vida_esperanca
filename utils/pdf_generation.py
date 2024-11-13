import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def gerar_pdf(nomes_selecionados):

    df = pd.read_csv('dados_pessoas.csv')

    df_filtrado = df[df['Nome Completo'].isin(nomes_selecionados)]

    pdf_file = 'lista_pessoas_grupo_vida_esperanca.pdf'
    c = canvas.Canvas(pdf_file, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(largura / 2, altura - 50, "Grupo Vida e Esperança")

    c.setFont("Helvetica", 10)
    y_position = altura - 100
    linha_altura = 15

    for i, (_, row) in enumerate(df_filtrado.iterrows()):
        linha = f"{row['Nome Completo']} - CPF: {row['CPF']}" if pd.notna(row['CPF']) else f"{row['Nome Completo']} - RG: {row['RG']}"

        if i % 2 == 1:
            c.setFillColor(colors.lightgrey)
            c.rect(45, y_position - 3, largura - 90, linha_altura, stroke=0, fill=1)

        c.setFillColor(colors.black)
        c.drawString(50, y_position, linha)

        y_position -= linha_altura
        if y_position < 50:
            c.showPage()
            y_position = altura - 50

    c.save()
    return pdf_file
