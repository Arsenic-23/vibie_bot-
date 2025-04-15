# vibie_bot/config.py

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")  # e.g. https://your-backend-url.com