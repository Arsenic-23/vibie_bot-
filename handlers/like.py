# vibie_bot/handlers/like.py

import httpx
from telegram import Update
from telegram.ext import ContextTypes

BACKEND_BASE_URL = "https://your-backend-url.com"  # Replace with your actual backend URL

async def like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    if chat.type not in ["group", "supergroup"]:
        await context.bot.send_message(chat_id=chat.id, text="Use /like in a group stream.")
        return

    try:
        payload = {
            "group_id": str(chat.id),
            "user_id": str(user.id),
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(f"{BACKEND_BASE_URL}/stream/like", json=payload)
            data = res.json()

        song = data.get("song")
        likes = data.get("likes", "?")

        if not song:
            await context.bot.send_message(chat_id=chat.id, text="No song is playing right now.")
            return

        title = song.get("title", "Unknown Song")

        await context.bot.send_message(
            chat_id=chat.id,
            text=f"❤️ <b>{user.full_name}</b> liked <b>{title}</b>!\n"
                 f"👍 Total likes: <b>{likes}</b>",
            parse_mode="HTML"
        )

    except Exception as e:
        print("Like error:", e)
        await context.bot.send_message(chat_id=chat.id, text="Failed to like the song.")