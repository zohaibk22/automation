from fpdf import FPDF
from pathlib import Path


if __name__ == "__main__":
    pdf = FPDF(orientation='P', unit='pt', format='letter')
    pdf.add_page()

    pdf.image('assets/download-1.jpg',w=80, h=50, x=500)

    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0,h=50, txt="My First PDF", align='C', border=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=0,h=50, txt="Description", )

    output_dir = Path('pdfs')
    output_dir.mkdir(exist_ok=True)

   

    pdf.output(output_dir / 'my_first_pdf.pdf')

