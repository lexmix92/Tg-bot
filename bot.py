import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")  # токен подтянется из Render

async def start(update, context):
    await update.message.reply_text("Привет! Я минимальный бот 😄")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
