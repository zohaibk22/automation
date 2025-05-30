from pathlib import Path


search_term= input("Enter search term: ")
root_dir = Path('destination')
files = root_dir.rglob("**/*")

for file in files:
    # print(file, "file")
    if file.is_file() and search_term in file.stem:
        print(file.absolute())
