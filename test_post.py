import requests
import json

url = 'http://127.0.0.1:80'
headers = {'Content-Type': 'application/json'}
data = {
    "message": {
        "symbol": "EURUSD",
        "direction": "BUY",
        "timeframe": "5m",
        "entry": 1.12345,
        "tp": 1.12545,
        "sl": 1.12145
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.text)
