# vibie_bot/handlers/start.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

VIBIE_DESCRIPTION = """
<b>Welcome to Vibie!</b>  
Where <i>music meets moments</i> — stream songs together with your group in real time.

<b>What you can do:</b>
• Create a shared group jukebox  
• Play and queue songs with friends  
• Like or skip tracks together  
• Join the stream via our beautiful Mini App  
• See who's vibing live  
• Powered by high-quality audio streaming

<b>Start a vibe, keep the music alive.</b>  
Type /help to see all available commands.
"""

JOIN_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎶 Join Stream", url="https://your-mini-app.vercel.app")],
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=VIBIE_DESCRIPTION,
        reply_markup=JOIN_BUTTON,
        parse_mode="HTML",
        disable_web_page_preview=True
    )