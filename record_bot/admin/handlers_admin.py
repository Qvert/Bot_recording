from aiogram import types, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from loguru import logger

from Bot_recording.record_bot.database.write_read_json import read_json, write_json
from Bot_recording.record_bot.state.class_state import AdminPanel
from Bot_recording.record_bot.utils.dict_util import dict_name_subjects

router = Router()


@router.message(StateFilter(None))
async def admin_panel(message: types.Message, state: FSMContext) -> None:
    if message.text == "Удалить из очереди":
        await state.set_state(AdminPanel.delete_users)
        await message.answer("Введите по шаблону 'название предмета, номер'")

    if message.text == "Открыть запись":
        write_check_entry("True")
        await message.answer("Запись открыта")

    if message.text == "Закрыть запись":
        write_check_entry("False")
        await message.answer("Запись закрыта")


@router.message(AdminPanel.delete_users)
async def admin_panel_delete(message: types.Message, state: FSMContext) -> None:
    logger.info("Start function: admin_panel_delete")
    try:
        message_subject, message_number = message.text.split(', ')
        dict_people = read_json(name_dict_file := dict_name_subjects[message_subject.lower()])
        logger.info(f"{dict_people = }")
        del dict_people[message_number]
        write_json(dict_people, name_dict_file)
        await message.answer('Запись успешно удалена')
        await state.clear()
    except Exception as _err:
        await state.set_state(AdminPanel.delete_users)
        await message.answer("Вы неправильно ввели данные, пожалуйста повторите")


def write_check_entry(text: str) -> None:
    with open("admin/check_entry.txt", mode="w+", encoding="utf-8") as file_write:
        file_write.truncate(0)
        file_write.write(text)
