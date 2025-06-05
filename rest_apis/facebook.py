import requests



url =  "https://graph.facebook.com/v21.0/me?fields=id%2Cname%2Cposts&access_token=EAAR1Pc6ZB2MUBOwlJ9lZC5lqD5sUl4V5WDxZBd202xJywwKlhuYZCVmBGmUXm6l92wo1EzkSQeQRGuFr1qPbACxgQVqtB90lM0b9CVyIDzNQJTT9loDRAiiGv4UL2PT5VNWgg4ZCVqhfzOlNEyImvIf3iFSjJH2eXRncOUFzcJIcuq41byXDpn9LmkP0ZAKbWCU9VLidCzjmKNI3RZCvwZDZD"

response = requests.get(url)
print(response.text, "CONTENT")