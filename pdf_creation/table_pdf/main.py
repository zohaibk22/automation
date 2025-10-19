import tabula
from pathlib import Path
import pandas as pd


def main():

    weather_pdf = Path('files/weather.pdf')

    table = tabula.read_pdf(weather_pdf, pages=1)
    print(table, "table")
    df = table[0]
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    df.to_csv(output_dir / 'weather_data.csv', index=False)

    



if __name__ == "__main__":
    main()