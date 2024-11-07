import requests

class MyCustomError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

def get_news(topic, from_date, to_date, language='en', api_key=''):
    try:
        r = requests.get(f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}")
        r = r.json()
        articles = r['articles']
    except KeyError as e :
        raise  KeyError("Something went wrong")


    for article in articles:
        print(f"article:  {article}")



def main():
    topic  = input("Enter topic: ")
    date_start = input("Enter Start Date: ")
    date_end = input("Enter End Date: ")
    lang = input("Enter Lang: ")
    api = input("Enter Api Key: ")

    get_news(topic, date_start, date_end,language=lang, api_key=api)


main()
