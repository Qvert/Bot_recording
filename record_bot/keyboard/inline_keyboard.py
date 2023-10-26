from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


inline_keyboard_add = InlineKeyboardBuilder()
inline_keyboard_add.add(
    types.InlineKeyboardButton(
        text="ВВПД",
        callback_data="add_vvpd"
    ),
    types.InlineKeyboardButton(
        text="Информатика",
        callback_data="add_comp"
    ),
    types.InlineKeyboardButton(
        text="ОП",
        callback_data="add_op"
    )
)