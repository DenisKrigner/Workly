from aiogram                    import Bot, Dispatcher, types, F, Router
from aiogram.filters            import CommandStart, Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types              import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from aiogram.types              import Message, CallbackQuery
from aiogram.enums.content_type import ContentType

import asyncio
import requests

from keyboard_manager import KeyBoard_manager

kb_manager = KeyBoard_manager()
router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    userID = message.from_user.id
    userID = str(userID)

    username = message.from_user.username

    keyboard = types.ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Workly', web_app=WebAppInfo(url=f"https://btcholder.pythonanywhere.com/{userID}/{username}")),
                                                   KeyboardButton(text="Чат", callback_data="get_chat")]],
                                         resize_keyboard=True, one_time_keyboard=False)

    #chat_link = f"https://t.me/Kitty22_Wb"
    #await message.reply(f"Открыть чат с пользователем: {chat_link}")
    await message.reply(f'Добро пожаловать в Workly, {username}', reply_markup=keyboard)


