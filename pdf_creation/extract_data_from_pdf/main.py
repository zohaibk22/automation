import fitz
from pathlib import Path

def main():

    file_path = Path('files/students.pdf')

    with fitz.open(file_path) as file:
        for page in file:
            print(page.get_text())


if __name__ == "__main__":
    main()