from telebot import TeleBot
from db_products import get_info
from keyboards import general_menu

# from keyboards import *

token = "8488082831:AAHfDJMbkzDPBGytPnAHdWCj11ChxnJwUiM"
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print("Bot ishlashni boshladi")
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu aleykum news|blog botimizga xush kelibsiz. tugmalardan birini tanlang", reply_markup=general_menu())
    bot.register_next_step_handler(message, news_to_user)

def news_to_user(message):
    chat_id = message.chat.id

    if message.text == "📰 Daryo":
        news = get_info()
        for new in news:
            image = new[2]
            news_daryo = news[1]
            bot.send_photo(chat_id, image, f"{news_daryo}")

    if message.text == "🌐 Kun":
        bot.send_message(chat_id, "Kun.uz hush kelibbsiz")

    if message.text == "🗞 Gazeta":
        bot.send_message(chat_id, "gazeta.uz hush kelibbsiz")

# def send_products_list(message):
#     chat_id = message.chat.id
#

bot.polling(non_stop=True)
