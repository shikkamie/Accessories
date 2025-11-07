from aiogram.filters import Command
from aiogram import F, Router


us_rt = Router()



@us_rt.message(Command("help"))
async def help_command_handler(message):
    await message.reply("Помощь по командам бота:\n"
                        "/start - Запустить бота\n"
                        "/orders - Просмотреть ваши заказы"
                        "/profile - Управление вашим профилем"
                        "/menu - Показать главное меню"
                        "/help - Показать это сообщение помощи\n"
                        "/info - Получить информацию о боте")