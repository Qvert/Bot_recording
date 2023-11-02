
from aiogram import F, types

from Bot_recording.record_bot.main import dis


@dis.message()
async def admin_panel(message: types.Message) -> None:
    if message.text == "Удалить черта":
        await message.answer("Обработка удаления")
    if message.text == "Поменять местами чертов":
        await message.answer("Поменять")
