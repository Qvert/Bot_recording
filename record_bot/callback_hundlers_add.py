from aiogram import F, types
from aiogram.fsm.context import FSMContext
from loguru import logger

from Bot_recording.record_bot.json_database.write_read_json import read_json
from Bot_recording.record_bot.state.class_state import (
    AddPracticeVVPD,
    AddPracticeComp,
    AddPracticeOP,
)
from state.hundlers_state import add_members_op, add_members_comp, add_members_vvpd
from main import dis


@dis.callback_query(F.data == "add_vvpd")
async def add_vvv(callback: types.CallbackQuery, state: FSMContext):
    dis.message.register(add_members_vvpd)
    dict_vvpd = read_json("vvpd_json")
    logger.debug(f"{dict_vvpd =}")
    if dict_vvpd == {}:
        await callback.message.answer("Никто пока не записан")
        await callback.message.answer(
            "Чтобы записаться введите запись в формате: <номер> <ФИО>"
        )
        await AddPracticeVVPD.add_to_dict.set()
    else:
        await callback.message.answer("Вот список записанных в очередь\n")
        answer_string = ""
        for el, members in dict_vvpd.items():
            answer_string += f"{el}: {members}\n"
        await callback.message.answer(answer_string)
        await callback.message.answer(
            "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
        )
        await AddPracticeVVPD.add_to_dict.set()


@dis.callback_query(F.data == "add_comp")
async def add_comp(callback: types.CallbackQuery, state: FSMContext):
    dis.message.register(add_members_comp)
    dict_comp = read_json("comp_json")
    logger.debug(f"{dict_comp =}")
    if dict_comp == {}:
        await callback.message.answer("Никто пока не записан")
        await callback.message.answer(
            "Чтобы записаться введите запись в формате: <номер> <ФИО>"
        )
        await AddPracticeComp.add_to_dict.set()
    else:
        await callback.message.answer("Вот список записанных в очередь\n")
        answer_string = ""
        for el, members in dict_comp.items():
            answer_string += f"{el}: {members}\n"
        await callback.message.answer(answer_string)
        await callback.message.answer(
            "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
        )
        await AddPracticeComp.add_to_dict.set()


@dis.callback_query(F.data == "add_op")
async def add_op(callback: types.CallbackQuery, state: FSMContext):
    dis.message.register(add_members_op)
    dict_op = read_json("op_json")
    logger.debug(f"{dict_op =}")
    if dict_op == {}:
        await callback.message.answer("Никто пока не записан")
        await callback.message.answer(
            "Чтобы записаться введите запись в формате: <номер> <ФИО>"
        )
        await AddPracticeOP.add_to_dict.set()
    else:
        await callback.message.answer("Вот список записанных в очередь\n")
        answer_string = ""
        for el, members in dict_op.items():
            answer_string += f"{el}: {members}\n"
        await callback.message.answer(answer_string)
        await callback.message.answer(
            "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
        )
        await AddPracticeOP.add_to_dict.set()
