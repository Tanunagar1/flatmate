from fpdf import FPDF

pdf = FPDF(orientation='p',unit='pt',format='A4')
pdf.add_page()

## add text

pdf.set_font(family='Times',style='B',size=24)
pdf.cell(w=0,h=80,txt='flatmats bill',border=1,align='C',ln=True)
pdf.cell(w=100,h=40,txt='period',border=1,align='C')
pdf.cell(w=100,h=40,txt='march 2024',border=1,align='C',ln=True)


pdf.output("bill.pdf")