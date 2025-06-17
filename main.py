from flask import Flask, request
import requests
import json

app = Flask(__name__)

TELEGRAM_TOKEN = "8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs"
CHAT_ID = "1974404417"

@app.route("/", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return {"status": "missing message"}, 400

        msg = data["message"]

        text = f"📊 *Semnal TradingView*\n" \
               f"➡️ Symbol: {msg.get('symbol')}\n" \
               f"📈 Direction: {msg.get('direction')}\n" \
               f"⏱ Timeframe: {msg.get('timeframe')}\n" \
               f"🎯 Entry: {msg.get('entry')}\n" \
               f"🏁 TP: {msg.get('tp')}\n" \
               f"🛡 SL: {msg.get('sl')}"

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }

        requests.post(url, json=payload)
        return {"status": "sent"}, 200

    except Exception as e:
        print("Eroare:", e)
        return {"status": "error", "detail": str(e)}, 500
