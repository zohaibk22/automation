from pathlib import Path
if __name__ == "__main__":
    root_dir = Path("rename_all_paths/files")
    file_path = root_dir.glob("**/*")

    for file in file_path:
        if file.is_file():
            parent_folder = file.parts
            print(parent_folder)
            new_name = f"{parent_folder[2]}-{file.name}"
            new_path = file.with_name(new_name)
            file.rename(new_path)
            



   
     