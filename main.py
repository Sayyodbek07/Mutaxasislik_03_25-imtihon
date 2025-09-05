from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from databasa import init_db, save_plan, get_plan

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom! Men — sizning rejalashtiruvchingiz!\n\n"
        "Ertaga nimalar qilmoqchisiz? Shu xabarni menga yozing — men saqlab qo'yaman.\n"
        "Keyin, ertaga rejangizni ko'rish uchun /ertaga buyrug'ini yuboring."
    )


async def handle_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    plan_text = update.message.text

    save_plan(user_id, plan_text)

    await update.message.reply_text(
        "✅ Rejangiz saqlandi! Ertaga ko'rish uchun /ertaga bosing."
    )


async def show_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    plan = get_plan(user_id)

    if plan:
        await update.message.reply_text(f"📋 Sizning ertangi rejangiz:\n\n{plan}")
    else:
        await update.message.reply_text("❌ Siz hali hech qanday reja kiritmadingiz.")


def main():
    TOKEN = "8488082831:AAHfDJMbkzDPBGytPnAHdWCj11ChxnJwUiM"


    init_db()


    application = Application.builder().token(TOKEN).build()

    # Handlerlar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ertaga", show_plan))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_plan))

    print("✅ Bot ishga tushdi...")
    application.run_polling()

if __name__ == "__main__":
    main()