import asyncio
import os

from aiogram import Dispatcher, types, Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv
from loguru import logger

from database.write_read_json import read_json
from keyboard.inline_keyboard import inline_keyboard_add
from keyboard.keyboard_admin import keyboard_admin


load_dotenv("../.env")
TOKEN = "6955649038:AAFxCJYhgxGsiX_m-T_Pt47gPRBWQEU1nk0"
bot = Bot(TOKEN)
storage = MemoryStorage()
dis = Dispatcher(storage=storage)


@dis.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Приветствую, {message.from_user.full_name}!\n"
        f"Этот бот поможет не потеряться в очереди)"
    )


@dis.message(Command("show"))
async def show_subjects(message: types.Message) -> None:
    logger.info("Start function: show")
    for files in os.listdir("database/json_files/"):
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
    logger.info("Finished function: show")


@dis.message(Command("add"))
async def add_handler(message: types.Message) -> None:
    logger.info(f"Start function 'add_handler'")
    boolean_read = open('admin/check_entry.txt', encoding='utf-8', mode='r').read()
    if boolean_read == 'True':
        await message.answer(
            "Сначала выберите предмет", reply_markup=inline_keyboard_add.as_markup())
    else:
        await message.answer(
            "Извините, запись закрыта"
        )


@dis.message(Command("admin"))
async def admin_panel(message: types.Message) -> None:
    logger.info(f"Start function 'admin_panel'")

    if str(message.from_user.id) != '1195216595':
        await message.answer("Доступ запрещён.")
    else:
        await message.answer(
            "Дорогой хозяин выбери пожалуйста действие",
            reply_markup=keyboard_admin,
        )


@dis.message(Command("help"))
async def echo_handler(message: types.Message) -> None:
    await message.answer("/add: добавить себя в очередь на предмет\n"
                         "/show: показать список очередей\n"
                         "/admin: для админов)\n")


async def main() -> None:
    import callback_hundlers_add
    import admin.handlers_admin
    dis.include_routers(callback_hundlers_add.router, admin.handlers_admin.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dis.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info("The bot is up and running")
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("The bot has stopped working")
