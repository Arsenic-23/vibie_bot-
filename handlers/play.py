# vibie_bot/handlers/play.py

import httpx
from telegram import Update
from telegram.ext import ContextTypes

BACKEND_BASE_URL = "https://your-backend-url.com"  # Replace with your backend

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    # Must be used in a group
    if chat.type not in ["group", "supergroup"]:
        await context.bot.send_message(chat_id=chat.id, text="Use /play in a group stream.")
        return

    # Extract query
    query = " ".join(context.args)
    if not query:
        await context.bot.send_message(chat_id=chat.id, text="Please provide a song name.\nExample: /play Blinding Lights")
        return

    try:
        payload = {
            "group_id": str(chat.id),
            "query": query,
            "user_id": str(user.id),
            "name": user.full_name,
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{BACKEND_BASE_URL}/stream/queue", json=payload)
            data = res.json()

        song = data.get("song")
        if not song:
            await context.bot.send_message(chat_id=chat.id, text="Song not found or failed to queue.")
            return

        title = song.get("title", "Unknown Song")
        artist = song.get("artist", "")
        added_by = user.full_name

        await context.bot.send_message(
            chat_id=chat.id,
            text=f"🎵 <b>{title}</b>\n<i>added by {added_by}</i>",
            parse_mode="HTML"
        )

    except Exception as e:
        print("Play error:", e)
        await context.bot.send_message(chat_id=chat.id, text="Something went wrong while queuing the song.")