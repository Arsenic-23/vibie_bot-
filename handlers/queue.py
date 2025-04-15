# vibie_bot/handlers/queue.py

import httpx
from telegram import Update
from telegram.ext import ContextTypes

BACKEND_BASE_URL = "https://your-backend-url.com"  # Replace with your backend

async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    if chat.type not in ["group", "supergroup"]:
        await context.bot.send_message(chat_id=chat.id, text="Use /queue in a group stream.")
        return

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(f"{BACKEND_BASE_URL}/stream/queue/{chat.id}")
            data = res.json()

        current = data.get("current")
        upcoming = data.get("upcoming", [])

        if not current:
            await context.bot.send_message(chat_id=chat.id, text="No songs are currently playing.")
            return

        text = f"🎶 <b>Now Playing:</b>\n<b>{current['title']}</b>\n"

        if upcoming:
            text += "\n<b>Next Up:</b>\n"
            for i, song in enumerate(upcoming[:5], start=1):
                text += f"{i}. {song['title']}\n"
        else:
            text += "\nNo songs in the queue."

        await context.bot.send_message(chat_id=chat.id, text=text, parse_mode="HTML")

    except Exception as e:
        print("Queue error:", e)
        await context.bot.send_message(chat_id=chat.id, text="Couldn't fetch the current queue.")