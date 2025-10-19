import tabula
from pathlib import Path

def main():
    file_path = Path('files/Table+and+Text.pdf')
    table = tabula.read_pdf(file_path, pages='all')
    print(table)

    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'extracted_data.csv'

    df = table[0]
    df.to_csv(output_file, index=False)
   

if __name__ == "__main__":
    main()