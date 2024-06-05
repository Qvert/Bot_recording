from aiogram.fsm.state import StatesGroup, State


class AddPracticeVVPD(StatesGroup):
    add_to_dict_vvpd = State()


class AddPracticeOP(StatesGroup):
    add_to_dict_op = State()


class AddPracticeComp(StatesGroup):
    add_to_dict_comp = State()


class AdminPanel(StatesGroup):
    delete_users = State()
