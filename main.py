from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# === AICI COMPLETEAZĂ CU DATELE TALE ===
TELEGRAM_BOT_TOKEN = "8107923831:AAEijMxg3rw-CdWRMICbAIJURWFj5LW2tEs"
TELEGRAM_CHAT_ID = "1974404417"
# =======================================

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
    try:
        data = request.json.get("message", {})
        symbol = data.get("symbol")
        direction = data.get("direction")
        timeframe = data.get("timeframe")
        entry = data.get("entry")
        tp = data.get("tp")
        sl = data.get("sl")

        message = f"📈 Signal:\nPair: {symbol}\nType: {direction}\nTF: {timeframe}\nEntry: {entry}\nTP: {tp}\nSL: {sl}"
        send_telegram_message(message)

        return jsonify({"status": "sent", "message": message}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
