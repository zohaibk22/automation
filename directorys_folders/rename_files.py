from pathlib import Path

dir_val = Path("files")
file_paths = dir_val.iterdir()
print(file_paths, "file paths")
print(Path.cwd(), 'path.cwd()')

for path in file_paths:
    print("HELLO")
    new_filename = f"zohaib-{path.stem}{path.suffix}"
    new_filepath = path.with_name(new_filename)
    # new_filepath = Path(new_filename)
    print(new_filepath, "test")
    path.rename(new_filepath)


