# vibie_bot/handlers/__init__.py

from telegram.ext import ApplicationBuilder, CommandHandler
from .play import play
from .queue import queue
from .like import like
from .skip import skip
from .start import start
from .help import help_command

def register_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("queue", queue))
    application.add_handler(CommandHandler("like", like))
    application.add_handler(CommandHandler("skip", skip))
    application.add_handler(CommandHandler("help", help_command))