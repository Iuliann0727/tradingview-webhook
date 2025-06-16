from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 Înlocuiește aceste valori cu datele tale reale
TELEGRAM_BOT_TOKEN = "PASTEAZĂ_AICI_TOKENUL_TĂU"
TELEGRAM_CHAT_ID = "PASTEAZĂ_AICI_CHAT_ID"

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Validare: toate cheile trebuie să fie prezente
        expected_keys = ['symbol', 'direction', 'timeframe', 'entry', 'tp', 'sl']
        if not all(k in data for k in expected_keys):
            return '[ERROR] Date incomplete în fișier.', 400

        # Extragem valorile
        symbol = data['symbol']
        direction = data['direction']
        timeframe = data['timeframe']
        entry = data['entry']
        tp = data['tp']
        sl = data['sl']

        # 🧾 Mesajul pentru Telegram
        message = f"""📡 Semnal TradingView:
🪙 Symbol: {symbol}
📊 Direcție: {direction}
⏱ Timeframe: {timeframe}
🎯 Entry: {entry}
✅ Take Profit: {tp}
❌ Stop Loss: {sl}"""

        # Trimitere mesaj
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        response = requests.post(telegram_url, json=payload)
        if response.status_code != 200:
            return f'[ERROR] Eroare Telegram: {response.text}', 500

        return '[OK] Mesaj trimis pe Telegram.', 200

    except Exception as e:
        return f'[EXCEPTION] {str(e)}', 500

@app.route('/', methods=['GET'])
def check():
    return '✅ Webhook activ și funcțional.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
