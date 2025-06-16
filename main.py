from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Poți folosi variabile din Environment sau direct valori hardcodate
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1974404417")

@app.route("/", methods=["GET"])
def home():
    return "✅ Webhook activ"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json.get("message")
        if not data:
            return {"error": "No 'message' in payload"}, 400

        symbol = data.get("symbol")
        direction = data.get("direction")
        timeframe = data.get("timeframe")
        entry = data.get("entry")
        tp = data.get("tp")
        sl = data.get("sl")

        # Verificăm dacă toate valorile există
        if not all([symbol, direction, timeframe, entry, tp, sl]):
            return {"error": "Date incomplete"}, 400

        # Creăm mesajul pentru Telegram
        message = f"""📊 Semnal TradingView:
✅ {direction} {symbol} ({timeframe})
🎯 Entry: {entry}
📈 TP: {tp}
📉 SL: {sl}"""

        send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(send_url, json=payload)
        if response.status_code != 200:
            return {"error": "Eroare la trimiterea pe Telegram"}, 500

        return {"status": "Mesaj trimis"}, 200

    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
