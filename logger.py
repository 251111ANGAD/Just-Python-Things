from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

LOG_FILE = f"logs/{datetime.now().strftime('%Y-%m-%d')}.txt"


def log(message):

    timestamp = datetime.now().strftime("%H:%M:%S")

    text = f"[{timestamp}] {message}"

    print(text)

    # FIX: force UTF-8 encoding so emojis/symbols work
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")