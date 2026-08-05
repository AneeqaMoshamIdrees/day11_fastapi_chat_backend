import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("day11_chatbot")
logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.handlers.clear()

file_handler = logging.FileHandler("logs/chat_server.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Don't pass messages to the root logger
logger.propagate = False