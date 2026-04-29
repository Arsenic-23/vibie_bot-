# 🎶 Vibie Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/telegram-bot--api-blue.svg)](https://core.telegram.org/bots/api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Vibie Bot** is a powerful Telegram bot that turns your group chats into shared, real-time jukeboxes. Connect your friends, queue up your favorite tracks, and vibe together seamlessly using our beautifully integrated Telegram Mini App. Where music meets moments.

---

## ✨ Features

- **🎧 Shared Group Jukebox**: Play and listen to music together in Telegram groups.
- **🎵 Queue Management**: Add songs, skip tracks, and manage the playlist collaboratively.
- **❤️ Interactive Playback**: Like tracks and see what the group is enjoying.
- **🚀 Telegram Mini App Integration**: Jump straight into the high-quality audio stream via a sleek, native-feeling Web App.
- **⚡ Fast & Async**: Built on `python-telegram-bot` and `httpx` for fast, asynchronous performance.

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Bot Framework**: [`python-telegram-bot`](https://python-telegram-bot.org/) (v20+)
- **HTTP Client**: `httpx` for asynchronous requests to the streaming backend.
- **Configuration**: `python-dotenv` for simple environment variable management.

## 🚀 Getting Started

### Prerequisites

1. Python 3.8 or higher.
2. A Telegram Bot Token from [@BotFather](https://t.me/BotFather).
3. A backend service/API for handling audio streaming (see configuration).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vibie_bot.git
   cd vibie_bot
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the root directory and add your environment variables:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

*Note: You also need to configure the `BACKEND_BASE_URL` in `handlers/play.py` and other relevant handlers to connect to your specific audio streaming backend, as well as the Mini App URL in `handlers/start.py`.*

### Running the Bot

Run the bot using Python:

```bash
python bot.py
```

You should see `Vibie Bot is running...` in your console. The bot is now actively polling for updates from Telegram!

## 🎮 Commands

Once added to a group (or in private chat, where applicable), you can use the following commands:

- `/start` - Get a welcome message and the link to join the Mini App stream.
- `/help` - Show the help message and available commands.
- `/join` - Get the link to join the active streaming session.
- `/play <song name>` - Search and add a song to the group's queue.
- `/queue` - View the current upcoming songs in the playlist.
- `/skip` - Vote to skip the currently playing track.
- `/like` - Like the current track.

## 📂 Project Structure

```text
vibie_bot/
├── bot.py               # Main entry point and bot setup
├── config.py            # Configuration and constants
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── handlers/            # Command handler modules
    ├── __init__.py
    ├── start.py         # /start command
    ├── help.py          # /help command
    ├── join.py          # /join command
    ├── play.py          # /play command (API integration)
    ├── queue.py         # /queue command
    ├── skip.py          # /skip command
    └── like.py          # /like command
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/yourusername/vibie_bot/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
