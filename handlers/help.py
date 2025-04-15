# vibie_bot/handlers/help.py

from telegram import Update
from telegram.ext import ContextTypes

HELP_TEXT = """
<b>Vibie Bot Help Menu</b>  
Here’s everything you can do:

<b>/start</b> – Start the bot and explore Vibie  
<b>/join</b> – Join the current stream in this group  
<b>/play &lt;song name&gt;</b> – Add a song to the group’s queue  
<b>/queue</b> – View the current song queue  
<b>/skip</b> – Vote to skip the current song  
<b>/like</b> – Like the currently playing song  
<b>/help</b> – Show this help message

<b>Tip:</b> Use these in any group where the bot is added. All group streams are separate and synced per group.

Join the stream using the Mini App button or simply type /join!
"""

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True
    )