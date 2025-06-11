from flask import Flask, request
import requests

app = Flask(__name__)

bot_token = '8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs'
chat_id = '1974404417'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return 'OK', 200
    else:
        data = request.get_json()
        msg = data.get('message', {})

        symbol = msg.get('symbol', '–')
        direction = msg.get('direction', '–')
        timeframe = msg.get('timeframe', '–')
        entry = msg.get('entry', '–')
        tp = msg.get('tp', '–')
        sl = msg.get('sl', '–')

        text = (
            f"🚨 Semnal nou [{symbol}] – {direction}\n"
            f"🕒 Interval: {timeframe}\n"
            f"🔹 Entry: {entry}\n"
            f"🎯 Take Profit: {tp}\n"
            f"🛑 Stop Loss: {sl}"
        )

        telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {'chat_id': chat_id, 'text': text}
        requests.post(telegram_url, data=payload)
        print("📡 Trimis mesaj:", text)

        return 'OK', 200

app.run(host='0.0.0.0', port=3000)
