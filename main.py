from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8995380950:AAHYZGlNPlyiSQS0EDmTdcIRwRW7-On4XMw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! 👋 Mi bot ya está funcionando correctamente."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot iniciado...")
app.run_polling()
