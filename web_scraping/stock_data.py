import requests
from datetime import datetime
import time


stock = input('Enter in symbol for stock: ')
date = input('Enter in the date  (yyy-mm-dd): ')

url = f'https://api.polygon.io/v1/open-close/{stock}/{date}?adjusted=true&apiKey=1vrEwg2M4HMStFlbpinp2aTSDlt2XvhY'

try:
    data = requests.get(url).content
    print(data, "DATA")
except:
    raise KeyError

filename = f"{stock} - {date}.txt"
with open(filename, 'w') as file:
    file.write(str(data))