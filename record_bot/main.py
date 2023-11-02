import asyncio
import os
from os import getenv

from aiogram import Dispatcher, types, Bot
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv
from loguru import logger

from json_database.write_read_json import read_json
from keyboard.inline_keyboard import inline_keyboard_add
from keyboard.keyboard_admin import keyboard_admin


load_dotenv("../.env")
TOKEN = getenv("BOT_TOKEN")

storage = MemoryStorage()
dis = Dispatcher(storage=storage)


@dis.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Дарова заебал, {message.from_user.full_name}!\n"
        f"Этот бот поможет не потеряться в очереди)"
    )


@dis.message(Command("show"))
async def show_subjects(message: types.Message) -> None:
    for files in os.listdir("json_database/json_files/"):
        string_result = ""
        file_dict = read_json(files[:-5])
        if files.startswith("comp"):
            string_result += "Информатика:\n"
        if files.startswith("op"):
            string_result += "Основы программирования:\n"
        if files.startswith("vvpd"):
            string_result += "ВВПД:\n"

        for num, members in file_dict.items():
            string_result += f"{num}: {members}\n"
        await message.answer(string_result)


@dis.message(Command("add"))
async def add_handler(message: types.Message) -> None:
    logger.info(f"Start function 'add_handler'")
    await message.answer(
        "Сначала выберите предмет", reply_markup=inline_keyboard_add.as_markup()
    )


@dis.message(Command("admin"))
async def admin_panel(message: types.Message) -> None:
    logger.info(f"Start function 'admin_panel'")
    if str(message.from_user.id) != str(getenv("USER_ADMIN_ID")):
        await message.answer("Сюда только админ ONI-CHAN может зайти.")
    else:
        from admin.handlers_admin import admin_panel
        dis.message.register(admin_panel)
        await message.answer(
            "Дорогой хозяйн выбери пожалуйста действие",
            reply_markup=keyboard_admin,
        )


@dis.message(Command("help"))
async def echo_handler(message: types.Message) -> None:
    await message.answer("Ой биляя чо тебе не понятно здесь?")


async def main() -> None:
    bot = Bot(TOKEN)
    from callback_hundlers_add import add_vvv, add_comp, add_op

    dis.callback_query.register(callback=add_vvv)
    dis.callback_query.register(callback=add_op)
    dis.callback_query.register(callback=add_comp)
    await dis.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info("The bot is up and running")
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("The bot has stopped working")
