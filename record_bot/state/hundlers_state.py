from loguru import logger

from aiogram.fsm.context import FSMContext
from aiogram import types
#fix imports below, imports on top - come from pyvenv
from record_bot.main import dis
from record_bot.json_database.write_read_json import read_json, write_json
from state.class_state import *

#TODO: USE MESSAGER ID TO PUT THEM INTO THE QUEUE, add user name to that to let admin delete them and for people to understand the q;

#add a user to the vvpd queue
@dis.message(AddPracticeVVPD.add_to_dict_vvpd)
async def add_members_vvpd(message: types.Message, state: FSMContext):
    logger.info("Start function: add_members_vvpd")
    try:
        #message_member = message.text.split(" ", 1)
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

#add user to the op queue
@dis.message(AddPracticeOP.add_to_dict_op)
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

#add user to computer science
@dis.message(AddPracticeComp.add_to_dict_comp)
async def add_members_comp(message: types.Message, state: FSMContext):
    try:
        message_member = message.text.split(" ", 1) # change to just text
        get_dict_members = read_json("comp_json") # what the fuck is this name? TODO: change to comp_member_list or smth.

        if (
            message_member[0] in get_dict_members.keys() # after change handle one case
            or message_member[1] in get_dict_members.values()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeComp.add_to_dict_comp)
        else:
            # no sortin, just add to the end, set key to dict len
            get_dict_members[message_member[0]] = message_member[1]
            get_dict_members = dict(
                sorted({int(k): v for k, v in get_dict_members.items()}.items())
            )
            # check what do
            write_json(get_dict_members, "comp_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeComp.add_to_dict_comp)
