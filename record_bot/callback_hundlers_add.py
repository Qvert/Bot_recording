from aiogram import F, types, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from loguru import logger

from database.write_read_json import read_json, write_json
from state.class_state import *

router = Router()


@router.callback_query(StateFilter(None))
async def add_subjects(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'add_vvpd':
        dict_vvpd = read_json("vvpd_json")
        logger.debug(f"{dict_vvpd = }")
        if dict_vvpd == {}:
            await callback.message.answer("Никто пока не записан")
            await callback.message.answer(
                "Чтобы записаться введите запись в формате: <номер> <ФИО>"
            )
            await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)
        else:
            await callback.message.answer("Вот список записанных в очередь\n")
            answer_string = ""
            for el, members in dict_vvpd.items():
                answer_string += f"{el}: {members}\n"
            await callback.message.answer(answer_string)
            await callback.message.answer(
                "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
            )
            await state.set_state(AddPracticeVVPD.add_to_dict_vvpd)

    if callback.data == 'add_comp':
        await add_comp(callback=callback, state=state)

    if callback.data == 'add_op':
        await add_op(callback=callback, state=state)


@router.callback_query(StateFilter(None))
async def add_comp(callback: types.CallbackQuery, state: FSMContext):
    dict_comp = read_json("comp_json")
    logger.debug(f"{dict_comp =}")
    if dict_comp == {}:
        await callback.message.answer("Никто пока не записан")
        await callback.message.answer(
            "Чтобы записаться введите запись в формате: <номер> <ФИО>"
        )
        await state.set_state(AddPracticeComp.add_to_dict_comp)
    else:
        await callback.message.answer("Вот список записанных в очередь\n")
        answer_string = ""
        for el, members in dict_comp.items():
            answer_string += f"{el}: {members}\n"
        await callback.message.answer(answer_string)
        await callback.message.answer(
            "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
        )
        await state.set_state(AddPracticeComp.add_to_dict_comp)


@router.callback_query(StateFilter(None))
async def add_op(callback: types.CallbackQuery, state: FSMContext):
    dict_op = read_json("op_json")
    logger.debug(f"{dict_op =}")
    if dict_op == {}:
        await callback.message.answer("Никто пока не записан")
        await callback.message.answer(
            "Чтобы записаться введите запись в формате: <номер> <ФИО>"
        )
        await state.set_state(AddPracticeOP.add_to_dict_op)
    else:
        await callback.message.answer("Вот список записанных в очередь\n")
        answer_string = ""
        for el, members in dict_op.items():
            answer_string += f"{el}: {members}\n"
        await callback.message.answer(answer_string)
        await callback.message.answer(
            "Теперь пожалуйста запишитесь в формате: <номер> <ФИО>"
        )
        await state.set_state(AddPracticeOP.add_to_dict_op)


@router.message(AddPracticeVVPD.add_to_dict_vvpd)
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


@router.message(AddPracticeOP.add_to_dict_op)
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


@router.message(AddPracticeComp.add_to_dict_comp)
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