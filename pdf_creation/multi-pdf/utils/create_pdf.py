from fpdf import FPDF

def create_pdf(data):
    name = data.get('name', 'No Name')
    kingdom = data.get('kingdom', 'No Kingdom')
    phylum = data.get('phylum', 'No Phylum')
    class_val = data.get('class', 'No Class')
    order = data.get('order', 'No Order')
    sub_order = data.get('suborder', 'No Suborder')


    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
   
    pdf.set_font('Times', 'B', 24)
    pdf.cell(0, 30, f"Name: {name}", ln=True, align='C')
    pdf.set_font('Times', 'B', 24)
    pdf.cell(0, 30, "Kingdom: ", ln=False)
    pdf.set_font('Times', '', 24)
    pdf.cell(40, 30, f"{kingdom}", ln=True)
    pdf.set_font('Times', '', 24)
    pdf.set_font('Times', '', 24)
    pdf.cell(0, 30, f"Phylum: {phylum}", ln=True)
    pdf.set_font('Times', '', 24)
    pdf.cell(0, 30, f"Class: {class_val}", ln=True)
    pdf.set_font('Times', '', 24)
    pdf.cell(0, 30, f"Order: {order}", ln=True)
    pdf.set_font('Times', '', 24)
    pdf.cell(0, 30, f"Suborder: {sub_order}", ln=True)

    return pdf
