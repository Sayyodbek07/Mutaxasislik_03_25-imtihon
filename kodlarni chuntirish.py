# 1. Kutubxonalarni ulash
# import requests
# import time
#
#
# requests → internetga so‘rov yuborish (Telegram API bilan gaplashish uchun).
#
# time → time.sleep(1) orqali kodni biroz to‘xtatib turish uchun.
#
# 2. Bot sozlamalari
# TOKEN = "...."
# BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
#
#
# TOKEN → BotFather’dan olingan token.
#
# BASE_URL → har bir API so‘rovi shu manzilga yuboriladi. Masalan:
#
# https://api.telegram.org/bot<TOKEN>/getUpdates
#
# https://api.telegram.org/bot<TOKEN>/sendMessage
#
# 3. Kategoriyalar (RSS manzillar)
# CATEGORIES = {
#     "📰 Daryo.uz": "https://daryo.uz/feed",
#     "🌐 Kun.uz": "https://kun.uz/news/rss",
#     "🗞 Gazeta.uz": "https://www.gazeta.uz/uz/rss/"
# }
#
#
# Bu lug‘at (dict) tugmalarda ko‘rinadigan matn (masalan, 📰 Daryo.uz) va uning RSS manzilini saqlaydi.
#
# Hozircha RSS ishlatilmayapti, faqat nomlar bor.
#
# 4. Yangilanishlarni olish (getUpdates)
# def get_updates(offset=None):
#     resp = requests.get(BASE_URL + "getUpdates", params={"offset": offset, "timeout": 100})
#     return resp.json().get("result", [])
#
#
# getUpdates → foydalanuvchi yuborgan xabarlarni olish uchun Telegram API so‘rovi.
#
# offset → eski xabarlarni qaytarmaslik uchun ishlatiladi.
#
# resp.json() → Telegram’dan kelgan JSON javobni dictga aylantiradi.
#
# .get("result", []) → foydalanuvchi xabarlari ro‘yxati.
#
# 5. Xabar yuborish (sendMessage)
# def send_message(chat_id, text, reply_markup=None):
#     payload = {"chat_id": chat_id, "text": text}
#     if reply_markup:
#         payload["reply_markup"] = reply_markup
#     requests.post(BASE_URL + "sendMessage", json=payload)
#
#
# chat_id → qaysi odamga yuborish kerak.
#
# text → yuboriladigan matn.
#
# reply_markup → qo‘shimcha tugmalar (masalan, kategoriyalar menyusi).
#
# requests.post → Telegram serveriga xabar yuboradi.
#
# 6. Asosiy funksiya (main)
# def main():
#     offset = None
#     while True:
#         updates = get_updates(offset)
#         for update in updates:
#             offset = update["update_id"] + 1
#             message = update.get("message")
#             if not message:
#                 continue
#             chat_id = message["chat"]["id"]
#             text = message.get("text", "")
#
#
# while True: → bot doimiy ishlaydi.
#
# get_updates → yangi xabarlarni oladi.
#
# offset → oxirgi update_idni eslab qoladi, eski xabarlar qaytib kelmaydi.
#
# chat_id → kim yuborganini aniqlaydi.
#
# text → foydalanuvchi yuborgan matn.
#
#  7. Xabarlarni qayta ishlash
# if text == "/start":
#     keyboard = {
#         "keyboard": [[{"text": k}] for k in CATEGORIES.keys()],
#         "resize_keyboard": True
#     }
#     send_message(chat_id, "Salom! Kategoriyani tanlang 👇", keyboard)
#
# elif text in CATEGORIES:
#     send_message(chat_id, f"Siz tanladingiz: {text}\nYangiliklarni keyin qo‘shamiz ✅")
#
#
# Agar foydalanuvchi /start yuborsa:
#  Bot unga menyu tugmalarini yuboradi (📰 Daryo.uz, 🌐 Kun.uz, 🗞 Gazeta.uz).
#
# Agar foydalanuvchi tugmalardan birini bossa:
#  Bot hozircha faqat "Siz tanladingiz... keyin qo‘shamiz ✅" deb yozadi.
# (chunki hali yangiliklarni o‘qib beradigan funksiya yo‘q).
#
# 8. Doimiy ishlash
# time.sleep(1)
#
#
# Bot har safar tekshiruvdan so‘ng 1 soniya kutadi, keyin yana yangi xabarlarni qidiradi.
#

