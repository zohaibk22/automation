from fpdf import FPDF

def create_pdf(data, cols):
    name = data.get('name', 'No Name')


    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    # Set background color (light gray)
    pdf.set_fill_color(r=240, g=240, b=240)
    pdf.rect(x=0, y=0, w=pdf.w, h=pdf.h, style='F')

    # Title styling
    pdf.set_font(family='Times', style='B', size=28)
    pdf.set_text_color(r=40, g=70, b=150)
    pdf.cell(w=0, h=50, txt=f"Name: {name}", ln=True, align='C')

    # Section styling

    for val in cols:
        
        pdf.set_font(family='Times', style='B', size=22)
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.cell(w=120, h=30, txt=f"{val.title()}:", ln=False)
        pdf.set_font(family='Times', style='', size=22)
        pdf.set_text_color(r=80, g=80, b=80)
        pdf.cell(w=0, h=30, txt=f"{data.get(val, 'No Data')}", ln=True)

    return pdf
