from pathlib import Path
import zipfile


if __name__ == "__main__":
    root_dir = Path('files')
    archive_path = root_dir / Path('archive.zip')
    # files = root_dir.glob("*.txt")

    with zipfile.ZipFile(archive_path, 'w') as zf:
        for path in root_dir.rglob("*.txt"):
            zf.write(path)
            path.unlink()