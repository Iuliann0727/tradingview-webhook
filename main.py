from flask import Flask, request
import json
import os
import requests

app = Flask(__name__)

# Telegram Bot Settings (înlocuiește cu valorile tale reale)
TELEGRAM_BOT_TOKEN = "8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs"
TELEGRAM_CHAT_ID = "1974404417"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.status_code

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return {"status": "missing message"}, 400

    msg = data["message"]
    try:
        symbol = msg["symbol"]
        direction = msg["direction"]
        timeframe = msg["timeframe"]
        entry = msg["entry"]
        tp = msg["tp"]
        sl = msg["sl"]

        # Formatăm mesajul pentru Telegram
        text = f"📈 Semnal TradingView:\n\nSymbol: {symbol}\nDirection: {direction}\nTimeframe: {timeframe}\nEntry: {entry}\nTP: {tp}\nSL: {sl}"
        send_telegram_message(text)
        return {"status": "message sent"}, 200

    except KeyError:
        return {"status": "incomplete data"}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
