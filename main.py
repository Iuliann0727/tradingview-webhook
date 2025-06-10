from flask import Flask, request
import requests

app = Flask(__name__)

bot_token = '8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs'
chat_id = '1974404417'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return 'UptimeRobot check – OK', 200
    else:
        data = request.get_json()
        message = data.get('message', '⚠️ Semnal necunoscut din TradingView')

        telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': f'📈 Semnal TradingView:\n{message}'
        }

        requests.post(telegram_url, data=payload)
        print("📡 Semnal primit și trimis:", message)
        return 'OK', 200

app.run(host='0.0.0.0', port=3000)
