import asyncio
from loguru import logger
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboard.inline_keyboard import inline_keyboard
from callback_hundlers import *

load_dotenv('../.env')
TOKEN = getenv("BOT_TOKEN")


dis = Dispatcher()


@dis.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Дарова заебал, {message.from_user.full_name}!\n"
                         f"Этот бот поможет не потеряться в очереди)")


@dis.message(Command("show"))
async def show_handler(message: types.Message) -> None:
    logger.info(f"Start function: {show_handler.__name__}")
    await message.answer("Сначала выберите предмет",
                         reply_markup=inline_keyboard.as_markup())


@dis.message(Command("help"))
async def echo_handler(message: types.Message) -> None:
    await message.answer("Ой биляя чо тебе не понятно здесь?")


async def main() -> None:
    bot = Bot(TOKEN)
    dis.callback_query.register(callback=send_answer_vvv)
    dis.callback_query.register(callback=send_answer_comp)
    dis.callback_query.register(callback=send_answer_op)
    await dis.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info("The bot is up and running")
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("The bot has stopped working")
