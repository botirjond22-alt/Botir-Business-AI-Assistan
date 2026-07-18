from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "BU_YERGA_TOKEN"

async def start(update: Update, context):
    await update.message.reply_text("Salom! Men Botir Business AI yordamchisiman.")

async def javob(update: Update, context):
    await update.message.reply_text("Savolingiz qabul qilindi: " + update.message.text)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, javob))

app.run_polling()