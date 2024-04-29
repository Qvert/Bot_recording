from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardMarkup

#admin markup
keyboard = [
    [
        types.KeyboardButton(text="Удалить из очереди"),
        types.KeyboardButton(text="Поменять местами"),
    ],
    [
        types.KeyboardButton(text="Открыть запись"),
        types.KeyboardButton(text="Закрыть запись"),
    ]
]
keyboard_admin = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
