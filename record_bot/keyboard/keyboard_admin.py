from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardMarkup

keyboard = [
    [
        types.KeyboardButton(text="Удалить черта"),
        types.KeyboardButton(text="Поменять местами чертов"),
    ],
    [
        types.KeyboardButton(text="Открыть запись"),
        types.KeyboardButton(text="Закрыть запись"),
    ]
]
keyboard_admin = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
