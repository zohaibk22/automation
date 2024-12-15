import requests
from dotenv import load_dotenv
import os

load_dotenv()

KEY=os.getenv('NEWS_API_KEY') or ""


def get_news_headlines(country, api_key=KEY):
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    try:
        r = requests.get(url=url)
        content= r.json()
        articles = content['articles']
        result = []
    except KeyError as e:
        raise KeyError("Unable to get articles")
    
    for article in articles:
        result.append(f"TITLE\n '{article['title']}, '\nDESCRIPTION\n', {article["description"]}")

    return result


def main():
     print(get_news_headlines(country='us'))

    
main()
