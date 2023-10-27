from aiogram.fsm.state import StatesGroup, State


class AddPracticeVVPD(StatesGroup):
    add_to_dict = State()


class AddPracticeOP(StatesGroup):
    add_to_dict = State()


class AddPracticeComp(StatesGroup):
    add_to_dict = State()


class StateAdminPanel(StatesGroup):
    choice_action = State()