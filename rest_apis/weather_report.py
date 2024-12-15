import requests
from dotenv import load_dotenv
import os

load_dotenv()
KEY=os.getenv('WEATHER_API_KEY') or ""


def get_weather_data(city, unit='metric', api_key=KEY):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={unit}"
    try:
        r = requests.get(url)
        content = r.json()

        weather_data = content['list']
    except KeyError as e:
        raise KeyError("Something went wrong")
    
    with open('data.txt', 'r') as file:
        lines = file.readlines()

    # Only proceed if there is at least one line
    if lines:
        with open('data.txt', 'w') as file:
            file.write(lines[0])
    for data in weather_data:
        city_val = city
        time = data['dt_txt']
        temp = data['main']['temp']
        description = data['weather'][0]['description']

        # print(city_val)
        # print(time)
        # print(temp)
        # print(description)
        file = open("data.txt", "a")
        file.write(f"\n{city_val},{time},{temp},{description}")
        file.close()

        


def main():
    get_weather_data("Aleppo")

main()