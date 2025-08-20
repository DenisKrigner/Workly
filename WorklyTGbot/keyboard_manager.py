from aiogram.types          import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types          import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram                import types
from aiogram.types          import CallbackQuery


import asyncio
class KeyBoard_manager:

    async def get_all_product_keyBoard(self, data):
        keyboard = InlineKeyboardBuilder()

        for product in data:
            keyboard.add(InlineKeyboardButton(text=f"articale - {str(product[0])}", callback_data=f"product {str(product[0])}"))

        return keyboard.adjust(1).as_markup()

