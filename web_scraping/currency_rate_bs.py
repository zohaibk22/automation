from bs4 import BeautifulSoup
import requests

def get_currency(input_currency, output_currency):
    
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1#google_vignette"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')

    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[0:-4])

    return rate


inputCur = input("Enter in first currency: ")
outputCur =input("Enter in second currency: ")
print(get_currency(inputCur, outputCur))