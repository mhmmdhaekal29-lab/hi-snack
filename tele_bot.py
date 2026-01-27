import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = os.getenv("8525944078:AAEtICQDqJcX5VCgMepLUMHQ78L7eN0Unlo")

app = ApplicationBuilder().token(TOKEN).build()

async def reply(update: Update, context):
    await update.message.reply_text("Bot aktif 24/7 🚀")

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot sedang berjalan...")
app.run_polling()
