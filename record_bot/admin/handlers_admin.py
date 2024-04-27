from loguru import logger

from aiogram import F, types

from record_bot.main import dis

#handler for admin panel
@dis.message()
async def admin_panel(message: types.Message) -> None:
    if message.text == "Удалить черта":
        await admin_panel_delete(message=message)

    if message.text == "Поменять местами чертов":
        await admin_panel_change(message=message)

#TODO: implement the deletion of a person by name/index. probably by index
@dis.message()
async def admin_panel_delete(message: types.Message) -> None:
    logger.info("Start function: admin_panel_delete")
    await message.answer('Привет')

#TODO: implement swap of numbers by name?
@dis.message()
async def admin_panel_change(message: types.Message) -> None:
    logger.info("Start function: admin_panel_change")
    pass
