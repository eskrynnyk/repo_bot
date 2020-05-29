from flask import Flask, request
import requests
import os

app = Flask(__name__)

def send_message(chat_id, text):
    method = "sendMessage"
    token = "1222181388:AAGJgJGKBcfGdpGGipYfCQC5f0ap5whmsT4"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id, "pong")
    return {"ok": True}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))