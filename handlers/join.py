# vibie_bot/handlers/join.py

import httpx
from telegram import Update
from telegram.ext import ContextTypes

BACKEND_BASE_URL = "https://your-backend-url.com"  # Change to your deployed backend

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    # Avoid processing if it's not a group
    if chat.type not in ["group", "supergroup"]:
        await context.bot.send_message(
            chat_id=chat.id,
            text="You can only join streams in groups.",
        )
        return

    try:
        # Register the user in the backend stream
        payload = {
            "group_id": str(chat.id),
            "user_id": str(user.id),
            "name": user.full_name,
            "username": user.username or "",
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(f"{BACKEND_BASE_URL}/stream/join", json=payload)
            data = res.json()

        participants = data.get("participant_count", "?")

        await context.bot.send_message(
            chat_id=chat.id,
            text=f"✨ <b>{user.full_name}</b> joined the stream!\n"
                 f"👥 Vibers vibing together: <b>{participants}</b>",
            parse_mode="HTML"
        )

    except Exception as e:
        print("Join error:", e)
        await context.bot.send_message(
            chat_id=chat.id,
            text="Something went wrong while joining the stream.",
        )