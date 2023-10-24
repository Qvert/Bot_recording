from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_keyboard = InlineKeyboardBuilder()
inline_keyboard.add(
    types.InlineKeyboardButton(
        text="ВВПД",
        callback_data="vvpd_json"
    ),
    types.InlineKeyboardButton(
        text="Информатика",
        callback_data="comp_json"
    ),
    types.InlineKeyboardButton(
        text="ОП",
        callback_data="op_json"
    )
)
