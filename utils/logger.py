
import logging

from utils.config import LOGS_DIR

LOG_FILE = LOGS_DIR / "chatbot.log"

logger = logging.getLogger("GenAIChatbot")

if not logger.handlers:
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)