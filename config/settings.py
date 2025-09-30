from dotenv import load_dotenv
from os import getenv
from pathlib import Path

# Загрузка .env
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

# Bot settings
BOT_TOKEN = getenv("BOT_TOKEN")

# Database settings
DATABASE_URL = getenv("DATABASE_URL")

# Redis settings (если будете использовать)
REDIS_HOST = getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(getenv("REDIS_PORT", 6379))

# Проверка обязательных переменных
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен в .env файле")
