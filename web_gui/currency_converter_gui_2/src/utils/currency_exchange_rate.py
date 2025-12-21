
import requests as request
from bs4 import BeautifulSoup
def get_currency(amount_usd: float, from_currency: str = 'USD', to_currency: str = 'EUR') -> float:

    url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount={amount_usd}'
    rate = 1.0

    try:
        data = request.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        result = soup.find("span", class_="ccOutputRslt")
        if result:
            rate = result.text.split(" ")[0]
            print(rate, "RATE")
        else:
            print("Currency rate element not found")
            raise ValueError("Could not find currency rate on the page.")

    except Exception as e:
        print("Error Occurred:", e)

    return rate

