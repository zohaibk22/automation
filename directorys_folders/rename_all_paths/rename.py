from pathlib import Path
if __name__ == "__main__":
    root_dir = Path("files")
    file_path = root_dir.iterdir()
    print(file_path, "file")

    for file in file_path:
        print(file)


    