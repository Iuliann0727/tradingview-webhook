from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔐 Înlocuiește cu datele tale reale
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Validare date primite
        required_keys = ['symbol', 'direction', 'timeframe', 'entry', 'tp', 'sl']
        if not all(key in data for key in required_keys):
            return '[ERROR] Date incomplete', 400

        symbol = data['symbol']
        direction = data['direction']
        timeframe = data['timeframe']
        entry = data['entry']
        tp = data['tp']
        sl = data['sl']

        # 🔔 Mesaj formatat
        message = f"""📊 Semnal TradingView:
🪙 Symbol: {symbol}
📈 Direction: {direction}
⏱ Timeframe: {timeframe}
🎯 Entry: {entry}
✅ TP: {tp}
❌ SL: {sl}"""

        # Trimite mesaj pe Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        response = requests.post(url, json=payload)
        if response.status_code != 200:
            return f"[ERROR] Trimitere eșuată: {response.text}", 500

        return '[OK] Semnal trimis pe Telegram', 200

    except Exception as e:
        return f"[ERROR] {str(e)}", 500

@app.route('/', methods=['GET'])
def check():
    return '✅ Webhook activ!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
