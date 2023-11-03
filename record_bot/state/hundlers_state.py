from loguru import logger

from aiogram.fsm.context import FSMContext
from aiogram import types

from Bot_recording.record_bot.main import form_router
from Bot_recording.record_bot.json_database.write_read_json import read_json, write_json
from .class_state import *


@form_router.message(AddPracticeVVPD.add_to_dict_vvpd)
async def add_members_vvpd(message: types.Message, state: FSMContext):
    logger.info("Start function: add_members_vvpd")
    try:
        message_member = message.text.split(" ", 1)
        get_dict_members = read_json("vvpd_json")

        if (
            message_member[0] in get_dict_members.keys()
            or message_member[1] in get_dict_members.values()
        ):
            await message.answer(
                "Извините, но уже чел под этим номером стоит, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)
        else:
            get_dict_members[message_member[0]] = message_member[1]
            get_dict_members = dict(
                sorted({int(k): v for k, v in get_dict_members.items()}.items())
            )

            write_json(get_dict_members, "vvpd_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)


@form_router.message(AddPracticeOP.add_to_dict_op)
async def add_members_op(message: types.Message, state: FSMContext):
    try:
        message_member = message.text.split(" ", 1)
        get_dict_members = read_json("op_json")

        if (
            message_member[0] in get_dict_members.keys()
            or message_member[1] in get_dict_members.values()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeOP.add_to_dict_op)
        else:
            get_dict_members[message_member[0]] = message_member[1]
            get_dict_members = dict(
                sorted({int(k): v for k, v in get_dict_members.items()}.items())
            )

            write_json(get_dict_members, "op_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeOP.add_to_dict_op)


@form_router.message(AddPracticeComp.add_to_dict_comp)
async def add_members_comp(message: types.Message, state: FSMContext):
    try:
        message_member = message.text.split(" ", 1)
        get_dict_members = read_json("comp_json")

        if (
            message_member[0] in get_dict_members.keys()
            or message_member[1] in get_dict_members.values()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeComp.add_to_dict_comp)
        else:
            get_dict_members[message_member[0]] = message_member[1]
            get_dict_members = dict(
                sorted({int(k): v for k, v in get_dict_members.items()}.items())
            )

            write_json(get_dict_members, "comp_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeComp.add_to_dict_comp)
