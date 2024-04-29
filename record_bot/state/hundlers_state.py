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
        queueDict = read_json("vvpd_json")
        #TODO: understand why the json stays the same
        if (
            message.from_user.id in queueDict.keys()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу"
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)
        else:
            queueDict[message.from_user.id] = [message.from_user.username, queueDict.length() + 1]
            # queueDict = dict(
            #     sorted({int(k): v for k, v in queueDict.items()}.items())
            # )
            write_json(queueDict, "vvpd_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:

        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)

#add user to the op queue
@dis.message(AddPracticeOP.add_to_dict_op)
async def add_members_op(message: types.Message, state: FSMContext):
    try:
        #message_member = message.text.split(" ", 1)
        queueDict = read_json("op_json")

        if (
            message.from_user.id in queueDict.keys()
            #or message_member[1] in queueDict.values()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeOP.add_to_dict_op)
        else:
            queueDict[message.from_user.id] = [message.from_user.username, queueDict.length() + 1]
#             queueDict = dict(
#                 sorted({int(k): v for k, v in queueDict
# .items()}.items())
            #)

            write_json(queueDict, "op_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeOP.add_to_dict_op)

#add user to computer science
@dis.message(AddPracticeComp.add_to_dict_comp)
async def add_members_comp(message: types.Message, state: FSMContext):
    try:
        #message_member = message.text.split(" ", 1) # change to just text
        queueDict = read_json("comp_json") # what the fuck is this name? TODO: change to comp_member_list or smth.

        if (
            message.from_user.id in queueDict.keys() # after change handle one case
            #or message_member[1] in queueDict.values()
        ):
            await message.answer(
                "Извините, но вы уже записаны, если вы хотите выписаться то обратитесь к админу "
                "ONI-CHAN"
            )
            await state.set_state(AddPracticeComp.add_to_dict_comp)
        else:
            # no sortin, just add to the end, set key to dict len
            queueDict[message.from_user.id] = [message.from_user.username, queueDict.length()]
            # queueDict = dict(
            #     sorted({int(k): v for k, v in queueDict.items()}.items())
            # )
            # check what do
            write_json(queueDict, "comp_json")
            await message.answer("Вы успешно записаны в очередь)")
            await state.clear()

    except IndexError:
        await message.answer("Извините, вы некоректно ввели данные")
        await state.set_state(AddPracticeComp.add_to_dict_comp)

def removePerson(number: int, fileName: str):
    queueDict = read_json(fileName)
    for key, value in queueDict.items():
        if value[1] == number:
            delKey = key
        elif value[1] > number:
            value[1] -= 1
    del queueDict[delKey]

def addPerson(userId: str, number: int, fileName: str):
    queueDict = read_json(fileName)
    for key, value in queueDict.items():
        if value[1] >= number:
            value[1] += 1
    
def print_json(fileName: str):
    queueDict = read_json(fileName)
    for key, value in queueDict.items():
        print(f"{value[0]} : place in queue {value[1]}")