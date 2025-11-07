import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from pathlib import Path

# Добавляем корневую папку проекта в путь
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from config.settings import BOT_TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


async def main():
    try:
        bot = Bot(
            token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
        await dp.start_polling(bot)
    except Exception as e:
        if "400" in str(e):
            print("Invalid token")
        else:
            print(e)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())
