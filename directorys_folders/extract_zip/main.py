import zipfile
from pathlib import Path


# root_dir = Path('files')
# archive_path = root_dir / Path('archive2.zip')


# with zipfile.ZipFile(archive_path, "w") as zf:
#         for path in root_dir.glob("*.csv"):
#                 zf.write(path)
#                 path.unlink()



root_dir = Path('files')
destination_dur = Path('destination')

for path in root_dir.rglob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_dur / Path(path.stem)
        zf.extractall(path=final_path)
 