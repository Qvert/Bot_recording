from loguru import logger

from aiogram import F, types

from Bot_recording.record_bot.main import dis


@dis.message()
async def admin_panel(message: types.Message) -> None:
    if message.text == "Удалить черта":
        await admin_panel_delete(message=message)

    if message.text == "Поменять местами чертов":
        await admin_panel_change(message=message)


@dis.message()
async def admin_panel_delete(message: types.Message) -> None:
    logger.info("Start function: admin_panel_delete")
    await message.answer('Привет')


@dis.message()
async def admin_panel_change(message: types.Message) -> None:
    logger.info("Start function: admin_panel_change")
    pass
