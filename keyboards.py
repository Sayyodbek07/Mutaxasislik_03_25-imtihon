from telebot import types

def general_menu():
    keyboards = types.ReplyKeyboardMarkup()
    daryo = types.KeyboardButton("📰 Daryo")
    kun = types.KeyboardButton("🌐 Kun")
    gazeta = types.KeyboardButton("🗞 Gazeta")

    keyboards.row(daryo)
    keyboards.row(kun)
    keyboards.row(gazeta)
    return keyboards