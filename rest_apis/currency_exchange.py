from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello Currency Rate API</h1> <p> Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<string:curr_1>-<string:curr_2>')
def api( curr_1, curr_2):
    print(curr_1, "curr_1")
    print(curr_2, "curr_2")
    url = url = f"https://www.x-rates.com/calculator/?from={curr_1}&to={curr_2}&amount=1#google_vignette"
    try:
        r = requests.get(url).text
    except Exception as e:
        print(e, "Did i make it here")
        return {'error': "internal error"}, 503
        
    
    soup = BeautifulSoup(r,'html.parser')
    # print(soup.prettify())
    
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = rate[:5]
    
    return jsonify({"data": {
        "from": curr_1,
        "to": curr_2,
        "exchange_rate": rate
    }}), 200



app.run(host='0.0.0.0', port=8080, debug=True)


# class Car:
#     def __init__(self, model, year, doors):
#         self.model = model
#         self.year = year
#         self.doors = doors

#     def __str__(self):
#         return f"{self.model}"


# class Ferrari(Car):
#     def __init__(self, model, year, doors, name):
#         super().__init__(self,model, year, doors)
#         self.name = name