from fpdf import FPDF
from pathlib import Path


if __name__ == "__main__":
    pdf = FPDF(orientation='P', unit='pt', format='letter')
    pdf.add_page()

    pdf.image('assets/download-1.jpg',w=80, h=50)

    output_dir = Path('pdfs')
    output_dir.mkdir(exist_ok=True)


    pdf.output(output_dir / 'my_first_pdf.pdf')

