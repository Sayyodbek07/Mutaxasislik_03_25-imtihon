import requests
import time

TOKEN = "8488082831:AAHfDJMbkzDPBGytPnAHdWCj11ChxnJwUiM"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

CATEGORIES = {
    "📰 Daryo.uz": "https://daryo.uz/feed",
    "🌐 Kun.uz": "https://kun.uz/news/rss",
    "🗞 Gazeta.uz": "https://www.gazeta.uz/uz/rss/"
}


def get_updates(offset=None):
    resp = requests.get(BASE_URL + "getUpdates", params={"offset": offset, "timeout": 100})
    return resp.json().get("result", [])

def send_message(chat_id, text, reply_markup=None):
    payload = {"chat_id": chat_id, "text": text}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(BASE_URL + "sendMessage", json=payload)


def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            message = update.get("message")
            if not message:
                continue
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            if text == "/start":
                keyboard = {
                    "keyboard": [[{"text": k}] for k in CATEGORIES.keys()],
                    "resize_keyboard": True
                }
                send_message(chat_id, "Salom! Kategoriyani tanlang 👇", keyboard)

            elif text in CATEGORIES:
                send_message(chat_id, f"Siz tanladingiz: {text}\nYangiliklarni keyin qo‘shamiz ✅")

        time.sleep(1)

if __name__ == "__main__":
    main()


