from aiogram.fsm.state import StatesGroup, State

class ReportState(StatesGroup):
    lavozim = State()
    nizom = State()
    duplicate = State()
    perevod = State()
    