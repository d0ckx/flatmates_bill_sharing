import os
import webbrowser

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    create a pdf file that comtains data about flatmates such as
    their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon
        pdf.image("files/house.png", w=38, h=30)

        # add the title to the pdf
        pdf.set_font(family="times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate1_pay, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate2_pay, border=0, ln=1)

        # change directory to open file from there
        os.chdir("files")
        # save file in directory
        pdf.output(self.filename)
        # automatically open file in browser
        webbrowser.open("file://" + os.path.realpath(self.filename))


class FileSharer:

    def __init__(self, filepath, api_key="API"):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
