from pathlib import Path

root_dir = Path('destination')

for path in root_dir.rglob("*"):
    print(path)

    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()
