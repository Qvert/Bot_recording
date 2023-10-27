
from aiogram import F, types

from Bot_recording.record_bot.main import dis


@dis.message()
async def delete_members(message: types.Message) -> None:
    if message.text == "Удалить черта":
        await message.answer("Обработка удаления")


@dis.message()
async def change_members(message: types.Message) -> None:
    if message.text == "Поменять местами чертов":
        await message.answer("Обработка поменяния местами")
