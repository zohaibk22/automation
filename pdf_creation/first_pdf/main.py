from fpdf import FPDF
from pathlib import Path


if __name__ == "__main__":
    pdf = FPDF(orientation='P', unit='pt', format='letter')
    pdf.add_page()

    pdf.image('assets/download-1.jpg',w=80, h=50, x=500)

    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0,h=50, txt="My First PDF", align='C', ln=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=0,h=50, txt="Description", ln=1)

    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=20, txt="This is my first PDF that I am creating using Python. "
                                 "I am so excited to create more PDFs using Python. "
                                 "I hope you are excited too. "
                                 "I am sure you are excited to create more PDFs using Python. "
                                 "I hope you are excited too. "
                                 "I am sure you are excited to create more PDFs using Python. "                 "I hope you are excited too. " )

    output_dir = Path('pdfs')
    output_dir.mkdir(exist_ok=True)

   

    pdf.output(output_dir / 'my_first_pdf.pdf')

