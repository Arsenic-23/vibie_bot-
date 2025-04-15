# vibie_bot/bot.py

import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from handlers import start, help_command, join, play, queue, skip, like

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set this in Termux env or .env

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("queue", queue))
    app.add_handler(CommandHandler("skip", skip))
    app.add_handler(CommandHandler("like", like))

    # Optional: Delete all command messages after handling
    app.add_handler(
        MessageHandler(filters.COMMAND, lambda update, context: update.message.delete())
    )

    print("Vibie Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()