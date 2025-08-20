from aiogram                    import Bot, Dispatcher, types, F, Router
from aiogram.filters            import CommandStart, Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types              import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from aiogram.types              import Message, CallbackQuery
from aiogram.enums.content_type import ContentType

from dotenv import load_dotenv
import os

import asyncio

from bot_handler import router

dp = Dispatcher()


load_dotenv(dotenv_path='data.env')

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
async def main():
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())