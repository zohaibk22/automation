import requests
r = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-10-05&sortBy=publishedAt&apiKey=1d1bb7a6be7e45b4a462923c03521274")
r = r.json()
print(r)