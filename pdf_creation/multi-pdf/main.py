import pandas as pd
from fpdf import FPDF
from pathlib import Path
from utils.create_pdf import create_pdf

if __name__ == "__main__":
    data = Path('data/data.xlsx')
    print(data.exists(),  'EXISTS')
    print(data, "DATA")
    df = pd.read_excel(data)
    
    # Remove row numbers (reset index)
    df = df.reset_index(drop=True)
    
    print(df, "DF")
    cols = df.columns

    output_dir = Path('output_pdfs')
    output_dir.mkdir(exist_ok=True)

    for index, row in df.iterrows():
        print(row['kingdom'], "ROW")
        pdf = create_pdf(row, cols[1:])

      
        output_path = output_dir / f"{row['name'].replace(' ', '_')}.pdf"
        pdf.output(str(output_path))
        print(f"Created PDF: {output_path}")



    