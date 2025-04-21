from pathlib import Path

if __name__ == "__main__":
    root_dir = Path("files")
    file_paths = root_dir.glob("**/**")
    for val in file_paths:
        if val.is_file():
            print(val)
            dir_val = val.parts[1:]
            new_name = "-".join(dir_val)
            new_path = val.with_name(new_name)
            val.rename(new_path)

            