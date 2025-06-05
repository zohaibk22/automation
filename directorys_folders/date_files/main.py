from pathlib import Path
from datetime import datetime


if __name__ == '__main__':
    path = Path("files")

    files = path.glob("**/*.txt")
    print(files, "FILES")
    for val in files:
        print(val, "VAL------")
        
        if val.is_file():
            print(val.stat(), "STATTTT")
            
            stats = val.stat().st_ctime
            # print(stats)
            date_created = datetime.fromtimestamp(stats)
            date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
            print(date_created_str)
            new_name = date_created_str + "-" + val.name
            print(new_name)
            new_path = val.with_name(new_name)
            print(new_path)
            # val.rename(new_path)


    # seconds_created = path.stat().st_ctime
    # date_created = datetime.fromtimestamp(seconds_created)
    # date_created_str = date_created.strftime("%Y-%m-$d_%H:%M:%S")
    # print(f"File created on: {date_created}")


