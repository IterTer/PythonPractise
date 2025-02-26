import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their name,
    their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('house.png', w=30, h=30)

        # Add title
        pdf.set_font(family='Times', size=24, style='B')
        # C = centered, w=0 will take the whole length of the page
        pdf.cell(w=0, h=80, txt='Apartment Bill', border=1, align='C', ln=1)

        # Add Period label and value
        # click the line you want to copy and press: CTRL + d
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Add flatmate name and the value of the payment:
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
