# vibie_bot/handlers/skip.py

import httpx
from telegram import Update
from telegram.ext import ContextTypes

BACKEND_BASE_URL = "https://your-backend-url.com"  # Replace with your backend URL

async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    if chat.type not in ["group", "supergroup"]:
        await context.bot.send_message(chat_id=chat.id, text="Use /skip in a group stream.")
        return

    try:
        payload = {
            "group_id": str(chat.id),
            "user_id": str(user.id),
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(f"{BACKEND_BASE_URL}/stream/skip", json=payload)
            data = res.json()

        song = data.get("song", {})
        title = song.get("title", "Unknown Song")
        votes = data.get("votes", 0)
        required = data.get("required", 3)
        skipped = data.get("skipped", False)

        if skipped:
            await context.bot.send_message(
                chat_id=chat.id,
                text=f"⏭️ <b>{title}</b> has been skipped!\nThanks for vibing!",
                parse_mode="HTML"
            )
        else:
            await context.bot.send_message(
                chat_id=chat.id,
                text=f"⚠️ <b>{user.full_name}</b> voted to skip <b>{title}</b>\n"
                     f"🗳️ Skip votes: <b>{votes}/{required}</b>",
                parse_mode="HTML"
            )

    except Exception as e:
        print("Skip error:", e)
        await context.bot.send_message(chat_id=chat.id, text="Something went wrong while skipping.")