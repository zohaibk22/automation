# Change file extensions of files in /file directory from .txt to .csv


from pathlib import Path


if __name__ == "__main__":
    path = Path('files')
    files = path.glob('**/*.txt')
    for file in files:
        new_file_val = file.with_suffix(".csv")
        file.rename(new_file_val)
