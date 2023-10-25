import json

from aiogram import types
from aiogram import F

from main import dis
from json_database.write_read_json import *


@dis.callback_query(F.data == "vvpd_json")
async def send_answer_vvv(callback: types.CallbackQuery):
    dict_vvpd_members = read_json("vvpd_json")
    if dict_vvpd_members is None:
        await callback.message.answer("Извините но никто пока не записан на ВВПД")

    for el, members in dict_vvpd_members.items():
        await callback.message.answer(
            f"{el}: {members}"
        )


@dis.callback_query(F.data == "comp_json")
async def send_answer_comp(callback: types.CallbackQuery):
    dict_comp_members = read_json("comp_json")
    if dict_comp_members is None:
        await callback.message.answer("Извините но никто пока не записан на информатику")

    for el, members in dict_comp_members.items():
        await callback.message.answer(
            f"{el}: {members}"
        )


@dis.callback_query(F.data == "op_json")
async def send_answer_op(callback: types.CallbackQuery):
    dict_op_members = read_json("op_json")
    if dict_op_members is None:
        await callback.message.answer("Извините но никто пока не записан на ОП")

    for el, members in dict_op_members.items():
        await callback.message.answer(
            f"{el}: {members}"
        )
