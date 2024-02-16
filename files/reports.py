import webbrowser
from filestack import Client


from fpdf import FPDF


class PdfReport:
    def __init__(self,filename):
        self.filename=filename

    def generate(self,flatmate1,flatmate2,bill):

        flatmate_1 = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate__2 = str(round(flatmate2.pays(bill,flatmate1),2))


        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        ##add logo
        pdf.image("images.jpg",w=30,h=30)

        ## Add Title

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=True)



        ## add period
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=100, h=40, txt='Names', border=0, align='C')
        pdf.cell(w=100, h=40, txt=str(bill.period), border=0, align='C',ln=True)

        # add name of flatmates
        pdf.set_font(family='Times', style='B', size=10)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='C')
        pdf.cell(w=100, h=25, txt=flatmate_1, border=0, align='C', ln=True)

        ## add second flatmate
        pdf.set_font(family='Times', style='B', size=10)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='C')
        pdf.cell(w=100, h=25, txt=flatmate__2, border=0, align='C', ln=True)



        pdf.output(f"{self.filename}")
        webbrowser.open(self.filename)
class FileSharer:
    def __init__(self,filepath,api_key="AWq9lvfiSS9yY0Jm8ja6Az"):
        self.filepath=filepath
        self.api_key=api_key

    def share(self):
        client= Client(self.api_key)
        new_file_link= client.upload(filepath=self.filepath)
        return new_file_link.url